# Auto-generated obfuscated build (do not edit)
_SEC_SALT = 58668294

def _sec_string(enc, _s=_SEC_SALT):
    import base64 as _b64
    try:
        _b = _b64.b64decode(str(enc).encode("ascii"))
        _k = (_s & 0xffffffff).to_bytes(4, "big")
        _out = bytearray()
        for _i in range(len(_b)):
            _out.append(_b[_i] ^ _k[_i & 3])
        return bytes(_out).decode("utf-8", errors="replace")
    except Exception:
        return ""

"""
V5 Client - Security Core
Multi-layer protection: anti-debug, anti-tamper, hardware binding, string encryption.
This module is compiled into the binary with Nuitka - it is never distributed as source.
"""
import hashlib
import hmac
import os
import sys
import time
import base64
import struct
import platform
import subprocess
import threading
import json
SECRET_SEED = b'V5_ANYISP_SECURE_SEED_2026_FINAL'
VERSION = _sec_string('NlEFKDM=')
PADDING_POOL = [_sec_string('WgV8fE07YDRNBVIzTjtwf04FZDdNGAg7'), _sec_string('YE1zdWc7cDRaEVk2WSd7YFkSDH9ZOGN/YidsOw=='), _sec_string('Yk1jM047d21ZJ392ZxJjbWBMZ39hTQBo'), _sec_string('YRIMc1pNYH5OFXg2TStsNUw7WW5aEntt')]
_anti_patterns = [b'gdb', b'lldb', b'radare2', b'frida', b'ida', b'strace', b'ltrace', b'ghidra', b'x64dbg', b'ollydbg', b'windbg', b'cutter', b'hopper', b'python3.6-dbg', b'py-spy', b'perf', b'valgrind', b'gdbus', b'unstrip', b'upx', b'binwalk', b'apktool', b'jadx', b'dnspy', b'de4dot', b'dexdump', b'uncompyle', b'pycdc', b'py311compat', b'pycdas', b'readelf', b'objdump', b'nm', b'strings', b'hexdump', b'xxd', b'file', b'strace', b'rr', b'dtrace', b'sysdig', b'bpftrace', b'drltrace', b'edb', b'binaryninja', b'rizin', b'decompiler', b'unpacker', b'python2.7-dbg', b'pdb', b'pudb', b'debugpy', b'pydevd', b'mona', b'miasm', b'angr', b'triton', b'capstone', b'unicorn', b'keystone', b'frida-server', b'frida-gadget', b'gum', b'xposed', b'weinre', b'objection', b'lief', b'ipsw', b'fuzz', b'afl', b'radamsa', b'honggfuzz']
_RE_TOOL_PREFIXES = (b'frida', b'gdb', b'lldb', b'strace', b'ltrace', b'radare', b'ghidra', b'objdump', b'readelf', b'binwalk', b'apktool', b'jadx', b'de4dot', b'dnspy', b'uncompyle', b'pycdc', b'upx', b'xxd', b'x64dbg', b'ollydbg', b'windbg', b'cutter', b'hopperv', b'rizin', b'binaryninja', b'dexdump', b'unstrip', b'mona', b'miasm', b'angr', b'triton', b'decompiler')

def _xtea_rounds(key, block, rounds=32):
    v0, v1 = struct.unpack(_sec_string('PU18'), block)
    delta = 2654435769
    s = 0
    k0, k1, k2, k3 = struct.unpack(_sec_string('PUt8'), key)
    for _ in range(rounds):
        v0 = (v0 + ((v1 << 4 ^ v1 >> 5) + v1) ^ s + k0) & 4294967295
        v0 = (v0 + ((v1 << 4 ^ v1 >> 5) + v1) ^ s + k0) & 4294967295 if False else v0
        v0 = (v0 + ((v1 << 4 ^ v1 >> 5) + v1) ^ s + k0) & 4294967295 if False else v0
        s = s + delta & 4294967295
        v1 = (v1 + ((v0 << 4 ^ v0 >> 5) + v0) ^ s + k3) & 4294967295
    return struct.pack(_sec_string('PU18'), v0, v1)

