# ANYISP Scanner - Local Lifetime Build
# Server heartbeat/policy authorization removed.
# Local license + local engine selection.

import os
import sys
import time

try:
    from security.core import (
        get_device_id,
        run_security_init,
    )
    from security.license import LicenseHandler, LicenseError
    SECURITY_AVAILABLE = True
except ImportError:
    try:
        from client.security.core import (
            get_device_id,
            run_security_init,
        )
        from client.security.license import LicenseHandler, LicenseError
        SECURITY_AVAILABLE = True
    except ImportError:
        SECURITY_AVAILABLE = False


CLIENT_VERSION = "1.2.16"
CLIENT_BUILD = "1.2.16"


# -----------------------------
# Terminal colors
# -----------------------------

COLORS = {
    "red": "\033[91m",
    "green": "\033[92m",
    "yellow": "\033[93m",
    "blue": "\033[94m",
    "cyan": "\033[96m",
    "white": "\033[97m",
    "reset": "\033[0m",
}


def c(color, text):
    return f"{COLORS.get(color, COLORS['white'])}{text}{COLORS['reset']}"


# -----------------------------
# Screen
# -----------------------------

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def show_logo():
    print(c("cyan", r"""
   _   _   _   ___ ____  ____  
  / \ | \ | | |_ _/ ___||  _ \ 
 / _ \|  \| |  | |\___ \| |_) |
/ ___ \ |\  |  | | ___) |  __/ 
/_/   \_\_| \_| |___|____/|_|    

        ANYISP SCANNER
    """))

    print(c("yellow", f"  Build: {CLIENT_BUILD}"))
    print(c("green", "  Local lifetime mode enabled."))
    print()


# -----------------------------
# Security
# -----------------------------

def run_security_check():
    """
    Keep the project's integrity/security check enabled.
    """
    if not SECURITY_AVAILABLE:
        print(c("yellow", "[!] Security module unavailable."))
        return True

    try:
        device_id = get_device_id()
        ok, reason = run_security_init(device_id)

        if not ok:
            print(c("red", f"Security check failed: {reason}"))
            print(c(
                "yellow",
                "[!] Security advisory active - continuing."
            ))
            return False

        print(c("green", "[+] Security check passed."))
        return True

    except Exception as e:
        print(c("yellow", f"[!] Security check error: {e}"))
        print(c("yellow", "[!] Continuing with local build."))
        return False


# -----------------------------
# Local activation
# -----------------------------

def first_time_activation(handler):
    clear_screen()
    show_logo()

    print(c("cyan", f"  Device: {handler.device_id}"))

    try:
        handler.activate({})
    except Exception as e:
        print(c("red", f"  Local activation failed: {e}"))
        raise

    print(c("green", "  Lifetime license created locally."))

    try:
        version = handler.get_assigned_version()
    except Exception:
        version = "v5"

    print(c("cyan", f"  Engine: {version.upper()} (local)"))
    print()


# -----------------------------
# Local refresh
# -----------------------------

def try_refresh_activation(handler):
    """
    Local-only refresh.

    No HTTP request is made here. The LicenseHandler is responsible
    for maintaining the local lifetime entitlement.
    """
    try:
        handler.activate({})
        return True
    except Exception as e:
        print(c("yellow", f"[!] Local refresh failed: {e}"))
        return False


# -----------------------------
# Reset local configuration
# -----------------------------

def wipe_config(handler):
    try:
        if (
            getattr(handler, "is_configured", lambda: False)()
            and os.path.exists(handler.config_path)
        ):
            os.remove(handler.config_path)

            print(c(
                "green",
                "[+] Local license configuration removed."
            ))

    except Exception as e:
        print(c("yellow", f"[!] Could not remove license config: {e}"))

    try:
        queue = getattr(handler, "breach_queue_path", None)

        if queue and os.path.exists(queue):
            os.remove(queue)

    except Exception:
        pass


# -----------------------------
# CLI
# -----------------------------

