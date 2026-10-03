# Auto-generated obfuscated build (do not edit)
_SEC_SALT = 3065579788

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
V6 ANYISP SNI FINDER SCRIPT 2026 PREMIUM
- Auto-adjusts to terminal width (zoom in/out safe)
- Universal back-to-main-menu on every prompt
- Menu renumbered uniformly 1-9
- Proxy scanner logo fixed
- V6 gradient menu, art alignment fixed
"""
import asyncio
import aiohttp
import ipaddress
import ssl
import socket
import re
import pyperclip
import shutil
import time
import sys
import json
from colorama import init, Fore, Style
from tqdm import tqdm
import hashlib
import datetime
import requests
from bs4 import BeautifulSoup
import os
import multithreading
import websocket
import subprocess
from colorama import Fore, Style, init
try:
    import pycurl
except Exception:
    pycurl = None
from io import BytesIO
import subprocess
import signal
from termcolor import colored
import math
import random
import string
from concurrent.futures import ThreadPoolExecutor, as_completed, wait, FIRST_COMPLETED
import urllib.parse
from urllib.parse import urlparse
from collections import OrderedDict, deque
import platform
import threading
import queue
import select
from dataclasses import dataclass, field
try:
    import dns.resolver
    DNS_AVAILABLE = True
except ImportError:
    DNS_AVAILABLE = False
init(autoreset=True)
RESULTS_FILE = _sec_string('4I8neM7N')
STATE_FILE = _sec_string('xdpoYunKfW3C3CdmxdZn')
BACK_TOKENS = (_sec_string('1NhqZw=='), _sec_string('08FgeA=='), _sec_string('x8xgeA=='), _sec_string('xw=='), _sec_string('29xneQ=='), _sec_string('29hgYg=='))
RESET_C = _sec_string('reI5YQ==')
FIRE_1 = (255, 40, 0)
FIRE_2 = (255, 200, 40)
CYAN_1 = (0, 200, 255)
CYAN_2 = (0, 100, 200)
PINK_1 = (255, 60, 150)
PINK_2 = (200, 20, 100)
SOFT_CYAN = _sec_string('reI6NI2LMj2DiTI+hYkyPoOMZA==')
GOLD = _sec_string('reI6NI2LMj6DjDI+hokyOIbU')
WHITE_B = _sec_string('reI4N4WOZA==')
DIM_GRAY = _sec_string('reI6NI2LMj2EiTI9hIkyPYSJZA==')
ORANGE = _sec_string('reI6NI2LMj6DjDI9gokyPNs=')
HOT_PINK = _sec_string('reI6NI2LMj6DjDI0hoI4NIbU')

def grad(text, c1, c2):
    if not text:
        return ''
    n = len(text)
    out = []
    for i, ch in enumerate(text):
        t = i / max(n - 1, 1)
        r = int(c1[0] + (c2[0] - c1[0]) * t)
        g = int(c1[1] + (c2[1] - c1[1]) * t)
        b = int(c1[2] + (c2[2] - c1[2]) * t)
        out.append(f'\x1b[38;2;{r};{g};{b}m{ch}')
    return ''.join(out) + RESET_C

def is_back(text):
    return isinstance(text, str) and text.strip().lower() in BACK_TOKENS

def ask(prompt, allow_back=True):
    """Input wrapper. Returns None if user typed a back token."""
    try:
        val = input(prompt).strip()
    except (EOFError, KeyboardInterrupt):
        print()
        return None
    if allow_back and is_back(val):
        return None
    return val

def term_width(default=100):
    try:
        t = shutil.get_terminal_size()
        columns = t.columns if t and t.columns else 0
    except Exception:
        columns = 0
    if columns <= 0:
        return default
    return max(24, min(columns, 200))

def term_lines(default=30):
    try:
        t = shutil.get_terminal_size()
        lines = t.lines if t and t.lines else 0
    except Exception:
        lines = 0
    if lines <= 0:
        return default
    return max(10, min(lines, 200))

def disp_width(text):
    """Visible column width of a string (CJK/emoji count double).

    Box-drawing/block glyphs (U+2500-U+257F) render narrow on Termux and
    are counted as 1; ambiguous symbols are conservatively counted as 2 so
    lines can never exceed the terminal width (no wrap/overlap).
    """
    import unicodedata as _ud
    total = 0
    for ch in text:
        cp = ord(ch)
        if 65024 <= cp <= 65039 or cp == 8205:
            continue
        cat = _ud.category(ch)
        if cat in (_sec_string('+9c='), _sec_string('+9w='), _sec_string('9d8=')):
            continue
        if 9472 <= cp <= 9599:
            total += 1
            continue
        if 4352 <= cp <= 4447 or 11904 <= cp <= 12350 or 12353 <= cp <= 13311 or (13312 <= cp <= 19903) or (19968 <= cp <= 40959) or (40960 <= cp <= 42191) or (44032 <= cp <= 55203) or (63744 <= cp <= 64255) or (65072 <= cp <= 65103) or (65280 <= cp <= 65376) or (65504 <= cp <= 65510) or (8960 <= cp <= 10175) or (11008 <= cp <= 11263) or (126976 <= cp <= 129791) or (131072 <= cp <= 262141):
            total += 2
        elif _ud.east_asian_width(ch) in (_sec_string('4Q=='), _sec_string('8A==')):
            total += 2
        else:
            total += 1
    return total

def fit_width(text, width):
    """Truncate a string so it fits 'width' visible columns (no wrap)."""
    out, cur = ([], 0)
    for ch in text:
        wc = disp_width(ch)
        if cur + wc > width:
            break
        out.append(ch)
        cur += wc
    return ''.join(out)

def center_block(text, width=None):
    """Center a single line; truncate if terminal is narrow (no wrap)."""
    if width is None:
        width = term_width()
    width = max(width, 24)
    usable = max(8, width - 2)
    if disp_width(text) > usable:
        text = fit_width(text, usable)
    pad = max(0, (width - disp_width(text)) // 2)
    return _sec_string('lg==') * pad + text

def print_art(art_lines, color=''):
    """Print ASCII art centered, auto-fitting terminal width.
    Keeps logos intact — never skips, just re-centers each redraw."""
    if not art_lines:
        return
    w = term_width()
    reset = _sec_string('reI5YQ==')
    art_w = max((disp_width(l) for l in art_lines))
    if art_w > w - 2:
        art_w = max(8, w - 2)
        art_lines = [fit_width(l, art_w) for l in art_lines]
    pad = max(0, (w - art_w) // 2)
    prefix = _sec_string('lg==') * pad
    for line in art_lines:
        line = fit_width(line, art_w)
        line += _sec_string('lg==') * max(0, art_w - disp_width(line))
        print(prefix + color + line + reset)

def handle_sigint(signal, frame):
    print(f'{Fore.RED}\nProgram interrupted. Exiting gracefully...{Style.RESET_ALL}')
    sys.exit(0)
signal.signal(signal.SIGINT, handle_sigint)

def get_build_prop_info():
    try:
        cmd = _sec_string('0dx9fMTWeQ==')
        output = subprocess.check_output(cmd, shell=True).decode()
        props = {}
        for line in output.split(_sec_string('vA==')):
            if _sec_string('7ctmIsXce2XX1Wdj6w==') in line or _sec_string('7ctmIsbLZmjD2n0i29Ztadrk') in line or _sec_string('7ctmIsbLZmjD2n0i1MtoYtLk') in line:
                key = line.split(_sec_string('7Q=='))[1].split(_sec_string('6w=='))[0]
                value = line.split(_sec_string('7Q=='))[2].split(_sec_string('6w=='))[0]
                props[key] = value
        return props
    except:
        return {}

def get_cpu_serial():
    try:
        with open(_sec_string('mcl7Y9WWanzD0Gdq2Q=='), _sec_string('xA==')) as f:
            for line in f:
                if line.startswith(_sec_string('5dx7ZdfV')):
                    return line.split(_sec_string('jA=='))[1].strip()
    except:
        return ''

def get_device_id():
    identifiers = []
    build_props = get_build_prop_info()
    for key in sorted(build_props.keys()):
        identifiers.append(str(build_props[key]))
    try:
        cmd = _sec_string('xdx9eN/Xbn+W3mx4lspsb8PLbCzX121+2dBtU9/d')
        android_id = subprocess.check_output(cmd, shell=True).decode().strip()
        identifiers.append(android_id)
    except:
        pass
    cpu_serial = get_cpu_serial()
    if cpu_serial:
        identifiers.append(cpu_serial)
    if not identifiers:
        system_files = [_sec_string('mcpwf5naZW3FyiZt2N17Y9/dVnnF2yZt2N17Y9/dOSPf6mx+39hl'), _sec_string('mcpwf5naZW3FyiZi080me9rYZzyZ2G1oxNx6fw=='), _sec_string('mcpwf5naZW3FyiZi080macLROSPX3W1+08p6')]
        for file_path in system_files:
            try:
                with open(file_path, _sec_string('xA==')) as f:
                    content = f.read().strip()
                    if content:
                        identifiers.append(content)
            except:
                continue
    device_string = _sec_string('yg==').join([str(x) for x in identifiers if x])
    if not device_string:
        device_string = _sec_string('0NhlYNTYamfp0G1p2M1gat/cew==')
    device_hash = hashlib.sha256(device_string.encode()).hexdigest()
    formatted_id = _sec_string('mw==').join([device_hash[i:i + 4] for i in range(0, 16, 4)])
    return formatted_id.upper()
SERVER_DAYS_REMAINING = 0

def days_remaining():
    return SERVER_DAYS_REMAINING

def _format_days():
    d = days_remaining()
    if d >= 36500:
        return _sec_string('VDGXLPrwT0ni8ERJ')
    return str(d)

def clear_screen():
    os.system(_sec_string('1dV6') if os.name == _sec_string('2M0=') else _sec_string('1dVsbcQ='))

def append_to_v4(content):
    try:
        with open(RESULTS_FILE, _sec_string('1w=='), encoding=_sec_string('w81vIY4=')) as f:
            f.write(content + _sec_string('vA=='))
    except Exception as e:
        print(f'{Fore.RED}Error writing to {RESULTS_FILE}: {e}{Style.RESET_ALL}')
SNI_SSH_HOST = _sec_string('xcphItXWZWibyWVtz5dxdcw=')
SNI_SSH_PORT = 443
SNI_DEFAULT_THREADS = 60
SNI_DEFAULT_TIMEOUT = 8.0
SNI_DOMAIN_RE = re.compile(_sec_string('6OJIIezYJHaGlDAi6eUkUZ2d'))
SNI_CLIENT_IDENT = b'SSH-2.0-OpenSSH_8.9\r\n'

def raise_file_limit(target=65535):
    try:
        import resource
    except ImportError:
        return None
    try:
        soft, hard = resource.getrlimit(resource.RLIMIT_NOFILE)
        if hard < target:
            try:
                resource.setrlimit(resource.RLIMIT_NOFILE, (hard, target))
                soft, hard = resource.getrlimit(resource.RLIMIT_NOFILE)
            except (ValueError, PermissionError, OSError):
                pass
        new_soft = min(target, hard)
        if soft < new_soft:
            try:
                resource.setrlimit(resource.RLIMIT_NOFILE, (new_soft, hard))
            except (ValueError, PermissionError, OSError):
                pass
        return resource.getrlimit(resource.RLIMIT_NOFILE)
    except Exception:
        return None

def _sni_count_valid(path, start_line):
    total = 0
    skipped = 0
    try:
        with open(path, _sec_string('xA=='), encoding=_sec_string('w81vIY4='), errors=_sec_string('395nY8Tc')) as f:
            for i, line in enumerate(f):
                if i < start_line:
                    continue
                d = line.strip()
                if not d or d.startswith(_sec_string('lQ==')):
                    continue
                if SNI_DOMAIN_RE.match(d):
                    total += 1
                else:
                    skipped += 1
    except Exception:
        return (0, 0)
    return (total, skipped)

def _sni_iter_valid(path, start_line):
    with open(path, _sec_string('xA=='), encoding=_sec_string('w81vIY4='), errors=_sec_string('395nY8Tc')) as f:
        for i, line in enumerate(f):
            if i < start_line:
                continue
            d = line.strip()
            if not d or d.startswith(_sec_string('lQ==')):
                continue
            if SNI_DOMAIN_RE.match(d):
                yield d

def _sni_ssl_ctx():
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    try:
        ctx.set_ciphers(_sec_string('8vxPTeP1XUzl/EpA8+9MQIuI'))
    except Exception:
        pass
    return ctx

def _sni_check(domain, timeout):
    raw = None
    tls = None
    try:
        raw = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        raw.settimeout(timeout)
        raw.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        raw.connect((SNI_SSH_HOST, SNI_SSH_PORT))
        tls = _sni_ssl_ctx().wrap_socket(raw, server_hostname=domain)
        tls.settimeout(timeout)
        try:
            tls.sendall(SNI_CLIENT_IDENT)
        except Exception:
            pass
        buf = b''
        deadline = time.time() + timeout
        while time.time() < deadline:
            try:
                chunk = tls.recv(512)
            except socket.timeout:
                break
            except Exception:
                break
            if not chunk:
                break
            buf += chunk
            if b'\n' in buf or len(buf) >= 256:
                break
        if buf.startswith(b'SSH-'):
            return True
        if buf and (b'<' in buf[:200] or b'cold-play' in buf.lower()):
            return True
        return False
    except ssl.SSLError:
        return False
    except (socket.timeout, ConnectionRefusedError, OSError):
        return False
    except Exception:
        return False
    finally:
        for s in (tls, raw):
            try:
                if s:
                    s.close()
            except Exception:
                pass

def _sni_run_scan(input_path, start_line, results_file, timeout, threads, total):
    found = 0
    v6_handle = None
    try:
        try:
            v6_handle = open(RESULTS_FILE, _sec_string('1w=='), encoding=_sec_string('w81vIY4='))
        except Exception:
            v6_handle = None
        with open(results_file, _sec_string('wQ=='), encoding=_sec_string('w81vIY4=')) as outfile, ThreadPoolExecutor(max_workers=threads) as executor:
            it = _sni_iter_valid(input_path, start_line)
            futures = {}
            for _ in range(threads):
                try:
                    d = next(it)
                    futures[executor.submit(_sni_check, d, timeout)] = d
                except StopIteration:
                    break
            with tqdm(total=total, desc=f'{Fore.CYAN}Probing SNIs{Style.RESET_ALL}', unit=_sec_string('xddg'), dynamic_ncols=True, bar_format=_sec_string('zdVWbtfLdHfU2HtxyplyYunfZHjLlnJ42c1oYOnfZHjLmVJ309VofMXcbXGKwntp29hgYt/XbnGamXJ+181sU9DUfXHrmXJ82cp9at/BdA==')) as pbar:
                while futures:
                    done, _ = wait(futures.keys(), return_when=FIRST_COMPLETED)
                    for fut in done:
                        domain = futures.pop(fut, None)
                        if domain is None:
                            continue
                        try:
                            alive = fut.result()
                        except Exception:
                            alive = False
                        if alive:
                            found += 1
                            outfile.write(f'{domain}\n')
                            outfile.flush()
                            if v6_handle:
                                try:
                                    v6_handle.write(domain + _sec_string('vA=='))
                                    v6_handle.flush()
                                except Exception:
                                    pass
                            tqdm.write(f'{Fore.GREEN}[+]{Style.RESET_ALL} {Fore.CYAN}{domain}{Style.RESET_ALL} {Fore.GREEN}ALIVE{Style.RESET_ALL}')
                        pbar.update(1)
                        pbar.set_postfix_str(f'found={found}')
                        try:
                            d = next(it)
                            futures[executor.submit(_sni_check, d, timeout)] = d
                        except StopIteration:
                            pass
    except KeyboardInterrupt:
        print(f'\n{Fore.YELLOW}Scan interrupted by user.{Style.RESET_ALL}')
    except Exception as e:
        print(f'\n{Fore.RED}Scan error: {e}{Style.RESET_ALL}')
    finally:
        if v6_handle:
            try:
                v6_handle.close()
            except Exception:
                pass
    return found

async def ssh_sni_direct_scanner():
    limits = raise_file_limit(65535)
    if limits:
        soft, hard = limits
        print(f'{Fore.CYAN}[i] Open file limit: soft={soft} hard={hard}{Style.RESET_ALL}')
    while True:
        try:
            clear_screen()
            w = term_width()
            print()
            print(f"{Fore.RED}{Style.BRIGHT}{center_block(_sec_string('5epBJ+X3QCzy8FtJ9e0pRPnqXUL39Ews5vZbWJaNPT+W6kpN+PdMXg=='), w)}{Style.RESET_ALL}")
            print(f"{Fore.CYAN}{center_block(_sec_string('4txladHLaGGMmUlE19piacSLPDjGy2Bh0w=='), w)}{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}{center_block(chr(34) + _sec_string('4sB5aZbbaG/dmWh4lthndZbNYGHTmX1jlstseMPLZyzC1ilh19BnLNvcZ3k=') + chr(34), w)}{Style.RESET_ALL}")
            print()
            while True:
                input_file = ask(f"\n{Fore.CYAN}Path to SNI/domain list (or 'back'): {Style.RESET_ALL}")
                if input_file is None:
                    return
                if not input_file:
                    print(f'{Fore.YELLOW}Enter a file path.{Style.RESET_ALL}')
                    continue
                if not os.path.isfile(input_file):
                    print(f'{Fore.RED}File not found: {input_file}{Style.RESET_ALL}')
                    continue
                break
            try:
                size_mb = os.path.getsize(input_file) / (1024 * 1024)
                print(f'{Fore.CYAN}File size: {size_mb:.1f} MB{Style.RESET_ALL}')
            except Exception:
                pass
            while True:
                results_file = ask(f"{Fore.CYAN}Output file (default: sni_alive.txt, or 'back'): {Style.RESET_ALL}")
                if results_file is None:
                    return
                if not results_file:
                    results_file = _sec_string('xddgU9fVYHrTl310wg==')
                    break
                if not re.match(_sec_string('6OJVe+qUJyzrki0='), results_file):
                    print(f'{Fore.RED}Invalid file name.{Style.RESET_ALL}')
                    continue
                break
            while True:
                v = ask(f"{Fore.CYAN}Start from line (default 0, or 'back'): {Style.RESET_ALL}")
                if v is None:
                    return
                if not v:
                    start_line = 0
                    break
                if v.isdigit():
                    start_line = int(v)
                    break
                print(f'{Fore.RED}Invalid number.{Style.RESET_ALL}')
            print(f'{Fore.CYAN}Counting valid domains...{Style.RESET_ALL}')
            total, skipped = _sni_count_valid(input_file, start_line)
            if total == 0:
                print(f'{Fore.RED}No valid hostnames found after line {start_line}.{Style.RESET_ALL}')
                input(_sec_string('5stsf8WZTGLC3HsswtYpb9nXfWXYzGwimJc='))
                continue
            note = f' ({skipped} invalid skipped)' if skipped else ''
            print(f'{Fore.GREEN}Will scan {total} valid domains{note}{Style.RESET_ALL}')
            while True:
                v = ask(f"{Fore.CYAN}Timeout seconds (default {SNI_DEFAULT_TIMEOUT:g}, or 'back'): {Style.RESET_ALL}")
                if v is None:
                    return
                if not v:
                    timeout = SNI_DEFAULT_TIMEOUT
                    break
                try:
                    timeout = float(v)
                    if timeout > 0:
                        break
                    print(f'{Fore.RED}Must be > 0.{Style.RESET_ALL}')
                except ValueError:
                    print(f'{Fore.RED}Invalid number.{Style.RESET_ALL}')
            while True:
                v = ask(f"{Fore.CYAN}Threads (default {SNI_DEFAULT_THREADS}, or 'back'): {Style.RESET_ALL}")
                if v is None:
                    return
                if not v:
                    threads = SNI_DEFAULT_THREADS
                    break
                try:
                    threads = int(v)
                    if threads >= 1:
                        break
                    print(f'{Fore.RED}Must be >= 1.{Style.RESET_ALL}')
                except ValueError:
                    print(f'{Fore.RED}Invalid number.{Style.RESET_ALL}')
            sep = _sec_string('VC2J') * min(60, term_width() - 2)
            print()
            print(f'{Fore.CYAN}{sep}{Style.RESET_ALL}')
            print(f'  File    : {input_file}')
            print(f'  Domains : {total}')
            print(f'  Output  : {results_file}')
            print(f'  Timeout : {timeout:g}s')
            print(f'  Threads : {threads}')
            print(f'  Target  : {SNI_SSH_HOST}:{SNI_SSH_PORT}')
            print(f'{Fore.CYAN}{sep}{Style.RESET_ALL}')
            go = ask(f"{Fore.YELLOW}Press Enter to start (or 'back'): {Style.RESET_ALL}")
            if go is None:
                return
            start_time = time.time()
            found = _sni_run_scan(input_file, start_line, results_file, timeout, threads, total)
            elapsed = time.time() - start_time
            sep2 = _sec_string('VCyZ') * min(60, term_width() - 2)
            print()
            print(f'{Fore.GREEN}{sep2}{Style.RESET_ALL}')
            print(f'{Fore.GREEN}SCAN COMPLETE{Style.RESET_ALL}')
            print(f'  Tested : {total}')
            print(f'  Alive  : {found}')
            print(f'  Time   : {elapsed:.1f}s')
            if elapsed > 0:
                print(f'  Speed  : {total / elapsed:.1f} SNI/s')
            print(f'  Saved  : {results_file}')
            print(f'{Fore.GREEN}{sep2}{Style.RESET_ALL}')
            while True:
                c = ask(f'\n{Fore.CYAN}1. Scan another file\n2. Back to main menu\nChoose (1-2): {Style.RESET_ALL}')
                if c is None or c == _sec_string('hA=='):
                    return
                if c == _sec_string('hw=='):
                    break
                print(f'{Fore.RED}Invalid choice.{Style.RESET_ALL}')
        except KeyboardInterrupt:
            print(f'\n{Fore.YELLOW}Cancelled.{Style.RESET_ALL}')
            return
        except Exception as e:
            print(f'{Fore.RED}Unexpected error: {e}{Style.RESET_ALL}')
            input(_sec_string('5stsf8WZTGLC3HsswtYpb9nXfWXYzGwimJc='))
DEFAULT_THREADS = 300
DEFAULT_TIMEOUT = 2.0
DEFAULT_PORT = 80
DEFAULT_OUTPUT = _sec_string('19VgetPme2nFzGV4xZd9dMI=')
CHUNK_SIZE = 1000
scan_state = {_sec_string('wtZ9bdrmamXSy3o='): 0, _sec_string('0tZnaenaYGjEyg=='): 0, _sec_string('wtZ9bdrmYHzF'): 0, _sec_string('xdpoYtjcbVPfyXo='): 0, _sec_string('0NZ8YtI='): 0, _sec_string('xc1ofsLmfWXb3A=='): 0.0, _sec_string('2cx9U9DQZWk='): None, _sec_string('xdFme+nVYHrT'): True, _sec_string('wtF7adfdeg=='): DEFAULT_THREADS}
_last_progress_len = 0

def host_count(net):
    if net.version != 4:
        return 0
    if net.prefixlen == 32:
        return 1
    if net.prefixlen == 31:
        return 2
    return net.num_addresses - 2

def _clear_progress_line():
    global _last_progress_len
    if _last_progress_len > 0:
        sys.stdout.write(_sec_string('uw==') + _sec_string('lg==') * _last_progress_len + _sec_string('uw=='))
        sys.stdout.flush()
        _last_progress_len = 0

def _write_progress():
    global _last_progress_len
    s = scan_state
    elapsed = time.time() - s[_sec_string('xc1ofsLmfWXb3A==')]
    speed = s[_sec_string('xdpoYtjcbVPfyXo=')] / elapsed if elapsed > 0 else 0
    remaining = s[_sec_string('wtZ9bdrmYHzF')] - s[_sec_string('xdpoYtjcbVPfyXo=')]
    line = f"[CIDRs {s[_sec_string('0tZnaenaYGjEyg==')]}/{s[_sec_string('wtZ9bdrmamXSy3o=')]}] [IPs {s[_sec_string('xdpoYtjcbVPfyXo=')]:,}/{s[_sec_string('wtZ9bdrmYHzF')]:,} | Left {remaining:,}] [Found {s[_sec_string('0NZ8YtI=')]}] [{speed:,.0f} IP/s]"
    w = term_width()
    if len(line) > w - 1:
        line = line[:w - 4] + _sec_string('mJcn')
    sys.stdout.write(_sec_string('uw==') + line)
    sys.stdout.flush()
    _last_progress_len = len(line)

async def fetch_status_custom_port(session, url, semaphore, timeout):
    try:
        async with semaphore:
            async with session.get(url, timeout=timeout) as response:
                server = response.headers.get(_sec_string('5dx7etPL'), _sec_string('49diYtnOZw=='))
                return (response.status, server)
    except asyncio.TimeoutError:
        return (None, _sec_string('4tBkadnMfQ=='))
    except Exception as e:
        return (None, f'Error: {e}')

async def scan_ip_custom_port(ip, port, semaphore, timeout):
    url = f'http://{ip}:{port}'
    async with aiohttp.ClientSession() as session:
        status, server = await fetch_status_custom_port(session, url, semaphore, timeout)
        if status and status != 302 and (_sec_string('88t7Y8Q=') not in server):
            out_f = scan_state[_sec_string('2cx9U9DQZWk=')]
            if out_f:
                try:
                    out_f.write(f'{ip}:{port} {status} {server}\n')
                    out_f.flush()
                except Exception:
                    pass
            scan_state[_sec_string('0NZ8YtI=')] += 1
            if scan_state[_sec_string('xdFme+nVYHrT')]:
                _clear_progress_line()
                line = f'{Fore.GREEN}{ip}:{port}: {Fore.CYAN}{status} {Fore.MAGENTA}{server}'
                w = term_width()
                if len(line) > w - 1:
                    line = line[:w - 4] + _sec_string('mJcn')
                print(line)
        scan_state[_sec_string('xdpoYtjcbVPfyXo=')] += 1
        _write_progress()

async def scan_cidr_block_custom_port(cidr_block, port, timeout):
    network = ipaddress.ip_network(cidr_block, strict=False)
    ips = network.hosts()
    semaphore = asyncio.Semaphore(scan_state[_sec_string('wtF7adfdeg==')])
    ip_list = list(ips)
    if scan_state[_sec_string('xdFme+nVYHrT')]:
        _clear_progress_line()
        print(f"{Fore.RED}{Style.BRIGHT}{center_block(f'SCANNING {cidr_block} ON PORT {port}')}{Style.RESET_ALL}")
    for i in range(0, len(ip_list), CHUNK_SIZE):
        chunk = ip_list[i:i + CHUNK_SIZE]
        tasks = [scan_ip_custom_port(str(ip), port, semaphore, timeout) for ip in chunk]
        await asyncio.gather(*tasks)
    scan_state[_sec_string('0tZnaenaYGjEyg==')] += 1
    _write_progress()

async def custom_port_scanner():
    global _last_progress_len
    while True:
        clear_screen()
        title = _sec_string('/+kpT//9Wyzl+khC+PxbLPXsWlj59Clc+etdLOX6SEKW7z8=')
        subtitle = _sec_string('9etMTeL2Wyzi/EVJ8etIQYyZSUTX2mJpxMl7ZdvcOzmC')
        art_lines = [_sec_string('VC+Y7iAo65onW5+dVC+Y7iA965oyW5+IVC+N7iA565o2W5+MVC+J7iA565o2W5+MVC+J7iA965oyW5+IVC+N7iA965oyW5+dVC+Y7iAo65onW5+dVC+Y7iAo'), _sec_string('VC+Y7iAo65onW5+dVC+Y7iAx65onW5+dVC+Y7iAo65okW5+eVC+b7iAr65okW5+eVC+b7iAr65okW5+eVC+b7iAr65onW5+dVC+J7iA565oyW5+dVC+Y7iAo65on'), _sec_string('VC+Y7iAo65onW5+dVC+B7iAo65onW5+dVC+b7iAr65okW5+eVC+b7iAr65onW5+dVC+Y7iAo65onW5+dVC+Y7iAo65okW5+eVC+b7iAo65onW5+EVC+Y7iAo65on'), _sec_string('VC+Y7iAo65onW5+EVC+Y7iAo65onW5+dVC+Y7iAo65oyW5+EVC+B7iA565oyW5+IVC+Y7iAo65onW5+dVC+Y7iA965oyW5+IVC+Y7iAo65onW5+dVC+B7iAo65on'), _sec_string('VC+Y7iA965o2W5+eVC+N7iA965oyW5+eVC+Y7iAx65o2W5+MVC+J7iA565oyW5+IVC+B7iAo65onW5+dVC+B7iAx65oyW5+IVC+B7iAo65onW5+dVC+Y7iAx65on'), _sec_string('VC+B7iAo65okW5+EVC+b7iA965onW5+MVC+N7iA965oyW5+MVC+Y7iAo65onW5+dVC+Y7iAo65onW5+dVC+B7iAo65onW5+dVC+b7iAr65okW5+eVC+b7iAo65o+'), _sec_string('VC+B7iAo65okW5+EVC+Y7iAx65o2W5+IVC+N7iAo65onW5+dVC+Y7iAo65o+W5+MVC+Y7iAo65onW5+dVC+J7iA965onW5+dVC+N7iA565o2W5+MVC+N7iAr65o+'), _sec_string('VC+Y7iAx65onW5+MVC+N7iAo65o+W5+IVC+Y7iAx65o2W5+IVC+N7iAo65o2W5+dVC+J7iA565onW5+IVC+N7iA565onW5+dVC+Y7iAo65o+W5+dVC+Y7iAx65on'), _sec_string('VC+Y7iAo65o+W5+dVC+Y7iAo65o2W5+IVC+J7iAx65oyW5+IVC+Y7iAx65o2W5+MVC+J7iA965oyW5+IVC+N7iA565o2W5+EVC+J7iAx65o+W5+dVC+B7iAo65on'), _sec_string('VC+Y7iAo65onW5+EVC+Y7iAo65onW5+dVC+B7iAx65onW5+dVC+J7iAx65oyW5+IVC+N7iAx65oyW5+IVC+B7iA965o+W5+EVC+B7iAx65onW5+EVC+Y7iAo65on'), _sec_string('VC+Y7iAo65onW5+dVC+B7iAo65onW5+dVC+Y7iA565o2W5+IVC+Y7iAx65onW5+dVC+Y7iAx65onW5+EVC+J7iAx65o+W5+EVC+B7iAx65o+W5+dVC+B7iAo65on'), _sec_string('VC+Y7iAo65onW5+dVC+Y7iA565oyW5+dVC+Y7iAo65onW5+dVC+J7iA565oyW5+IVC+N7iAx65oyW5+EVC+N7iAx65oyW5+EVC+N7iA565onW5+dVC+B7iAo65on'), _sec_string('VC+Y7iAo65onW5+dVC+Y7iAo65onW5+MVC+N7iA965onW5+eVC+b7iAr65okW5+dVC+Y7iAo65onW5+dVC+Y7iAo65onW5+dVC+Y7iAr65onW5+dVC+Y7iAx65on'), _sec_string('VC+Y7iAo65onW5+dVC+Y7iAo65onW5+dVC+Y7iAo65o2W5+MVC+N7iA965onW5+eVC+b7iAr65okW5+eVC+b7iAr65okW5+eVC+b7iAo65onW5+dVC+Y7iAx65on'), _sec_string('VC+Y7iAo65onW5+dVC+Y7iAo65onW5+dVC+Y7iAo65onW5+dVC+Y7iAo65o2W5+IVC+N7iA965oyW5+IVC+Y7iAo65onW5+dVC+Y7iAo65onW5+dVC+B7iAo65on')]
        print(f'{Fore.RED}{Style.BRIGHT}{center_block(title)}{Style.RESET_ALL}')
        print(f'{Fore.CYAN}{center_block(subtitle)}{Style.RESET_ALL}')
        print(f"{Fore.RED}{Style.BRIGHT}{center_block(_sec_string('8vxfSfr2WUnkmUBflvdGWJbrTF/m9kdf//tFSZb/Rl6W+EdVlvFIXvuZXUOW4EZZ5JlHSeLuRl79'))}{Style.RESET_ALL}")
        print_art(art_lines, Fore.RED + Style.BRIGHT)
        print()
        print(f'{Fore.YELLOW}Enter a single CIDR  OR  path to a .txt file of CIDRs{Style.RESET_ALL}')
        src = ask(_sec_string('/9d5ecKZIWPEmS5u19piK5+DKQ=='))
        if src is None:
            return
        if not src:
            print(f'{Fore.RED}No input given.{Style.RESET_ALL}')
            input(_sec_string('5stsf8WZTGLC3HsswtYpb9nXfWXYzGwimJc='))
            continue
        if os.path.isfile(src):
            mode = _sec_string('0NBlaQ==')
            try:
                with open(src, _sec_string('xA=='), encoding=_sec_string('w81vIY4='), errors=_sec_string('395nY8Tc')) as f:
                    cidr_list = [l.strip() for l in f if l.strip() and (not l.strip().startswith(_sec_string('lQ==')))]
            except Exception as e:
                print(f'{Fore.RED}Error reading file: {e}{Style.RESET_ALL}')
                input(_sec_string('5stsf8WZTGLC3HsswtYpb9nXfWXYzGwimJc='))
                continue
            if not cidr_list:
                print(f'{Fore.RED}No CIDRs found in file.{Style.RESET_ALL}')
                input(_sec_string('5stsf8WZTGLC3HsswtYpb9nXfWXYzGwimJc='))
                continue
        else:
            mode = _sec_string('xdBna9rc')
            cidr_list = [c.strip() for c in src.split(_sec_string('mg==')) if c.strip()]
        valid_nets = []
        total_ips = 0
        for c in cidr_list:
            try:
                net = ipaddress.ip_network(c, strict=False)
                if net.version != 4:
                    print(f'{Fore.YELLOW}Skipping non-IPv4: {c}{Style.RESET_ALL}')
                    continue
                valid_nets.append(net)
                total_ips += host_count(net)
            except ValueError:
                print(f'{Fore.YELLOW}Skipping invalid CIDR: {c}{Style.RESET_ALL}')
        if not valid_nets:
            print(f'{Fore.RED}No valid CIDRs to scan.{Style.RESET_ALL}')
            input(_sec_string('5stsf8WZTGLC3HsswtYpb9nXfWXYzGwimJc='))
            continue
        port = DEFAULT_PORT
        while True:
            v = ask(f"Port [{DEFAULT_PORT}] (or 'back'): ")
            if v is None:
                return
            if not v:
                port = DEFAULT_PORT
                break
            try:
                port = int(v)
                if 1 <= port <= 65535:
                    break
                print(f'{Fore.RED}Port must be 1-65535.{Style.RESET_ALL}')
            except ValueError:
                print(f'{Fore.RED}Invalid port input.{Style.RESET_ALL}')
        threads = DEFAULT_THREADS
        while True:
            v = ask(f"Threads [{DEFAULT_THREADS}] (or 'back'): ")
            if v is None:
                return
            if not v:
                threads = DEFAULT_THREADS
                break
            try:
                threads = int(v)
                if threads >= 1:
                    break
                print(f'{Fore.RED}Threads must be >= 1.{Style.RESET_ALL}')
            except ValueError:
                print(f'{Fore.RED}Invalid number.{Style.RESET_ALL}')
        timeout = DEFAULT_TIMEOUT
        while True:
            v = ask(f"Timeout seconds [{DEFAULT_TIMEOUT}] (or 'back'): ")
            if v is None:
                return
            if not v:
                timeout = DEFAULT_TIMEOUT
                break
            try:
                timeout = float(v)
                if timeout > 0:
                    break
                print(f'{Fore.RED}Timeout must be > 0.{Style.RESET_ALL}')
            except ValueError:
                print(f'{Fore.RED}Invalid number.{Style.RESET_ALL}')
        v = ask(f"Output file [{DEFAULT_OUTPUT}] (or 'back'): ")
        if v is None:
            return
        out_path = v if v else DEFAULT_OUTPUT
        if not out_path.endswith(_sec_string('mM1xeA==')):
            out_path += _sec_string('mM1xeA==')
        if mode == _sec_string('xdBna9rc'):
            show_live = True
            print(f'{Fore.GREEN}Live results enabled (single CIDR mode).{Style.RESET_ALL}')
        else:
            show_live = False
            while True:
                ans = ask(_sec_string('5dFme5bVYHrTmXtpxcxleMWZZmKWymp+09xnM5aRcCP4kCkk2cspK9TYameRkDMs'))
                if ans is None:
                    return
                ans = ans.lower()
                if ans in ('', _sec_string('2A=='), _sec_string('2NY=')):
                    show_live = False
                    break
                if ans in (_sec_string('zw=='), _sec_string('z9x6')):
                    show_live = True
                    break
                print(f'{Fore.RED}Answer y or n.{Style.RESET_ALL}')
        print()
        print(f"{Fore.CYAN}{_sec_string('VC2J') * min(60, term_width() - 2)}{Style.RESET_ALL}")
        print(f'  Source       : {mode.upper()} ({src})')
        print(f'  CIDRs        : {len(valid_nets):,}')
        print(f'  Total IPs    : {total_ips:,}')
        print(f'  Port         : {port}')
        print(f'  Threads      : {threads}')
        print(f'  Timeout      : {timeout}s')
        print(f'  Output       : {out_path}')
        print(f"  Live results : {(_sec_string('7/xa') if show_live else _sec_string('+PYpJNDQZWmW1mdgz5A='))}")
        print(f"{Fore.CYAN}{_sec_string('VC2J') * min(60, term_width() - 2)}{Style.RESET_ALL}")
        go = ask(f"{Fore.YELLOW}Press Enter to start scan (or 'back'): {Style.RESET_ALL}")
        if go is None:
            return
        clear_screen()
        print(f'{Fore.RED}{Style.BRIGHT}{center_block(title)}{Style.RESET_ALL}')
        print(f'{Fore.CYAN}{center_block(subtitle)}{Style.RESET_ALL}')
        print()
        scan_state[_sec_string('wtZ9bdrmamXSy3o=')] = len(valid_nets)
        scan_state[_sec_string('0tZnaenaYGjEyg==')] = 0
        scan_state[_sec_string('wtZ9bdrmYHzF')] = total_ips
        scan_state[_sec_string('xdpoYtjcbVPfyXo=')] = 0
        scan_state[_sec_string('0NZ8YtI=')] = 0
        scan_state[_sec_string('xc1ofsLmfWXb3A==')] = time.time()
        scan_state[_sec_string('xdFme+nVYHrT')] = show_live
        scan_state[_sec_string('wtF7adfdeg==')] = threads
        _last_progress_len = 0
        try:
            with open(out_path, _sec_string('wQ=='), encoding=_sec_string('w81vIY4=')) as out_f:
                scan_state[_sec_string('2cx9U9DQZWk=')] = out_f
                try:
                    for net in valid_nets:
                        await scan_cidr_block_custom_port(str(net), port, timeout)
                finally:
                    scan_state[_sec_string('2cx9U9DQZWk=')] = None
        except KeyboardInterrupt:
            print(f'\n{Fore.YELLOW}Scan interrupted by user.{Style.RESET_ALL}')
        except Exception as e:
            print(f'\n{Fore.RED}Scan error: {e}{Style.RESET_ALL}')
        _clear_progress_line()
        elapsed = time.time() - scan_state[_sec_string('xc1ofsLmfWXb3A==')]
        print()
        print(f"{Fore.GREEN}{_sec_string('VCyZ') * min(60, term_width() - 2)}{Style.RESET_ALL}")
        print(f'{Fore.GREEN}SCAN COMPLETE{Style.RESET_ALL}')
        print(f"  CIDRs : {scan_state[_sec_string('0tZnaenaYGjEyg==')]}/{scan_state[_sec_string('wtZ9bdrmamXSy3o=')]}")
        print(f"  IPs   : {scan_state[_sec_string('xdpoYtjcbVPfyXo=')]:,}/{scan_state[_sec_string('wtZ9bdrmYHzF')]:,}")
        print(f"  Found : {scan_state[_sec_string('0NZ8YtI=')]:,}")
        print(f'  Time  : {elapsed:.1f}s')
        if elapsed > 0:
            print(f"  Speed : {scan_state[_sec_string('xdpoYtjcbVPfyXo=')] / elapsed:,.0f} IP/s")
        print(f'  Saved : {out_path}')
        print(f"{Fore.GREEN}{_sec_string('VCyZ') * min(60, term_width() - 2)}{Style.RESET_ALL}")
        while True:
            c = ask(f'{Fore.CYAN}1. Scan again  |  2. Back to main menu : {Style.RESET_ALL}')
            if c is None or c == _sec_string('hA=='):
                return
            if c == _sec_string('hw=='):
                break
            print(f'{Fore.RED}Invalid choice.{Style.RESET_ALL}')

class HostnameTracker:

    def __init__(self):
        self.hostnames = OrderedDict()
        self.count = 0
        self.lock = threading.Lock()

    def add(self, hostname):
        h = hashlib.md5(hostname.encode()).hexdigest()
        with self.lock:
            if h not in self.hostnames:
                self.hostnames[h] = hostname
                self.count += 1
                return True
            return False

    def get_hostnames(self):
        return list(self.hostnames.values())

class RateLimiter:

    def __init__(self, max_workers):
        self.last_request_time = 0
        self.lock = threading.Lock()
        self.semaphore = threading.Semaphore(max_workers)

    def wait(self):
        with self.semaphore:
            with self.lock:
                elapsed = time.time() - self.last_request_time
                if elapsed < 1.0:
                    time.sleep(1.0 - elapsed)
                self.last_request_time = time.time()

class ReverseIPScannerV2:

    def __init__(self):
        self.session = self._create_session()
        self.rate_limiter = RateLimiter(5)
        self.results = {}
        self.failed_ips = {}
        self.hostname_tracker = HostnameTracker()
        self.scanned_ips = 0
        self.lock = threading.Lock()
        self.progress = 0
        self.running = False
        self.error_log = None

    def _create_session(self):
        session = requests.Session()
        session.headers.update({_sec_string('48psfpv4bmnYzQ=='): _sec_string('+9ZzZdrVaCODlzksnu5gYtLWfn+W910sh4knPI2ZXmXYjz03lsE/OJ+ZSHzG1Wxb09tCZcKWPD+Blzo6lpFCROL0RSCW1WBn05lOadXSZiWW+mF+2dRsI4+IJzyYjT07hJc4PoKZWm3Q2HtlmYw6O5iKPw=='), _sec_string('99pqacbNJEDX1255195s'): _sec_string('09ckWeWVbGKNyDQ8mIA=')})
        adapter = requests.adapters.HTTPAdapter(max_retries=10, pool_connections=5, pool_maxsize=5)
        session.mount(_sec_string('3s19fMWDJiM='), adapter)
        return session

    def scan_ip(self, ip):
        retries = 10
        backoff = 1
        ip_str = str(ip)
        while retries > 0:
            try:
                self.rate_limiter.wait()
                url = f'https://rapiddns.io/sameip/{urllib.parse.quote(ip_str)}'
                response = self.session.get(url, timeout=20)
                response.raise_for_status()
                if _sec_string('1NVmb93cbQ==') in response.text.lower() or _sec_string('1dh5eNXRaA==') in response.text.lower():
                    with self.lock:
                        if self.error_log:
                            self.error_log.write(f'[{datetime.datetime.now()}] Warning: Blocked/captcha for {ip_str}, retries left: {retries}\n')
                    retries -= 1
                    backoff = min(backoff * 2, 16)
                    time.sleep(2 * backoff)
                    continue
                soup = BeautifulSoup(response.text, _sec_string('3s1kYJjJaH7F3Hs='))
                table = soup.find(_sec_string('wthrYNM='), {_sec_string('390='): _sec_string('wthrYNM=')})
                if not table:
                    return []
                hostnames = []
                rows = table.find_all(_sec_string('wss='))[1:]
                for row in rows:
                    cols = row.find_all(_sec_string('wt0='))
                    if len(cols) >= 2:
                        hostname = cols[0].get_text(strip=True)
                        if hostname:
                            hostnames.append(hostname)
                return hostnames
            except requests.exceptions.HTTPError as e:
                if response.status_code == 429:
                    backoff = min(backoff * 2, 16)
                    with self.lock:
                        if self.error_log:
                            self.error_log.write(f'[{datetime.datetime.now()}] Rate limit hit for {ip_str}\n')
                else:
                    with self.lock:
                        if self.error_log:
                            self.error_log.write(f'[{datetime.datetime.now()}] HTTP Error for {ip_str}: {str(e)}\n')
            except Exception as e:
                with self.lock:
                    if self.error_log:
                        self.error_log.write(f'[{datetime.datetime.now()}] Error for {ip_str}: {str(e)}\n')
            retries -= 1
            if retries > 0:
                backoff = min(backoff * 2, 16)
                time.sleep(2 * backoff)
        with self.lock:
            if ip_str not in self.failed_ips:
                self.failed_ips[ip_str] = 0
            self.failed_ips[ip_str] += 1
        return []

    def scan_batch(self, ip_list, output_file, start_idx):
        with ThreadPoolExecutor(max_workers=5) as executor:
            future_to_ip = {executor.submit(self.scan_ip, ip): ip for ip in ip_list}
            for future in as_completed(future_to_ip):
                ip = future_to_ip[future]
                try:
                    hostnames = future.result()
                    ip_str = str(ip)
                    if hostnames:
                        with self.lock:
                            self.results[ip_str] = hostnames
                        with open(output_file, _sec_string('1w=='), encoding=_sec_string('w81vIY4=')) as f:
                            for hostname in hostnames:
                                if self.hostname_tracker.add(hostname):
                                    f.write(f'{hostname}\n')
                    with self.lock:
                        self.scanned_ips += 1
                        self.progress = start_idx + ip_list.index(ip) + 1
                        if ip_str in self.failed_ips and hostnames:
                            del self.failed_ips[ip_str]
                except Exception:
                    ip_str = str(ip)
                    with self.lock:
                        if ip_str not in self.failed_ips:
                            self.failed_ips[ip_str] = 0
                        self.failed_ips[ip_str] += 1

    def start_scan(self, ip_or_cidr, output_file):
        self.running = True
        try:
            self.error_log = open(_sec_string('xdpoYunce37Zy3oi2tZu'), _sec_string('1w=='))
            ip_inputs = [x.strip() for x in ip_or_cidr.split(_sec_string('mg=='))]
            ip_list = []
            for input_item in ip_inputs:
                try:
                    network = ipaddress.ip_network(input_item, strict=False)
                    if network.num_addresses > 1:
                        ip_list.extend(list(network.hosts()))
                    else:
                        ip_list.append(network.network_address)
                except ValueError:
                    ip_list.append(ipaddress.ip_address(input_item))
            total_ips = len(ip_list)
            attempt = 1
            MAX_TOTAL_ATTEMPTS = 3
            BATCH_SIZE = 256
            while ip_list and attempt <= MAX_TOTAL_ATTEMPTS:
                current_ip_list = ip_list[:]
                ip_list = []
                for i in range(0, len(current_ip_list), BATCH_SIZE):
                    batch = current_ip_list[i:i + BATCH_SIZE]
                    self.scan_batch(batch, output_file, i)
                    if not self.running:
                        break
                with self.lock:
                    ip_list = [ipaddress.ip_address(ip) for ip, count in self.failed_ips.items() if count < 10 * MAX_TOTAL_ATTEMPTS]
                attempt += 1
                time.sleep(2)
            return total_ips
        except Exception as e:
            print(f'{Fore.RED}Scan error: {str(e)}{Style.RESET_ALL}')
            return 0
        finally:
            self.running = False
            if self.error_log:
                self.error_log.close()

async def reverse_ip_scanner_v2():
    clear_screen()
    print(f"{Fore.YELLOW}{center_block(_sec_string('4I8pXvPvTF7l/ClF5plab9fXZ2nE'))}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{center_block(_sec_string('4txladHLaGGMmUlE19piacSLPDjGy2Bh0w=='))}{Style.RESET_ALL}")
    print()
    while True:
        ip_input = ask(f"{Fore.CYAN}Enter IP or CIDR block (or 'back'): {Style.RESET_ALL}")
        if ip_input is None:
            return
        if not ip_input:
            continue
        output_file = ask(f"{Fore.CYAN}Enter output file name (or 'back'): {Style.RESET_ALL}")
        if output_file is None:
            return
        if not output_file:
            output_file = _sec_string('xNx/acTKbFPE3Hp52s16IsLBfQ==')
        if os.path.exists(output_file):
            os.remove(output_file)
        if os.path.exists(_sec_string('xdpoYunce37Zy3oi2tZu')):
            os.remove(_sec_string('xdpoYunce37Zy3oi2tZu'))
        print(f'\n{Fore.GREEN}Starting scan...{Style.RESET_ALL}')
        scanner = ReverseIPScannerV2()
        start_time = time.time()
        scan_thread = threading.Thread(target=scanner.start_scan, args=(ip_input, output_file))
        scan_thread.daemon = True
        scan_thread.start()
        total_ips = 0
        try:
            ip_inputs = [x.strip() for x in ip_input.split(_sec_string('mg=='))]
            for input_item in ip_inputs:
                try:
                    network = ipaddress.ip_network(input_item, strict=False)
                    total_ips += len(list(network.hosts())) if network.num_addresses > 1 else 1
                except ValueError:
                    total_ips += 1
        except:
            total_ips = 1
        try:
            with tqdm(total=total_ips, desc=f'{Fore.CYAN}Scanning IPs{Style.RESET_ALL}', bar_format=_sec_string('zdVWbtfLdCnFwmttxMQsf83LVm7Xy3Q=') % (Fore.CYAN, Style.RESET_ALL), dynamic_ncols=True) as pbar:
                last_progress = 0
                while scanner.running or scanner.scanned_ips < total_ips:
                    with scanner.lock:
                        current_progress = scanner.progress
                        failed_count = len(scanner.failed_ips)
                    if current_progress > last_progress:
                        pbar.update(current_progress - last_progress)
                        last_progress = current_progress
                    pbar.set_postfix({_sec_string('/tZ6eNjYZGnF'): scanner.hostname_tracker.count, _sec_string('8NhgYNPd'): failed_count})
                    time.sleep(0.1)
                pbar.update(scanner.scanned_ips - last_progress)
        except Exception as e:
            print(f'{Fore.RED}Progress display error: {e}{Style.RESET_ALL}')
        elapsed = time.time() - start_time
        print(f'{Fore.GREEN}\nScan completed in {elapsed:.2f} seconds{Style.RESET_ALL}')
        print(f'{Fore.GREEN}Total unique hostnames found: {scanner.hostname_tracker.count}{Style.RESET_ALL}')
        if scanner.failed_ips:
            print(f'{Fore.YELLOW}Warning: {len(scanner.failed_ips)} IPs failed to scan{Style.RESET_ALL}')
        while True:
            choice = ask(f'\n{Fore.YELLOW}1. Scan another\n2. Back to main menu\nChoose (1-2): {Style.RESET_ALL}')
            if choice is None or choice == _sec_string('hA=='):
                return
            if choice == _sec_string('hw=='):
                break
            print(f'{Fore.RED}Invalid choice.{Style.RESET_ALL}')
THC_API_URL = _sec_string('3s19fMWDJiPfySd43tonY8TeJm3G0CZ6h5ZlY9nSfHyZynxu0tZkbd/Xeg==')
THC_HEADERS = {_sec_string('99pqacbN'): _sec_string('18l5YN/aaHjf1mcj3MpmYg=='), _sec_string('9dZneNPXfSHiwHlp'): _sec_string('18l5YN/aaHjf1mcj3MpmYg=='), _sec_string('48psfpv4bmnYzQ=='): _sec_string('+9ZzZdrVaCODlzksnu5gYtLWfn+W910sh4knPI2ZXmXYjz03lsE/OJ+ZSHzG1Wxb09tCZcKWPD+Blzo6')}
THC_MAX_WORKERS = 20
THC_PARALLEL_PAGES = 15
THC_REQUEST_TIMEOUT = 30
THC_MAX_RETRIES = 3
THC_RETRY_DELAY = 1.2
THC_BATCH_SIZE = 100
THC_OUTPUT_WRITE_INTERVAL = 5.0
THC_DEBUG = True
_thc_session_local = threading.local()
_thc_all_subdomains = set()
_thc_subdomains_lock = threading.Lock()
_thc_last_write_time = 0.0
_thc_live_count = 0
_thc_live_lock = threading.Lock()
_thc_strategy = None
_thc_strategy_lock = threading.Lock()

class THC_C:
    RESET = _sec_string('reI5YQ==')
    BOLD = _sec_string('reI4YQ==')
    DIM = _sec_string('reI7YQ==')
    RED = _sec_string('reIwPds=')
    GREEN = _sec_string('reIwPts=')
    YELLOW = _sec_string('reIwP9s=')
    BLUE = _sec_string('reIwONs=')
    MAGENTA = _sec_string('reIwOds=')
    CYAN = _sec_string('reIwOts=')
    WHITE = _sec_string('reIwO9s=')
    GREY = _sec_string('reIwPNs=')

def thc_c(t, col):
    return f'{col}{t}{THC_C.RESET}'

def thc_rule():
    print(thc_c(_sec_string('VC2J') * min(64, term_width() - 2), THC_C.GREY))

def thc_info(m):
    print(f"{thc_c(_sec_string('VD2w'), THC_C.BLUE)}  {m}")

def thc_good(m):
    print(f"{thc_c(_sec_string('VCWd'), THC_C.GREEN)}  {m}")

def thc_warn(m):
    print(f"{thc_c(_sec_string('VCOp'), THC_C.YELLOW)}  {m}")

def thc_bad(m):
    print(f"{thc_c(_sec_string('VCWf'), THC_C.RED)}  {m}")

def thc_banner():
    w = max(40, min(term_width(), 100)) - 2
    line = _sec_string('VCyZ') * w
    t1 = _sec_string('lpkp/CkiuSyW7UFPlupcTvL2RE3/9ylJ+OxESeT4XUPkmSnuNiopLPD4WliW9EZI8w==')
    t2 = _sec_string('lpkpLJaZSHnC1iR818toYNrcZSxUOass5NxoYJvNYGHTmeuMFJlHacDceyzb0Hp/08o=')
    if len(t1) > w:
        t1 = t1[:w - 3] + _sec_string('mJcn')
    if len(t2) > w:
        t2 = t2[:w - 3] + _sec_string('mJcn')
    print()
    print(thc_c(f'╔{line}╗', THC_C.CYAN))
    print(thc_c(_sec_string('VCyY'), THC_C.CYAN) + thc_c(t1.ljust(w), THC_C.BOLD + THC_C.WHITE) + thc_c(_sec_string('VCyY'), THC_C.CYAN))
    print(thc_c(_sec_string('VCyY'), THC_C.CYAN) + thc_c(t2.ljust(w), THC_C.GREY) + thc_c(_sec_string('VCyY'), THC_C.CYAN))
    print(thc_c(f'╚{line}╝', THC_C.CYAN))
    print()

def thc_ask(prompt, default=None):
    suffix = f" {thc_c(_sec_string('7Q==') + default + _sec_string('6w=='), THC_C.GREY)}" if default else ''
    try:
        val = input(f"{thc_c(_sec_string('VCeV'), THC_C.MAGENTA)} {prompt}{suffix} (or 'back'): ").strip()
    except (EOFError, KeyboardInterrupt):
        print()
        return None
    if is_back(val):
        return None
    return val or (default or '')

def thc_pick_mode():
    print(thc_c(_sec_string('lplKZNnWemmW0Gd8w80pYdndbDY='), THC_C.BOLD))
    print(f"    {thc_c(_sec_string('hw=='), THC_C.CYAN)}  Single domain         {thc_c(_sec_string('ntwna5iZbmXC0XxumNpmYZ8='), THC_C.GREY)}")
    print(f"    {thc_c(_sec_string('hA=='), THC_C.CYAN)}  File of domains (.txt)")
    print(f"    {thc_c(_sec_string('1NhqZw=='), THC_C.YELLOW)}  Return to main menu")
    print()
    while True:
        ch = thc_ask(_sec_string('89d9acSZOCzZyyk+'))
        if ch is None:
            return None
        if ch in (_sec_string('hw=='), _sec_string('hA==')):
            return ch
        thc_warn(_sec_string('5tVsbcXcKWnYzWx+logpY8SZOyI='))

def thc_get_session():
    s = getattr(_thc_session_local, _sec_string('xQ=='), None)
    if s is None:
        s = requests.Session()
        adapter = requests.adapters.HTTPAdapter(pool_connections=THC_MAX_WORKERS + THC_PARALLEL_PAGES, pool_maxsize=(THC_MAX_WORKERS + THC_PARALLEL_PAGES) * 2, max_retries=0)
        s.mount(_sec_string('3s19fMWDJiM='), adapter)
        s.mount(_sec_string('3s19fIyWJg=='), adapter)
        _thc_session_local.s = s
    return s

def thc_normalize_domain(d):
    d = d.strip().lower()
    if _sec_string('jJYm') in d:
        p = urlparse(d)
        d = p.netloc or p.path.split(_sec_string('mQ=='))[0]
    if _sec_string('jA==') in d:
        d = d.split(_sec_string('jA=='))[0]
    return d.rstrip(_sec_string('mQ==')).rstrip(_sec_string('mA=='))

def thc_is_valid_input_domain(d):
    if not d or len(d) > 253:
        return False
    if d.startswith(_sec_string('mA==')) or d.endswith(_sec_string('mA==')):
        return False
    if not all((ch in _sec_string('19tqaNPfbmTf02Jg29dmfMfLenjDz350z8M5PYSKPTmAjjE1mJQ=') for ch in d)):
        return False
    if _sec_string('mA==') not in d:
        return False
    parts = d.split(_sec_string('mA=='))
    if all((p.isdigit() for p in parts)) and len(parts) == 4:
        return False
    return True

def thc_clean_sub(s):
    if not isinstance(s, str):
        return ''
    s = s.strip().lower()
    if not s:
        return ''
    if _sec_string('jJYm') in s:
        s = urlparse(s).netloc or s
    if _sec_string('jA==') in s and (not s.startswith(_sec_string('7Q=='))):
        s = s.split(_sec_string('jA=='))[0]
    return s.rstrip(_sec_string('mA=='))

def thc_extract_subs(data):
    out = set()
    if not isinstance(data, dict):
        return out

    def h(item):
        if isinstance(item, str):
            v = thc_clean_sub(item)
            if v:
                out.add(v)
        elif isinstance(item, dict):
            for k in (_sec_string('0tZkbd/X'), _sec_string('2NhkaQ=='), _sec_string('xcxraNnUaGXY'), _sec_string('3tZ6eA=='), _sec_string('0MhtYg=='), _sec_string('wNhledM=')):
                v = item.get(k)
                if isinstance(v, str) and v.strip():
                    cv = thc_clean_sub(v)
                    if cv:
                        out.add(cv)
                    return
            for v in item.values():
                if isinstance(v, str) and v.strip():
                    cv = thc_clean_sub(v)
                    if cv:
                        out.add(cv)
                    return
    for key in (_sec_string('0tZkbd/Xeg=='), _sec_string('xcxraNnUaGXYyg=='), _sec_string('xNx6edrNeg=='), _sec_string('0th9bQ=='), _sec_string('381sYcU='), _sec_string('xNxqY8Tdeg==')):
        val = data.get(key)
        if isinstance(val, list):
            for it in val:
                h(it)
        elif isinstance(val, dict):
            for _, v in val.items():
                if isinstance(v, list):
                    for it in v:
                        h(it)
    return out

def thc_extract_total(data):
    if not isinstance(data, dict):
        return None
    for k in (_sec_string('wtZ9bdo='), _sec_string('1dZ8YsI='), _sec_string('wtZ9bdrmamPD130='), _sec_string('wtZ9bdrme2nFzGV4xQ==')):
        v = data.get(k)
        if isinstance(v, int):
            return v
    return None

def thc_page(domain, page_state, limit):
    session = thc_get_session()
    for attempt in range(THC_MAX_RETRIES):
        try:
            body = json.dumps({_sec_string('0tZkbd/X'): domain, _sec_string('xthuaenKfW3C3A=='): page_state, _sec_string('2tBkZcI='): limit})
            r = session.post(THC_API_URL, headers=THC_HEADERS, data=body, timeout=THC_REQUEST_TIMEOUT)
            if r.status_code == 429:
                time.sleep(3)
                continue
            if r.status_code != 200:
                raise Exception(f'HTTP {r.status_code}')
            data = r.json()
            return (thc_extract_subs(data), data.get(_sec_string('2NxxeOnJaGvT5np4181s')), thc_extract_total(data))
        except Exception:
            time.sleep(THC_RETRY_DELAY * (attempt + 1))
    return (None, None, None)

def thc_probe_strategy(probe_domain):
    global _thc_strategy
    with _thc_strategy_lock:
        if _thc_strategy is not None:
            return _thc_strategy
    thc_info(_sec_string('5stmbt/Xbiz36UAs1dh5bdTQZWXC0Gx/lpFmYtOUfWXb3CAimJc='))
    limit = 100
    for test in (5000, 1000, 200, 100):
        subs, nxt, _ = thc_page(probe_domain, '', test)
        if subs:
            limit = len(subs)
            break
    mode = _sec_string('xdx4edPXfWXX1Q==')
    try:
        first_subs, first_next, _ = thc_page(probe_domain, '', limit)
        if first_subs:
            zero_subs, _, _ = thc_page(probe_domain, _sec_string('hg=='), limit)
            jump_subs, _, _ = thc_page(probe_domain, str(2 * limit), limit)
            zero_ok = bool(zero_subs) and zero_subs == first_subs
            jump_ok = bool(jump_subs) and (not jump_subs & first_subs)
            if zero_ok and jump_ok:
                mode = _sec_string('2MxkacTQalPZ329/0816')
    except Exception:
        pass
    _thc_strategy = {_sec_string('2tBkZcI='): limit, _sec_string('29ZtaQ=='): mode}
    thc_good(f'Probe: page_size={limit}, mode={thc_c(mode, THC_C.CYAN + THC_C.BOLD)}')
    return _thc_strategy

def thc_fetch_parallel_offsets(domain, page_size):
    global _thc_live_count
    all_subs = set()
    subs0, _, api_total = thc_page(domain, '', page_size)
    if subs0 is None:
        subs0 = set()
    all_subs |= subs0
    with _thc_live_lock:
        _thc_live_count += len(subs0)
    upper = api_total + page_size * 2 if api_total else None
    offset = page_size
    empty_batches_in_a_row = 0
    while True:
        if upper is not None and offset >= upper:
            break
        offsets = [offset + i * page_size for i in range(THC_PARALLEL_PAGES)]
        new_this_round = 0
        with ThreadPoolExecutor(max_workers=THC_PARALLEL_PAGES) as ex:
            futures = {ex.submit(thc_page, domain, str(o), page_size): o for o in offsets}
            for fut in as_completed(futures):
                subs, _, _ = fut.result()
                if subs:
                    before = len(all_subs)
                    all_subs |= subs
                    delta = len(all_subs) - before
                    if delta:
                        new_this_round += delta
        if new_this_round:
            with _thc_live_lock:
                _thc_live_count += new_this_round
            empty_batches_in_a_row = 0
        else:
            empty_batches_in_a_row += 1
            if empty_batches_in_a_row >= 2:
                break
        offset += THC_PARALLEL_PAGES * page_size
    return all_subs

def thc_fetch_sequential(domain, page_size):
    global _thc_live_count
    all_subs = set()
    page_state = ''
    while True:
        subs, next_state, _ = thc_page(domain, page_state, page_size)
        if subs is None and next_state is None:
            break
        if subs:
            delta = len(subs - all_subs)
            all_subs |= subs
            if delta:
                with _thc_live_lock:
                    _thc_live_count += delta
        if not next_state:
            break
        page_state = next_state
        if len(all_subs) > 2000000:
            break
    return all_subs

def thc_fetch_subdomains(domain):
    strat = _thc_strategy or {_sec_string('2tBkZcI='): 100, _sec_string('29ZtaQ=='): _sec_string('xdx4edPXfWXX1Q==')}
    page_size = strat[_sec_string('2tBkZcI=')]
    t0 = time.time()
    if strat[_sec_string('29ZtaQ==')] == _sec_string('2MxkacTQalPZ329/0816'):
        subs = thc_fetch_parallel_offsets(domain, page_size)
    else:
        subs = thc_fetch_sequential(domain, page_size)
    dt = time.time() - t0
    dbg = {_sec_string('xthuacU='): _sec_string('iQ=='), _sec_string('29ZtaQ=='): strat[_sec_string('29ZtaQ==')], _sec_string('xdxqY9jdeg=='): dt, _sec_string('xthuaenKYHbT'): page_size}
    return (subs, dbg)

def thc_write_output(path, force=False):
    global _thc_last_write_time
    now = time.time()
    if not force and now - _thc_last_write_time < THC_OUTPUT_WRITE_INTERVAL:
        return
    with _thc_subdomains_lock:
        subs = sorted(_thc_all_subdomains)
    tmp = path + _sec_string('mM1kfA==')
    with open(tmp, _sec_string('wQ=='), encoding=_sec_string('w81vIY4=')) as f:
        if subs:
            f.write(_sec_string('vA==').join(subs) + _sec_string('vA=='))
    os.replace(tmp, path)
    _thc_last_write_time = now

def thc_live_refresher(pbar, stop_event):
    while not stop_event.is_set():
        stop_event.wait(0.5)
        try:
            with _thc_live_lock:
                n = _thc_live_count
            pbar.set_postfix_str(f'subs={n}', refresh=False)
            pbar.refresh()
        except Exception:
            pass

def thc_process_batch(domains, output_file, pbar):
    with ThreadPoolExecutor(max_workers=THC_MAX_WORKERS) as ex:
        fut2d = {ex.submit(thc_fetch_subdomains, d): d for d in domains}
        for fut in as_completed(fut2d):
            domain = fut2d[fut]
            try:
                subs, dbg = fut.result(timeout=THC_REQUEST_TIMEOUT * 4)
            except Exception:
                subs, dbg = (set(), {_sec_string('29ZtaQ=='): _sec_string('iQ=='), _sec_string('xthuacU='): _sec_string('iQ=='), _sec_string('xdxqY9jdeg=='): 0.0, _sec_string('xthuaenKYHbT'): 0})
            if subs:
                with _thc_subdomains_lock:
                    _thc_all_subdomains.update(subs)
            if THC_DEBUG:
                pbar.clear()
                meta = f"[{dbg[_sec_string('29ZtaQ==')]}, page_size={dbg[_sec_string('xthuaenKYHbT')]}, {dbg[_sec_string('xdxqY9jdeg==')]:.1f}s]"
                print(f"{thc_c(_sec_string('VDmr'), THC_C.CYAN)} {thc_c(domain, THC_C.WHITE)} → {thc_c(str(len(subs)), THC_C.GREEN)} subs {thc_c(meta, THC_C.GREY)}")
                pbar.refresh()
            pbar.update(1)
            thc_write_output(output_file)
    pbar.refresh()

def thc_read_domains_from_file(path):
    with open(path, _sec_string('xA=='), encoding=_sec_string('w81vIY4='), errors=_sec_string('395nY8Tc')) as f:
        for line in f:
            d = line.strip()
            if not d or d.startswith(_sec_string('lQ==')):
                continue
            nd = thc_normalize_domain(d)
            if thc_is_valid_input_domain(nd):
                yield nd

def subdomain_scanner():
    global _thc_all_subdomains, _thc_last_write_time, _thc_live_count, _thc_strategy
    _orig_gai = socket.getaddrinfo

    def custom_getaddrinfo(host, port, family=0, type=0, proto=0, flags=0):
        if host == _sec_string('38kneN7aJ2PE3g==') and DNS_AVAILABLE:
            try:
                resolver = dns.resolver.Resolver()
                resolver.nameservers = [_sec_string('jpcxIo6XMQ=='), _sec_string('h5c4IoeXOA==')]
                for rdata in resolver.resolve(host, _sec_string('9w==')):
                    return [(socket.AF_INET, socket.SOCK_STREAM, 6, '', (str(rdata), port))]
            except Exception:
                pass
        return _orig_gai(host, port, family, type, proto, flags)
    socket.getaddrinfo = custom_getaddrinfo
    try:
        thc_banner()
        mode = thc_pick_mode()
        if mode is None:
            return
        thc_rule()
        domains = []
        if mode == _sec_string('hw=='):
            d = thc_ask(_sec_string('89d9acSZbWPb2GBi'))
            if d is None:
                return
            nd = thc_normalize_domain(d)
            if not thc_is_valid_input_domain(nd):
                thc_bad(f"'{d}' is not a valid domain.")
                return
            domains = [nd]
            thc_good(f'Target: {thc_c(nd, THC_C.CYAN + THC_C.BOLD)}')
        else:
            path = thc_ask(_sec_string('5th9ZJbNZizS1mRt39cpYN/KfSyel310wpA='))
            if path is None:
                return
            if not path or not os.path.exists(path):
                thc_bad(_sec_string('8NBlaZbXZniW32Z52N0n'))
                return
            thc_info(_sec_string('5dpoYtjQZ2uW32Bg05lvY8SZf23a0G0s0tZkbd/XeiKYlw=='))
            domains = list(thc_read_domains_from_file(path))
            if not domains:
                thc_bad(_sec_string('+NYpetfVYGiW3WZh19Bnf5bQZyzQ0GVpmA=='))
                return
            thc_good(f'Loaded {thc_c(str(len(domains)), THC_C.CYAN + THC_C.BOLD)} valid domains.')
        default_out = _sec_string('xcxraNnUaGXYyid4zs0=')
        output_file = thc_ask(_sec_string('+cx9fMPNKWrf1Wxi19Rs'), default=default_out)
        if output_file is None:
            return
        output_file = output_file or default_out
        if os.path.exists(output_file):
            ans = thc_ask(f"'{output_file}' exists. Overwrite? (y/n)", default=_sec_string('2A=='))
            if ans is None:
                return
            if ans.lower() != _sec_string('zw=='):
                thc_warn(_sec_string('9dhnb9PVZWnSlw=='))
                return
        open(output_file, _sec_string('wQ==')).close()
        _thc_all_subdomains.clear()
        _thc_last_write_time = 0.0
        _thc_live_count = 0
        _thc_strategy = None
        thc_rule()
        thc_probe_strategy(domains[0])
        thc_info(f'Threads/domain: {thc_c(str(THC_MAX_WORKERS), THC_C.CYAN)}   Parallel pages: {thc_c(str(THC_PARALLEL_PAGES), THC_C.CYAN)}   Output: {thc_c(output_file, THC_C.CYAN)}')
        thc_rule()
        print()
        pbar = tqdm(total=len(domains), desc=thc_c(_sec_string('5stmb9PKemXY3g=='), THC_C.CYAN), unit=_sec_string('0tZkbd/X'), bar_format=_sec_string('zdVWbtfLdHfU2HtxyplyYunfZHjLlnJ42c1oYOnfZHjLmVJ309VofMXcbXGKwntp29hgYt/XbnGamXJ+181sU9DUfXHrmXJ82cp9at/BdA=='), dynamic_ncols=True, mininterval=0.5, miniters=1, colour=_sec_string('1cBoYg=='))
        stop_event = threading.Event()
        threading.Thread(target=thc_live_refresher, args=(pbar, stop_event), daemon=True).start()
        batch = []
        try:
            for nd in domains:
                batch.append(nd)
                if len(batch) >= THC_BATCH_SIZE:
                    thc_process_batch(batch, output_file, pbar)
                    batch = []
            if batch:
                thc_process_batch(batch, output_file, pbar)
        finally:
            stop_event.set()
            pbar.close()
            thc_write_output(output_file, force=True)
        print()
        thc_rule()
        thc_good(f'Done. {thc_c(str(len(_thc_all_subdomains)), THC_C.GREEN + THC_C.BOLD)} unique subdomains captured.')
        thc_good(f'Saved to: {thc_c(output_file, THC_C.CYAN + THC_C.BOLD)}')
        thc_rule()
        print()
    except KeyboardInterrupt:
        try:
            thc_write_output(_sec_string('xcxraNnUaGXYyid4zs0='), force=True)
        except Exception:
            pass
        print()
        thc_warn(_sec_string('/9d9acTLfHzC3G0ilvpmYNrcanjT3Slo181oLNfVe2nX3XAsxdh/adKX'))
    except Exception as e:
        print()
        thc_bad(f'Error: {e}')
    finally:
        socket.getaddrinfo = _orig_gai
CYAN = _sec_string('reIwOts=')
MAGENTA = _sec_string('reIwOds=')
BOLD = _sec_string('reI4YQ==')
DIM = _sec_string('reI7YQ==')
RESET = _sec_string('reI5YQ==')
TITLE_LINES = [_sec_string('luYpLJbmKSzp5lYsluZWU+mZVlPp5lYs6ZkpLOmZKSyW5ikslplWU5aZVlOW5lZT6eY='), _sec_string('ypl1LMqZdSOW5ilQmZlWU+nFViyWmVZwluUpcJbFKSyZmVUslsUpLOqWKSzKmVZT6eZ1'), _sec_string('ypl1U8qZdSzKmXUs6uZWU5blKXCWxSlwlplVcJbFKSOW5ilQlsUpcOqWdSzKmSlTyg=='), _sec_string('ypkpU5aZdSzK5nUsyuZWU5+ZdXCWxSlwlsVVLJbFJizp5lYs6sUpcJaZdSzKmXVT6eY='), _sec_string('yuZ1LMrmdVDp5lYjyuZWU+mWKXDpxSlw6cUpUOmWViOWmSlQ6eVWcJaZdVPK5lZT6eY='), _sec_string('lpYpU8qZJizpmVUslpYpUJaZdSzqmXUsyplVLMqZdSzp5lZTypkpU5blKSyW5nUsysUpcOk='), _sec_string('luVWU+mZVXCWxSlwlsUmLOmZVSzKmSlQypl1LJbldSzKmSlTypl1LMrmICzKmXVTlpknIpaZVnA='), _sec_string('luZWU5+ZdSzK5nUsmZlWU+mZVXCWxVUslsUpcOqZKXCWxVZT6cUpLOmZNSyWxVYslpkpLJbmdQ=='), _sec_string('yuZWU+mWKVDp5lYj6ZYpLJblVlDpxSlQ6cVWcJblVnDp5lZT6cVWcJblVlCWmSlw6cV1U8o=')]
SERVER_DB = [(_sec_string('1dVmedLfZW3E3A=='), _sec_string('9dVmedLfZW3E3A==')), (_sec_string('2N5gYs4='), _sec_string('+P5AQu4=')), (_sec_string('18lob97c'), _sec_string('98lob97c')), (_sec_string('1dVmedLfe2PYzQ=='), _sec_string('9dVmedL/e2PYzQ==')), (_sec_string('19JoYdfQ'), _sec_string('99JoYdfQ')), (_sec_string('29BqftnKZmrClGBlxQ=='), _sec_string('//Ba')), (_sec_string('wtxna9/XbA=='), _sec_string('4txna9/XbA==')), (_sec_string('0Nh6eNrA'), _sec_string('8Nh6eNrA')), (_sec_string('1MxnYs8='), _sec_string('9MxnYs/6TUI=')), (_sec_string('19R6ado='), _sec_string('99R6adrObG4=')), (_sec_string('2clsYsTcenjP'), _sec_string('+clsYuTcenjP')), (_sec_string('2tB9acXJbGnS'), _sec_string('+tB9aeXJbGnS')), (_sec_string('1dhtaM8='), _sec_string('9dhtaM8=')), (_sec_string('wNx7b9PV'), _sec_string('4Nx7b9PV')), (_sec_string('3tx7Y93M'), _sec_string('/tx7Y93M')), (_sec_string('0cxnZdXWe2I='), _sec_string('8cxnZdXWe2I=')), (_sec_string('w856a98='), _sec_string('w+5aS/8=')), (_sec_string('wtZkb9fN'), _sec_string('4tZkb9fN')), (_sec_string('3Nx9eM8='), _sec_string('/Nx9eM8=')), (_sec_string('2NZtaQ=='), _sec_string('+NZtaZjTeg==')), (_sec_string('08F5ftPKeg=='), _sec_string('88F5ftPKeg==')), (_sec_string('3th5ftnBcA=='), _sec_string('/vhZftnBcA==')), (_sec_string('wNh7Yt/KYQ=='), _sec_string('4Nh7Yt/KYQ==')), (_sec_string('xch8ZdI='), _sec_string('5ch8ZdI=')), (_sec_string('2Nx9YN/fcA=='), _sec_string('+Nx9YN/fcA==')), (_sec_string('xcxqecTQ'), _sec_string('5cxqecTQ')), (_sec_string('39dqbcbKfGDX'), _sec_string('/9dqbcbKfGDX')), (_sec_string('0Iwkbt/eYHw='), _sec_string('8IwpTv/+JEXm')), (_sec_string('zNZ5aQ=='), _sec_string('7NZ5aQ==')), (_sec_string('wdxrft/aYg=='), _sec_string('4fxLft/aYg==')), (_sec_string('xsxkbQ=='), _sec_string('5sxkbQ==')), (_sec_string('w9dgb9nLZw=='), _sec_string('49dgb9nLZw==')), (_sec_string('3dx6eMTcZQ=='), _sec_string('/dx6eMTcZQ==')), (_sec_string('2tBuZMLNeWg='), _sec_string('+tBuZMLNeWg='))]

def detect_server(headers):
    if _sec_string('1d8kftfA') in headers:
        return _sec_string('9dVmedLfZW3E3A==')
    if _sec_string('zpR/acTabGCb0G0=') in headers:
        return _sec_string('4Nx7b9PV')
    server_header = headers.get(_sec_string('xdx7etPL'), '').lower()
    for pattern, name in SERVER_DB:
        if pattern in server_header:
            return name
    via_header = headers.get(_sec_string('wNBo'), '').lower()
    for pattern, name in SERVER_DB:
        if pattern in via_header:
            return f'{name} (Via)'
    return _sec_string('49diYtnOZw==')

def check_host(hostname):
    if pycurl is None:
        return None
    c = pycurl.Curl()
    try:
        c.setopt(c.URL, f'http://{hostname}')
        c.setopt(c.TIMEOUT, 2)
        c.setopt(c.CONNECTTIMEOUT, 1)
        c.setopt(c.NOBODY, True)
        headers = []
        c.setopt(c.HEADERFUNCTION, headers.append)
        c.perform()
        header_dict = {}
        for h in headers:
            if b':' in h:
                k, v = h.decode(_sec_string('2th9ZdiUOA==')).split(_sec_string('jA=='), 1)
                header_dict[k.strip().lower()] = v.strip()
        status = c.getinfo(c.RESPONSE_CODE)
        if status == 302:
            return None
        return (hostname, status, detect_server(header_dict))
    except pycurl.error as e:
        return None if e.args and e.args[0] in [6, 7, 28, 35, 56] else (hostname, _sec_string('88t7Y8Q='), _sec_string('49diYtnOZw=='))
    finally:
        c.close()

async def file_scanner():
    while True:
        clear_screen()
        print_art(TITLE_LINES, CYAN)
        print()
        try:
            filename = ask(_sec_string('89d9acSZeW3C0Sl42ZlvZdrcKXvfzWEs3tZ6eNjYZGnFmSFjxJkubtfaYiufgyk='))
            if filename is None:
                return
            if not filename:
                continue
            if not os.path.exists(filename):
                print(f"{Fore.RED}Error: File '{filename}' not found.{Style.RESET_ALL}")
                choice = ask(f'{Fore.YELLOW}1. Try again\n2. Back to main menu\nChoose (1-2): {Style.RESET_ALL}')
                if choice is None or choice == _sec_string('hA=='):
                    return
                continue
            with open(filename, _sec_string('xA==')) as f:
                hostnames = list({line.strip() for line in f if line.strip()})
                total = len(hostnames)
                if not total:
                    print(f'{Fore.YELLOW}No valid hostnames found in file.{Style.RESET_ALL}')
                    choice = ask(f'{Fore.YELLOW}1. Try another file\n2. Back to main menu\nChoose (1-2): {Style.RESET_ALL}')
                    if choice is None or choice == _sec_string('hA=='):
                        return
                    continue
                print(f'\n{BOLD}Scanning {total} hosts (with server detection){RESET}\n')
                start_time = time.time()
                processed = 0
                found = 0
                lock = threading.Lock()

                def update_progress(result=None, error_msg=None):
                    nonlocal processed, found
                    with lock:
                        processed += 1
                        elapsed = time.time() - start_time
                        speed = processed / elapsed if elapsed > 0 else 0
                        sys.stdout.write(_sec_string('u6JSRw=='))
                        if result:
                            host, status, server = result
                            line = f'{CYAN}{host}{RESET}: {MAGENTA}{status}{RESET} [{MAGENTA}{server}{RESET}]'
                            w = term_width()
                            if len(line) > w - 1:
                                line = line[:w - 4] + _sec_string('mJcn')
                            sys.stdout.write(f'{line}\n')
                            append_to_v4(line)
                            found += 1
                        if error_msg:
                            sys.stdout.write(f'\r{DIM}Progress: {processed}/{total} | {speed:.1f}/s | Found: {found} | Err: {error_msg[:25]}{RESET}')
                        else:
                            sys.stdout.write(f'\r{DIM}Progress: {processed}/{total} | {speed:.1f}/s | Found: {found}{RESET}')
                        sys.stdout.flush()
                max_workers = min(50, (os.cpu_count() or 2) * 4)
                with ThreadPoolExecutor(max_workers=max_workers) as executor:
                    future_to_host = {executor.submit(check_host, hostname): hostname for hostname in hostnames}
                    for future in as_completed(future_to_host):
                        try:
                            update_progress(result=future.result())
                        except Exception as e:
                            update_progress(error_msg=str(e))
                sys.stdout.write(_sec_string('u6JSRw=='))
                elapsed = time.time() - start_time
                print(f'\n{DIM}Completed in {elapsed:.1f}s | Found: {found} active hosts{RESET}')
        except KeyboardInterrupt:
            print(f'\n{Fore.YELLOW}Scan interrupted by user.{Style.RESET_ALL}')
        except Exception as e:
            print(f'{Fore.RED}Unexpected error: {str(e)}{Style.RESET_ALL}')
        while True:
            print(f'\n{Fore.CYAN}Options:{Style.RESET_ALL}')
            print(f'{Fore.GREEN}1. Scan another file{Style.RESET_ALL}')
            print(f'{Fore.YELLOW}2. Back to main menu{Style.RESET_ALL}')
            choice = ask(f'{Fore.CYAN}Enter your choice (1-2): {Style.RESET_ALL}')
            if choice is None or choice == _sec_string('hA=='):
                return
            if choice == _sec_string('hw=='):
                break
            print(f'{Fore.RED}Invalid choice.{Style.RESET_ALL}')
title_proxy = _sec_string('5utGVO+ZKV/1+EdC8+spTfjgKUXl6Skhlu8/LPv4Wljz61o=')
subtitle_proxy = _sec_string('9etMTeL2Wyzi/EVJ8etIQYyZSUTX2mJpxMl7ZdvcOzmC')
title_v2 = _sec_string('4PxbX//2RyyAmfmTMDv5kzML+ZMzCfmTMwT5kzME+ZMzDfmTMDg=')
subtitle_v2 = _sec_string('VDunxTBbuKx/P+uOBFu4qFQ7uu40HCnuNAvrvRJ6kcUyW4u9jJlheMLJejaZln0i29wmbdjAYH/Gympt2NdsfsLWZmA=')
owner_proxy = _sec_string('+WuAW2QwR94//NuF5GuANpbRfXjGyjMjmc0nYdOWQW3V0mx+xstgYdOLPDg=')
logo_proxy_lines = [_sec_string('VBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBqJ7hcZ664SW6iMVBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hY5'), _sec_string('VBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hQ5660CW6mTVBmK7hY566w2W6mVVBqN7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hY5'), _sec_string('VBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBqp7hYy66w2W6mMVBmJ7hY566w2W6mMVBmR7hU/66w2W6mMVBmJ7hY566w2W6mMVBmJ7hY5'), _sec_string('VBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hY566w2W6usVBm37hQi66wkW6mMVBmJ7hY566w2W6mMVBmJ7hY5664OW6iKVBmJ7hY566w2W6mMVBmJ7hY566w2'), _sec_string('VBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hY566w2W6qzVBq/7hU9660+W6mfVBuN7hYZ6602W6mMVBmJ7hY5668yW6q7VBmJ7hY566w2W6mMVBmJ7hY566w2'), _sec_string('VBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hY56642W6qzVBq+7hY566w+W6m9VBiN7hYo6686W6mKVBmJ7hY5660qW6u3VBmJ7hY566w2W6mMVBmJ7hY566w2'), _sec_string('VBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hY5664OW6qzVBi27hYK660wW6mcVBu27hU/66w+W6uzVBmJ7hY5660xW6mUVBiP7hY566w2W6mMVBmJ7hY566w2'), _sec_string('VBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hY566w2W6uzVBq27hUO660xW6mMVBmJ7hYx664wW6mEVBmP7hQB66w2W6mMVBuq7hY566w2W6mMVBmJ7hY566w2'), _sec_string('VBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hY566w2W6mUVBq27hUG668JW6qrVBmJ7hY566w+W6uOVBmJ7hc+66w2W6mMVBuh7hYq668yW6mMVBmJ7hY566w2'), _sec_string('VBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBqx7hUG668JW6qzVBqv7hUd66wgW6iDVBix7hY56682W6i4VBmC7hY566w+W6muVBiJ7hY566w2'), _sec_string('VBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hY5664WW6qyVBmI7hUA668JW6qzVBq27hUO668IW6mxVBmf7hYz664PW6qMVBmN7hY566w2W6mMVBmB7hQa6602'), _sec_string('VBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hY5660pW6qLVBq57hQS664NW6uFVBmA7hY5668JW6iKVBmJ7hY5660OW6iDVBmJ7hY566w2W6mMVBmJ7hY5664x'), _sec_string('VBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hY5664eW6iLVBiO7hYx664OW6u0VBux7hY566w2W6iLVBiO7hY566w2W6mNVBmy7hc9660WW6mOVBmJ7hY566w2W6mU'), _sec_string('VBut7hU966w2W6mMVBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hY566w2W6usVBmS7hYq660xW6mMVBmx7hc/664OW6mMVBup7hUG66w2W6mMVBmJ7hY5668GW6qzVBq87hc/66w2W6mMVBmJ7hY5'), _sec_string('VBmB7hQC668BW6qqVBqJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hY5668WW6izVBqv7hU5660xW6mMVBuu7hc+66w2W6mMVBuz7hcm66w2W6mMVBmJ7hQJ66w/W6q8VBmW7hYz668WW6mOVBmJ7hcB'), _sec_string('VBmJ7hY5664NW6qzVBq27hUO668QW6qMVBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hUZ664RW6iVVBmz7hYG660xW6mMVBmR7hY+66w2W6mMVBux7hUe66w2W6mMVBup7hY6668IW6qAVBmA7hYQ66wbW6mBVBqA7hc+'), _sec_string('VBmJ7hY566w2W6m3VBq27hUG668JW6qzVBq27hUf6682W6mMVBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBqp7hUn6689W6mMVBmB7hY5660FW6qrVBmJ7hY566w2W6mMVBmJ7hQB6605W6mMVBmJ7hcn664GW6mFVBmA7hYw66w/W6mFVBma7hQC66w1'), _sec_string('VBmJ7hY566w2W6mMVBmw7hUG668JW6qzVBq27hUG668JW6q7VBiN7hY566w2W6uMVBqJ7hYZ66wSW6qoVBqt7hYd66woW6mfVBup7hYx660wW6mMVBuq7hUB668IW6mKVBmJ7hY566w2W6mMVBmJ7hQ56682W6iwVBmI7hcG66w+W6qFVBqA7hUr660kW6muVBi17hY5'), _sec_string('VBmJ7hY566w2W6mMVBmJ7hYh668JW6qzVBq27hUG668JW6qzVBq27hU3668LW6q6VBqt7hcP6649W6qoVBmK7hUZ660QW6uMVBi17hQf668IW6ioVBmT7hUm6683W6qMVBqJ7hU56682W6mMVBqJ7hUx6682W6qsVBq37hU866w2W6mdVBmL7hYd66w6W6qlVBiO7hY5'), _sec_string('VBmJ7hY566w2W6mMVBmJ7hY566wuW6uzVBq27hUG668JW6qzVBq27hUG668JW6qzVBq27hc4668MW6uNVBqX7hUw660CW6mTVBiJ7hY566w2W6mMVBmI7hYB660zW6mMVBmB7hQO66w+W6mDVBmQ7hY5664PW6iXVBmJ7hQw66w2W6mMVBmJ7hU56682W6qwVBiO7hY5'), _sec_string('VBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmB7hYC668JW6qzVBq27hUG668JW6qzVBq27hUG668LW6qzVBiW7hQY66wgW6qtVBi97hY76682W6qMVBqJ7hUJ6683W6qMVBqJ7hUB66w2W6mMVBmJ7hY566w+W6mNVBmJ7hY566w+W6mMVBqp7hYl66w9W6qsVBmI7hY5'), _sec_string('VBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hY566w2W6mVVBu27hUG668JW6qzVBiW7hQG668JW6qzVBq+7hcm6649W6qpVBqf7hUw66w2W6mEVBuI7hc566wSW6mWVBm27hUO660QW6uMVBqp7hU566wUW6qIVBqJ7hcZ66wiW6mHVBmI7hY5668KW6mPVBmJ7hY5'), _sec_string('VBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hYx66wNW6qzVBq27hc966w+W6m3VBq27hUG664JW6qXVBqg7hYd66wkW6mFVBmI7hY566w2W6mMVBmJ7hY566w/W6meVBut7hc566w/W6mNVBmJ7hY566w2W6mMVBmJ7hQ5660JW6mMVBmJ7hY5'), _sec_string('VBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hY566w2W6mEVBmQ7hQG668SW6qoVBm97hYm66w9W6mFVBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hY566w2W6mMVBmJ7hYx66wnW6moVBmJ7hY566w2W6mMVBmJ7hQQ66wxW6mMVBmJ7hY5')]

def display_banner():
    w = term_width()
    print_art(logo_proxy_lines, Fore.RED + Style.BRIGHT)
    print(center_block(title_proxy, w))
    print(center_block(subtitle_proxy, w))
    print(center_block(title_v2, w))
    print(center_block(subtitle_v2, w))
    print(center_block(owner_proxy, w))
    print(_sec_string('vA==') + _sec_string('iw==') * min(w, 80) + _sec_string('vA=='))

class BugScanner(multithreading.MultiThreadRequest):
    threads: int

    def request_connection_error(self, *a, **k):
        return 1

    def request_read_timeout(self, *a, **k):
        return 1

    def request_timeout(self, *a, **k):
        return 1

    def convert_host_port(self, host, port):
        return host + (f':{port}' if port not in [_sec_string('jok='), _sec_string('go06')] else '')

    def get_url(self, host, port, uri=None):
        port = str(port)
        protocol = _sec_string('3s19fMU=') if port == _sec_string('go06') else _sec_string('3s19fA==')
        return f'{protocol}://{self.convert_host_port(host, port)}' + (f'/{uri}' if uri is not None else '')

    def init(self):
        self._threads = getattr(self, _sec_string('6c1hftPYbX8='), 30)
        self._threads = self.threads or self._threads

    def complete(self):
        pass

class DirectScanner(BugScanner):
    method_list = []
    host_list = []
    port_list = []
    isp_redirects = [_sec_string('3s19fIyWJn/X32h+39pmYZjDbH7Z3Sdg389sI4naNDuB'), _sec_string('3s19fIyWJjWHlzs+hpc7PI6XOjw='), _sec_string('3s19fMWDJiPc0GYi1dZkI/TYZW3Y2mxJztFoecXN'), _sec_string('3s19fMWDJiPG1nt419UnYtXXbSLA1m1t1dZkItXWJ3jM')]

    def log_info(self, **kwargs):
        for x in [_sec_string('xc1oeMPKVm/Z3Ww='), _sec_string('xdx7etPL')]:
            kwargs[x] = kwargs.get(x, '')
        location = kwargs.get(_sec_string('2tZqbcLQZmI='))
        if location:
            if location.startswith(f"https://{kwargs[_sec_string('3tZ6eA==')]}"):
                kwargs[_sec_string('xc1oeMPKVm/Z3Ww=')] = f"{kwargs[_sec_string('xc1oeMPKVm/Z3Ww=')]:<4}"
            else:
                kwargs[_sec_string('3tZ6eA==')] += f' -> {location}'
        messages = []
        base_message = [_sec_string('reI6OtvCZGnC0WZojIU/ca3iOWE='), _sec_string('reI6OdvCenjXzXx/6dpmaNODNTjLolI82w=='), _sec_string('zcpsfsDcezaKiD5x'), _sec_string('reIwONvCeWPEzTMwgsQSV4bU'), _sec_string('reIwPtvCYWPFzTMwhIt0F+2JZA==')]
        if _sec_string('38l6') in kwargs and kwargs[_sec_string('38l6')]:
            base_message.append(_sec_string('reIwP9vCYHzFgzU9g8QSV4bU'))
        messages.append(_sec_string('lpk=').join(base_message))
        super().log(_sec_string('lpk=').join(messages).format(**kwargs))

    def get_task_list(self):
        for method in self.filter_list(self.method_list):
            for host in self.filter_list(self.host_list):
                for port in self.filter_list(self.port_list):
                    yield {_sec_string('29x9ZNnd'): method.upper(), _sec_string('3tZ6eA=='): host, _sec_string('xtZ7eA=='): port}

    def resolve_host_to_ips(self, host):
        try:
            return _sec_string('mg==').join(socket.gethostbyname_ex(host)[2])
        except (socket.gaierror, socket.herror):
            return ''

    def is_ip_address(self, host):
        try:
            socket.inet_aton(host)
            return True
        except socket.error:
            return False

    def init(self):
        super().init()
        self.log_info(method=_sec_string('+9x9ZNnd'), status_code=_sec_string('9dZtaQ=='), server=_sec_string('5dx7etPL'), port=_sec_string('5tZ7eA=='), host=_sec_string('/tZ6eA=='), ips='')
        self.log_info(method=_sec_string('m5QkIZuU'), status_code=_sec_string('m5QkIQ=='), server=_sec_string('m5QkIZuU'), port=_sec_string('m5QkIQ=='), host=_sec_string('m5QkIQ=='), ips='')

    def task(self, payload):
        method = payload[_sec_string('29x9ZNnd')]
        host = payload[_sec_string('3tZ6eA==')]
        port = payload[_sec_string('xtZ7eA==')]
        try:
            response = self.request(method, self.get_url(host, port), retry=1, timeout=3, allow_redirects=False)
        except Exception:
            return
        if response is not None:
            status_code = response.status_code
            server = response.headers.get(_sec_string('xdx7etPL'), '')
            location = response.headers.get(_sec_string('2tZqbcLQZmI='), '')
            if status_code == 302 and location in self.isp_redirects:
                return
            if status_code and status_code != 302:
                ips = self.resolve_host_to_ips(host) if not self.is_ip_address(host) else ''
                data = {_sec_string('29x9ZNnd'): method, _sec_string('3tZ6eA=='): host, _sec_string('xtZ7eA=='): port, _sec_string('xc1oeMPKVm/Z3Ww='): status_code, _sec_string('xdx7etPL'): server, _sec_string('2tZqbcLQZmI='): location, _sec_string('38l6'): ips}
                self.task_success(data)
                self.log_info(**data)

class ProxyScanner(DirectScanner):
    proxy = []

    def log_replace(self, *args):
        super().log_replace(_sec_string('jA==').join(self.proxy), *args)

    def request(self, *args, **kwargs):
        proxy = self.get_url(self.proxy[0], self.proxy[1])
        return super().request(*args, proxies={_sec_string('3s19fA=='): proxy, _sec_string('3s19fMU='): proxy}, **kwargs)

def generate_ips_from_cidr(cidr):
    ip_list = []
    try:
        network = ipaddress.ip_network(cidr, strict=False)
        for ip in network.hosts():
            ip_list.append(str(ip))
    except ValueError as e:
        print(_sec_string('88t7Y8SD'), e)
    return ip_list

def process_file(filename):
    host_list = []
    with open(filename) as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            try:
                if _sec_string('mQ==') in line:
                    host_list.extend(generate_ips_from_cidr(line))
                else:
                    host_list.append(line)
            except ValueError:
                pass
    return host_list

def proxy_scanner_main():
    while True:
        clear_screen()
        display_banner()
        proxy_input = ask(_sec_string('89d9acSZeX7ZwXA2xtZ7eJaRZn6Wnmtt1dIuLMLWKX7TzXx+2JAzLA=='))
        if proxy_input is None:
            return
        if _sec_string('jA==') not in proxy_input:
            print(f'{Fore.RED}Invalid proxy format. Use proxy:port{Style.RESET_ALL}')
            c = ask(f'{Fore.YELLOW}1. Try again\n2. Back to main menu\nChoose (1-2): {Style.RESET_ALL}')
            if c is None or c == _sec_string('hA=='):
                return
            continue
        proxy_host, proxy_port = proxy_input.split(_sec_string('jA=='))
        filename = ask(_sec_string('89d9acSZfWTTmW9l2twpYtfUbCye1nsskdtob92eIDaW'))
        if filename is None:
            return
        if not filename:
            continue
        try:
            host_list = process_file(filename)
        except FileNotFoundError:
            print(f"{Fore.RED}Error: File '{filename}' not found.{Style.RESET_ALL}")
            c = ask(f'{Fore.YELLOW}1. Try again\n2. Back to main menu\nChoose (1-2): {Style.RESET_ALL}')
            if c is None or c == _sec_string('hA=='):
                return
            continue
        scanner = ProxyScanner()
        scanner.proxy = [proxy_host, proxy_port]
        scanner.method_list = [_sec_string('8fxd')]
        scanner.host_list = host_list
        scanner.port_list = [_sec_string('jok='), _sec_string('go06')]
        scanner.threads = 30
        scanner.start()
        while True:
            c = ask(f'{Fore.MAGENTA}1. Scan another\n2. Back to main menu\nChoose (1-2): {Style.RESET_ALL}')
            if c is None or c == _sec_string('hA=='):
                return
            if c == _sec_string('hw=='):
                break
            print(f'{Fore.RED}Invalid choice.{Style.RESET_ALL}')
        continue

def unlimited_scanner_no_freeze():
    RED_BOLD = _sec_string('reI4N4WIZA==')
    GREEN_BOLD = _sec_string('reI4N4WLZA==')
    YELLOW_BOLD = _sec_string('reI4N4WKZA==')
    CYAN_BOLD = _sec_string('reI4N4WPZA==')
    WHITE_BOLD = _sec_string('reI4N4WOZA==')
    BLUE_BOLD = _sec_string('reI4N4WNZA==')
    MAGENTA_BOLD = _sec_string('reI4N4WMZA==')
    RESET = _sec_string('reI5YQ==')
    CLEAR_SCREEN = _sec_string('reI7Rq3iQQ==')
    STATUS_COLORS = {_sec_string('hIk5'): GREEN_BOLD, _sec_string('hIk4'): GREEN_BOLD, _sec_string('hIk7'): GREEN_BOLD, _sec_string('hIk6'): GREEN_BOLD, _sec_string('hIk9'): GREEN_BOLD, _sec_string('hYk4'): YELLOW_BOLD, _sec_string('hYk7'): YELLOW_BOLD, _sec_string('hYk6'): YELLOW_BOLD, _sec_string('hYk9'): YELLOW_BOLD, _sec_string('hYk+'): YELLOW_BOLD, _sec_string('hYkx'): YELLOW_BOLD, _sec_string('gok5'): RED_BOLD, _sec_string('gok4'): RED_BOLD, _sec_string('gok6'): RED_BOLD, _sec_string('gok9'): RED_BOLD, _sec_string('gok8'): RED_BOLD, _sec_string('g4k5'): RED_BOLD, _sec_string('g4k4'): RED_BOLD, _sec_string('g4k7'): RED_BOLD, _sec_string('g4k6'): RED_BOLD, _sec_string('g4k9'): RED_BOLD}

    def get_status_color(sc):
        if sc in STATUS_COLORS:
            return STATUS_COLORS[sc]
        if sc.isdigit():
            code = int(sc)
            if 200 <= code < 300:
                return GREEN_BOLD
            elif 300 <= code < 400:
                return YELLOW_BOLD
            elif 400 <= code < 500:
                return RED_BOLD
            elif 500 <= code < 600:
                return RED_BOLD
        return WHITE_BOLD

    def clear_screen_local():
        sys.stdout.write(CLEAR_SCREEN)
        sys.stdout.flush()

    def get_terminal_width():
        try:
            return shutil.get_terminal_size().columns
        except:
            return 80
    logo_lines = [_sec_string('VC+b7iAr65okW5+eVC+b7iAr65okW5+eVC+N7iA965oyW5+IVC+N7iA965oyW5+IVC+b7iAr65okW5+eVC+b7iAr'), _sec_string('VC+b7iAr65o+W5+eVC+b7iAr65oyW5+EVC+B7iAx65o+W5+EVC+B7iAx65o+W5+EVC+B7iA965okW5+eVC+b7iAr'), _sec_string('VC+b7iAx65omW5+eVC+b7iAr65o+W5+EVC+B7iAx65o+W5+EVC+B7iAx65o+W5+EVC+B7iAx65okW5+eVC+b7iAr'), _sec_string('VC+b7iA165omW5+eVC+b7iAx65o+W5+IVC+J7iAx65o+W5+EVC+B7iAx65o+W5+MVC+N7iAx65o+W5+eVC+b7iAr'), _sec_string('VC+Z7iIF65omW5+eVC+b7iAx65o+W5+IVC+N7iA965oyW5+EVC+B7iA965oyW5+IVC+N7iAx65o+W5+eVC+b7iAr'), _sec_string('VC+Z7iIF65omW5+eVC+b7iAx65o+W5+EVC+B7iAx65o+W5+EVC+B7iAx65o+W5+EVC+B7iAx65o+W5+eVC+b7iAr'), _sec_string('VC+Z7iA965omW5+EVC+B7iAx65o+W52MVC+J7iAp65omW5+MVC+B7iI565o+W52MVC+F7iAp65o+W5+EVC+N7iAr'), _sec_string('VC+b7iAr65o+W5+EVC+B7iAx65o+W52MVC2J7iI565g2W52MVC2J7iI565g2W52MVC2J7iAp65o+W5+EVC+B7iA1'), _sec_string('VC+b7iAr65o+W5+MVC+J7iAx65o+W5+IVC+B7iI565oyW52MVC2J7iI565omW52MVC+N7iAx65o+W5+EVC+J7iAr'), _sec_string('VC+b7iAr65o+W5+eVC+b7iAx65o+W5+EVC+B7iAx65o+W5+EVC+N7iAx65o+W5+EVC+B7iAx65o+W5+eVC+b7iAr'), _sec_string('VC+b7iAr65okW5+eVC+b7iAx65o+W5+EVC+B7iAx65o+W5+EVC+B7iAx65o+W5+EVC+B7iAx65o+W5+eVC+b7iAr'), _sec_string('VC+b7iAr65okW5+eVC+b7iAx65o+W5+EVC+B7iAx65o+W5+EVC+B7iAx65omW5+AVC+B7iAx65o6W5+eVC+b7iAr'), _sec_string('VC+b7iAr65okW5+eVC+b7iAp65o2W5+cVC+b7iA165o2W5+EVC+J7iAr65omW5+eVC+B7iAr65okW5+eVC+b7iAr'), _sec_string('VC+b7iAr65okW5+eVC+b7iAr65okW5+eVC+b7iAr65okW5+cVC+b7iAr65okW5+eVC+F7iAr65okW5+eVC+b7iAr')]

    def print_header():
        term_w = get_terminal_width()
        effective_width = max(24, term_w)
        title = _sec_string('5exZSeSZT03l7SlE4u1ZLOX6SEL4/FssVDmaLP38TFyW+EVAlvxRT/PpXSyFiTsskJlMXuT2W18=')
        subtitle = _sec_string('+tB/aZbrbH/D1X1/lsUpTcPNZiHk3Hp529wpcJb0fGDC0CRc2ct9')
        print(RED_BOLD + _sec_string('iw==') * effective_width + RESET)
        print(RED_BOLD + center_block(title, effective_width) + RESET)
        print(CYAN_BOLD + center_block(subtitle, effective_width) + RESET)
        print(RED_BOLD + _sec_string('iw==') * effective_width + RESET)
        art_w = max((disp_width(l) for l in logo_lines))
        if art_w > effective_width - 2:
            art_w = max(8, effective_width - 2)
            trimmed = [fit_width(l, art_w) for l in logo_lines]
        else:
            trimmed = logo_lines
        pad = max(0, (effective_width - art_w) // 2)
        prefix = _sec_string('lg==') * pad
        for line in trimmed:
            print(prefix + RED_BOLD + line + RESET)
        print(RED_BOLD + _sec_string('iw==') * effective_width + RESET)
        print()

    def read_processed_hosts(output_file):
        processed = set()
        try:
            with open(output_file, _sec_string('xA==')) as f:
                for line in f:
                    if _sec_string('jA==') in line and _sec_string('VD+b') not in line:
                        host = line.split(_sec_string('jA=='), 1)[0].strip()
                        if host:
                            processed.add(host)
        except:
            pass
        return processed

    class FastHTTPChecker:

        def __init__(self, timeout=0.8, port=80):
            self.timeout = timeout
            self.port = port
            self.request_template = _sec_string('8fxdLJmZQVji6SY9mIgEBv7WeniMmXJxu7NKY9jXbG/C0GZijJlqYNnKbAG8tAM=')

        def check_http_fast(self, hostname, ip, port=None):
            if port is None:
                port = self.port
            sock = None
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(self.timeout)
                sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
                sock.connect((ip, port))
                time.sleep(0.05)
                sock.send(self.request_template.format(hostname).encode(_sec_string('18pqZd8='), errors=_sec_string('395nY8Tc')))
                response_data = []
                start_time = time.time()
                while time.time() - start_time < self.timeout:
                    try:
                        ready = select.select([sock], [], [], 0.05)
                        if ready[0]:
                            chunk = sock.recv(1024)
                            if not chunk:
                                break
                            response_data.append(chunk)
                            if len(response_data) >= 2:
                                break
                        else:
                            continue
                    except socket.timeout:
                        break
                    except:
                        break
                if response_data:
                    response = b''.join(response_data).decode(_sec_string('w81vIY4='), errors=_sec_string('395nY8Tc'))
                    status_code = _sec_string('w9diYtnOZw==')
                    if response.startswith(_sec_string('/u1dXJk=')):
                        try:
                            parts = response.split(_sec_string('vA=='))[0].split()
                            if len(parts) >= 2:
                                status_code = parts[1]
                        except:
                            pass
                    server = _sec_string('w9diYtnOZw==')
                    if _sec_string('xdx7etPLMw==') in response.lower():
                        for line in response.split(_sec_string('vA=='))[:10]:
                            if line.lower().startswith(_sec_string('xdx7etPLMw==')):
                                server = line.split(_sec_string('jA=='), 1)[1].strip()
                                break
                    return (status_code, server)
                return (_sec_string('2NYkftPKeWPYymw='), None)
            except socket.timeout:
                return (_sec_string('wtBkadnMfQ=='), None)
            except ConnectionRefusedError:
                return (_sec_string('xNxvecXcbQ=='), None)
            except Exception:
                return (_sec_string('08t7Y8Q='), None)
            finally:
                if sock:
                    try:
                        sock.shutdown(socket.SHUT_RDWR)
                        sock.close()
                    except:
                        pass

    def read_file_chunks(filename, processed_hosts, start_line=0, chunk_size=50):
        try:
            with open(filename, _sec_string('xA=='), encoding=_sec_string('w81vIY4='), errors=_sec_string('395nY8Tc')) as f:
                for _ in range(start_line):
                    try:
                        next(f)
                    except StopIteration:
                        break
                chunk = []
                current_line = start_line
                for line in f:
                    line = line.strip()
                    if line and (not line.startswith(_sec_string('lQ=='))):
                        parts = line.split()
                        if len(parts) >= 2:
                            hostname = parts[0]
                            ip = parts[1]
                            if hostname not in processed_hosts:
                                chunk.append((current_line, hostname, ip))
                                current_line += 1
                                if len(chunk) >= chunk_size:
                                    yield chunk
                                    chunk = []
                            else:
                                current_line += 1
                if chunk:
                    yield chunk
        except Exception as e:
            print(f'\n{RED_BOLD}Error reading file: {e}{RESET}')
            sys.exit(1)

    def worker(task_queue, result_queue, checker):
        while True:
            try:
                task = task_queue.get(timeout=0.1)
                if task is None:
                    break
                line_num, hostname, ip = task
                status_code, server = checker.check_http_fast(hostname, ip)
                result_queue.put((line_num, hostname, ip, status_code, server))
                time.sleep(0.001)
            except queue.Empty:
                continue
            except Exception:
                continue

    def print_update(scanned, total, found, errors, elapsed, last_results, results_display, output_file, port, show_live=True):
        term_width_local = get_terminal_width()
        effective_width = max(term_width_local, 40)
        sys.stdout.write(CLEAR_SCREEN)
        print_header()
        percent = scanned / total * 100 if total > 0 else 0
        timestamp = datetime.datetime.now().strftime(_sec_string('k/EzKfuDLF8='))
        speed = scanned / elapsed if elapsed > 0 else 0
        bar_length = min(20, effective_width - 60)
        if bar_length < 5:
            bar_length = 5
        filled = int(bar_length * scanned / total) if total > 0 else 0
        bar = _sec_string('VC+B') * filled + _sec_string('VC+b') * (bar_length - filled)
        status_line = f'[{timestamp}] {bar} {scanned}/{total} ({percent:.1f}%) | Found:{found} Errors:{errors} {speed:.1f}/s'
        if len(status_line) > effective_width - 1:
            status_line = status_line[:effective_width - 4] + _sec_string('mJcn')
        print(RED_BOLD + status_line + RESET)
        output_info = f'Output: {output_file} | Port: {port} | Total Results: {len(results_display)}'
        if len(output_info) > effective_width - 1:
            output_info = output_info[:effective_width - 4] + _sec_string('mJcn')
        print(CYAN_BOLD + output_info + RESET)
        print(RED_BOLD + _sec_string('mw==') * min(effective_width, 50) + RESET)
        if show_live:
            print(f'{GREEN_BOLD}=== ALL LIVE RESULTS ({len(results_display)} total) ==={RESET}')
            print(f'{YELLOW_BOLD}Scroll up to see all results{RESET}')
            print(RED_BOLD + _sec_string('mw==') * min(effective_width, 50) + RESET)
            if results_display:
                for line in results_display[-50:] if len(results_display) > 50 else results_display:
                    if len(line) > effective_width - 2:
                        line = line[:effective_width - 5] + _sec_string('mJcn')
                    print(line)
                if len(results_display) > 50:
                    print(f'{CYAN_BOLD}... and {len(results_display) - 50} more results{RESET}')
            else:
                print(f'{YELLOW_BOLD}Waiting for results...{RESET}')
            print(RED_BOLD + _sec_string('mw==') * min(effective_width, 50) + RESET)
        else:
            print(f'{YELLOW_BOLD}Live display OFF — results saved to file only{RESET}')
            print(RED_BOLD + _sec_string('mw==') * min(effective_width, 50) + RESET)
        if last_results:
            h, ip_addr, s, sv = last_results[-1]
            short_h = h[:15] + _sec_string('mJc=') if len(h) > 15 else h
            status_color = get_status_color(s)
            last_line = f'{CYAN_BOLD}{short_h}{RESET}:{YELLOW_BOLD}{port}{RESET} → {status_color}{s}{RESET}'
            if sv and sv != _sec_string('w9diYtnOZw=='):
                last_line += f' [{MAGENTA_BOLD}{sv[:10]}{RESET}]'
            if ip_addr:
                last_line += f' ({BLUE_BOLD}{ip_addr}{RESET})'
            print(YELLOW_BOLD + _sec_string('+th6eIyZ') + last_line + RESET)
        print(RED_BOLD + _sec_string('iw==') * min(effective_width, 40) + RESET)
        print(f'{YELLOW_BOLD}Press Ctrl+C to stop{RESET}')
        sys.stdout.flush()

    def format_result_line(hostname, ip, port, sc, server):
        sc_color = get_status_color(sc)
        line = f'{CYAN_BOLD}{hostname}{RESET}:{YELLOW_BOLD}{port}{RESET} → {sc_color}{sc}{RESET}'
        if ip:
            line += f' ({BLUE_BOLD}{ip}{RESET})'
        if server and server != _sec_string('w9diYtnOZw=='):
            line += f' [{MAGENTA_BOLD}{server[:15]}{RESET}]'
        return line

    def count_total_lines(filename):
        try:
            with open(filename, _sec_string('xNs=')) as f:
                return sum((1 for _ in f))
        except:
            return 0
    while True:
        clear_screen_local()
        print_header()
        while True:
            v = ask(f"{YELLOW_BOLD}Threads (1-50, default 20) (or 'back'):{RESET} ")
            if v is None:
                return
            if not v:
                workers = 20
                break
            try:
                workers = int(v)
                if 1 <= workers <= 50:
                    break
                workers = max(1, min(50, workers))
                break
            except:
                print(f'{RED_BOLD}Invalid number.{RESET}')
        while True:
            v = ask(f"{YELLOW_BOLD}Timeout seconds (0.3-3, default 0.8) (or 'back'):{RESET} ")
            if v is None:
                return
            if not v:
                timeout = 0.8
                break
            try:
                timeout = float(v)
                timeout = max(0.3, min(3, timeout))
                break
            except:
                print(f'{RED_BOLD}Invalid number.{RESET}')
        while True:
            v = ask(f"{YELLOW_BOLD}Port (default 80) (or 'back'):{RESET} ")
            if v is None:
                return
            if not v:
                port = 80
                break
            try:
                port = int(v)
                port = max(1, min(65535, port))
                break
            except:
                print(f'{RED_BOLD}Invalid number.{RESET}')
        while True:
            v = ask(f"{YELLOW_BOLD}Display results live as it scans? (Y/n) (or 'back'):{RESET} ")
            if v is None:
                return
            v = v.lower()
            if v in ('', _sec_string('zw=='), _sec_string('z9x6')):
                show_live = True
                break
            if v in (_sec_string('2A=='), _sec_string('2NY=')):
                show_live = False
                break
            print(f'{RED_BOLD}Please answer Y or N.{RESET}')
        while True:
            input_file = ask(f"\n{YELLOW_BOLD}Hosts file (hostname IP per line) (or 'back'):{RESET} ")
            if input_file is None:
                return
            if os.path.isfile(input_file):
                break
            print(f'{RED_BOLD}File not found{RESET}')
        while True:
            output_file = ask(f"\n{YELLOW_BOLD}Output file (or 'back'):{RESET} ")
            if output_file is None:
                return
            if output_file:
                if not output_file.endswith(_sec_string('mM1xeA==')):
                    output_file += _sec_string('mM1xeA==')
                break
            print(f'{RED_BOLD}Please enter an output file name{RESET}')
        if os.path.exists(output_file):
            print(f"\n{CYAN_BOLD}Output file '{os.path.basename(output_file)}' already exists.{RESET}")
            print(f"{YELLOW_BOLD}  1. Resume\n  2. Start fresh\n  3. Use different filename\n  'back' to return{RESET}")
            while True:
                choice = ask(f"\n{YELLOW_BOLD}Enter choice (1, 2, 3, or 'back'):{RESET} ")
                if choice is None:
                    return
                if choice == _sec_string('hw=='):
                    processed_hosts = read_processed_hosts(output_file)
                    start_line = 0
                    resume_mode = True
                    print(f'\n{GREEN_BOLD}✓ Resuming — {len(processed_hosts)} hosts already processed{RESET}')
                    input(f'\n{YELLOW_BOLD}Press Enter to continue...{RESET}')
                    break
                elif choice == _sec_string('hA=='):
                    resume_mode = False
                    start_line = 0
                    processed_hosts = set()
                    print(f'\n{YELLOW_BOLD}Starting fresh...{RESET}')
                    input(f'\n{YELLOW_BOLD}Press Enter to continue...{RESET}')
                    break
                elif choice == _sec_string('hQ=='):
                    base, ext = os.path.splitext(output_file)
                    i = 1
                    while True:
                        new_file = f'{base}_{i}{ext}'
                        if not os.path.exists(new_file):
                            output_file = new_file
                            break
                        i += 1
                    resume_mode = False
                    start_line = 0
                    processed_hosts = set()
                    print(f'\n{GREEN_BOLD}Using new file: {output_file}{RESET}')
                    input(f'\n{YELLOW_BOLD}Press Enter to continue...{RESET}')
                    break
                else:
                    print(f'{RED_BOLD}Invalid choice.{RESET}')
        else:
            print(f'\n{CYAN_BOLD}New output file: {os.path.basename(output_file)}{RESET}')
            print(f"{YELLOW_BOLD}  1. Start from beginning\n  2. Start from specific line\n  'back' to return{RESET}")
            while True:
                choice = ask(f"\n{YELLOW_BOLD}Enter choice (1, 2, or 'back'):{RESET} ")
                if choice is None:
                    return
                if choice == _sec_string('hw=='):
                    resume_mode = False
                    start_line = 0
                    processed_hosts = set()
                    print(f'\n{GREEN_BOLD}Starting from beginning{RESET}')
                    break
                elif choice == _sec_string('hA=='):
                    while True:
                        v = ask(f"{YELLOW_BOLD}Enter line number (or 'back'):{RESET} ")
                        if v is None:
                            return
                        try:
                            start_line = int(v)
                            if start_line >= 0:
                                resume_mode = False
                                processed_hosts = set()
                                print(f'\n{GREEN_BOLD}Starting from line: {start_line}{RESET}')
                                break
                            else:
                                print(f'{RED_BOLD}Must be 0 or greater.{RESET}')
                        except:
                            print(f'{RED_BOLD}Invalid number.{RESET}')
                    break
                else:
                    print(f'{RED_BOLD}Invalid choice.{RESET}')
            input(f'\n{YELLOW_BOLD}Press Enter to continue...{RESET}')
        total_lines = count_total_lines(input_file)
        if start_line > total_lines:
            print(f'{RED_BOLD}Warning: Start line exceeds total lines.{RESET}')
            start_line = 0
            input(f'\n{YELLOW_BOLD}Press Enter to continue...{RESET}')
        clear_screen_local()
        checker = FastHTTPChecker(timeout=timeout, port=port)
        task_queue = queue.Queue(maxsize=workers * 5)
        result_queue = queue.Queue()
        threads = []
        for _ in range(workers):
            t = threading.Thread(target=worker, args=(task_queue, result_queue, checker))
            t.daemon = True
            t.start()
            threads.append(t)
        try:
            out_f = open(output_file, _sec_string('1w==') if resume_mode else _sec_string('wQ=='), buffering=1)
        except Exception as e:
            print(f'{RED_BOLD}Error opening output file: {e}{RESET}')
            return
        scanned = start_line
        found = 0
        errors = 0
        last_results = deque(maxlen=3)
        results_display = []
        start_time = time.time()
        last_update = 0
        try:
            for chunk in read_file_chunks(input_file, processed_hosts, start_line, chunk_size=50):
                for task in chunk:
                    task_queue.put(task)
                    time.sleep(0.0005)
                results_needed = len(chunk)
                results_received = 0
                while results_received < results_needed:
                    try:
                        line_num, hostname, ip, status_code, server = result_queue.get(timeout=0.5)
                        results_received += 1
                        scanned += 1
                        unwanted = {_sec_string('hYk7'), _sec_string('wtBkadnMfQ=='), _sec_string('xNxvecXcbQ=='), _sec_string('08t7Y8Q='), _sec_string('2NYkftPKeWPYymw=')}
                        if status_code not in unwanted:
                            out_f.write(f"{hostname}:{port} {status_code} : {server or _sec_string('w9diYtnOZw==')}\n")
                            out_f.flush()
                            found += 1
                            results_display.append(format_result_line(hostname, ip, port, status_code, server))
                        else:
                            errors += 1
                        last_results.append((hostname, ip, status_code, server))
                        current_time = time.time()
                        if current_time - last_update >= 0.2:
                            elapsed = time.time() - start_time
                            print_update(scanned, total_lines, found, errors, elapsed, last_results, results_display, output_file, port, show_live)
                            last_update = current_time
                    except queue.Empty:
                        continue
        except KeyboardInterrupt:
            print(f'\n\n{YELLOW_BOLD}⚠ Scan stopped by user{RESET}')
        except Exception as e:
            print(f'\n{RED_BOLD}Error: {e}{RESET}')
        finally:
            for _ in threads:
                task_queue.put(None)
            for t in threads:
                t.join(timeout=1)
            elapsed = time.time() - start_time
            out_f.close()
            print(f'\n\n{GREEN_BOLD}✓ SCAN COMPLETE — Found: {found} | Errors: {errors} | Time: {elapsed:.1f}s{RESET}')
            if results_display:
                print(f'  Total results: {len(results_display)}')
        while True:
            choice = ask(f'\n{CYAN_BOLD}1. Scan another file\n2. Back to main menu\nChoose (1-2): {RESET}')
            if choice is None or choice == _sec_string('hA=='):
                return
            if choice == _sec_string('hw=='):
                break
            print(f'{RED_BOLD}Invalid choice.{RESET}')

def load_hostnames_simple(file_path, start_line):
    try:
        with open(file_path, _sec_string('xA==')) as f:
            for _ in range(start_line):
                next(f, None)
            for line in f:
                yield line.strip()
    except FileNotFoundError:
        print(f'{Fore.RED}File not found: {file_path}{Style.RESET_ALL}')
        return None
    except Exception as e:
        print(f'{Fore.RED}Error reading file: {e}{Style.RESET_ALL}')
        return None

class AdvancedHostnameScannerSimple:

    def __init__(self):
        self.SERVER_MAPPINGS = {_sec_string('98lob97c'): [_sec_string('98lob97c'), _sec_string('98lob97cJj4='), _sec_string('98lob97cJj6Yiw=='), _sec_string('98lob97cJj6YjQ=='), _sec_string('3s19fNI=')], _sec_string('+N5gYs4='): [_sec_string('2N5gYs4='), _sec_string('+P5AQu4='), _sec_string('4txna9/XbA==')], _sec_string('+9BqftnKZmrClEBF5Q=='): [_sec_string('+9BqftnKZmrClEBF5Q=='), _sec_string('//Ba'), _sec_string('+9BqftnKZmrClEFY4ulIXP8=')], _sec_string('+tB9aeXJbGnS'): [_sec_string('+tB9aeXJbGnS'), _sec_string('+tB9acXJbGnS'), _sec_string('+tB9aeXJbGnS7Wxv3g==')], _sec_string('+clsYuTcenjP'): [_sec_string('2clsYsTcenjP')], _sec_string('9dhtaM8='): [_sec_string('1dhtaM8=')], _sec_string('8cxnZdXWe2I='): [_sec_string('0cxnZdXWe2I=')], _sec_string('w+5aS/8='): [_sec_string('w+5aS/8=')], _sec_string('9dFsftnSbGk='): [_sec_string('9dFsftnSbGk=')], _sec_string('4tZkb9fN'): [_sec_string('98lob97cJE/ZwGZ40w=='), _sec_string('4tZkb9fN')], _sec_string('/Nx9eM8='): [_sec_string('/Nx9eM8=')], _sec_string('+tBuZMLNeWg='): [_sec_string('2tBuZMLNeWg=')], _sec_string('9dVmedLfZW3E3A=='): [_sec_string('1dVmedLfZW3E3A=='), _sec_string('9f8='), _sec_string('9dVmedL/ZW3E3A==')], _sec_string('/9R5acTPaA=='): [_sec_string('39R5acTPaA=='), _sec_string('39dqbcbKfGDX')], _sec_string('99JoYdfQ'): [_sec_string('99JoYdfQTkTZyn0='), _sec_string('99JoYdfQR2nC6n1jxNhuaQ=='), _sec_string('99JoYdfQ')], _sec_string('8Nh6eNrA'): [_sec_string('8Nh6eNrA'), _sec_string('0Nh6eNrA')], _sec_string('9+5aLPXVZnnS/3tj2M0='): [_sec_string('9dVmedL/e2PYzQ==')], _sec_string('8dZma9rcKU/a1nxolvpNQg=='): [_sec_string('8dZma9rcKUrE1md409dt'), _sec_string('0c56')], _sec_string('9MxnYs/6TUI='): [_sec_string('1MxnYs/abWI='), _sec_string('9MxnYs/6TUI=')], _sec_string('99RodtnXKV+F'): [_sec_string('99RodtnXWj8='), _sec_string('5Yo=')], _sec_string('+Nx9YN/fcA=='): [_sec_string('+Nx9YN/fcA==')], _sec_string('4ekpSdjeYGLT'): [_sec_string('4ekpSdjeYGLT'), _sec_string('4elMIQ==')], _sec_string('/dBnf8LY'): [_sec_string('/dBnf8LY')], _sec_string('/tx7Y93M'): [_sec_string('3tx7Y93M'), _sec_string('/tx7Y93M')], _sec_string('8NB7adTYemk='): [_sec_string('8NB7adTYemk=')], _sec_string('4Nx7b9PV'): [_sec_string('4Nx7b9PV')], _sec_string('8tBuZcLYZUPV3Ghi'): [_sec_string('8vZHQ/L8')], _sec_string('98N8ftM='): [_sec_string('98N8ftM='), _sec_string('9+tb'), _sec_string('4fheXw==')], _sec_string('+c1hacQ='): [_sec_string('5dx7etPL'), _sec_string('xdx7etPL')], _sec_string('49diYtnOZw=='): []}

    def detect_server(self, sh):
        if not sh:
            return _sec_string('49diYtnOZw==')
        sh = sh.lower()
        for server, patterns in self.SERVER_MAPPINGS.items():
            for pattern in patterns:
                if pattern.lower() in sh:
                    return server
        return _sec_string('+c1hacQ=')

    def get_http_response_fast(self, hostname, port=80, timeout=2):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(timeout)
                s.connect((hostname, port))
                s.send(f'HEAD / HTTP/1.1\r\nHost: {hostname}\r\nConnection: close\r\n\r\n'.encode())
                response = b''
                while True:
                    data = s.recv(1024)
                    if not data or b'\r\n\r\n' in response:
                        break
                    response += data
                return response.decode(errors=_sec_string('395nY8Tc')).split(_sec_string('u7MEBg=='))[0]
        except:
            return None

    def scan_host_fast(self, hostname):
        hostname = hostname.strip()
        if not hostname:
            return (hostname, None, None)
        headers = self.get_http_response_fast(hostname)
        if not headers:
            return (hostname, None, None)
        status_code = None
        server_header = None
        lines = headers.split(_sec_string('u7M='))
        if len(lines) > 0:
            try:
                status_code = int(lines[0].split(_sec_string('lg=='))[1])
            except:
                pass
        for line in lines[1:]:
            if line.lower().startswith(_sec_string('xdx7etPLMw==')):
                server_header = line.split(_sec_string('jA=='), 1)[1].strip()
                break
        return (hostname, status_code, self.detect_server(server_header))

    def run_scan_fast(self, file_path, results_file, start_line):
        try:
            with open(results_file, _sec_string('wQ==')) as outfile:
                hostnames = load_hostnames_simple(file_path, start_line)
                if hostnames is None:
                    return
                futures = set()
                with ThreadPoolExecutor(max_workers=100) as executor:
                    for _ in range(1000):
                        try:
                            h = next(hostnames)
                            if h:
                                futures.add(executor.submit(self.scan_host_fast, h))
                        except StopIteration:
                            break
                    pbar = tqdm(desc=_sec_string('5dpoYtjQZ2uW0WZ/wso='), unit=_sec_string('3tZ6eMU='), dynamic_ncols=True)
                    try:
                        while futures:
                            done, _ = wait(futures, return_when=FIRST_COMPLETED)
                            for future in done:
                                futures.remove(future)
                                result = future.result()
                                if result[1] and result[1] != 302:
                                    line = f'{result[0]} : {result[1]} : {result[2]}'
                                    outfile.write(line + _sec_string('vA=='))
                                    outfile.flush()
                                    append_to_v4(line)
                                pbar.update(1)
                                try:
                                    h = next(hostnames)
                                    if h:
                                        futures.add(executor.submit(self.scan_host_fast, h))
                                except StopIteration:
                                    pass
                    except KeyboardInterrupt:
                        print(f'{Fore.YELLOW}\nScan paused.{Style.RESET_ALL}')
                        return
                    pbar.close()
        except Exception as e:
            print(f'{Fore.RED}Error in scan: {e}{Style.RESET_ALL}')
            return

async def option_10_advanced_hostname_scanner():
    while True:
        try:
            clear_screen()
            w = term_width()
            print()
            print(f"{Fore.RED}{Style.BRIGHT}{center_block(_sec_string('8vZETf/3KV/1+EdC8+spWO7tKUPk/UBC9+tQLOCP'), w)}{Style.RESET_ALL}")
            print(f"{Fore.CYAN}{center_block(_sec_string('4txladHLaGGMmUlE19piacSLPDjGy2Bh0w=='), w)}{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}{center_block(_sec_string('4sB5aZaea23V0i4s180pbdjAKXjf1GwswtYpftPNfH7YmX1jltRoZdiZZGnYzA=='), w)}{Style.RESET_ALL}")
            print()
            scanner = AdvancedHostnameScannerSimple()
            while True:
                input_file = ask(f"\n{Fore.CYAN}Enter path to hostnames file (or 'back'): {Style.RESET_ALL}")
                if input_file is None:
                    return
                if not input_file:
                    print(f'{Fore.YELLOW}Please enter a file path.{Style.RESET_ALL}')
                    continue
                if not os.path.isfile(input_file):
                    print(f'{Fore.RED}File not found: {input_file}{Style.RESET_ALL}')
                    while True:
                        c = ask(f'{Fore.YELLOW}1. Try again\n2. Back to main menu\nChoose (1-2): {Style.RESET_ALL}')
                        if c is None or c == _sec_string('hA=='):
                            return
                        if c == _sec_string('hw=='):
                            break
                        print(f'{Fore.RED}Invalid choice.{Style.RESET_ALL}')
                    continue
                break
            while True:
                results_file = ask(f"{Fore.CYAN}Enter results file (default: host_results.txt, or 'back'): {Style.RESET_ALL}")
                if results_file is None:
                    return
                if not results_file:
                    results_file = _sec_string('3tZ6eOnLbH/D1X1/mM1xeA==')
                    break
                if not re.match(_sec_string('6OJVe+qUJyzrki0='), results_file):
                    print(f'{Fore.RED}Invalid file name.{Style.RESET_ALL}')
                    continue
                break
            while True:
                print(f'\n{Fore.CYAN}Choose scan mode:{Style.RESET_ALL}')
                print(f'{Fore.WHITE}1 = NEW scan (start from line 0){Style.RESET_ALL}')
                print(f'{Fore.WHITE}2 = RESUME scan from specific line{Style.RESET_ALL}')
                print(f"{Fore.YELLOW}Type 'back' to return{Style.RESET_ALL}")
                mode = ask(f"{Fore.CYAN}Enter choice (1/2 or 'back'): {Style.RESET_ALL}")
                if mode is None:
                    return
                if mode == _sec_string('hw=='):
                    start_line = 0
                    print(f'{Fore.GREEN}Starting NEW scan...{Style.RESET_ALL}')
                    break
                elif mode == _sec_string('hA=='):
                    while True:
                        ri = ask(f"{Fore.CYAN}Enter line number to resume from (or 'back'): {Style.RESET_ALL}")
                        if ri is None:
                            return
                        if ri.isdigit():
                            start_line = int(ri)
                            if start_line >= 0:
                                print(f'{Fore.GREEN}Resuming from line {start_line}...{Style.RESET_ALL}')
                                break
                            else:
                                print(f'{Fore.RED}Must be 0 or greater.{Style.RESET_ALL}')
                        else:
                            print(f'{Fore.RED}Invalid number.{Style.RESET_ALL}')
                    break
                else:
                    print(f'{Fore.RED}Invalid choice.{Style.RESET_ALL}')
            print(f'\n{Fore.CYAN}Starting scan...{Style.RESET_ALL}')
            scanner.run_scan_fast(input_file, results_file, start_line)
            print(f'\n{Fore.GREEN}Scan completed! Results saved to {results_file}{Style.RESET_ALL}')
            while True:
                c = ask(f'\n{Fore.CYAN}1. Scan another file\n2. Back to main menu\nChoose (1-2): {Style.RESET_ALL}')
                if c is None or c == _sec_string('hA=='):
                    return
                if c == _sec_string('hw=='):
                    break
                print(f'{Fore.RED}Invalid choice.{Style.RESET_ALL}')
        except KeyboardInterrupt:
            print(f'\n{Fore.YELLOW}Operation cancelled.{Style.RESET_ALL}')
            return
        except Exception as e:
            print(f'{Fore.RED}Unexpected error: {str(e)}{Style.RESET_ALL}')
            return

async def create_anti_dpi_format():
    RED_BOLD = _sec_string('reI4N4WIZA==')
    GREEN_BOLD = _sec_string('reI4N4WLZA==')
    YELLOW_BOLD = _sec_string('reI4N4WKZA==')
    CYAN_BOLD = _sec_string('reI4N4WPZA==')
    RESET = _sec_string('reI5YQ==')

    @dataclass
    class Stats:
        processed: int = 0
        success: int = 0
        failed: int = 0
        written: int = 0
        duplicates: int = 0
        start_time: float = field(default_factory=time.time)
        lock: threading.Lock = field(default_factory=threading.Lock)

        def update(self, processed=0, success=0, failed=0, written=0, duplicates=0):
            with self.lock:
                self.processed += processed
                self.success += success
                self.failed += failed
                self.written += written
                self.duplicates += duplicates
                return (self.processed, self.success, self.failed, self.written, self.duplicates)

        @property
        def rate(self):
            with self.lock:
                elapsed = time.time() - self.start_time
                return self.processed / elapsed if elapsed > 0 else 0

    class ProgressDisplay:

        def __init__(self, total, unique):
            self.total = total
            self.unique = unique
            self.last_len = 0
            self.start = time.time()

        def fmt(self, n):
            if n >= 1000000000:
                return f'{n / 1000000000.0:.1f}B'
            if n >= 1000000:
                return f'{n / 1000000.0:.1f}M'
            if n >= 1000:
                return f'{n / 1000.0:.0f}K'
            return str(n)

        def show(self, stats, current=''):
            proc, succ, fail, writ, dup = stats.update()
            pct = min(100, int(proc * 100 / self.total)) if self.total else 0
            bar = _sec_string('iw==') * (pct // 5) + _sec_string('iA==') + _sec_string('lg==') * (20 - pct // 5 - 1)
            if pct == 100:
                bar = _sec_string('iw==') * 20
            rate = stats.rate / 1000
            w = term_width()
            line = f'\r[{bar}] {pct:3d}% | {self.fmt(proc):>6} | ✓{self.fmt(succ):>5} | ✗{self.fmt(fail):>5} | 🔄{self.fmt(dup):>5} | 💾{self.fmt(writ):>5} | {rate:.1f}K/s | {current[:20]:<20}'
            if len(line) > w - 1:
                line = line[:w - 4] + _sec_string('mJcn')
            sys.stdout.write(_sec_string('uw==') + _sec_string('lg==') * self.last_len + _sec_string('uw=='))
            sys.stdout.write(line)
            sys.stdout.flush()
            self.last_len = len(line)

        def done(self):
            sys.stdout.write(_sec_string('vA=='))

    class ImmediateWriter:

        def __init__(self, filename):
            self.filename = filename
            self.file = open(filename, _sec_string('wQ=='), buffering=1, encoding=_sec_string('w81vIY4='), errors=_sec_string('xNx5YNfabA=='))
            self.lock = threading.Lock()
            self._closed = False
            self.seen_hostnames = set()

        def write(self, hostname, ip):
            with self.lock:
                if not self._closed:
                    if hostname in self.seen_hostnames:
                        return False
                    self.file.write(f'{hostname}\t{ip}\n')
                    self.file.flush()
                    os.fsync(self.file.fileno())
                    self.seen_hostnames.add(hostname)
                    return True
            return False

        def close(self):
            with self.lock:
                if not self._closed:
                    self.file.close()
                    self._closed = True

        def __enter__(self):
            return self

        def __exit__(self, *args):
            self.close()

    def resolve_getaddrinfo(hostname):
        try:
            result = socket.getaddrinfo(hostname, None, socket.AF_INET, socket.SOCK_STREAM)
            if result:
                return result[0][4][0]
        except:
            pass
        return None

    def count_lines_and_deduplicate(filename):
        size = os.path.getsize(filename)
        print(f'📊 Analyzing {size / 1000000000.0:.2f} GB file...')
        total = 0
        unique_hostnames = set()
        with open(filename, _sec_string('xA=='), encoding=_sec_string('w81vIY4='), errors=_sec_string('xNx5YNfabA==')) as f:
            for line in f:
                h = line.strip()
                if h and (not h.startswith(_sec_string('lQ=='))):
                    total += 1
                    unique_hostnames.add(h)
        return (total, len(unique_hostnames))
    while True:
        clear_screen()
        w = min(term_width(), 90)
        line = _sec_string('iw==') * w
        print(f'{CYAN_BOLD}{line}{RESET}')
        print(f"{GREEN_BOLD}{center_block(_sec_string('9etMTeL8KUr/9Uws8PZbQfftKUr56ylN+O1ALPLpQCye/UdflutMX/n1X0nkmX86mIsg'), w)}{RESET}")
        print(f'{CYAN_BOLD}{line}{RESET}')
        print(f"{YELLOW_BOLD}{center_block(_sec_string('4sB5aZaea23V0i4s180pbdjAKXzE1mR8wpl9Y5bLbHjDy2cswtYpYdfQZyzb3Gd5'), w)}{RESET}")
        print()
        infile = ask(f"{CYAN_BOLD}📥 Input file (or 'back'): {RESET}")
        if infile is None:
            return
        infile = infile.strip(_sec_string('lJ4='))
        if not os.path.exists(infile):
            print(f'{RED_BOLD}❌ File not found{RESET}')
            input(_sec_string('5stsf8WZTGLC3HsswtYpb9nXfWXYzGwimJc='))
            continue
        outfile = ask(f"{CYAN_BOLD}📤 Output file (or 'back'): {RESET}")
        if outfile is None:
            return
        outfile = outfile.strip(_sec_string('lJ4='))
        if os.path.exists(outfile):
            ans = ask(f"{YELLOW_BOLD}⚠️  Overwrite {outfile}? (y/N) (or 'back'): {RESET}")
            if ans is None:
                return
            if ans.lower() != _sec_string('zw=='):
                continue
        size = os.path.getsize(infile)
        print(f'\n📦 {size / 1000000000.0:.2f} GB input')
        if size > 20000000000.0:
            concurrency = 1000
            print(_sec_string('RiaTjJbsRVjk+Clh2d1sNpaIOTyGmWpj2Np8fsTcZ3g='))
        elif size > 2000000000.0:
            concurrency = 500
            print(_sec_string('VCOoLP7wTkSW1GZo04MpOYaJKW/Z12p5xMtsYsI='))
        else:
            concurrency = 200
            print(_sec_string('RiadtZb3Rl77+EUs29ZtaYyZOzyGmWpj2Np8fsTcZ3g='))
        total, unique = count_lines_and_deduplicate(infile)
        duplicates = total - unique
        print(f'🎯 {total:,} total hostnames\n📊 {unique:,} unique hostnames')
        if duplicates > 0:
            print(f'🔄 {duplicates:,} duplicates will be resolved once')
        print()
        if total == 0:
            print(_sec_string('VCSFLPPUeXjPmW9l2tw='))
            input(_sec_string('5stsf8WZTGLC3HsswtYpb9nXfWXYzGwimJc='))
            continue
        stats = Stats()
        progress = ProgressDisplay(total, unique)
        sem = asyncio.Semaphore(concurrency)
        shutdown = False
        seen_for_processing = set()

        def signal_handler(s, f):
            nonlocal shutdown
            shutdown = True
            print(_sec_string('vFuTrFkBhiyW6mF5ws1gYtGZbWPB1ylrxNhqadDMZWDPlyci'))
        signal.signal(signal.SIGINT, signal_handler)
        signal.signal(signal.SIGTERM, signal_handler)
        print(_sec_string('RiaTjJbrbH/Z1X9l2N4nIpg='))
        print(_sec_string('iw==') * min(term_width(), 85))
        try:
            with ThreadPoolExecutor(max_workers=concurrency) as executor, ImmediateWriter(outfile) as writer:
                loop = asyncio.get_event_loop()
                pending = set()

                async def resolve_one(hostname):
                    if shutdown:
                        return
                    async with sem:
                        ip = await loop.run_in_executor(executor, resolve_getaddrinfo, hostname)
                        if ip:
                            written = await loop.run_in_executor(executor, writer.write, hostname, ip)
                            if written:
                                stats.update(success=1, written=1)
                            else:
                                stats.update(success=1, duplicates=1)
                        else:
                            stats.update(failed=1)
                        stats.update(processed=1)
                        if stats.processed % 10 == 0:
                            progress.show(stats, hostname)
                with open(infile, _sec_string('xA=='), encoding=_sec_string('w81vIY4='), errors=_sec_string('xNx5YNfabA==')) as f:
                    for line in f:
                        if shutdown:
                            break
                        hostname = line.strip()
                        if not hostname or hostname.startswith(_sec_string('lQ==')):
                            continue
                        if hostname in seen_for_processing:
                            stats.update(processed=1, duplicates=1)
                            continue
                        seen_for_processing.add(hostname)
                        task = asyncio.create_task(resolve_one(hostname))
                        pending.add(task)
                        if len(pending) >= concurrency:
                            done, pending = await asyncio.wait(pending, return_when=asyncio.FIRST_COMPLETED)
                            for t in done:
                                try:
                                    await t
                                except:
                                    pass
                if pending and (not shutdown):
                    await asyncio.gather(*pending, return_exceptions=True)
        except KeyboardInterrupt:
            print(f'\n{YELLOW_BOLD}⚠️  Interrupted{RESET}')
        except Exception as e:
            print(f'\n{RED_BOLD}💥 Error: {e}{RESET}')
        progress.done()
        proc, succ, fail, writ, dup = stats.update()
        elapsed = time.time() - stats.start_time
        line = _sec_string('iw==') * min(term_width(), 85)
        print(line)
        print(f'✅ COMPLETE')
        print(f'   Total processed: {proc:,}')
        print(f'   Unique hostnames: {unique:,}')
        print(f'   Successful resolutions: {succ:,}')
        print(f'   Failed resolutions: {fail:,}')
        print(f'   Duplicates skipped: {dup:,}')
        print(f'   Written to file: {writ:,}')
        print(f'   Time: {elapsed / 60:.1f} minutes @ {stats.rate:.0f}/s')
        if os.path.exists(outfile):
            fsize = os.path.getsize(outfile)
            print(f'   Output: {outfile} ({fsize / 1000000.0:.1f} MB)')
        while True:
            c = ask(f'\n{CYAN_BOLD}1. Run another\n2. Back to main menu\nChoose (1-2): {RESET}')
            if c is None or c == _sec_string('hA=='):
                return
            if c == _sec_string('hw=='):
                break
            print(f'{RED_BOLD}Invalid choice.{RESET}')

def option_9_exit():
    print(f'\n{Fore.YELLOW}Exiting program...{Style.RESET_ALL}')
    try:
        state_data = {_sec_string('2th6eOnccWXC'): datetime.datetime.now().strftime(_sec_string('k+AkKduULGiWnEE2k/QzKeU=')), _sec_string('xNx6edrNelPQ0GVp'): RESULTS_FILE, _sec_string('xNxkbd/XYGLR5m1tz8o='): days_remaining()}
        with open(STATE_FILE, _sec_string('wQ==')) as f:
            json.dump(state_data, f, indent=2)
        print(f'{Fore.GREEN}State saved successfully.{Style.RESET_ALL}')
    except Exception as e:
        print(f'{Fore.YELLOW}Warning: Could not save state: {e}{Style.RESET_ALL}')
    try:
        if _sec_string('+vhaWOnrXELp/0BA8w==') in globals():
            update_last_run_date()
    except:
        pass
    print(f'{Fore.CYAN}Goodbye!{Style.RESET_ALL}')
    sys.exit(0)

async def safe_dispatch(name, func, is_async=False):
    try:
        if is_async:
            await func()
        else:
            res = func()
            if asyncio.iscoroutine(res):
                await res
    except KeyboardInterrupt:
        print(f'\n{GOLD}{name} interrupted. Returning to menu...{RESET_C}')
        time.sleep(0.6)
    except Exception as e:
        print(f'\n\x1b[38;2;255;60;60mError in {name}: {e}{RESET_C}')
        try:
            input(f'{GOLD}Press Enter to return to main menu...{RESET_C}')
        except Exception:
            time.sleep(2)

async def main_menu():
    while True:
        clear_screen()
        w = min(term_width(), 100)
        w = max(24, w)
        border = _sec_string('VCyZ') * (w - 2)
        print()
        print(grad(_sec_string('VCyd') + border + _sec_string('VCye'), FIRE_1, FIRE_2))
        title = center_block(_sec_string('4I8pTfjgJF/48ClK//dNSeSZWk/k8FlYlos5PoCZWV7z9EBZ+w=='), w - 2)
        print(f'\x1b[38;2;255;60;20m║{RESET_C}' + grad(title, FIRE_1, FIRE_2) + f'\x1b[38;2;255;200;40m║{RESET_C}')
        print(grad(_sec_string('VCyT') + border + _sec_string('VCyU'), FIRE_2, FIRE_1))
        print()
        art = [_sec_string('lpkpLJaZKSyWmSkslpkpLOmVJyGblCQhmJVW'), _sec_string('lpkpLJaZKSyWmSkslpkpIJvHKSyWmSkslpkpLJbHJCI='), _sec_string('lpkpLJaZKSyWmSkslpklUunmViyWmSkslpkpLJaZVlPp5yc='), _sec_string('lpkpLJaZKSyWmSksmccrLJaZdy6WmSkilpkpLsiZKSyUx1U='), _sec_string('lpkpLJaZKSyWmSlVlpklIZuXViyWmSlFlpkpLOmXJCGYmSlV'), _sec_string('lpkpLJaZKSyWmSksyplQLJaZKSzIlCcsypklIciZKSyWmVAsyg=='), _sec_string('lpkpLJaZKSyWmSksypl1LJaZKSyWmSlxy4Nyd5aZKSyWmSksypl1'), _sec_string('lpkpLJaZKSyWmSks3JllLJaZKSyWmSYsyplVLJaZKSyWmSgs2g=='), _sec_string('lpkpLJaZKSyWlyRylpkhU+mVJyGbmyki6JcpLpuUJyDp5iAslsckIg=='), _sec_string('lpkpLJaZKSyemSkslpkpLJaZKSyZmSYsyplVLOqZKSyWmSkslpkpLJ8='), _sec_string('lpkpLJaZKSyW5SdT6eZWIJaZKXKWmVUjlOUmLJbHKSyWl1ZT6eYlIw=='), _sec_string('lpkpLJaZKSyWmVci6eZWU5aZKSyWmSkslpkpLJaZKSyW5lZT6ZdX'), _sec_string('lpkpLJaZKSyWmSkslsUpcOKZd1CWmSgslpkoLJaWdyzixSlw'), _sec_string('lpkpLJaZKSyWmSkslsUpcNqZKSzpmVYs6ZlWLOmZKSyXxSlw'), _sec_string('lpkpLJaZKSyWmSkslsUpYJblJlqW7ylalu8pWpbvVSOW0ylw'), _sec_string('lpkpLJaZKSyWmSksltUpLOqZVXDpxVZw6cVWcOnFJiyZmSkt'), _sec_string('lpkpLJaZKSyWmSkslplVLJblUliW7SlYlu0pWJbtQCOWmSY='), _sec_string('lpkpLJaZKSyWmSkslpkpUJaZaVKb5yRSm+ckUpvnLiyWlg=='), _sec_string('lpkpLJaZKSyWmSkslpkpLOqZKSyWmSkslpkpLJaZKSyZ'), _sec_string('lpkpLJaZKSyWmSkslpkpLJblJyyWmSkslpkpLJaZJSM='), _sec_string('lpkpLJaZKSyWmSkslpkpLJaZKS7olCdT6eYlIeib')]
        art_width = max((len(line) for line in art))
        art = [line.ljust(art_width) for line in art]
        if art_width > w - 2:
            art_width = w - 2
            art = [line[:art_width] for line in art]
        pad = max(0, (w - art_width) // 2)
        total = len(art)
        for i, line in enumerate(art):
            t = i / max(total - 1, 1)
            r = int(FIRE_1[0] + (FIRE_2[0] - FIRE_1[0]) * t)
            g = int(FIRE_1[1] + (FIRE_2[1] - FIRE_1[1]) * t)
            b = int(FIRE_1[2] + (FIRE_2[2] - FIRE_1[2]) * t)
            print(_sec_string('lg==') * pad + f'\x1b[38;2;{r};{g};{b}m{line}{RESET_C}')
        print()
        tagline = _sec_string('VC6PLJbqR0WW/0BC8vxbLJZ7viyW90xY4fZbR5bqSk3490xelpnLu5aZSELi8CRI5vApWPn2RUf/7SksVC6P')
        print(grad(center_block(tagline, w), CYAN_1, CYAN_2))
        print()
        days = days_remaining()
        dim_display = _format_days()
        print(grad(_sec_string('VC2I') * w, PINK_1, PINK_2))
        label = f'  ● DAYS REMAINING '
        val = f'  {dim_display}  '
        pad_line = w - disp_width(f'  ● DAYS REMAINING   {dim_display}  ')
        print(f'{SOFT_CYAN}{label}{RESET_C}{GOLD}\x1b[1m{val}{RESET_C}' + _sec_string('lg==') * max(0, pad_line))
        print(f"{SOFT_CYAN}  ● OWNER          {RESET_C}  {HOT_PINK}\x1b[1m{fit_width(_sec_string('3s19fMWDJiPCl2RpmfFob93ce3zE0GRphIw9'), w - 30)}{RESET_C}")
        print(f"{SOFT_CYAN}  ● GROUP          {RESET_C}  \x1b[38;2;0;200;255m{fit_width(_sec_string('3s19fMWDJiPCl2Rpmdhndd/KeX/V2Gdi08t9Y9nV'), w - 30)}{RESET_C}")
        print(grad(_sec_string('VC2I') * w, PINK_2, PINK_1))
        print()
        note_top = _sec_string('VCyk') + _sec_string('VC2J') * (w - 2) + _sec_string('VCyn')
        note_text = _sec_string('lpnrlhaZKUvE1nx8ltVgYt2ZZ2PCmX5jxNJgYtGGKU/Z131t1c0peN7cKWPB12x+ltZnLOLcZWnRy2hhjJlJRNfaYmnEyXtl29w7OYI=')
        note_text = fit_width(note_text, max(8, w - 4))
        note_pad = max(0, w - 2 - disp_width(note_text))
        note_bot = _sec_string('VCy5') + _sec_string('VC2J') * (w - 2) + _sec_string('VCym')
        print(f'{ORANGE}{note_top}{RESET_C}')
        print(f"{ORANGE}│{RESET_C}{GOLD}{note_text}{RESET_C}{_sec_string('lg==') * note_pad}{ORANGE}│{RESET_C}")
        print(f'{ORANGE}{note_bot}{RESET_C}')
        print()
        title_menu = _sec_string('lvRIRfiZREn47ClagJk=')
        print(grad(_sec_string('VCyd') + title_menu.center(w - 2, _sec_string('VCyZ')) + _sec_string('VCye'), CYAN_1, CYAN_2))
        menu = [(_sec_string('hw=='), _sec_string('/+kpT//9Wyzl+khC+PxbLPXsWlj59Clc+etdLOX6SEKWW4mYlupcXOb2W1jlmUpF8uspWO7tKUPkmVpF+P5FSZb6QEjk')), (_sec_string('hA=='), _sec_string('5PxfSeTqTCz/6Slf9fhHQvPrKVqA')), (_sec_string('hQ=='), _sec_string('5exLSPn0SEX45lpP9/dHSeQ=')), (_sec_string('gg=='), _sec_string('8PBFSZjtUViW6kpN+PdMXpaRWkH39UUs8PBFSZ8=')), (_sec_string('gw=='), _sec_string('5utGVO+ZWk/390dJ5A==')), (_sec_string('gA=='), _sec_string('+PYpSuT8TFbzmVpP9/dHSeSZQUPl7UdN+/wpReaZT0Pk9EhY')), (_sec_string('gQ=='), _sec_string('8vZETf/3KV/1+EdC8+spWO7tKUPk/UBC9+tQ')), (_sec_string('jg=='), _sec_string('9etMTeL8KUr/9Uws8PZbQfftKUr56ylN+O1ALPLpQCye/UdflutMX/n1X0nkkA==')), (_sec_string('jw=='), _sec_string('5epBJ+X3QCzy8FtJ9e0pRPnqXUL39Ews5vZbWJaNPT+W6kpN+PdMXg==')), (_sec_string('h4k='), _sec_string('8+FAWA=='))]
        for num, desc in menu:
            if num == _sec_string('h4k='):
                arrow = f'\x1b[38;2;255;40;40m▸{RESET_C}'
                num_c = f'\x1b[38;2;255;60;60m\x1b[1m{num:>2}{RESET_C}'
                desc_c = f'\x1b[38;2;255;100;100m{desc}{RESET_C}'
            else:
                arrow = f'{GOLD}▸{RESET_C}'
                num_c = f'{GOLD}\x1b[1m{num:>2}{RESET_C}'
                desc_c = f'{WHITE_B}{desc}{RESET_C}'
            row = f'   {arrow}  {num_c}{DIM_GRAY}.{RESET_C}  {desc_c}'
            vis = f'   ▸  {num:>2}.  {desc}'
            max_vis = w - 4
            if len(vis) > max_vis:
                vis = vis[:max_vis - 3] + _sec_string('mJcn')
                desc = desc[:max(0, len(desc) - (len(f'   ▸  {num:>2}.  {desc}') - max_vis))] + _sec_string('mJcn')
            pad = w - 2 - len(vis)
            border_l = grad(_sec_string('VCyY'), CYAN_1, CYAN_2)
            border_r = grad(_sec_string('VCyY'), CYAN_2, CYAN_1)
            print(f"{border_l}{RESET_C}{row}{_sec_string('lg==') * max(0, pad)} {border_r}")
        print(grad(_sec_string('VCyT') + _sec_string('VCyZ') * (w - 2) + _sec_string('VCyU'), CYAN_2, CYAN_1))
        print()
        try:
            prompt = f"{grad(_sec_string('lpnrmzCZ'), FIRE_1, FIRE_2)}{SOFT_CYAN}Select an option {RESET_C}{DIM_GRAY}(1-10){RESET_C}{SOFT_CYAN}:{RESET_C} "
            choice = input(prompt).strip()
            if choice == _sec_string('hw=='):
                await safe_dispatch(_sec_string('+cl9ZdnXKT0='), custom_port_scanner, is_async=True)
            elif choice == _sec_string('hA=='):
                await safe_dispatch(_sec_string('+cl9ZdnXKT4='), reverse_ip_scanner_v2, is_async=True)
            elif choice == _sec_string('hQ=='):
                await safe_dispatch(_sec_string('+cl9ZdnXKT8='), subdomain_scanner, is_async=False)
            elif choice == _sec_string('gg=='):
                await safe_dispatch(_sec_string('+cl9ZdnXKTg='), file_scanner, is_async=True)
            elif choice == _sec_string('gw=='):
                await safe_dispatch(_sec_string('+cl9ZdnXKTk='), proxy_scanner_main, is_async=False)
            elif choice == _sec_string('gA=='):
                await safe_dispatch(_sec_string('+cl9ZdnXKTo='), unlimited_scanner_no_freeze, is_async=False)
            elif choice == _sec_string('gQ=='):
                await safe_dispatch(_sec_string('+cl9ZdnXKTs='), option_10_advanced_hostname_scanner, is_async=True)
            elif choice == _sec_string('jg=='):
                await safe_dispatch(_sec_string('+cl9ZdnXKTQ='), create_anti_dpi_format, is_async=True)
            elif choice == _sec_string('jw=='):
                await safe_dispatch(_sec_string('+cl9ZdnXKTU='), ssh_sni_direct_scanner, is_async=True)
            elif choice == _sec_string('h4k='):
                option_9_exit()
            else:
                print(f'\x1b[38;2;255;60;60mInvalid choice. Please select 1-10.{RESET_C}')
                time.sleep(1)
        except KeyboardInterrupt:
            print(f'\n{GOLD}Returning to menu...{RESET_C}')
            time.sleep(0.5)
        except Exception as e:
            print(f'\n\x1b[38;2;255;60;60mError: {e}{RESET_C}')
            time.sleep(2)

def run_engine():
    with open(RESULTS_FILE, _sec_string('wQ=='), encoding=_sec_string('w81vIY4=')) as f:
        f.write(_sec_string('5dpoYpbrbH/D1X1/lvVma5aUKVqAl310wrM='))
        f.write(_sec_string('iw==') * 50 + _sec_string('vA=='))
        f.write(f'Scan session started: {datetime.datetime.now()}\n\n')
    asyncio.run(main_menu())
if __name__ == _sec_string('6eZkbd/XVlM='):
    run_engine()