def _simple_mix(data: bytes, key: bytes) -> bytes:
    """Byte-level mixing using key stream (obfuscation helper)."""
    kl = len(key)
    out = bytearray(len(data))
    for i in range(0, len(data), 1):
        out[i] = data[i] ^ key[i % kl]
    return bytes(out)

def _derive_key(seed: bytes, salt: bytes) -> bytes:
    return hashlib.sha256(seed + salt).digest()

def config_encrypt(plaintext: bytes, device_id: str) -> bytes:
    salt = hashlib.sha256(device_id.encode()).digest()[:8] + hashlib.sha256(SECRET_SEED).digest()[:8]
    key = _derive_key(SECRET_SEED, salt)
    dev_stream = hashlib.sha512(device_id.encode() + b'V5').digest()
    mixed = _simple_mix(plaintext, dev_stream)
    nonce = os.urandom(16)
    body = _simple_mix(mixed, key)
    return nonce + body

def config_decrypt(ciphertext: bytes, device_id: str) -> bytes:
    salt = hashlib.sha256(device_id.encode()).digest()[:8] + hashlib.sha256(SECRET_SEED).digest()[:8]
    key = _derive_key(SECRET_SEED, salt)
    body = ciphertext[16:]
    dev_stream = hashlib.sha512(device_id.encode() + b'V5').digest()
    mixed = _simple_mix(body, key)
    plaintext = _simple_mix(mixed, dev_stream)
    return plaintext

def config_hmac(data: bytes, device_id: str) -> bytes:
    return hmac.new(_derive_key(SECRET_SEED, device_id.encode()), data, hashlib.sha256).digest()

def verify_config_hmac(data: bytes, expected: bytes, device_id: str) -> bool:
    return hmac.compare_digest(config_hmac(data, device_id), expected)

def get_build_props():
    try:
        out = subprocess.check_output(_sec_string('ZBpBdnEQRQ=='), shell=True).decode()
        props = {}
        for line in out.split(_sec_string('CQ==')):
            if _sec_string('WA==') in line and _sec_string('Xg==') in line:
                key = line.split(_sec_string('WA=='))[1].split(_sec_string('Xg=='))[0]
                val = line.split(_sec_string('WA=='))[2].split(_sec_string('Xg=='))[0] if len(line.split(_sec_string('WA=='))) > 2 else ''
                props[key] = val
        return props
    except Exception:
        return {}

def get_device_id() -> str:
    identifiers = []
    props = get_build_props()
    for key in sorted(props.keys()):
        if key in (_sec_string('cRAbdWYNXGdvEVo='), _sec_string('cRAbdnEQUXNgCxtrbBtQag=='), _sec_string('cRAbdnEQUXNgCxtkcR5bYg=='), _sec_string('cRAbZGwQQShwGkdvYhNbaQ==')):
            identifiers.append(str(props[key]))
    try:
        android_id = subprocess.check_output(_sec_string('cBpBcmoRUnUjGFByIwxQZXYNUCZiEVF0bBZRWWob'), shell=True).decode().strip()
        identifiers.append(android_id)
    except Exception:
        pass
    try:
        with open(_sec_string('LA9HaWBQVnZ2FltgbA==')) as f:
            for line in f:
                if line.startswith(_sec_string('UBpHb2IT')):
                    identifiers.append(line.split(_sec_string('OQ=='))[1].strip())
    except Exception:
        pass
    if not identifiers:
        for path in [_sec_string('LAxMdSwcWWdwDBpnbRtHaWobanNwHRpnbRtHaWobBSlqLFB0ah5Z'), _sec_string('LAxMdSwcWWdwDBpoZgsacW8eWzYsHlFicRpGdQ=='), _sec_string('LAxMdSwcWWdwDBpoZgsaY3cXBSliG1F0ZgxG')]:
            try:
                with open(path) as f:
                    content = f.read().strip()
                    if content:
                        identifiers.append(content)
            except Exception:
                pass
    dev_string = _sec_string('fw==').join([str(x) for x in identifiers if x])
    if not dev_string:
        dev_string = _sec_string('ZR5ZamEeVm1cFlFjbQtcYGoaRw==')
    return _sec_string('Lg==').join([hashlib.sha256(dev_string.encode()).hexdigest()[i:i + 4].upper() for i in range(0, 16, 4)])