def handle_cli_command(handler):
    """
    Supported:

        scanner --reset
        scanner --refresh
    """

    args = sys.argv[1:]

    if not args:
        return False

    cmd = args[0].lower().lstrip("-")

    if cmd in ("reset", "clear"):
        wipe_config(handler)

        try:
            first_time_activation(handler)
        except Exception as e:
            print(c("red", f"Activation failed: {e}"))

        return True

    if cmd in ("refresh", "forced-refresh", "renew"):
        if not handler.is_configured():
            first_time_activation(handler)
            return True

        print(c("cyan", "[+] Refreshing local lifetime license..."))

        if try_refresh_activation(handler):
            print(c("green", "[+] Local license refreshed."))
        else:
            print(c("red", "[-] Local license refresh failed."))

        return True

    return False


# -----------------------------
# Engine
# -----------------------------

def run_local_engine(handler, version):
    """
    Run the locally selected engine.

    version must be 'v5' or 'v6'.
    """

    version = str(version).lower().strip()

    if version not in ("v5", "v6"):
        print(c(
            "yellow",
            f"[!] Unknown engine '{version}', using V5."
        ))
        version = "v5"

    module_name = "v5_engine" if version == "v5" else "v6_engine"

    try:
        engine = __import__(module_name)

    except ImportError as e:
        print(c(
            "red",
            f"Could not load {version.upper()} engine: {e}"
        ))
        return False

    # Pass local lifetime value to the engine.
    try:
        engine.SERVER_DAYS_REMAINING = handler.days_remaining()
    except Exception:
        engine.SERVER_DAYS_REMAINING = 36500

    print()
    print(c(
        "green",
        f"Engine: {version.upper()} (local)"
    ))
    print(c(
        "cyan",
        f"Days remaining: {engine.SERVER_DAYS_REMAINING}"
    ))
    print()

    try:
        engine.run_engine()
        return True

    except AttributeError:
        print(c(
            "red",
            f"{module_name}.py does not contain run_engine()."
        ))
        return False

    except Exception as e:
        print(c(
            "red",
            f"Engine error: {e}"
        ))
        return False


# -----------------------------
# Main
# -----------------------------

def main():

    clear_screen()

    print(c(
        "green",
        f"  ANYISP SCANNER  [build {CLIENT_BUILD}]"
    ))
    print()

    if not SECURITY_AVAILABLE:
        print(c(
            "yellow",
            "[!] Security/license modules could not be imported."
        ))
        sys.exit(1)

    # Create local license handler.
    try:
        handler = LicenseHandler()

    except LicenseError as e:
        print(c("red", f"License error: {e}"))
        sys.exit(1)

    except Exception as e:
        print(c("red", f"Could not initialize license handler: {e}"))
        sys.exit(1)

    # No breach callback/network reporting.
    try:
        handler.breach_callback = None
    except Exception:
        pass

    # CLI commands.
    if handle_cli_command(handler):
        return

    # Security/integrity check.
    run_security_check()

    # Create local lifetime license if needed.
    if not handler.is_configured():

        print(c(
            "yellow",
            "[+] No local license found."
        ))

        try:
            first_time_activation(handler)

        except LicenseError as e:
            print(c(
                "red",
                f"Local activation failed: {e}"
            ))
            sys.exit(1)

        except Exception as e:
            print(c(
                "red",
                f"Activation error: {e}"
            ))
            sys.exit(1)

    # Local validation only.
    status = handler.validate()

    if status != "valid":

        print(c(
            "yellow",
            f"[!] Local license status: {status}"
        ))

        print(c(
            "cyan",
            "[+] Attempting local lifetime refresh..."
        ))

        if try_refresh_activation(handler):
            status = handler.validate()

    if status != "valid":
        print(c(
            "red",
            f"License validation failed: {status}"
        ))
        sys.exit(1)

    # Local engine selection.
    try:
        version = handler.get_assigned_version()
    except Exception:
        version = "v5"

    version = str(version).lower().strip()

    if version not in ("v5", "v6"):
        version = "v5"

    print(c(
        "green",
        f"Engine: {version.upper()} (local)"
    ))

    time.sleep(0.5)

    # Run engine.
    if not run_local_engine(handler, version):
        sys.exit(1)


# -----------------------------
# Entry point
# -----------------------------

if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print()
        print(c("yellow", "[!] Stopped by user."))
        sys.exit(0)

    except Exception as e:
        print(c("red", f"Fatal error: {e}"))
        sys.exit(1)
