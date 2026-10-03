"""Local lifetime license handler.

This build intentionally has no remote activation, heartbeat, or policy server.
The project owner can use the scanner locally without an external licensing backend.
"""
import os
import json
import threading
from datetime import datetime
from .core import (
    config_encrypt,
    config_decrypt,
    config_hmac,
    verify_config_hmac,
    get_device_id,
    get_hw_fingerprint,
    start_security_monitor,
    check_timing_anomaly,
)

CLIENT_BUILD = "local-lifetime"

class LicenseError(Exception):
    pass

class LicenseHandler:
    """Local, non-expiring entitlement used by the project owner's build."""

    def __init__(self, config_dir=None):
        self.device_id = get_device_id()
        self.hw_fingerprint = get_hw_fingerprint()
        self.config_dir = config_dir or self._default_config_dir()
        self.config_path = os.path.join(self.config_dir, "license.json.enc")
        self.breach_queue_path = os.path.join(self.config_dir, "breach_queue.json")
        self.lock = threading.Lock()
        self.stop_event = threading.Event()
        self.monitor = None
        self.breach_callback = None

    def _default_config_dir(self):
        return os.path.join(os.path.expanduser("~"), ".anyisp_scanner")

    def ensure_dirs(self):
        os.makedirs(self.config_dir, exist_ok=True)

    def _save_config(self, data):
        self.ensure_dirs()
        payload = json.dumps(data, sort_keys=True).encode()
        encrypted = config_encrypt(payload, self.device_id)
        signature = config_hmac(encrypted, self.device_id)
        with open(self.config_path, "wb") as f:
            f.write(encrypted + b"|SIG|" + signature)

    def _load_config(self):
        if not os.path.exists(self.config_path):
            return {}
        try:
            with open(self.config_path, "rb") as f:
                content = f.read()
            if b"|SIG|" not in content:
                raise LicenseError("Invalid local license file")
            encrypted, signature = content.split(b"|SIG|", 1)
            if not verify_config_hmac(encrypted, signature, self.device_id):
                raise LicenseError("Local license signature verification failed")
            return json.loads(config_decrypt(encrypted, self.device_id))
        except LicenseError:
            raise
        except Exception as e:
            raise LicenseError(f"Failed to load local license: {e}")

    def is_configured(self):
        return os.path.exists(self.config_path)

    def activate(self, config=None, use_https=True):
        """Create/refresh the local lifetime entitlement; no network request is made."""
        cfg = {
            "device_id": self.device_id,
            "hw_fingerprint": self.hw_fingerprint,
            "license_type": "lifetime",
            "expiry_date": "",
            "token": "local",
            "version": "v5",
            "assigned_version": "v5",
            "activated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "policy_issued_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "policy_fresh": True,
            "local_only": True,
        }
        self._save_config(cfg)
        return True

    def validate(self):
        if not self.is_configured():
            return "not_configured"
        try:
            cfg = self._load_config()
        except LicenseError:
            return "tampered"
        if cfg.get("device_id") != self.device_id:
            return "tampered"
        if cfg.get("license_type") != "lifetime" or not cfg.get("local_only"):
            return "tampered"
        if self.monitor is None:
            self.monitor = start_security_monitor(self.stop_event, self.breach_callback)
        if check_timing_anomaly():
            return "tampered"
        return "valid"

    def get_expiry(self):
        return ""

    def get_server_url(self):
        return ""

    def get_token(self):
        return "local"

    def get_breach_queue_path(self):
        return self.breach_queue_path

    def has_pending_breach_report(self):
        return False

    def flush_pending_breach_queue(self, server_url=None, use_https=True):
        return 0

    def get_assigned_version(self):
        try:
            cfg = self._load_config()
            version = cfg.get("assigned_version", cfg.get("version", "v5"))
            return version if version in ("v5", "v6") else "v5"
        except Exception:
            return "v5"

    def set_assigned_version(self, version):
        if version not in ("v5", "v6"):
            return
        try:
            cfg = self._load_config()
            cfg["assigned_version"] = version
            cfg["version"] = version
            self._save_config(cfg)
        except Exception:
            pass

    def _sync_server_expiry(self, expiry_date):
        # Kept for API compatibility; there is no server in this build.
        return None

    def days_remaining(self):
        return 36500

    def fetch_policy(self, use_https=True):
        # Local lifetime builds do not require a remote policy.
        try:
            cfg = self._load_config()
            cfg["policy_fresh"] = True
            cfg["policy_issued_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self._save_config(cfg)
        except Exception:
            pass
        return True

    def has_fresh_policy(self, max_age_seconds=None):
        try:
            cfg = self._load_config()
            return bool(cfg.get("local_only") and cfg.get("license_type") == "lifetime")
        except Exception:
            return False

    def heartbeat(self, use_https=True):
        # Always valid locally; no remote authorization check exists.
        return True