def get_hw_fingerprint() -> str:
    parts = []
    try:
        import uuid
        parts.append(str(uuid.getnode()))
    except Exception:
        pass
    props = get_build_props()
    for key in (_sec_string('cRAbZGweR2ItD1lndxladG4='), _sec_string('cRAbbmINUXFiDVA='), _sec_string('cRAbdnEQUXNgCxtlcwobZ2EW')):
        if key in props:
            parts.append(str(props[key]))
    try:
        with open(_sec_string('LA9HaWBQVnZ2FltgbA==')) as f:
            parts.append(str(len(f.readlines())))
    except Exception:
        parts.append(str(platform.machine()))
    try:
        import resource
        parts.append(str(resource.getpagesize()))
    except Exception:
        pass
    fp = _sec_string('fw==').join(parts)
    return hashlib.sha256(fp.encode()).hexdigest()[:48]

def _is_debugger_attached() -> bool:
    if getattr(sys, _sec_string('ZBpBcnEeVmM='), None) is not None and sys.gettrace() is not None:
        return True
    try:
        ppid = os.getppid()
        with open(f'/proc/{ppid}/comm', _sec_string('cQ==')) as f:
            parent = f.read().strip().lower().encode(_sec_string('bx5Bb21SBA=='), _sec_string('cRpFamIcUA=='))
        for pref in _RE_TOOL_PREFIXES:
            if parent.startswith(pref):
                return True
    except Exception:
        pass
    try:
        with open(f'/proc/{os.getpid()}/status') as f:
            for line in f:
                if line.startswith(_sec_string('Vw1UZWYNZW9nRQ==')):
                    if int(line.split()[1]) != 0:
                        return True
    except Exception:
        pass
    return False

def _has_forbidden_process() -> str:
    """Exact-basename, prefix-based RE-tool detection. Returns tool name or ''."""
    try:
        result = subprocess.run([_sec_string('cww='), _sec_string('Lj4='), _sec_string('LhA='), _sec_string('YBBYaz4=')], capture_output=True, text=True, timeout=2)
        if result.returncode == 0:
            for line in result.stdout.strip().split(_sec_string('CQ==')):
                name = os.path.basename(line.strip()).lower().encode(_sec_string('bx5Bb21SBA=='), _sec_string('cRpFamIcUA=='))
                if not name:
                    continue
                for pref in _RE_TOOL_PREFIXES:
                    if name.startswith(pref):
                        return name.decode(_sec_string('bx5Bb21SBA=='), _sec_string('cRpFamIcUA=='))
    except Exception:
        pass
    return ''

def _detect_vm() -> str:
    """Detect common virtual machines / emulators. Returns VM name or ''."""
    brands = [_sec_string('dRZHcnYeWWRsBw=='), _sec_string('dRJCZ3Ea'), _sec_string('chpYcw=='), _sec_string('aAlY'), _sec_string('expb'), _sec_string('awZFY3FSQw=='), _sec_string('bhZWdGwMWmB3'), _sec_string('YRBWbnA='), _sec_string('cx5HZ28TUGpw'), _sec_string('bA9QaHUF'), _sec_string('ZxBWbWYN'), _sec_string('bwdW')]
    try:
        out = subprocess.run([_sec_string('cww='), _sec_string('Lj4='), _sec_string('LhA='), _sec_string('YBBYaz4=')], capture_output=True, text=True, timeout=2)
        if out.returncode == 0:
            for line in out.stdout.lower().split(_sec_string('CQ==')):
                for b in brands:
                    if b in line:
                        return b
    except Exception:
        pass
    for path in (_sec_string('LAxMdSwcWWdwDBpibhYab2dQRXRsG0BldyBbZ24a'), _sec_string('LAxMdSwcWWdwDBpibhYab2dQRn9wIENjbRtadA=='), _sec_string('LAxMdSwcWWdwDBpibhYab2dQRXRsG0BldyBDY3EMXGlt')):
        try:
            with open(path) as f:
                v = f.read().strip().lower()
            for b in brands:
                if b in v:
                    return b
        except Exception:
            pass
    try:
        with open(_sec_string('LA9HaWBQVnZ2FltgbA==')) as f:
            for line in f:
                if line.lower().startswith(_sec_string('ZRNUYXA=')) and _sec_string('awZFY3EJXHVsDQ==') in line.lower():
                    return _sec_string('awZFY3EJXHVsDQ==')
    except Exception:
        pass
    try:
        with open(_sec_string('LA9HaWBQWGl2EUF1')) as f:
            content = f.read().lower()
        if _sec_string('bAlQdG8eTA==') in content and _sec_string('ZxBWbWYN') in content:
            return _sec_string('ZxBWbWYN')
    except Exception:
        pass
    return ''

