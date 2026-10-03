# Auto-generated obfuscated build (do not edit)
_SEC_SALT = 2839264508

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
Universal ANYISP Scanner - One install, both engines.
The server decides (per user) which engine this device runs: V5 or V6.
After activation the assigned version is stored locally, and every heartbeat
re-checks the panel setting so flipping V5<->V6 takes effect on next run.
"""
import os
import sys
import time
import json
import base64
import hashlib
import asyncio
import platform
import threading
import subprocess
from datetime import datetime
CLIENT_VERSION = _sec_string('nhWM0pk=')
try:
    from security.core import get_device_id, get_hw_fingerprint, run_security_init, get_build_props
    from security.license import LicenseHandler, LicenseError
    SECURITY_AVAILABLE = True
except ImportError:
    try:
        from client.security.core import get_device_id, get_hw_fingerprint, run_security_init, get_build_props
        from client.security.license import LicenseHandler, LicenseError
        SECURITY_AVAILABLE = True
    except ImportError:
        SECURITY_AVAILABLE = False
SERVER_URL = _sec_string('wU/IjNoBk9PfDpGKnxbencpQ2ZLNFdOS217SmMxJkp/GVg==')
SERVER_PORT = 443
USE_HTTPS = True
CLIENT_BUILD = _sec_string('mBWO0pgN')
TIMEOUT = 15
COLORS = {_sec_string('217Y'): _sec_string('smCNx5oK0Q=='), _sec_string('zknZmcc='): _sec_string('smCNx5oJ0Q=='), _sec_string('0F7QkMZM'): _sec_string('smCNx5oI0Q=='), _sec_string('y1fJmQ=='): _sec_string('smCNx5oP0Q=='), _sec_string('xFrbmcdP3Q=='): _sec_string('smCNx5oO0Q=='), _sec_string('ykLdkg=='): _sec_string('smCNx5oN0Q=='), _sec_string('3lPViMw='): _sec_string('smCNx5oM0Q=='), _sec_string('217Pmd0='): _sec_string('smCMkQ=='), _sec_string('zVLR'): _sec_string('smCOkQ==')}

def c(color, text):
    return f"{COLORS.get(color, COLORS[_sec_string('217Pmd0=')])}{text}{COLORS[_sec_string('217Pmd0=')]}"

def show_device_id():
    if not SECURITY_AVAILABLE:
        print(c(_sec_string('217Y'), _sec_string('+l7fidtSyIWJVtOY3FfZ3NxV3YrIUtCdy1fZ')))
        return
    device_id = get_device_id()
    print(c(_sec_string('ykLdkg=='), _sec_string('7X7qtep+nLXtG/+z+WKG3A==')) + c(_sec_string('zknZmcc='), device_id))
    print(c(_sec_string('zVLR'), _sec_string('+l7SmIlP1JXaG/W4iU/T3N1T2dzIX9GVxxvIk4la34jATd2IzBvFk9xJnJDAWNmS2l6S')))
    input(c(_sec_string('0F7QkMZM'), _sec_string('o2vOmdpInLnHT9mOiU/T3MpU0ojAVcmZhxWS')))

def show_logo():
    art = _sec_string('oxuc3IkbnNyJG5zciRuc3IlkkNKEFpHRhBWQo6MbnNyJG5zciRuc3IkbnNyFFsLciRuc3IkbnNyJG8LRhzGc3IkbnNyJG5zciRuc3IVl46P2G5zciRuc3IkbnNz2ZOOihzGc3IkbnNyJG5zciRuTgosbnNzXGZzciRWc3IkZwtyJG56C9TGc3IkbnNyJG5zciWKc3IUWkdL2G5zciXKc3Ikb49KEFpLciWK23IkbnNyJG5zciRucgIlinNyJG5yChBWcgIkXkYKJG5zciWKcgKMbnNyJG5zciRuc3IlHnICJG5zciRuc3NRGhofSG5zciRuc3IlHnICjG5zciRuc3IkbnNyJUZyQiRuc3IkbnNOJR5ygiRuc3IkbnN2JV7bciRuc3IkbnNyHFsLciRPjo4UVkdGLG5Kihxue0YQVkKP2Epzc1xaS9okbnNyJG5zcgRuc3IkbnNyJG5zchhuT3NUb4Nz1G5zciRuc3IkbnNyAMZzciRuc3IkbnKCHZOOj9hec3IlFnNz1FJ6ghhucgokbnNL2ZOOjhRS23IkbnNyJG5zciWWSo/Zk49yJG5zciRuc3IkbnNyJG5zc9mTjo4dlttyJG5zciRuc3IkbnNzVG8CoiUXg3IkanNyJGpzchkWcqNUbwPaJG5zciRuc3IkbnNyJR5yAxRuc3PYb49z2G+Pc9huc3IhHnICjG5zciRuc3IkbnNyJG8DcxRvg0/8b6tz/G+rc/xvqoIYb1tzVMZzciRuc3IkbnNyJG5yQiRvg3PVH44D2R+OA9kfjgIYbk9yJGrbciRuc3IkbnNyJG5zciWec3PVg6Nz9G+jc/Rvo3P1yk9yJFLbciRuc3IkbnNyJG5zciRvg3Ilb4tH3FuLR9xbi0fccnNyGMZzciRuc3IkbnNyJG5zciRvg3IkbnNyJG5zciRuc3Ikbk/aJG5zciRuc3IkbnNyJG5zciWeS3IkbnNyJG5zciRuQ06MbnNyJG5zciRuc3IkbnNyJG5zci2WR0vZk49CEZZ72')
    print(c(_sec_string('217Y'), art))
    print(c(_sec_string('y1fJmQ=='), _sec_string('6HXltfprnK/ncpy64HX4ufsb77/7cuyoiQmMzp8blKnncuq5+2j9sIA=')))
    print(c(_sec_string('xFrbmcdP3Q=='), _sec_string('5mzyufsBnJTdT8yPkxSTiIdW2dPhWt+XzEnMjsBW2c6cDw==')))

def clear_screen():
    os.system(_sec_string('ylfZnds=')) if os.name == _sec_string('2VTPldE=') else os.system(_sec_string('ylfP'))

def run_security_check(handler=None):
    if not SECURITY_AVAILABLE:
        return True
    device_id = get_device_id()
    ok, reason = run_security_init(device_id)
    if not ok:
        print(c(_sec_string('217Y'), f'Security check failed: {reason}'))
        return False
    return True

def first_time_activation(handler):
    clear_screen()
    show_logo()
    print(c(_sec_string('0F7QkMZM'), '  Local lifetime mode enabled.'))
    print(c(_sec_string('ykLdkg=='), f'  Device: {handler.device_id}'))
    handler.activate({})
    print(c(_sec_string('zknZmcc='), '  Lifetime license created locally.'))
    print(c(_sec_string('ykLdkg=='), f'  Engine: {handler.get_assigned_version().upper()}'))
    time.sleep(0.5)

def run_assigned_engine(handler, version):
    """
    version: the server-assigned engine, 'v5' or 'v6'.
    Runs the matching ORIGINAL premium engine so the panel choice
    is what the end user actually runs - nothing else.
    """
    if version == _sec_string('3w0='):
        mod = _sec_string('3w3jmcdc1ZLM')
    else:
        mod = _sec_string('3w7jmcdc1ZLM')
    try:
        engine = __import__(mod)
    except ImportError as e:
        print(c(_sec_string('217Y'), f'Could not load the {version.upper()} engine: {e}'))
        print(c(_sec_string('0F7QkMZM'), _sec_string('+lTRmYlX1Z7bWs6VzEickchCnJ7MG9GV2kjVks4VnK7MFs6JxwGcnshI1NzAVc+IyFfQ0tpTnNTGSZyMwEuclcdIyJ3FV5yIwV6ckcBIz5XHXJyMyFjXnc5eldI=')))
        input(c(_sec_string('0F7QkMZM'), _sec_string('+UnZj9ob+ZLdXs7ShxU=')))
        return
    engine.SERVER_DAYS_REMAINING = handler.days_remaining()
    engine.run_engine()

def make_activation_config():
    return {_sec_string('2l7OisxJ44nbVw=='): SERVER_URL, _sec_string('2VTOiA=='): SERVER_PORT, _sec_string('3EjZo8FPyIza'): USE_HTTPS, _sec_string('3VLRmcZOyA=='): TIMEOUT}

def try_refresh_activation(handler, attempts=2):
    try:
        handler.activate({})
        return True
    except LicenseError:
        return False

def _wipe_config(handler):
    """Remove the saved activation so a fresh one can be issued (config only)."""
    try:
        if handler.is_configured() and os.path.exists(handler.config_path):
            os.remove(handler.config_path)
    except Exception:
        pass
    try:
        if os.path.exists(handler.breach_queue_path):
            os.remove(handler.breach_queue_path)
    except Exception:
        pass

def handle_cli_command(handler):
    """scanner --refresh  /  scanner --reset  /  scanner --forced-refresh"""
    args = sys.argv[1:]
    if not args:
        return False
    cmd = args[0].lower().lstrip(_sec_string('hA=='))
    if cmd in (_sec_string('217Pmd0='), _sec_string('217VktpP3ZDF')):
        _wipe_config(handler)
        print(c(_sec_string('zknZmcc='), _sec_string('5lfY3MhYyJXfWsiVxlWcn8Ve3Y7MX5Lc+k/djt1S0puJXc6Z2lOcncpP1YrIT9WTxxWS0g==')))
        first_time_activation(handler)
        return True
    if cmd in (_sec_string('217ajsxI1A=='), _sec_string('214='), _sec_string('217Smd4='), _sec_string('z1TOn8xfkY7MXc6Z2lM='), _sec_string('216RncpP1YrIT9k=')):
        if not handler.is_configured():
            print(c(_sec_string('0F7QkMZM'), _sec_string('51Scj8hN2ZiJWt+IwE3diMBU0tzPVMmSzRWcrtxV0pXHXJyawEnPiIRP1ZHMG92f3VLKnd1S05KHFZI=')))
            first_time_activation(handler)
            return True
        print(c(_sec_string('ykLdkg=='), _sec_string('+17ajsxI1JXHXJydyk/VishP1ZPHG9qOxlacj8xJypnbFZLS')))
        if try_refresh_activation(handler, attempts=3):
            print(c(_sec_string('zknZmcc='), _sec_string('o3/TkswVnL3KT9WKyE/Vk8cbzpnPSdmPwV7Y3IQb1onaT5yO3FWc29pY3ZLHXs7biU/T3NpP3Y7dFQ==')))
        else:
            print(c(_sec_string('217Y'), _sec_string('o2nZmttez5SJXd2VxV7Y0olv1JmJSNmO317O3NpaxY+JT9SV2hvYmd9S35mJUs/cx1TI3MhYyJXfXpI=')))
            print(c(_sec_string('0F7QkMZM'), _sec_string('6lTSiMhYyNzpc92fwl7OjNtS0ZmbDojcgVPIiNlIhtOGT5KRzBT0ncpQ2Y7ZSdWRzAmJyIAb3ZLNG8+Zx1+ciMFSz9zNXsqVyl6cte0B')))
            print(c(_sec_string('ykLdkg=='), handler.device_id))
        return True
    return False

def main():
    clear_screen()
    print(c(_sec_string('zknZmcc='), f'  ANYISP SCANNER  [build {CLIENT_BUILD}]  '))
    try:
        handler = LicenseHandler()
    except LicenseError as e:
        print(c(_sec_string('217Y'), f'License error: {e}'))
        sys.exit(1)

    handler.breach_callback = None
    if handle_cli_command(handler):
        return
    if not run_security_check(handler):
        print(c(_sec_string('0F7QkMZM'), _sec_string('iRvn3fQb75nKTs6V3UKcnc1N1Y/GScXcyFjIld9enNGJWNOS3VLSicBV29I=')))
    if not handler.is_configured():
        try:
            first_time_activation(handler)
        except LicenseError as e:
            print(c(_sec_string('217Y'), f'Activation failed: {e}'))
            input(c(_sec_string('0F7QkMZM'), _sec_string('+UnZj9ob+ZLdXs7c3VScmdFSyNKHFQ==')))
            sys.exit(1)
    hb = None
    try:
        hb = handler.heartbeat(USE_HTTPS)
    except Exception:
        hb = None
    if hb is False:
        print(c(_sec_string('217Y'), _sec_string('o3r/v+xo79ztfvK17H+cHimvnKjBUs/c2ljOldlPnJXaG9KTiVfTks5eztzIWMiV316S')))
        print(c(_sec_string('0F7QkMZM'), _sec_string('/VPVj4lOz4nIV9CFiVbZncdInIjBXpyQwFjZktpenIvISJyOzE3Tl8xfk47MVdmLzF+ck8cbyJTMG8+Z203Zjoc=')))
        print(c(_sec_string('0F7QkMZM'), _sec_string('8FTJ3Mpa0tzbXtqOzEjU3NBUyY6JWt+IwE3diMBU0tzbUtuU3RvSk94bkdzHVJyOzFLSj91a0JCJVdmZzV7Y0g==')))
        choice = input(c(_sec_string('0F7QkMZM'), _sec_string('o2nZmttez5SJWt+IwE3diMBU0tzPSdORiUjZjt9eztzHVMvDiRPF08cShtw='))).strip().lower()
        refreshed = False
        if choice in (_sec_string('0A=='), '', _sec_string('217ajsxI1A==')):
            refreshed = try_refresh_activation(handler)
            if refreshed:
                try:
                    hb = handler.heartbeat(USE_HTTPS)
                except Exception:
                    hb = None
    if hb is False:
        print(c(_sec_string('217Y'), _sec_string('6Hj/ufponLjsdfW57RtefD0b6JTASJyPyknVjN0b1Y+JVdPcxVTSm8xJnJ3KT9WKzBU=')))
        print(c(_sec_string('0F7QkMZM'), _sec_string('/VPZ3NpezorMSZyPyELP3N1T1Y+JX9mKwFjZ3MpOzo7MVciQ0BvUndob8rOJWt+IwE3Z3MVS35nHSNnS')))
        print(c(_sec_string('0F7QkMZM'), _sec_string('+l7SmIlP1JXaG/i5/3L/uYly+NzdVJyIwV6cnc1W1ZKJT9PcyFjIld9ayJmGSdmSzEyG')))
        print(c(_sec_string('ykLdkg=='), f'  {handler.device_id}'))
        print(c(_sec_string('0F7QkMZM'), _sec_string('+16RjtxVnNvaWN2Sx17O3IQWzpnPSdmPwRycnc9P2Y6JT9SZiVrYkcBVnI7MWt+IwE3diMxInIXGTpzUxkmcld0by5XFV5yOzF3OmdpTnJXdSNmQzxvTkolP1JmJVdmE3RvOiccSkg==')))
        print(c(_sec_string('0F7QkMZM'), _sec_string('6lTSiMhYyNzpc92fwl7OjNtS0ZmbDojcgVPIiNlIhtOGT5KRzBT0ncpQ2Y7ZSdWRzAmJyIAbyJOJWt+IwE3diMwb046JSdmSzEyS')))
        input(c(_sec_string('0F7QkMZM'), _sec_string('+UnZj9ob+ZLdXs7ShxU=')))
        sys.exit(1)
    status = handler.validate()
    if status == _sec_string('zEPMldte2A=='):
        print(c(_sec_string('0F7QkMZM'), _sec_string('oxucp4hmnLDGWN2QiV7EjMBJxdzZWs+PzF+S3Pte2o7MSNSVx1ycmttU0dzaXs6KzEmS0oc=')))
        if try_refresh_activation(handler):
            status = handler.validate()
    if status == _sec_string('zEPMldte2A=='):
        print(c(_sec_string('217Y'), _sec_string('+njutflvnLnxa/Wu7H+cHimvnKXGTs7cyFjfmdpInJTISJyZx1/ZmIc=')))
        print(c(_sec_string('0F7QkMZM'), _sec_string('6lTSiMhYyNzpc92fwl7OjNtS0ZmbDojcgVPIiNlIhtOGT5KRzBT0ncpQ2Y7ZSdWRzAmJyIAbyJOJSdmSzEyS')))
        input(c(_sec_string('0F7QkMZM'), _sec_string('+UnZj9ob+ZLdXs7ShxU=')))
        sys.exit(1)
    elif status == _sec_string('x1TIo8pU0prAXMmOzF8='):
        print(c(_sec_string('217Y'), _sec_string('51TI3MpU0prAXMmOzF+S3PtekY7cVZydyk/VishP1ZPHFQ==')))
        sys.exit(1)
    elif status == _sec_string('3VrRjMxJ2Zg='):
        print(c(_sec_string('217Y'), _sec_string('5VLfmcdI2dzPUtCZiVLSiMxczpXdQpyfxlbMjsZW1Y/MX5I=')))
        input(c(_sec_string('0F7QkMZM'), _sec_string('+UnZj9ob+ZLdXs7ShxU=')))
        sys.exit(1)
    elif status != _sec_string('31rQlc0='):
        print(c(_sec_string('217Y'), _sec_string('5VLfmcdI2dzAVcqdxVLY0g==')))
        sys.exit(1)
    try:
        policy_ok = handler.fetch_policy(USE_HTTPS)
        if policy_ok is False:
            refreshed = try_refresh_activation(handler)
            if refreshed:
                try:
                    policy_ok = handler.fetch_policy(USE_HTTPS)
                except Exception:
                    policy_ok = None
        if policy_ok is False:
            print(c(_sec_string('217Y'), _sec_string('6Hj/ufponLjsdfW57RtefD0b6JTASJyPyknVjN0b1Y+JVdPcxVTSm8xJnJ3KT9WKzBU=')))
            print(c(_sec_string('0F7QkMZM'), _sec_string('6lTSiMhYyNzpc92fwl7OjNtS0ZmbDojcgVPIiNlIhtOGT5KRzBT0ncpQ2Y7ZSdWRzAmJyIAbyJOJSdmSzEyS')))
            input(c(_sec_string('0F7QkMZM'), _sec_string('+UnZj9ob+ZLdXs7ShxU=')))
            sys.exit(1)
    except Exception:
        policy_ok = None
    if not handler.has_fresh_policy():
        print(c(_sec_string('0F7QkMZM'), _sec_string('8FTJ3MROz4iJWNOSx17fiIlP09zdU9nc2l7OisxJnJ3dG9CZyEjI3MZV35mJTNWIwVLS3N1T2dzZVNCVykKci8BV2JPe')))
        print(c(_sec_string('0F7QkMZM'), _sec_string('y17ak9tenInaUtKbiUjfncdV1ZLOFZyowVLP3MpU0prASdGPiULTidsb0JXKXtKPzBvVj4la34jATdnS')))
        print(c(_sec_string('ykLdkg=='), _sec_string('+VfZndpenJ/BXt+XiULTidsb1ZLdXs6SzE+cn8ZV0pnKT9WTxxvdks0bzonHG9yPylrSksxJ3NzIXN2VxxvTksVS0pmH')))
        input(c(_sec_string('0F7QkMZM'), _sec_string('+UnZj9ob+ZLdXs7ShxU=')))
        sys.exit(1)
    version = handler.get_assigned_version()
    print(c(_sec_string('ykLdkg=='), f'Engine: {version.upper()}  (assigned by server)'))
    time.sleep(1)
    run_assigned_engine(handler, version)
if __name__ == _sec_string('9mTRncBV46M='):
    try:
        main()
    except KeyboardInterrupt:
        print(c(_sec_string('0F7QkMZM'), _sec_string('o37Eld1S0puHFZI=')))
        sys.exit(0)
    except Exception as e:
        print(c(_sec_string('217Y'), f'Fatal error: {e}'))
        input(c(_sec_string('0F7QkMZM'), _sec_string('+UnZj9ob+ZLdXs7ShxU=')))
        sys.exit(1)