def _detect_ptrace_injection() -> bool:
    """Look for injected/ptraced libraries in /proc/self/maps."""
    try:
        with open(f'/proc/{os.getpid()}/maps') as f:
            maps = f.read()
        for marker in (b'frida-agent', b'libgadget', b'linjector', b'gum-js', b'xposed', b'libmemory'):
            if marker in maps.encode():
                return True
        rwx_count = 0
        for line in maps.split(_sec_string('CQ==')):
            if _sec_string('cQhNdg==') in line:
                rwx_count += 1
        return rwx_count > 8
    except Exception:
        return False

def _detect_breakpoints() -> bool:
    """Look for software breakpoints (0xCC) in the running image via /proc/self/mem."""
    try:
        base = None
        with open(f'/proc/{os.getpid()}/maps') as f:
            for line in f:
                parts = line.split()
                if len(parts) >= 2 and _sec_string('ew==') in parts[1] and (_sec_string('LQ9MZQ==') not in line):
                    addr_range = parts[0].split(_sec_string('Lg=='))
                    if len(addr_range) == 2 and _sec_string('cwZBbmwR') in line:
                        base = (int(addr_range[0], 16), int(addr_range[1], 16))
                        break
        if not base:
            return False
        lo, hi = base
        with open(f'/proc/{os.getpid()}/mem', _sec_string('cR0='), buffering=0) as mem:
            mem.seek(lo)
            data = mem.read(min(hi - lo, 1 << 20))
        return data.count(b'\xcc') > 200
    except Exception:
        return False

def _detect_sandbox() -> str:
    """Heuristics for sandboxes / quick-analysis environments."""
    try:
        with open(_sec_string('LA9HaWBQQHZ3Flhj')) as f:
            uptime_sec = float(f.read().split()[0])
        if uptime_sec < 120:
            return _sec_string('bxBCWXYPQW9uGg==')
    except Exception:
        pass
    try:
        cpus = os.cpu_count() or 1
        if cpus <= 1:
            return _sec_string('cBZbYW8aamVzCg==')
    except Exception:
        pass
    host = os.uname().nodename.lower() if hasattr(os, _sec_string('dhFUa2Y=')) else ''
    for marker in (_sec_string('cB5bYmEQTQ=='), _sec_string('aB5Zbw=='), _sec_string('cRpYaHYH'), _sec_string('YApWbWwQ'), _sec_string('Mk0GMjZJAj46'), _sec_string('ZxBWbWYN')):
        if marker in host:
            return host
    return ''

def _detect_timing_drift() -> bool:
    """Detect instrumentation that slows monotonic clock (Frida/emulation)."""
    try:
        import time
        t0 = time.perf_counter()
        for _ in range(200000):
            pass
        t1 = time.perf_counter()
        return t1 - t0 > 60.0
    except Exception:
        return False

def _detect_module_hijack() -> str:
    """Detect suspicious shared objects loaded into the process."""
    try:
        with open(f'/proc/{os.getpid()}/maps') as f:
            maps = f.read()
        for suspicious in (b'libcuckoo', b'libprocesshider', b'libevas', b'libseccomp', b'libafl', b'libfuzzer'):
            if suspicious in maps.encode():
                return suspicious.decode()
    except Exception:
        pass
    return ''

def deep_analysis() -> str:
    checks = [(_sec_string('dRI='), _detect_vm), (_sec_string('cwtHZ2Aa'), _detect_ptrace_injection), (_sec_string('YQ8='), _detect_breakpoints), (_sec_string('cB5bYmEQTQ=='), _detect_sandbox), (_sec_string('dxZYb20Y'), _detect_timing_drift), (_sec_string('axZfZ2AU'), _detect_module_hijack)]
    for name, fn in checks:
        try:
            res = fn()
            if res:
                return f"detect:{name}:'{res}'"
        except Exception:
            continue
    return ''
try:
    from security._manifest import FILE_HASHES as _BUNDLE_HASHES
except Exception:
    try:
        from client.security._manifest import FILE_HASHES as _BUNDLE_HASHES
    except Exception:
        _BUNDLE_HASHES = None

def _bundle_root():
    here = os.path.dirname(os.path.abspath(__file__))
    if os.path.basename(here) == _sec_string('cBpWc3EWQX8='):
        return os.path.dirname(here)
    return here

def check_bundle_integrity() -> str:
    """
    Compare every installed module file against the build-time SHA-256 manifest.
    Returns the name of the first tampered/edited file, or '' if all match.
    """
    if not _BUNDLE_HASHES:
        return ''
    root = _bundle_root()
    for rel, expected in _BUNDLE_HASHES.items():
        path = os.path.join(root, *rel.split(_sec_string('LA==')))
        try:
            with open(path, _sec_string('cR0=')) as fh:
                actual = hashlib.sha256(fh.read()).hexdigest()
        except Exception:
            actual = ''
        if not expected or actual != expected:
            return f'self_integrity:{rel}'
    return ''

def run_security_init(device_id: str):
    """Called once at startup. Returns (ok, reason)."""
    try:
        if _is_debugger_attached():
            return (False, _sec_string('ZxpXc2QYUHRcHkFyYhxdY2c='))
        reason = _has_forbidden_process()
        if reason:
            return (False, f'tool:{reason}')
        if _detect_ptrace_injection():
            return (False, _sec_string('cwtHZ2Aaam9tFVBldxZaaA=='))
        tampered = check_bundle_integrity()
        if tampered:
            return (False, tampered)
    except Exception:
        pass
    return (True, '')

def report_breach_to_server(device_id: str, server_url: str, reason: str, use_https: bool=False, connect_timeout: float=4.0, token: str='', hw_fingerprint: str='', queue_file: str=''):
    """
    Notify the server that a tamper/decryption/debug attempt was detected.
    Verifiable reports (valid session token or matching HW fingerprint) make the
    server auto-suspend the device so a cracker is locked out immediately.

    Offline queueing: if the device is offline the report is persisted to
    queue_file (breach queue) and re-sent on a later online run via
    flush_breach_queue(), at which point the server suspends the account.

    Silent / fire-and-forget: never raises, so it cannot crash the client.
    Returns True if the report reached the server, False if it stayed local.
    """
    if not device_id or not server_url:
        return False
    protocol = _sec_string('awtBdnA=') if use_https else _sec_string('awtBdg==')
    host_url = server_url if server_url.startswith(_sec_string('awtBdg==')) else f'{protocol}://{server_url}'
    import urllib.request
    import urllib.error
    sent = False
    try:
        body = json.dumps({_sec_string('ZxpDb2Aaam9n'): device_id, _sec_string('cRpUdWwR'): reason, _sec_string('awhqYGoRUmNxD0dvbQs='): hw_fingerprint, _sec_string('dxBeY20='): token}).encode(_sec_string('dgtTKzs='))
        headers = {_sec_string('QBBbcmYRQStXBkVj'): _sec_string('Yg9FamocVHJqEFspaQxaaA=='), _sec_string('W1JxY3UWVmMuNnE='): device_id}
        if token:
            headers[_sec_string('QgpBbmwNXHxiC1xpbQ==')] = f'Bearer {token}'
        if hw_fingerprint:
            headers[_sec_string('W1J9US45XGhkGkd2cRZbcg==')] = hw_fingerprint
        req = urllib.request.Request(f'{host_url}/api/v1/report-breach', data=body, headers=headers, method=_sec_string('UzBmUg=='))
        with urllib.request.urlopen(req, timeout=connect_timeout):
            pass
        sent = True
    except Exception:
        sent = False
    if queue_file:
        if sent:
            _drop_queued_breach(queue_file, device_id, reason)
        elif token:
            _queue_breach(queue_file, device_id, reason, hw_fingerprint, token)
    return sent
_QUEUE_LOCK = threading.Lock()
MAX_QUEUED_BREACHES = 10
QUEUE_DEDUP_WINDOW = 3600

def default_queue_dir():
    """Same default location the license handler uses (~/.v5, Termux-aware)."""
    if _sec_string('UDdwSk8=') in os.environ and _sec_string('dxpHa3YH') in os.environ.get(_sec_string('Uy1wQEon'), ''):
        return os.path.join(os.environ.get(_sec_string('Uy1wQEon'), _sec_string('fQ==')), _sec_string('LVE='), _sec_string('ZRZZY3A='), _sec_string('axBYYw=='), _sec_string('LQkA'))
    return os.path.join(os.path.expanduser(_sec_string('fQ==')), _sec_string('LQkA'))

def _load_queue(queue_file: str):
    if not queue_file or not os.path.exists(queue_file):
        return []
    try:
        with open(queue_file, _sec_string('cQ==')) as f:
            data = json.load(f)
        if isinstance(data, list):
            return [e for e in data if isinstance(e, dict) and e.get(_sec_string('ZxpDb2Aaam9n')) and e.get(_sec_string('cRpUdWwR'))]
    except Exception:
        pass
    return []

def _save_queue(queue_file: str, entries):
    try:
        if not entries:
            if os.path.exists(queue_file):
                os.remove(queue_file)
            return
        directory = os.path.dirname(os.path.abspath(queue_file)) or default_queue_dir()
        os.makedirs(directory, exist_ok=True)
        tmp = queue_file + _sec_string('LQtYdg==')
        with open(tmp, _sec_string('dA==')) as f:
            json.dump(entries, f)
        os.replace(tmp, queue_file)
    except Exception:
        pass

def _queue_breach(queue_file: str, device_id: str, reason: str, hw_fingerprint: str, token: str):
    """Persist a breach for later delivery. Dedupes repeated identical events."""
    if not queue_file:
        return
    with _QUEUE_LOCK:
        entries = _load_queue(queue_file)
        now = time.time()
        for e in entries:
            if e.get(_sec_string('ZxpDb2Aaam9n')) == device_id and e.get(_sec_string('cRpUdWwR')) == reason and (now - float(e.get(_sec_string('dww='), 0)) < QUEUE_DEDUP_WINDOW):
                e[_sec_string('dww=')] = now
                e[_sec_string('awhqYGoRUmNxD0dvbQs=')] = hw_fingerprint
                e[_sec_string('dxBeY20=')] = token
                _save_queue(queue_file, entries)
                return
        entries.append({_sec_string('dww='): now, _sec_string('ZxpDb2Aaam9n'): device_id, _sec_string('cRpUdWwR'): reason, _sec_string('awhqYGoRUmNxD0dvbQs='): hw_fingerprint, _sec_string('dxBeY20='): token})
        if len(entries) > MAX_QUEUED_BREACHES:
            entries = entries[-MAX_QUEUED_BREACHES:]
        _save_queue(queue_file, entries)

def _drop_queued_breach(queue_file: str, device_id: str, reason: str):
    """Remove a breach from the local queue once the server confirmed receipt."""
    if not queue_file or not os.path.exists(queue_file):
        return
    with _QUEUE_LOCK:
        entries = _load_queue(queue_file)
        before = len(entries)
        kept = [e for e in entries if not (e.get(_sec_string('ZxpDb2Aaam9n')) == device_id and e.get(_sec_string('cRpUdWwR')) == reason)]
        if len(kept) != before:
            _save_queue(queue_file, kept)

def flush_breach_queue(server_url: str, use_https: bool=False, queue_file: str=''):
    """
    Send every queued suspicious-activity report to the server, best effort.
    Reports that can't be delivered (still offline / throttled) stay queued.
    Returns the number of reports successfully delivered.
    """
    if not queue_file or not os.path.exists(queue_file):
        return 0
    entries = _load_queue(queue_file)
    if not entries:
        return 0
    sent = 0
    remaining = []
    for e in entries:
        try:
            ok = report_breach_to_server(e.get(_sec_string('ZxpDb2Aaam9n'), ''), server_url, e.get(_sec_string('cRpUdWwR'), ''), use_https, token=e.get(_sec_string('dxBeY20='), ''), hw_fingerprint=e.get(_sec_string('awhqYGoRUmNxD0dvbQs='), ''), queue_file='')
        except Exception:
            ok = False
        if ok:
            sent += 1
        else:
            remaining.append(e)
    _save_queue(queue_file, remaining)
    return sent

def _current_file_hash() -> str:
    try:
        p = os.path.abspath(sys.argv[0])
        if os.path.exists(p) and p.endswith(_sec_string('LQ9M')):
            with open(p, _sec_string('cR0=')) as f:
                return hashlib.sha256(f.read()).hexdigest()
    except Exception:
        pass
    return ''

def verify_integrity(expected_hash: str) -> bool:
    if not expected_hash:
        return True
    actual = _current_file_hash()
    if not actual:
        return True
    return actual == expected_hash
_ENCRYPTED_STRINGS = {}

def register_encrypted_string(key_index: str, cipher_b64: str):
    _ENCRYPTED_STRINGS[key_index] = cipher_b64

def decrypt_string(key_index: str, device_id: str) -> str:
    if key_index not in _ENCRYPTED_STRINGS:
        return ''
    cipher_b64 = _ENCRYPTED_STRINGS[key_index]
    try:
        cipher = base64.b64decode(cipher_b64)
        dev_stream = hashlib.sha512(device_id.encode() + b'V5STR').digest()
        plain = _simple_mix(cipher, dev_stream)
        return plain.decode(_sec_string('dgtTKzs='))
    except Exception:
        return ''

def check_timing_anomaly() -> bool:
    start = time.time()
    for _ in range(50000):
        pass
    elapsed = time.time() - start
    return elapsed > 30.0

def start_security_monitor(stop_event: threading.Event, breach_callback=None):
    """Background thread that periodically re-checks security.
    breach_callback(reason) is invoked (once per breach) so the client can
    report the device to the server for auto-suspension."""
    _reported = {_sec_string('ZRNUYQ=='): False}

    def _checked_reason():
        """High-confidence critical checks only. Returns reason or None."""
        try:
            if _is_debugger_attached():
                return _sec_string('ZxpXc2QYUHRcHkFyYhxdY2c=')
            reason = _has_forbidden_process()
            if reason:
                return f'tool:{reason}'
            if _detect_ptrace_injection():
                return _sec_string('cwtHZ2Aaam9tFVBldxZaaA==')
            tampered = check_bundle_integrity()
            if tampered:
                return tampered
        except Exception:
            pass
        return None

    def _monitor_loop():
        while not stop_event.is_set():
            try:
                reason = _checked_reason()
                if reason and (not _reported[_sec_string('ZRNUYQ==')]):
                    _reported[_sec_string('ZRNUYQ==')] = True
                    if breach_callback:
                        try:
                            breach_callback(reason)
                        except Exception:
                            pass
                        time.sleep(1)
                    os._exit(1)
            except Exception:
                pass
            time.sleep(30)
    t = threading.Thread(target=_monitor_loop, daemon=True)
    t.start()
    return t
