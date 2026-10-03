# Auto-generated obfuscated build (do not edit)
_SEC_SALT = 2715234182

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
V5 ANYISP SNI FINDER SCRIPT 2026 PREMIUM
Updated with:
- UNLIMITED SCANN_NO FREEZE (Option 8)
- CREATE FILE FORMAT FOR ANTI DPI (Option 11)
- Responsive main menu UI
- Fixed datetime error in Option 8
- Fixed Option 2 back-to-menu handling
- Fixed Option 4 multiprocessing crash (ThreadPoolExecutor)
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
from collections import OrderedDict, deque
import platform
import threading
import queue
import select
from dataclasses import dataclass, field
init(autoreset=True)
RESULTS_FILE = _sec_string('9+MB8tmj')
STATE_FILE = _sec_string('0rRO6P6kW+fVsgHs0rhB')

def handle_sigint(signal, frame):
    print(f'{Fore.RED}\nProgram interrupted. Exiting gracefully...{Style.RESET_ALL}')
    sys.exit(0)
signal.signal(signal.SIGINT, handle_sigint)

def get_build_prop_info():
    try:
        cmd = _sec_string('xrJb9tO4Xw==')
        output = subprocess.check_output(cmd, shell=True).decode()
        props = {}
        for line in output.split(_sec_string('qw==')):
            if _sec_string('+qVAqNKyXe/Au0Hp/A==') in line or _sec_string('+qVAqNGlQOLUtFuozLhL482K') in line or _sec_string('+qVAqNGlQOLUtFuow6VO6MWK') in line:
                key = line.split(_sec_string('+g=='))[1].split(_sec_string('/A=='))[0]
                value = line.split(_sec_string('+g=='))[2].split(_sec_string('/A=='))[0]
                props[key] = value
        return props
    except:
        return {}

def get_cpu_serial():
    try:
        with open(_sec_string('jqdd6cL4TPbUvkHgzg=='), _sec_string('0w==')) as f:
            for line in f:
                if line.startswith(_sec_string('8rJd78C7')):
                    return line.split(_sec_string('mw=='))[1].strip()
    except:
        return ''

def get_device_id():
    identifiers = []
    build_props = get_build_prop_info()
    for key in sorted(build_props.keys()):
        identifiers.append(str(build_props[key]))
    try:
        cmd = _sec_string('0rJb8si5SPWBsErygaRK5dSlSqbAuUv0zr5L2ciz')
        android_id = subprocess.check_output(cmd, shell=True).decode().strip()
        identifiers.append(android_id)
    except:
        pass
    cpu_serial = get_cpu_serial()
    if cpu_serial:
        identifiers.append(cpu_serial)
    if not identifiers:
        system_files = [_sec_string('jqRW9Y60Q+fSpADnz7Nd6cizcPPStQDnz7Nd6cizH6nIhEr0yLZD'), _sec_string('jqRW9Y60Q+fSpADoxKMA8c22QbaOtkvi07Jc9Q=='), _sec_string('jqRW9Y60Q+fSpADoxKMA49W/H6nAs0v0xKRc')]
        for file_path in system_files:
            try:
                with open(file_path, _sec_string('0w==')) as f:
                    content = f.read().strip()
                    if content:
                        identifiers.append(content)
            except:
                continue
    device_string = _sec_string('3Q==').join([str(x) for x in identifiers if x])
    if not device_string:
        device_string = _sec_string('x7ZD6sO2TO3+vkvjz6NG4MiyXQ==')
    device_hash = hashlib.sha256(device_string.encode()).hexdigest()
    formatted_id = _sec_string('jA==').join([device_hash[i:i + 4] for i in range(0, 16, 4)])
    return formatted_id.upper()
SERVER_DAYS_REMAINING = 0

def days_remaining():
    return SERVER_DAYS_REMAINING

def _format_days():
    d = days_remaining()
    if d >= 36500:
        return _sec_string('Q1+xpu2eacP1nmLD')
    return str(d)

def clear_screen():
    os.system(_sec_string('wrtc') if os.name == _sec_string('z6M=') else _sec_string('wrtK59M='))

def append_to_v4(content):
    """Append results to V4.txt"""
    try:
        with open(RESULTS_FILE, _sec_string('wA=='), encoding=_sec_string('1KNJq5k=')) as f:
            f.write(content + _sec_string('qw=='))
    except Exception as e:
        print(f'{Fore.RED}Error writing to V4.txt: {e}{Style.RESET_ALL}')

async def fetch_status(session, url, semaphore):
    try:
        async with semaphore:
            async with session.get(url, timeout=2) as response:
                server = response.headers.get(_sec_string('8rJd8MSl'), _sec_string('9LlE6M6gQQ=='))
                return (response.status, server)
    except asyncio.TimeoutError:
        return (None, _sec_string('9b5C486iWw=='))
    except Exception as e:
        return (None, f'Error: {e}')

async def scan_ip(ip, total_ips, index, server_dict, semaphore):
    url = f'http://{ip}'
    async with aiohttp.ClientSession() as session:
        status, server = await fetch_status(session, url, semaphore)
        if status and status != 302 and (_sec_string('5KVd6dM=') not in server):
            server_dict[ip] = (status, server)
            sys.stdout.write(_sec_string('rA==') + _sec_string('gQ==') * 80 + _sec_string('rA=='))
            sys.stdout.flush()
            result_line = f'{Fore.GREEN}{ip}: {Fore.CYAN}{status} {Fore.MAGENTA}{server}'
            print(result_line)
            append_to_v4(result_line)
        scanned = index + 1
        progress = scanned / total_ips
        speed = scanned / (time.time() - start_time)
        progress_line = f'\rIPs scanned: {Fore.CYAN}{scanned}/{total_ips}{Style.RESET_ALL} ({progress * 100:.2f}%) - Speed: {Fore.CYAN}{speed:.2f} IPs/s{Style.RESET_ALL}'
        sys.stdout.write(progress_line)
        sys.stdout.flush()

async def scan_cidr_block(cidr_block):
    network = ipaddress.ip_network(cidr_block, strict=False)
    total_ips = network.num_addresses
    ips = network.hosts()
    server_dict = {}
    semaphore = asyncio.Semaphore(300)
    global start_time
    start_time = time.time()
    chunk_size = 1000
    ip_list = list(ips)
    print(f'{Fore.RED}{Style.BRIGHT}ACTIVE IPS ALIVE\n' + _sec_string('jA==') * 20)
    for i in range(0, len(ip_list), chunk_size):
        chunk = ip_list[i:i + chunk_size]
        tasks = [scan_ip(str(ip), total_ips, i + j, server_dict, semaphore) for j, ip in enumerate(chunk)]
        await asyncio.gather(*tasks)
    end_time = time.time()
    duration = end_time - start_time
    sys.stdout.write(_sec_string('rA==') + _sec_string('gQ==') * 80 + _sec_string('rA=='))
    total_scanned = len(server_dict)
    speed = total_scanned / duration if duration > 0 else 0
    print(f'\n{Fore.YELLOW}Time taken for scanning: {duration:.2f} seconds')
    print(f'{Fore.YELLOW}Scanning speed: {Fore.CYAN}{speed:.2f} IPs per second{Style.RESET_ALL}')

async def scan_multiple_cidr_blocks(cidr_blocks):
    for cidr_block in cidr_blocks:
        try:
            ipaddress.ip_network(cidr_block, strict=False)
            print(f'\nScanning CIDR block: {cidr_block}')
            await scan_cidr_block(cidr_block)
        except ValueError:
            print(f"{Fore.RED}Invalid CIDR block '{cidr_block}'. Skipping.")

async def ip_scanner():
    clear_screen()
    title = f'{Fore.RED}{Style.BRIGHT}ANY ISP IP SCANNER V5 UPDATED  {Style.RESET_ALL}'
    subtitle = f'{Fore.CYAN}CREATOR TELEGRAM: @Hackerprime254{Style.RESET_ALL}'
    logo = f'{Fore.RED}{Style.BRIGHT}DEVELOPER IS NOT RESPONSIBLE FOR ANY HARM TO YOUR NETWORK\n' + _sec_string('Q0G+ZDdGzRAwNbkXQ0G+ZDdTzRAlNbkCQ0GrZDdXzRAhNbkGQ0GvZDdXzRAhNbkGQ0GvZDdTzRAlNbkCQ0GrZDdTzRAlNbkXQ0G+ZDdGzRAwNbkXQ0G+ZDdGJQ==') + _sec_string('Q0G+ZDdGzRAwNbkXQ0G+ZDdfzRAwNbkXQ0G+ZDdGzRAzNbkUQ0G9ZDdFzRAzNbkUQ0G9ZDdFzRAzNbkUQ0G9ZDdFzRAwNbkXQ0GvZDdXzRAlNbkXQ0G+ZDdGzRAw3Q==') + _sec_string('Q0G+ZDdGzRAwNbkXQ0GnZDdGzRAwNbkXQ0G9ZDdFzRAzNbkUQ0G9ZDdFzRAwNbkXQ0G+ZDdGzRAwNbkXQ0G+ZDdGzRAzNbkUQ0G9ZDdGzRAwNbkOQ0G+ZDdGzRAw3Q==') + _sec_string('Q0G+ZDdGzRAwNbkOQ0G+ZDdGzRAwNbkXQ0G+ZDdGzRAlNbkOQ0GnZDdXzRAlNbkCQ0G+ZDdGzRAwNbkXQ0G+ZDdTzRAlNbkCQ0G+ZDdGzRAwNbkXQ0GnZDdGzRAw3Q==') + _sec_string('Q0G+ZDdTzRAhNbkUQ0GrZDdTzRAlNbkUQ0G+ZDdfzRAhNbkGQ0GvZDdXzRAlNbkCQ0GnZDdGzRAwNbkXQ0GnZDdfzRAlNbkCQ0GnZDdGzRAwNbkXQ0G+ZDdfzRAw3Q==') + _sec_string('Q0GnZDdGzRAzNbkOQ0G9ZDdTzRAwNbkGQ0GrZDdTzRAlNbkGQ0G+ZDdGzRAwNbkXQ0G+ZDdGzRAwNbkXQ0GnZDdGzRAwNbkXQ0G9ZDdFzRAzNbkUQ0G9ZDdGzRAp3Q==') + _sec_string('Q0GnZDdGzRAzNbkOQ0G+ZDdfzRAhNbkCQ0GrZDdGzRAwNbkXQ0G+ZDdGzRApNbkGQ0G+ZDdGzRAwNbkXQ0GvZDdTzRAwNbkXQ0GrZDdXzRAhNbkGQ0GrZDdFzRAp3Q==') + _sec_string('Q0G+ZDdfzRAwNbkGQ0GrZDdGzRApNbkCQ0G+ZDdfzRAhNbkCQ0GrZDdGzRAhNbkXQ0GvZDdXzRAwNbkCQ0GrZDdXzRAwNbkXQ0G+ZDdGzRApNbkXQ0G+ZDdfzRAw3Q==') + _sec_string('Q0G+ZDdGzRApNbkXQ0G+ZDdGzRAhNbkCQ0GvZDdfzRAlNbkCQ0G+ZDdfzRAhNbkGQ0GvZDdTzRAlNbkCQ0GrZDdXzRAhNbkOQ0GvZDdfzRApNbkXQ0GnZDdGzRAw3Q==') + _sec_string('Q0G+ZDdGzRAwNbkOQ0G+ZDdGzRAwNbkXQ0GnZDdfzRAwNbkXQ0GvZDdfzRAlNbkCQ0GrZDdfzRAlNbkCQ0GnZDdTzRApNbkOQ0GnZDdfzRAwNbkOQ0G+ZDdGzRAw3Q==') + _sec_string('Q0G+ZDdGzRAwNbkXQ0GnZDdGzRAwNbkXQ0G+ZDdXzRAhNbkCQ0G+ZDdfzRAwNbkXQ0G+ZDdfzRAwNbkOQ0GvZDdfzRApNbkOQ0GnZDdfzRApNbkXQ0GnZDdGzRAw3Q==') + _sec_string('Q0G+ZDdGzRAwNbkXQ0G+ZDdXzRAlNbkXQ0G+ZDdGzRAwNbkXQ0GvZDdXzRAlNbkCQ0GrZDdfzRAlNbkOQ0GrZDdfzRAlNbkOQ0GrZDdXzRAwNbkXQ0GnZDdGzRAw3Q==') + _sec_string('Q0G+ZDdGzRAwNbkXQ0G+ZDdGzRAwNbkGQ0GrZDdTzRAwNbkUQ0G9ZDdFzRAzNbkXQ0G+ZDdGzRAwNbkXQ0G+ZDdGzRAwNbkXQ0G+ZDdFzRAwNbkXQ0G+ZDdfzRAw3Q==') + _sec_string('Q0G+ZDdGzRAwNbkXQ0G+ZDdGzRAwNbkXQ0G+ZDdGzRAhNbkGQ0GrZDdTzRAwNbkUQ0G9ZDdFzRAzNbkUQ0G9ZDdFzRAzNbkUQ0G9ZDdGzRAwNbkXQ0G+ZDdfzRAw3Q==') + _sec_string('Q0G+ZDdGzRAwNbkXQ0G+ZDdGzRAwNbkXQ0G+ZDdGzRAwNbkXQ0G+ZDdGzRAhNbkCQ0GrZDdTzRAlNbkCQ0G+ZDdGzRAwNbkXQ0G+ZDdGzRAwNbkXQ0GnZDdGzRAw3Q==') + f'{Style.RESET_ALL}'
    print(title)
    print(subtitle)
    print(logo)
    while True:
        cidr_input = input(_sec_string('5Llb49P3ZtaBlGbC8/dN6s60RPWB/0qoxvkDppDuHaiQ4RiokfkfqZDhA7eY5QG3l+8Bto/nALeX/hWm'))
        cidr_blocks = [cidr.strip() for cidr in cidr_input.split(_sec_string('jQ=='))]
        await scan_multiple_cidr_blocks(cidr_blocks)
        continue_scanning = input(_sec_string('5bgP/86iD/HAuVum1bgP9cK2QabMuF3jgZRmwvP3TerOtET1nvcH/8SkAOjO/hWm')).strip().lower()
        if continue_scanning != _sec_string('2LJc'):
            print(_sec_string('5K9G8si5SKbVv0qm0rRO6M+yXag='))
            break

class HostnameTracker:

    def __init__(self):
        self.hostnames = OrderedDict()
        self.count = 0
        self.lock = threading.Lock()

    def add(self, hostname):
        hostname_hash = hashlib.md5(hostname.encode()).hexdigest()
        with self.lock:
            if hostname_hash not in self.hostnames:
                self.hostnames[hostname_hash] = hostname
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
        session.headers.update({_sec_string('9KRK9IyWSOPPow=='): _sec_string('7LhV7827TqmU+R+miYBG6MW4WPWBmXumkOcBtpr3eO/P4Ru9ga8Zsoj3bvbRu0rRxLVk79X4GrWW+Rywgf9kzvWaY6qBu0btxPdo48K8QK+BlEf0zrpKqZjmAbaP4xuxk/ketJX3fOfHtl3vjuIcsY/kGQ=='), _sec_string('4LRM49GjAsrAuUjzwLBK'): _sec_string('xLkC0/L7SuiaphK2j+4=')})
        adapter = requests.adapters.HTTPAdapter(max_retries=10, pool_connections=5, pool_maxsize=5)
        session.mount(_sec_string('yaNb9tLtAKk='), adapter)
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
                if _sec_string('w7tA5cqySw==') in response.text.lower() or _sec_string('wrZf8sK/Tg==') in response.text.lower():
                    with self.lock:
                        if self.error_log:
                            self.error_log.write(f'[{datetime.datetime.now()}] Warning: Blocked/captcha for {ip_str}, retries left: {retries}\n')
                    retries -= 1
                    backoff = min(backoff * 2, 16)
                    time.sleep(2 * backoff)
                    continue
                soup = BeautifulSoup(response.text, _sec_string('yaNC6o+nTvTSsl0='))
                table = soup.find(_sec_string('1bZN6sQ='), {_sec_string('yLM='): _sec_string('1bZN6sQ=')})
                if not table:
                    return []
                hostnames = []
                rows = table.find_all(_sec_string('1aU='))[1:]
                for row in rows:
                    cols = row.find_all(_sec_string('1bM='))
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
                        with open(output_file, _sec_string('wA=='), encoding=_sec_string('1KNJq5k=')) as f:
                            for hostname in hostnames:
                                if self.hostname_tracker.add(hostname):
                                    f.write(f'{hostname}\n')
                    with self.lock:
                        self.scanned_ips += 1
                        self.progress = start_idx + ip_list.index(ip) + 1
                        if ip_str in self.failed_ips and hostnames:
                            del self.failed_ips[ip_str]
                except Exception as e:
                    ip_str = str(ip)
                    with self.lock:
                        if ip_str not in self.failed_ips:
                            self.failed_ips[ip_str] = 0
                        self.failed_ips[ip_str] += 1

    def start_scan(self, ip_or_cidr, output_file):
        self.running = True
        try:
            self.error_log = open(_sec_string('0rRO6P6yXfTOpVyozbhI'), _sec_string('wA=='))
            ip_inputs = [x.strip() for x in ip_or_cidr.split(_sec_string('jQ=='))]
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
    print(f'{Fore.YELLOW}V4 REVERSE IP Scanner{Style.RESET_ALL}')
    print(f'{Fore.CYAN}Telegram: @Hacker254prime{Style.RESET_ALL}')
    while True:
        ip_input = input(f"{Fore.CYAN}Enter IP or CIDR block (e.g., 1.2.3.4 or 1.2.3.0/24, multiple separated by commas, or 'back'): {Style.RESET_ALL}").strip()
        if ip_input.lower() in [_sec_string('w7ZM7Q=='), _sec_string('xK9G8g=='), _sec_string('0KJG8g=='), _sec_string('0A==')]:
            return
        output_file = input(f"{Fore.CYAN}Enter output file name (e.g., results.txt, or 'back'): {Style.RESET_ALL}").strip()
        if output_file.lower() in [_sec_string('w7ZM7Q=='), _sec_string('xK9G8g=='), _sec_string('0KJG8g=='), _sec_string('0A==')]:
            return
        if not output_file:
            output_file = _sec_string('07JZ49OkStnTslzzzaNcqNWvWw==')
        if os.path.exists(output_file):
            os.remove(output_file)
        if os.path.exists(_sec_string('0rRO6P6yXfTOpVyozbhI')):
            os.remove(_sec_string('0rRO6P6yXfTOpVyozbhI'))
        print(f'\n{Fore.GREEN}Starting scan...{Style.RESET_ALL}')
        scanner = ReverseIPScannerV2()
        start_time = time.time()
        scan_thread = threading.Thread(target=scanner.start_scan, args=(ip_input, output_file))
        scan_thread.daemon = True
        scan_thread.start()
        total_ips = 0
        try:
            ip_inputs = [x.strip() for x in ip_input.split(_sec_string('jQ=='))]
            for input_item in ip_inputs:
                try:
                    network = ipaddress.ip_network(input_item, strict=False)
                    total_ips += len(list(network.hosts())) if network.num_addresses > 1 else 1
                except ValueError:
                    total_ips += 1
        except:
            total_ips = 1
        try:
            with tqdm(total=total_ips, desc=f'{Fore.CYAN}Scanning IPs{Style.RESET_ALL}', bar_format=_sec_string('2rtw5MClUqPSrE3n06oK9dqlcOTApVI=') % (Fore.CYAN, Style.RESET_ALL)) as pbar:
                last_progress = 0
                while scanner.running or scanner.scanned_ips < total_ips:
                    with scanner.lock:
                        current_progress = scanner.progress
                        failed_count = len(scanner.failed_ips)
                    if current_progress > last_progress:
                        pbar.update(current_progress - last_progress)
                        last_progress = current_progress
                    pbar.set_postfix({_sec_string('6bhc8s+2QuPS'): scanner.hostname_tracker.count, _sec_string('57ZG6sSz'): failed_count})
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
            choice = input(f'\n{Fore.YELLOW}1. Scan another\n2. Return to main menu\nChoose (1-2): {Style.RESET_ALL}').strip()
            if choice == _sec_string('kA=='):
                break
            elif choice == _sec_string('kw=='):
                return
            else:
                print(f'{Fore.RED}Invalid choice. Please enter 1 or 2.{Style.RESET_ALL}')

def extract_root_domain(user_input):
    try:
        clean = re.sub(_sec_string('//kFvI74U6mP/Qv6m/kFot2XAayF'), '', user_input)
        parts = clean.lower().split(_sec_string('jw=='))
        second_level_domains = {_sec_string('wrg='), _sec_string('wrhC'), _sec_string('zqVI'), _sec_string('z7Jb'), _sec_string('xrhZ'), _sec_string('xLNa'), _sec_string('wLQ='), _sec_string('xrg='), _sec_string('zL5D'), _sec_string('z7I='), _sec_string('zqU='), _sec_string('z75M'), _sec_string('w75V'), _sec_string('yLlJ6Q=='), _sec_string('z7ZC4w=='), _sec_string('0aVA'), _sec_string('0rRH'), _sec_string('1rJN'), _sec_string('1aE='), _sec_string('0bhD78Ky'), _sec_string('0btM'), _sec_string('zaNL'), _sec_string('yLlM'), _sec_string('0rRH6c67'), _sec_string('1LlG8MSlXO/Vrg=='), _sec_string('wLJd6Q=='), _sec_string('0bhc8g=='), _sec_string('1bJD'), _sec_string('yLlb'), _sec_string('wKVf5w=='), _sec_string('wKRG5w=='), _sec_string('wKdf'), _sec_string('w7tA4Q=='), _sec_string('0r9A9g=='), _sec_string('wrta5A=='), _sec_string('xbJZ'), _sec_string('0r5b4w=='), _sec_string('0qNA9MQ='), _sec_string('1bJM7g=='), _sec_string('0aVK9dI='), _sec_string('wLQ='), _sec_string('wLM='), _sec_string('wLI='), _sec_string('wLE='), _sec_string('wLA='), _sec_string('wL4='), _sec_string('wLs='), _sec_string('wLo='), _sec_string('wLg='), _sec_string('wKY='), _sec_string('wKU='), _sec_string('wKQ='), _sec_string('wKM='), _sec_string('wKI='), _sec_string('wKA='), _sec_string('wK8='), _sec_string('wK0='), _sec_string('w7Y='), _sec_string('w7U='), _sec_string('w7M='), _sec_string('w7I='), _sec_string('w7E='), _sec_string('w7A='), _sec_string('w78='), _sec_string('w74='), _sec_string('w70='), _sec_string('w7o='), _sec_string('w7k='), _sec_string('w7g='), _sec_string('w6U='), _sec_string('w6Q='), _sec_string('w6M='), _sec_string('w6A='), _sec_string('w64='), _sec_string('w60='), _sec_string('wrY='), _sec_string('wrQ='), _sec_string('wrM='), _sec_string('wrE='), _sec_string('wrA='), _sec_string('wr8='), _sec_string('wr4='), _sec_string('wrw='), _sec_string('wrs='), _sec_string('wro='), _sec_string('wrk='), _sec_string('wrg='), _sec_string('wqU='), _sec_string('wqI='), _sec_string('wqE='), _sec_string('wqA='), _sec_string('wq8='), _sec_string('wq4='), _sec_string('wq0='), _sec_string('xbI='), _sec_string('xb0='), _sec_string('xbw='), _sec_string('xbo='), _sec_string('xbg='), _sec_string('xa0='), _sec_string('xLQ='), _sec_string('xLI='), _sec_string('xLA='), _sec_string('xKU='), _sec_string('xKQ='), _sec_string('xKM='), _sec_string('xKI='), _sec_string('x74='), _sec_string('x70='), _sec_string('x7w='), _sec_string('x7o='), _sec_string('x7g='), _sec_string('x6U='), _sec_string('xrY='), _sec_string('xrM='), _sec_string('xrI='), _sec_string('xrE='), _sec_string('xrA='), _sec_string('xr8='), _sec_string('xr4='), _sec_string('xrs='), _sec_string('xro='), _sec_string('xrk='), _sec_string('xqc='), _sec_string('xqY='), _sec_string('xqU='), _sec_string('xqQ='), _sec_string('xqM='), _sec_string('xqI='), _sec_string('xqA='), _sec_string('xq4='), _sec_string('ybw='), _sec_string('ybo='), _sec_string('ybk='), _sec_string('yaU='), _sec_string('yaM='), _sec_string('yaI='), _sec_string('yLM='), _sec_string('yLI='), _sec_string('yLs='), _sec_string('yLo='), _sec_string('yLk='), _sec_string('yLg='), _sec_string('yKY='), _sec_string('yKU='), _sec_string('yKQ='), _sec_string('yKM='), _sec_string('y7I='), _sec_string('y7o='), _sec_string('y7g='), _sec_string('y6c='), _sec_string('yrI='), _sec_string('yrA='), _sec_string('yr8='), _sec_string('yr4='), _sec_string('yro='), _sec_string('yrk='), _sec_string('yqc='), _sec_string('yqU='), _sec_string('yqA='), _sec_string('yq4='), _sec_string('yq0='), _sec_string('zbY='), _sec_string('zbU='), _sec_string('zbQ='), _sec_string('zb4='), _sec_string('zbw='), _sec_string('zaU='), _sec_string('zaQ='), _sec_string('zaM='), _sec_string('zaI='), _sec_string('zaE='), _sec_string('za4='), _sec_string('zLY='), _sec_string('zLQ='), _sec_string('zLM='), _sec_string('zLI='), _sec_string('zLA='), _sec_string('zL8='), _sec_string('zLw='), _sec_string('zLs='), _sec_string('zLo='), _sec_string('zLk='), _sec_string('zLg='), _sec_string('zKc='), _sec_string('zKY='), _sec_string('zKU='), _sec_string('zKQ='), _sec_string('zKM='), _sec_string('zKI='), _sec_string('zKE='), _sec_string('zKA='), _sec_string('zK8='), _sec_string('zK4='), _sec_string('zK0='), _sec_string('z7Y='), _sec_string('z7Q='), _sec_string('z7I='), _sec_string('z7E='), _sec_string('z7A='), _sec_string('z74='), _sec_string('z7s='), _sec_string('z7g='), _sec_string('z6c='), _sec_string('z6U='), _sec_string('z6I='), _sec_string('z60='), _sec_string('zro='), _sec_string('0bY='), _sec_string('0bI='), _sec_string('0bE='), _sec_string('0bA='), _sec_string('0b8='), _sec_string('0bw='), _sec_string('0bs='), _sec_string('0bo='), _sec_string('0bk='), _sec_string('0aU='), _sec_string('0aQ='), _sec_string('0aM='), _sec_string('0aA='), _sec_string('0a4='), _sec_string('0LY='), _sec_string('07I='), _sec_string('07g='), _sec_string('06Q='), _sec_string('06I='), _sec_string('06A='), _sec_string('0rY='), _sec_string('0rU='), _sec_string('0rQ='), _sec_string('0rM='), _sec_string('0rI='), _sec_string('0rA='), _sec_string('0r8='), _sec_string('0r4='), _sec_string('0rw='), _sec_string('0rs='), _sec_string('0ro='), _sec_string('0rk='), _sec_string('0rg='), _sec_string('0qU='), _sec_string('0qQ='), _sec_string('0qM='), _sec_string('0qI='), _sec_string('0qE='), _sec_string('0q8='), _sec_string('0q4='), _sec_string('0q0='), _sec_string('1bQ='), _sec_string('1bM='), _sec_string('1bE='), _sec_string('1bA='), _sec_string('1b8='), _sec_string('1b0='), _sec_string('1bw='), _sec_string('1bs='), _sec_string('1bo='), _sec_string('1bk='), _sec_string('1bg='), _sec_string('1aU='), _sec_string('1aM='), _sec_string('1aE='), _sec_string('1aA='), _sec_string('1a0='), _sec_string('1LY='), _sec_string('1LA='), _sec_string('1Lw='), _sec_string('1KQ='), _sec_string('1K4='), _sec_string('1K0='), _sec_string('17Y='), _sec_string('17Q='), _sec_string('17I='), _sec_string('17A='), _sec_string('174='), _sec_string('17k='), _sec_string('16I='), _sec_string('1rE='), _sec_string('1qQ='), _sec_string('2LI='), _sec_string('2KM='), _sec_string('27Y='), _sec_string('27o='), _sec_string('26A='), _sec_string('xrgB7cQ='), _sec_string('wrgB7cQ=')}
        if len(parts) >= 3:
            tld = parts[-1]
            sld = parts[-2]
            if len(tld) == 2 and sld in second_level_domains:
                return _sec_string('jw==').join(parts[-3:])
            if len(tld) == 2:
                return _sec_string('jw==').join(parts[-2:])
        country_tld_patterns = [(_sec_string('/flM6f35B93A+lXb2uVSr4U='), 3), (_sec_string('/flO5f35B93A+lXb2uVSr4U='), 3), (_sec_string('/flI6deLAa76tgL8/Kwd+4jz'), 3), (_sec_string('/flK4tSLAa76tgL8/Kwd+4jz'), 3), (_sec_string('/flA9MaLAa76tgL8/Kwd+4jz'), 3), (_sec_string('/flB49WLAa76tgL8/Kwd+4jz'), 3), (_sec_string('/flM6cyLAa76tgL8/Kwd+4jz'), 3)]
        clean_lower = clean.lower()
        for pattern, keep_parts in country_tld_patterns:
            if re.search(pattern, clean_lower):
                return _sec_string('jw==').join(parts[-keep_parts:])
        if len(parts) > 2:
            return _sec_string('jw==').join(parts[-2:])
        return clean
    except:
        return None

def query_crtsh(domain):
    url = f'https://crt.sh/?q=%.{domain}&output=json'
    subdomains = set()
    try:
        response = requests.get(url, timeout=25)
        if response.status_code == 200:
            for entry in response.json():
                names = entry.get(_sec_string('z7ZC4/6hTurUsg=='), '')
                for name in re.split(_sec_string('/blTqt2LWw=='), names):
                    name = re.sub(_sec_string('/4sF2o/o'), '', name.strip().lower())
                    if re.fullmatch(_sec_string('//9054ytH6uY+nKt/fkGrPq2Avz8rB2q3PM='), name):
                        if name.endswith(domain) or name == domain:
                            subdomains.add(name)
    except:
        pass
    return subdomains

async def tls_scanner():
    clear_screen()
    print(colored(_sec_string('qzW7CkNDr2Q1V80SITW7BkNDr2Q1V80SITW7BkNDr2Q1V80SITW7BkNDr2Q1V80SITW7BkNDr2Q1V80SITW7BkNDr2Q1V80SITW7BkNDr2Q1V80SITW7BkNDr2Q1V80SITW7BkNDr2Q1V80SITW7BkNDr2Q1V80SITW7BkNDr2Q1V80SITW7BkNDr2Q1V80SITW7BkNDr2Q1V80SITW7BkNDr2Q1V80SMfcPpoH3D6aB9w+mgd3NEiP3D6aB9w9kNVvNEiE1uwZDQ69kNVfNEiE1uwZDQ69kNVfNEiE1uwZDQ69kNVfNEiE1uwZDQ69kNVfNEiE1uwZDQ69kNVfNEiE1uwZDQ69kNVfNEiE1uwZDQ69kNVfNEiE1uwZDQ69kNVfNEiE1uwZDQ69kNVfNEiE1uwZDQ69kNVfNEiE1uwZDQ7+mgfcPZDVVD6aB9w+mgfcPpoH3JWQ1VQ+mQ0OjZDVXzRIhNbsGQ0OTZDVXzRIhNbsGQ0OvZDVXD6aB9w+mgfcPpoH3D6aB9w+mgfcPpoH3D6aB9w+mgfcPpoH3D2Q1a80SITW7BkNDr2Q1V80SHfcPpoH3D6aB9w+mgd3NEh01uwZDQ69kNWvNEiE1uwZDQ69kNWvNEiGEesTlmGLH6JkPwYz3Ysfyg2rUgZBqyOSFbtLuhQ+mgfcPpoH3D6aB980SI/cPpoE1uwSB9w+mgfcPpoH3D6arNbsEgffNEiP3D6ZDQ62mgfcPpoH3D6aB9w+mgfcPpoH3D6aB9w+mgfcPpoH3D6aB9w+mgfcPpoE1uwSB9w+mQ0OTZDVXzRIhNbsGQ0OvZDVXzRIx9w+mgfcPjENDraaBNbsEgfcPZDVVD2Q1VWHJ9ZIPz/X3fNPxh2DU9YQPwOibaqj1j3umh/dnyfKDYcfskg/P74d60oH3D2Q1VQ+mgfcPZDVVD6aB9w+mqzW7OkNDr2Q1V80SHTW7BkNDr2Q1V80SHTW7BkNDt6aB9w+mgTW7CkNDr6aB980SI/cPpoH3D6aB9w+mgfcPpoH3D6aB9w+mgfcPpoE1uwSB9w+mQ0OtpoH3D6ZDQ62mgfcPpoHdzRIj9w9kNUvNEiE1uwZDQ69kNWvNEiE1uwZDQ69kNVfNEiE1uwZDQ69kNVfNEh01uwZDQ69kNVfNEBs1uwTgmXam6IR/puyWfNLkhXym9ZhgyoGBGqaB9w9kNWvNEiE1uwZDQ69kNVfNEh33D6aB980SI/cPpoH3D4xDQ62mgTW7BIH3D2Q1VQ+mgfcPpoH3zRIj9w+mgTW7BIH3D6aB9w+mgfcPpoH3D6aB9w+mgfcPpoH3D6ZDQ62mgfcPZDVVD6aB9w9kNVUPpoH3D6arNbsEgfcPpoH3zRIj9w+mgfcPpoE1uwSB9w+mQ0OtpoH3D6aB9w+mgfcPpoH3D6aB9w+mgfcPpoH3D2Q1VQ+mgffNEiP3D6aB980SI/cPpoH3D4xDQ62mgfcPpoE1uwSB9w+mgfcPpkNDraaB980SLTW7BkNDr2Q1V80SITW7BkNDr2Q1V80SITW7BkNDr2Q1V80SITW7BkNDr2Q1V80SITW7BkNDr2Q1V80SITW7BkNDr2Q1V80SITW7BkNDr2Q1V80SITW7BkNDr2Q1V80SITW7BkNDr2Q1V80SITW7BkNDr2Q1V80SITW5OkNDr2Q1V80SITW7BkNDr2Q1RyVkNVUPpoH3D6ZDQ62mgfcPpoH3D2Q1VQ+mgTW7BIGYeMjkhQ/G6ZZszeSHfc/skg/u1aNf9Zv4APKPukqp6bZM7cSlHbOVp13vzLLNEiPdzRI1NbsGQ0OvZDVXzRIhNbsGQ0OvZDVVzRIhNbsGQ0OvZDVXzRIhNbsGQ0OvZDVXzRIVNbsGQ0OvZDVXzRIjNbsGQ0OvZDVXzRIhNbsGQ0OvZDVXzRIhNbsGQ0OvZDVXzRIhNbsGQ0OvZDVXzRIhNbsGQ0OvZDVXzRIhNbsGQ0OvZDVXzRIhNbsGQ0OvZDVXzRIhNbsGQ0OtZDVXzRIhNbsGQ0OvZDVPD6aB9w+mgfcPpoE1uwSr9w+mgfcPpkNDraaB9w+mgfcPpoH3D2Q1Q80SITW7BkNDr2Q1V80SITW7BkNDr2Q1V80SITW7BkNDr2Q1V80SITW7BkNDr2Q1V80SITW7BkNDr2Q1V80SITW7BkNDr2Q1V80SITW7BkNDr2Q1V80SITW7BkNDr2Q1V80SITW7BkNDr2Q1V80SITW7BkNDr2Q1V80SITW7BkNDr2Q1V80SITW7BkNDt4yB9w+mgfcPZDVDzRIhNbsGQ0OvZDVXzRIhNbsGQ0OvZDVXzRIhNbsGQ0OvZDVXzRIhNbsGQ0OvZDVXzRIhNbsGQ0OvZDVXzRIhNbsGQ0OvZDVXzRIhNbsGQ0OvZDVXzRIhNbsGQ0OvZDVXzRIhNbsGQ0OvZDVXzRIhNbsGQ0OvZDVXzRIhNbsGQ0O3poH3D6aB9w+mgfcPpoH3D6ar'), _sec_string('wq5O6A=='), attrs=[_sec_string('w7hD4g==')]))
    while True:
        target = input(colored(_sec_string('q4wQ24GSQfLEpQ/izrpO78/4Se/Nsg+u0Pdb6YGmWu/V/hWm'), _sec_string('2LJD6s6g'))).strip()
        if target.lower() in (_sec_string('0A=='), _sec_string('0KJG8g==')):
            break
        if os.path.isfile(target):
            domains = []
            try:
                with open(target, _sec_string('0w==')) as f:
                    for line in f:
                        domain = extract_root_domain(line.strip())
                        if domain and re.match(_sec_string('//9054ytH6uY+nKt/fkGrfq2Avz8rB2q3PM='), domain):
                            domains.append(domain)
            except Exception as e:
                print(colored(f'[!] File error: {str(e)}', _sec_string('07JL')))
                continue
            if not domains:
                print(colored(_sec_string('+vpypu+4D/DAu0bigbNA68C+QfWBvkGmx75D4w=='), _sec_string('07JL')))
                continue
            total = len(domains)
            print(colored(f'\n[+] Scanning {total} domains...', _sec_string('w7ta4w==')))
            all_subs = set()
            for idx, domain in enumerate(domains, 1):
                sys.stdout.write(f'\rProcessing {idx}/{total} ({idx / total * 100:.1f}%)')
                sys.stdout.flush()
                all_subs.update(query_crtsh(domain))
            sys.stdout.write(_sec_string('qw=='))
            if not all_subs:
                print(colored(_sec_string('+vpypu+4D/XUtUvpzLZG6NL3SenUuUs='), _sec_string('07JL')))
                continue
            filename = input(colored(_sec_string('+uhypvK2WeOBo0Cmx75D44H/SqjG+QOm0qJN9Y+jV/KI7Q8='), _sec_string('2LJD6s6g'))).strip()
            if not filename:
                filename = _sec_string('0qJN4s66Tu/PpAHy2aM=')
            try:
                with open(filename, _sec_string('1g==')) as f:
                    f.write(_sec_string('qw==').join(sorted(all_subs)))
                print(colored(f'\n[+] Results saved to {filename}', _sec_string('xqVK488=')))
            except Exception as e:
                print(colored(f'[!] Save error: {str(e)}', _sec_string('07JL')))
        else:
            domain = extract_root_domain(target)
            if not domain or not re.match(_sec_string('//9054ytH6uY+nKt/fkGrfq2Avz8rB2q3PM='), domain):
                print(colored(_sec_string('+vZypui5WefNvkumxbhC58i5D+DOpULn1Q=='), _sec_string('07JL')))
                continue
            print(colored(f'\n[+] Scanning {domain}...', _sec_string('w7ta4w==')))
            results = query_crtsh(domain)
            if not results:
                print(colored(_sec_string('+vpypu+4D/XUtUvpzLZG6NL3SenUuUs='), _sec_string('07JL')))
                continue
            filename = input(colored(_sec_string('+uhypvK2WeOBo0Cmx75D44H/SqjG+QOmzqJb9tSjAfLZowa8gQ=='), _sec_string('2LJD6s6g'))).strip()
            if not filename:
                filename = f"{domain.replace(_sec_string('jw=='), _sec_string('/g=='))}_subs.txt"
            try:
                with open(filename, _sec_string('1g==')) as f:
                    f.write(_sec_string('qw==').join(sorted(results)))
                print(colored(f'\n[+] Results saved to {filename}', _sec_string('xqVK488=')))
            except Exception as e:
                print(colored(f'[!] Save error: {str(e)}', _sec_string('07JL')))
CYAN = _sec_string('uowWsMw=')
MAGENTA = _sec_string('uowWs8w=')
BOLD = _sec_string('uowe6w==')
DIM = _sec_string('uowd6w==')
RESET = _sec_string('uowf6w==')
TITLE = f'{CYAN}\n _   _  ___  ____ _____ _   _    _    __  __ _____\n| | | |/ _ \\/ ___|_   _| \\ | |  / \\  |  \\/  | ____|\n| |_| | | | \\___ \\ | | |  \\| | / _ \\ | |\\/| |  _|\n|  _  | |_| |___) || | | |\\  |/ ___ \\| |  | | |___\n|_| |_|\\___/|____/ |_| |_| \\_/_/   \\_\\_|  |_|_____\n / _| / _ \\  / \\  | \\ | | \\ | | ____|  _ \\   _| || |_\n \\___ \\| | | |/ _ \\ |  \\| |  \\| |  _| | |_) | |_  ..  _|\n ___) | |_| / ___ \\| |\\  | |\\  | |___|  _ <  |_      _|\n|____/ \\___/_/   \\_\\_| \\_|_| \\_|_____|_| \\_\\   |_||_|\n{RESET}'
SERVER_DB = [(_sec_string('wrtA88WxQ+fTsg=='), _sec_string('4rtA88WxQ+fTsg==')), (_sec_string('z7BG6Nk='), _sec_string('75BmyPk=')), (_sec_string('wKdO5cmy'), _sec_string('4KdO5cmy')), (_sec_string('wrtA88WxXenPow=='), _sec_string('4rtA88WRXenPow==')), (_sec_string('wLxO68C+'), _sec_string('4LxO68C+')), (_sec_string('zL5M9M6kQODV+kbv0g=='), _sec_string('6J58')), (_sec_string('1bJB4ci5Sg=='), _sec_string('9bJB4ci5Sg==')), (_sec_string('x7Zc8s2u'), _sec_string('57Zc8s2u')), (_sec_string('w6JB6Ng='), _sec_string('46JB6NiUa8g=')), (_sec_string('wLpc480='), _sec_string('4Lpc482gSuQ=')), (_sec_string('zqdK6NOyXPLY'), _sec_string('7qdK6POyXPLY')), (_sec_string('zb5b49KnSuPF'), _sec_string('7b5b4/KnSuPF')), (_sec_string('wrZL4tg='), _sec_string('4rZL4tg=')), (_sec_string('17Jd5cS7'), _sec_string('97Jd5cS7')), (_sec_string('ybJd6cqi'), _sec_string('6bJd6cqi')), (_sec_string('xqJB78K4Xeg='), _sec_string('5qJB78K4Xeg=')), (_sec_string('1KBc4cg='), _sec_string('1IB8weg=')), (_sec_string('1bhC5cCj'), _sec_string('9bhC5cCj')), (_sec_string('y7Jb8tg='), _sec_string('67Jb8tg=')), (_sec_string('z7hL4w=='), _sec_string('77hL44+9XA==')), (_sec_string('xK9f9MSkXA=='), _sec_string('5K9f9MSkXA==')), (_sec_string('ybZf9M6vVg=='), _sec_string('6ZZ/9M6vVg==')), (_sec_string('17Zd6MikRw=='), _sec_string('97Zd6MikRw==')), (_sec_string('0qZa78U='), _sec_string('8qZa78U=')), (_sec_string('wrZL4tg='), _sec_string('4rZL4tg=')), (_sec_string('z7Jb6sixVg=='), _sec_string('77Jb6sixVg==')), (_sec_string('0qJM89O+'), _sec_string('8qJM89O+')), (_sec_string('yLlM59GkWurA'), _sec_string('6LlM59GkWurA')), (_sec_string('x+IC5MiwRvY='), _sec_string('5+IPxOiQAs/x')), (_sec_string('27hf4w=='), _sec_string('+7hf4w==')), (_sec_string('1rJN9Mi0RA=='), _sec_string('9pJt9Mi0RA==')), (_sec_string('0aJC5w=='), _sec_string('8aJC5w==')), (_sec_string('1LlG5c6lQQ=='), _sec_string('9LlG5c6lQQ==')), (_sec_string('yrJc8tOyQw=='), _sec_string('6rJc8tOyQw==')), (_sec_string('zb5I7tWjX+I='), _sec_string('7b5I7tWjX+I='))]

def detect_server(headers):
    if _sec_string('wrEC9MCu') in headers:
        return _sec_string('4rtA88WxQ+fTsg==')
    if _sec_string('2fpZ49O0SuqMvks=') in headers:
        return _sec_string('97Jd5cS7')
    server_header = headers.get(_sec_string('0rJd8MSl'), '').lower()
    for pattern, name in SERVER_DB:
        if pattern in server_header:
            return name
    via_header = headers.get(_sec_string('175O'), '').lower()
    for pattern, name in SERVER_DB:
        if pattern in via_header:
            return f'{name} (Via)'
    return _sec_string('9LlE6M6gQQ==')

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
                k, v = h.decode(_sec_string('zbZb78/6Hg==')).split(_sec_string('mw=='), 1)
                header_dict[k.strip().lower()] = v.strip()
        status = c.getinfo(c.RESPONSE_CODE)
        if status == 302:
            return None
        return (hostname, status, detect_server(header_dict))
    except pycurl.error as e:
        return None if e.args and e.args[0] in [6, 7, 28, 35, 56] else (hostname, _sec_string('5KVd6dM='), _sec_string('9LlE6M6gQQ=='))
    finally:
        c.close()

async def file_scanner():
    while True:
        clear_screen()
        print(TITLE)
        try:
            filename = input(_sec_string('5Llb49P3X+fVvw/yzvdJ782yD/HIo0emybhc8s+2QuPS9wfp0/cI5MC0RKGI7Q8=')).strip()
            if filename.lower() in [_sec_string('w7ZM7Q=='), _sec_string('xK9G8g=='), _sec_string('0KJG8g=='), _sec_string('0A==')]:
                return
            if not os.path.exists(filename):
                print(f"{Fore.RED}Error: File '{filename}' not found.{Style.RESET_ALL}")
                choice = input(f'{Fore.YELLOW}1. Try again\n2. Return to main menu\nChoose (1-2): {Style.RESET_ALL}').strip()
                if choice == _sec_string('kw=='):
                    return
                continue
            with open(filename, _sec_string('0w==')) as f:
                hostnames = list({line.strip() for line in f if line.strip()})
                total = len(hostnames)
                if not total:
                    print(f'{Fore.YELLOW}No valid hostnames found in file.{Style.RESET_ALL}')
                    choice = input(f'{Fore.YELLOW}1. Try another file\n2. Return to main menu\nChoose (1-2): {Style.RESET_ALL}').strip()
                    if choice == _sec_string('kw=='):
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
                        sys.stdout.write(_sec_string('rMx0zQ=='))
                        if result:
                            host, status, server = result
                            result_line = f'{CYAN}{host}{RESET}: {MAGENTA}{status}{RESET} [{MAGENTA}{server}{RESET}]'
                            sys.stdout.write(f'{result_line}\n')
                            append_to_v4(result_line)
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
                            result = future.result()
                            update_progress(result=result)
                        except Exception as e:
                            update_progress(error_msg=str(e))
                sys.stdout.write(_sec_string('rMx0zQ=='))
                elapsed = time.time() - start_time
                print(f'\n{DIM}Completed in {elapsed:.1f}s | Found: {found} active hosts{RESET}')
        except KeyboardInterrupt:
            print(f'\n{Fore.YELLOW}Scan interrupted by user.{Style.RESET_ALL}')
        except Exception as e:
            print(f'{Fore.RED}Unexpected error: {str(e)}{Style.RESET_ALL}')
        while True:
            print(f'\n{Fore.CYAN}Options:{Style.RESET_ALL}')
            print(f'{Fore.GREEN}1. Scan another file{Style.RESET_ALL}')
            print(f'{Fore.YELLOW}2. Return to main menu{Style.RESET_ALL}')
            choice = input(f'{Fore.CYAN}Enter your choice (1-2): {Style.RESET_ALL}').strip()
            if choice == _sec_string('kA=='):
                break
            elif choice == _sec_string('kw=='):
                return
            else:
                print(f'{Fore.RED}Invalid choice. Please enter 1 or 2.{Style.RESET_ALL}')
title_proxy = f'{Fore.RED}{Style.BRIGHT}PROXY  SCANNER ANY ISP - V5 MASTERS {Style.RESET_ALL}'
subtitle_proxy = f'{Fore.CYAN}CREATOR TELEGRAM: @Hackerprime254{Style.RESET_ALL}'
title_v2 = f'{Fore.RED}\x1b[1VERSION 4 🆂🅲🅰🅽🅽🅴🆁\x1b[0m{Style.RESET_ALL}'
subtitle_v2 = f'{Fore.BLUE}₮ɆⱠɆ₲Ɽ₳₥ ₲ⱤØɄ₱: https://t.me/anyispscannertool{Style.RESET_ALL}'
owner_proxy = f'{Fore.CYAN}O҉W҉N҉E҉R҉: https://t.me/Hackerprime254{Style.RESET_ALL}'
logo_proxy = f'\n    {Fore.RED}\x1b[1m\n    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡠⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠟⠃⠀⠀⠙⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀\n    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠋⠀⠀⠀⠀⠀⠀⠘⣆⠀⠀⠀⠀⠀⠀⠀⠀\n    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠾⢛⠒⠀⠀⠀⠀⠀⠀⠀⢸⡆⠀⠀⠀⠀⠀⠀⠀\n    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣶⣄⡈⠓⢄⠠⡀⠀⠀⠀⣄⣷⠀⠀⠀⠀⠀⠀⠀\n    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣷⠀⠈⠱⡄⠑⣌⠆⠀⠀⡜⢻⠀⠀⠀⠀⠀⠀⠀\n    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡿⠳⡆⠐⢿⣆⠈⢿⠀⠀⡇⠘⡆⠀⠀⠀⠀⠀⠀\n    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣷⡇⠀⠀⠈⢆⠈⠆⢸⠀⠀⢣⠀⠀⠀⠀⠀⠀\n    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣧⠀⠀⠈⢂⠀⡇⠀⠀⢨⠓⣄⠀⠀⠀⠀\n    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣦⣤⠖⡏⡸⠀⣀⡴⠋⠀⠈⠢⡀⠀⠀\n    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠁⣹⣿⣿⣿⣷⣾⠽⠖⠊⢹⣀⠄⠀⠀⠀⠈⢣⡀\n    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡟⣇⣰⢫⢻⢉⠉⠀⣿⡆⠀⠀⡸⡏⠀⠀⠀⠀⠀⠀⢇\n    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⡇⡇⠈⢸⢸⢸⠀⠀⡇⡇⠀⠀⠁⠻⡄⡠⠂⠀⠀⠀⠘\n    ⢤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠛⠓⡇⠀⠸⡆⢸⠀⢠⣿⠀⠀⠀⠀⣰⣿⣵⡆⠀⠀⠀⠀\n    ⠈⢻⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡿⣦⣀⡇⠀⢧⡇⠀⠀⢺⡟⠀⠀⠀⢰⠉⣰⠟⠊⣠⠂⠀⡸\n    ⠀⠀⢻⣿⣿⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⢧⡙⠺⠿⡇⠀⠘⠇⠀⠀⢸⣧⠀⠀⢠⠃⣾⣌⠉⠩⠭⠍⣉⡇\n    ⠀⠀⠀⠻⣿⣿⣿⣿⣿⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣞⣋⠀⠈⠀⡳⣧⠀⠀⠀⠀⠀⢸⡏⠀⠀⡞⢰⠉⠉⠉⠉⠉⠓⢻⠃\n    ⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⢀⣀⠠⠤⣤⣤⠤⠞⠓⢠⠈⡆⠀⢣⣸⣾⠆⠀⠀⠀⠀⠀⢀⣀⡼⠁⡿⠈⣉⣉⣒⡒⠢⡼⠀\n    ⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣎⣽⣶⣤⡶⢋⣤⠃⣠⡦⢀⡼⢦⣾⡤⠚⣟⣁⣀⣀⣀⣀⠀⣀⣈⣀⣠⣾⣅⠀⠑⠂⠤⠌⣩⡇⠀\n    ⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡁⣺⢁⣞⣉⡴⠟⡀⠀⠀⠀⠁⠸⡅⠀⠈⢷⠈⠏⠙⠀⢹⡛⠀⢉⠀⠀⠀⣀⣀⣼⡇⠀\n    ⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⡟⢡⠖⣡⡴⠂⣀⣀⣀⣰⣁⣀⣀⣸⠀⠀⠀⠀⠈⠁⠀⠀⠈⠀⣠⠜⠋⣠⠁⠀\n    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⡟⢿⣿⣿⣷⡟⢋⣥⣖⣉⠀⠈⢁⡀⠤⠚⠿⣷⡦⢀⣠⣀⠢⣄⣀⡠⠔⠋⠁⠀⣼⠃⠀⠀\n    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⡄⠈⠻⣿⣿⢿⣛⣩⠤⠒⠉⠁⠀⠀⠀⠀⠀⠉⠒⢤⡀⠉⠁⠀⠀⠀⠀⠀⢀⡿⠀⠀⠀\n    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣤⣤⠴⠟⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠤⠀⠀⠀⠀⠀⢩⠇⠀⠀⠀\n    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n    ' + _sec_string('uowf6w==')

def display_banner():
    print(logo_proxy)
    print(title_proxy.center(80))
    print(subtitle_proxy.center(80))
    print(title_v2.center(80))
    print(subtitle_v2.center(80))
    print(owner_proxy.center(80))
    print(_sec_string('qw==') + _sec_string('nA==') * 80 + _sec_string('qw=='))

class BugScanner(multithreading.MultiThreadRequest):
    threads: int

    def request_connection_error(self, *args, **kwargs):
        return 1

    def request_read_timeout(self, *args, **kwargs):
        return 1

    def request_timeout(self, *args, **kwargs):
        return 1

    def convert_host_port(self, host, port):
        return host + (f':{port}' if port not in [_sec_string('mec='), _sec_string('leMc')] else '')

    def get_url(self, host, port, uri=None):
        port = str(port)
        protocol = _sec_string('yaNb9tI=') if port == _sec_string('leMc') else _sec_string('yaNb9g==')
        return f'{protocol}://{self.convert_host_port(host, port)}' + (f'/{uri}' if uri is not None else '')

    def init(self):
        self._threads = getattr(self, _sec_string('/qNH9MS2S/U='), 30)
        self._threads = self.threads or self._threads

    def complete(self):
        pass

class DirectScanner(BugScanner):
    method_list = []
    host_list = []
    port_list = []
    isp_redirects = [_sec_string('yaNb9pv4APXAsU70yLRA64+tSvTOswHqyKFKqZ60ErGW'), _sec_string('yaNb9pv4AL+Q+R20kfkdtpn5HLY='), _sec_string('yaNb9tLtAKnLvkCowrhCqeO2Q+fPtErD2b9O89Kj'), _sec_string('yaNb9tLtAKnRuF3ywLsB6MK5S6jXuEvnwrhCqMK4AfLb')]

    def log_info(self, **kwargs):
        for x in [_sec_string('0qNO8tSkcOXOs0o='), _sec_string('0rJd8MSl')]:
            kwargs[x] = kwargs.get(x, '')
        location = kwargs.get(_sec_string('zbhM59W+QOg='))
        if location:
            if location.startswith(f"https://{kwargs[_sec_string('ybhc8g==')]}"):
                kwargs[_sec_string('0qNO8tSkcOXOs0o=')] = f"{kwargs[_sec_string('0qNO8tSkcOXOs0o=')]:<4}"
            else:
                kwargs[_sec_string('ybhc8g==')] += f' -> {location}'
        messages = []
        base_message = [_sec_string('uowcsMysQuPVv0Dim+sZ+7qMH+s='), _sec_string('uowcs8ysXPLAo1r1/rRA4sTtE7LczHS2zA=='), _sec_string('2qRK9NeyXbyd5hj7'), _sec_string('uowWssysX+nToxW6lao03ZG6'), _sec_string('uowWtMysR+nSoxW6k+VSnfrnQg==')]
        if _sec_string('yKdc') in kwargs and kwargs[_sec_string('yKdc')]:
            base_message.append(_sec_string('uowWtcysRvbS7RO3lKo03ZG6'))
        messages.append(_sec_string('gfc=').join(base_message))
        super().log(_sec_string('gfc=').join(messages).format(**kwargs))

    def get_task_list(self):
        for method in self.filter_list(self.method_list):
            for host in self.filter_list(self.host_list):
                for port in self.filter_list(self.port_list):
                    yield {_sec_string('zLJb7s6z'): method.upper(), _sec_string('ybhc8g=='): host, _sec_string('0bhd8g=='): port}

    def resolve_host_to_ips(self, host):
        try:
            ips = socket.gethostbyname_ex(host)[2]
            return _sec_string('jQ==').join(ips)
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
        self.log_info(method=_sec_string('7LJb7s6z'), status_code=_sec_string('4rhL4w=='), server=_sec_string('8rJd8MSl'), port=_sec_string('8bhd8g=='), host=_sec_string('6bhc8g=='), ips='')
        self.log_info(method=_sec_string('jPoCq4z6'), status_code=_sec_string('jPoCqw=='), server=_sec_string('jPoCq4z6'), port=_sec_string('jPoCqw=='), host=_sec_string('jPoCqw=='), ips='')

    def task(self, payload):
        method = payload[_sec_string('zLJb7s6z')]
        host = payload[_sec_string('ybhc8g==')]
        port = payload[_sec_string('0bhd8g==')]
        try:
            response = self.request(method, self.get_url(host, port), retry=1, timeout=3, allow_redirects=False)
        except Exception as e:
            return
        if response is not None:
            status_code = response.status_code
            server = response.headers.get(_sec_string('0rJd8MSl'), '')
            location = response.headers.get(_sec_string('zbhM59W+QOg='), '')
            if status_code == 302 and location in self.isp_redirects:
                return
            if status_code and status_code != 302:
                ips = self.resolve_host_to_ips(host) if not self.is_ip_address(host) else ''
                data = {_sec_string('zLJb7s6z'): method, _sec_string('ybhc8g=='): host, _sec_string('0bhd8g=='): port, _sec_string('0qNO8tSkcOXOs0o='): status_code, _sec_string('0rJd8MSl'): server, _sec_string('zbhM59W+QOg='): location, _sec_string('yKdc'): ips}
                self.task_success(data)
                self.log_info(**data)

class ProxyScanner(DirectScanner):
    proxy = []

    def log_replace(self, *args):
        super().log_replace(_sec_string('mw==').join(self.proxy), *args)

    def request(self, *args, **kwargs):
        proxy = self.get_url(self.proxy[0], self.proxy[1])
        return super().request(*args, proxies={_sec_string('yaNb9g=='): proxy, _sec_string('yaNb9tI='): proxy}, **kwargs)

def generate_ips_from_cidr(cidr):
    ip_list = []
    try:
        network = ipaddress.ip_network(cidr, strict=False)
        for ip in network.hosts():
            ip_list.append(str(ip))
    except ValueError as e:
        print(_sec_string('5KVd6dPt'), e)
    return ip_list

def process_file(filename):
    host_list = []
    with open(filename) as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            try:
                if _sec_string('jg==') in line:
                    host_list.extend(generate_ips_from_cidr(line))
                else:
                    host_list.append(line)
            except ValueError as e:
                pass
    return host_list

def proxy_scanner_main():
    while True:
        clear_screen()
        display_banner()
        while True:
            proxy_input = input(_sec_string('5Llb49P3X/TOr1a80bhd8oH/QPSB8E3nwrwIptW4D/TEo1r0z/4Vpg==')).strip()
            if proxy_input.lower() in [_sec_string('w7ZM7Q=='), _sec_string('xK9G8g=='), _sec_string('0KJG8g=='), _sec_string('0A==')]:
                return
            if _sec_string('mw==') not in proxy_input:
                print(f'{Fore.RED}Invalid proxy format. Use proxy:port{Style.RESET_ALL}')
                choice = input(f'{Fore.YELLOW}1. Try again\n2. Return to main menu\nChoose (1-2): {Style.RESET_ALL}').strip()
                if choice == _sec_string('kw=='):
                    return
                continue
            proxy_host, proxy_port = proxy_input.split(_sec_string('mw=='))
            filename = input(_sec_string('5Llb49P3W+7E90nvzbIP6MC6SqaJsgHhj/sP4Mi7SqjVr1uvm/c=')).strip()
            if filename.lower() in [_sec_string('w7ZM7Q=='), _sec_string('xK9G8g=='), _sec_string('0KJG8g=='), _sec_string('0A==')]:
                break
            try:
                host_list = process_file(filename)
            except FileNotFoundError:
                print(f"{Fore.RED}Error: File '{filename}' not found.{Style.RESET_ALL}")
                choice = input(f'{Fore.YELLOW}1. Try again\n2. Return to main menu\nChoose (1-2): {Style.RESET_ALL}').strip()
                if choice == _sec_string('kw=='):
                    return
                continue
            scanner = ProxyScanner()
            scanner.proxy = [proxy_host, proxy_port]
            scanner.method_list = [_sec_string('5pJ7')]
            scanner.host_list = host_list
            scanner.port_list = [_sec_string('mec='), _sec_string('leMc')]
            scanner.threads = 30
            scanner.start()
            while True:
                choice = input(f'{Fore.MAGENTA}Do you want to scan again? (yes/no): {Style.RESET_ALL}').strip().lower()
                if choice in [_sec_string('2LJc'), _sec_string('z7g=')]:
                    break
                print(_sec_string('6LlZ582+S6bCv0DvwrIBpvG7SufSsg/jz6NK9IHwVuPS8A/p0/cI6M7wAQ=='))
            if choice == _sec_string('z7g='):
                print(_sec_string('5K9G8si5SKbVv0qm0aVA4dO2QqiBkEDpxbVW44A='))
                break
AQUA = _sec_string('uowWsMw=')
YELLOW = _sec_string('uowWtcw=')
ORANGE = _sec_string('uowcvpriFLSQ40I=')
GREEN = _sec_string('uowWtMw=')
BRIGHT_GREEN = _sec_string('uowevZLlQg==')
RESET = _sec_string('uowf6w==')

def extract_domains(text):
    domain_regex = _sec_string('/bUHuZuMTqvblgLckfoWq/z8c6iI/HTnjK1uq/uKVLSNqnPk')
    return set(re.findall(domain_regex, text))

def save_to_file(domains, filename):
    with open(filename, _sec_string('1g==')) as file:
        for domain in domains:
            file.write(domain + _sec_string('qw=='))
    print(f'{GREEN}Output saved in {filename}{RESET}')
    print(f'{GREEN}Total extracted domains: {len(domains)}{RESET}')

def center_text(text, width=40):
    return text.center(width)

def domain_extractor():
    while True:
        clear_screen()
        print(_sec_string('Q0OuZDVWzRIgNbsHQ0OuZDVWzRIgNbsHQ0OuZDVWzRIgNbsHQ0OuZDVWzRIgNbsHQ0OuZDVWzRIgNbsHQ0OuZDVWzRIgNbsHQ0OuZDVWzRIgNbsHQ0OuZDVWzRIgNbsHQ0OuZDVWzRIgNbsHQ0OuZDVWzRIg'))
        print(f'\x1b[31m\x1b[1mDOMAIN COLLECTOR  FROM TEXT CONTEXT\x1b[0m')
        print(_sec_string('Q0OuZDVWzRIgNbsHQ0OuZDVWzRIgNbsHQ0OuZDVWzRIgNbsHQ0OuZDVWzRIgNbsHQ0OuZDVWzRIgNbsHQ0OuZDVWzRIgNbsHQ0OuZDVWzRIgNbsHQ0OuZDVWzRIgNbsHQ0OuZDVWzRIgNbsHQ0OuZDVWzRIg'))
        print(_sec_string('Q0G+ZDdGzRAwNbkXQ0G+ZDdTzRAlNbkCQ0GrZDdTzRAwNbkCQ0G+ZDdTzRAwNbkCQ0G+ZDdT'))
        print(_sec_string('Q0GrZDdTzRAlNbkCQ0GnZDdfzRAlNbkOQ0GnZDdfzRApNbkGQ0GnZDdXzRApNbkGQ0GnZDdXzRApNbkOQ0Gr'))
        print(_sec_string('Q0GvZDdTzRAhNbkCQ0GvZDdTzRApNbkOQ0GnZDdfzRAlNbkOQ0GrZDdfzRAlNbkOQ0GrZDdfzRApNbkOQ0GnZDdf'))
        print(_sec_string('uowct8w1uRRDQa9kN1fNECE1uQZDQa9kN1fNECE1uQZDQadkN1/NECE1uQZDQa9kN1fNECk1uQ5DQa9kN0XNECU1uQ5DQaed+udC'))
        print(_sec_string('Q0G9ZDdFzRAzNbkUQ0G9ZDdFzRAzNbkUQ0GvZDdXzRAzNbkUQ0G9ZDdFzRAhNbkGQ0GrZDdTzRApNbkOQ0GvZDdF'))
        print(f'{BRIGHT_GREEN}Select an option:{RESET}')
        print(f'{AQUA}1) Extract from file (csv/json/txt){RESET}')
        print(f'{AQUA}2) Extract from text content{RESET}')
        print()
        print(f'{BRIGHT_GREEN}c: Clear  e: Exit{Style.RESET_ALL}')
        print(_sec_string('Q0OuZDVWzRIgNbsHQ0OuZDVWzRIgNbsHQ0OuZDVWzRIgNbsHQ0OuZDVWzRIgNbsHQ0OuZDVWzRIgNbsHQ0OuZDVWzRIgNbsHQ0OuZDVWzRIgNbsHQ0OuZDVWzRIgNbsHQ0OuZDVWzRIgNbsHQ0OuZDVWzRIg'))
        choice = input(f'{BRIGHT_GREEN}Select: {RESET}').strip()
        if choice == _sec_string('kA=='):
            print()
            file_name = input(f'{YELLOW}Enter file name: {RESET}').strip()
            output_file = input(f'{YELLOW}File name for output: {RESET}').strip()
            try:
                with open(file_name, _sec_string('0w==')) as f:
                    text = f.read()
                domains = extract_domains(text)
                print()
                print(f'{ORANGE}Domains extracted:{RESET}')
                for domain in domains:
                    print(f'{ORANGE}{domain}{RESET}')
                save_to_file(domains, output_file)
            except FileNotFoundError:
                print(f'{YELLOW}File not found. Please check the file name and try again.{RESET}')
        elif choice == _sec_string('kw=='):
            print()
            terminal_width = shutil.get_terminal_size().columns
            print(_sec_string('Q0OuZDVWzRIgNbsHQ0OuZDVWzRIgNbsHQ0OuZDVWzRIgNbsHQ0OuZDVWzRIgNbsHQ0OuZDVWzRIgNbsHQ0OuZDVWzRIgNbsHQ0OuZDVWzRIgNbsHQ0OuZDVWzRIgNbsHQ0OuZDVWzRIgNbsHQ0OuZDVWzRIg'))
            print(center_text(f'{YELLOW}Paste your text content below{RESET}', terminal_width))
            print(center_text(f'{YELLOW}and when finished, type done..{RESET}', terminal_width))
            print(_sec_string('Q0OuZDVWzRIgNbsHQ0OuZDVWzRIgNbsHQ0OuZDVWzRIgNbsHQ0OuZDVWzRIgNbsHQ0OuZDVWzRIgNbsHQ0OuZDVWzRIgNbsHQ0OuZDVWzRIgNbsHQ0OuZDVWzRIgNbsHQ0OuZDVWzRIgNbsHQ0OuZDVWzRIg'))
            user_input = ''
            while True:
                line = input()
                if _sec_string('xbhB44/5') in line.lower():
                    break
                user_input += line + _sec_string('qw==')
            domains = extract_domains(user_input)
            print()
            print(f'{ORANGE}Domains extracted:{RESET}')
            for domain in domains:
                print(f'{ORANGE}{domain}{RESET}')
            output_file = input(f'{YELLOW}File name for output: {RESET}').strip()
            save_to_file(domains, output_file)
        elif choice.lower() == _sec_string('wg=='):
            print(_sec_string('urQ='), end='')
        elif choice.lower() == _sec_string('xA=='):
            print(f'{YELLOW}Exiting program. Goodbye!{RESET}')
            break
        else:
            print(f'{YELLOW}Invalid choice. Please select 1, 2, c, or e.{RESET}')

async def fetch_status_custom_port(session, url, semaphore):
    try:
        async with semaphore:
            async with session.get(url, timeout=2) as response:
                server = response.headers.get(_sec_string('8rJd8MSl'), _sec_string('9LlE6M6gQQ=='))
                return (response.status, server)
    except asyncio.TimeoutError:
        return (None, _sec_string('9b5C486iWw=='))
    except Exception as e:
        return (None, f'Error: {e}')

async def scan_ip_custom_port(ip, port, total_ips, index, server_dict, semaphore):
    url = f'http://{ip}:{port}'
    async with aiohttp.ClientSession() as session:
        status, server = await fetch_status_custom_port(session, url, semaphore)
        if status and status != 302 and (_sec_string('5KVd6dM=') not in server):
            server_dict[ip] = (status, server, port)
            sys.stdout.write(_sec_string('rA==') + _sec_string('gQ==') * 80 + _sec_string('rA=='))
            sys.stdout.flush()
            result_line = f'{Fore.GREEN}{ip}:{port}: {Fore.CYAN}{status} {Fore.MAGENTA}{server}'
            print(result_line)
            append_to_v4(result_line)
        scanned = index + 1
        progress = scanned / total_ips
        speed = scanned / (time.time() - start_time)
        progress_line = f'\rIPs scanned: {Fore.CYAN}{scanned}/{total_ips}{Style.RESET_ALL} ({progress * 100:.2f}%) - Speed: {Fore.CYAN}{speed:.2f} IPs/s{Style.RESET_ALL}'
        sys.stdout.write(progress_line)
        sys.stdout.flush()

async def scan_cidr_block_custom_port(cidr_block, port):
    network = ipaddress.ip_network(cidr_block, strict=False)
    total_ips = network.num_addresses
    ips = network.hosts()
    server_dict = {}
    semaphore = asyncio.Semaphore(300)
    global start_time
    start_time = time.time()
    chunk_size = 1000
    ip_list = list(ips)
    print(f'{Fore.RED}{Style.BRIGHT}ACTIVE IPS ALIVE ON PORT {port}\n' + _sec_string('jA==') * 20)
    for i in range(0, len(ip_list), chunk_size):
        chunk = ip_list[i:i + chunk_size]
        tasks = [scan_ip_custom_port(str(ip), port, total_ips, i + j, server_dict, semaphore) for j, ip in enumerate(chunk)]
        await asyncio.gather(*tasks)
    end_time = time.time()
    duration = end_time - start_time
    sys.stdout.write(_sec_string('rA==') + _sec_string('gQ==') * 80 + _sec_string('rA=='))
    total_scanned = len(server_dict)
    speed = total_scanned / duration if duration > 0 else 0
    print(f'\n{Fore.YELLOW}Time taken for scanning: {duration:.2f} seconds')
    print(f'{Fore.YELLOW}Scanning speed: {Fore.CYAN}{speed:.2f} IPs per second{Style.RESET_ALL}')

async def scan_multiple_cidr_blocks_custom_port(cidr_blocks, port):
    for cidr_block in cidr_blocks:
        try:
            ipaddress.ip_network(cidr_block, strict=False)
            print(f'\nScanning CIDR block: {cidr_block} on port {port}')
            await scan_cidr_block_custom_port(cidr_block, port)
        except ValueError:
            print(f"{Fore.RED}Invalid CIDR block '{cidr_block}'. Skipping.")

async def custom_port_scanner():
    while True:
        clear_screen()
        title = f'{Fore.RED}{Style.BRIGHT}CUSTOM PORT SCANNER ANY 443/22/8080/....... {Style.RESET_ALL}'
        subtitle = f'{Fore.CYAN}CREATOR TELEGRAM: @Hackerprime254{Style.RESET_ALL}'
        logo = f'{Fore.RED}{Style.BRIGHT}DEVELOPER IS NOT RESPONSIBLE FOR ANY HARM TO YOUR NETWORK\n' + _sec_string('Q0G+ZDdGzRAwNbkXQ0G+ZDdTzRAlNbkCQ0GrZDdXzRAhNbkGQ0GvZDdXzRAhNbkGQ0GvZDdTzRAlNbkCQ0GrZDdTzRAlNbkXQ0G+ZDdGzRAwNbkXQ0G+ZDdGJQ==') + _sec_string('Q0G+ZDdGzRAwNbkXQ0G+ZDdfzRAwNbkXQ0G+ZDdGzRAzNbkUQ0G9ZDdFzRAzNbkUQ0G9ZDdFzRAzNbkUQ0G9ZDdFzRAwNbkXQ0GvZDdXzRAlNbkXQ0G+ZDdGzRAw3Q==') + _sec_string('Q0G+ZDdGzRAwNbkXQ0GnZDdGzRAwNbkXQ0G9ZDdFzRAzNbkUQ0G9ZDdFzRAwNbkXQ0G+ZDdGzRAwNbkXQ0G+ZDdGzRAzNbkUQ0G9ZDdGzRAwNbkOQ0G+ZDdGzRAw3Q==') + _sec_string('Q0G+ZDdGzRAwNbkOQ0G+ZDdGzRAwNbkXQ0G+ZDdGzRAlNbkOQ0GnZDdXzRAlNbkCQ0G+ZDdGzRAwNbkXQ0G+ZDdTzRAlNbkCQ0G+ZDdGzRAwNbkXQ0GnZDdGzRAw3Q==') + _sec_string('Q0G+ZDdTzRAhNbkUQ0GrZDdTzRAlNbkUQ0G+ZDdfzRAhNbkGQ0GvZDdXzRAlNbkCQ0GnZDdGzRAwNbkXQ0GnZDdfzRAlNbkCQ0GnZDdGzRAwNbkXQ0G+ZDdfzRAw3Q==') + _sec_string('Q0GnZDdGzRAzNbkOQ0G9ZDdTzRAwNbkGQ0GrZDdTzRAlNbkGQ0G+ZDdGzRAwNbkXQ0G+ZDdGzRAwNbkXQ0GnZDdGzRAwNbkXQ0G9ZDdFzRAzNbkUQ0G9ZDdGzRAp3Q==') + _sec_string('Q0GnZDdGzRAzNbkOQ0G+ZDdfzRAhNbkCQ0GrZDdGzRAwNbkXQ0G+ZDdGzRApNbkGQ0G+ZDdGzRAwNbkXQ0GvZDdTzRAwNbkXQ0GrZDdXzRAhNbkGQ0GrZDdFzRAp3Q==') + _sec_string('Q0G+ZDdfzRAwNbkGQ0GrZDdGzRApNbkCQ0G+ZDdfzRAhNbkCQ0GrZDdGzRAhNbkXQ0GvZDdXzRAwNbkCQ0GrZDdXzRAwNbkXQ0G+ZDdGzRApNbkXQ0G+ZDdfzRAw3Q==') + _sec_string('Q0G+ZDdGzRApNbkXQ0G+ZDdGzRAhNbkCQ0GvZDdfzRAlNbkCQ0G+ZDdfzRAhNbkGQ0GvZDdTzRAlNbkCQ0GrZDdXzRAhNbkOQ0GvZDdfzRApNbkXQ0GnZDdGzRAw3Q==') + _sec_string('Q0G+ZDdGzRAwNbkOQ0G+ZDdGzRAwNbkXQ0GnZDdfzRAwNbkXQ0GvZDdfzRAlNbkCQ0GrZDdfzRAlNbkCQ0GnZDdTzRApNbkOQ0GnZDdfzRAwNbkOQ0G+ZDdGzRAw3Q==') + _sec_string('Q0G+ZDdGzRAwNbkXQ0GnZDdGzRAwNbkXQ0G+ZDdXzRAhNbkCQ0G+ZDdfzRAwNbkXQ0G+ZDdfzRAwNbkOQ0GvZDdfzRApNbkOQ0GnZDdfzRApNbkXQ0GnZDdGzRAw3Q==') + _sec_string('Q0G+ZDdGzRAwNbkXQ0G+ZDdXzRAlNbkXQ0G+ZDdGzRAwNbkXQ0GvZDdXzRAlNbkCQ0GrZDdfzRAlNbkOQ0GrZDdfzRAlNbkOQ0GrZDdXzRAwNbkXQ0GnZDdGzRAw3Q==') + _sec_string('Q0G+ZDdGzRAwNbkXQ0G+ZDdGzRAwNbkGQ0GrZDdTzRAwNbkUQ0G9ZDdFzRAzNbkXQ0G+ZDdGzRAwNbkXQ0G+ZDdGzRAwNbkXQ0G+ZDdFzRAwNbkXQ0G+ZDdfzRAw3Q==') + _sec_string('Q0G+ZDdGzRAwNbkXQ0G+ZDdGzRAwNbkXQ0G+ZDdGzRAhNbkGQ0GrZDdTzRAwNbkUQ0G9ZDdFzRAzNbkUQ0G9ZDdFzRAzNbkUQ0G9ZDdGzRAwNbkXQ0G+ZDdfzRAw3Q==') + _sec_string('Q0G+ZDdGzRAwNbkXQ0G+ZDdGzRAwNbkXQ0G+ZDdGzRAwNbkXQ0G+ZDdGzRAhNbkCQ0GrZDdTzRAlNbkCQ0G+ZDdGzRAwNbkXQ0G+ZDdGzRAwNbkXQ0GnZDdGzRAw3Q==') + f'{Style.RESET_ALL}'
        print(title)
        print(subtitle)
        print(logo)
        while True:
            cidr_input = input(_sec_string('5Llb49P3ZtaBlGbC8/dN6s60RPWB/0qoxvkDppDuHaiQ4RiokfkfqZDhA7eY5QG3l+8Bto/nALeX/g/p0/cI5MC0RKGb9w==')).strip()
            if cidr_input.lower() in [_sec_string('w7ZM7Q=='), _sec_string('xK9G8g=='), _sec_string('0KJG8g=='), _sec_string('0A==')]:
                return
            port_input = input(_sec_string('5Llb49P3W+7E91/p06MP8s73XOXAuQ+uxPlIqI33F7aN9xuykv4Vpg=='))
            try:
                port = int(port_input)
                if port < 1 or port > 65535:
                    print(f'{Fore.RED}Invalid port number. Port must be between 1 and 65535.{Style.RESET_ALL}')
                    continue
            except ValueError:
                print(f'{Fore.RED}Invalid port input. Please enter a valid port number.{Style.RESET_ALL}')
                continue
            cidr_blocks = [cidr.strip() for cidr in cidr_input.split(_sec_string('jQ=='))]
            await scan_multiple_cidr_blocks_custom_port(cidr_blocks, port)
            while True:
                continue_scanning = input(_sec_string('5bgP/86iD/HAuVum1bgP9cK2QabMuF3jgZRmwvP3TerOtET1nvcH/8SkAOjO/hWm')).strip().lower()
                if continue_scanning in [_sec_string('2LJc'), _sec_string('z7g=')]:
                    break
                print(f"{Fore.RED}Invalid input. Please enter 'yes' or 'no'.{Style.RESET_ALL}")
            if continue_scanning != _sec_string('2LJc'):
                break

def unlimited_scanner_no_freeze():
    """Super Fast HTTP Status Checker – Filters out 302 and errors, keeps all other responses"""
    RED_BOLD = _sec_string('uowevZLmQg==')
    GREEN_BOLD = _sec_string('uowevZLlQg==')
    YELLOW_BOLD = _sec_string('uowevZLkQg==')
    CYAN_BOLD = _sec_string('uowevZLhQg==')
    WHITE_BOLD = _sec_string('uowevZLgQg==')
    BLUE_BOLD = _sec_string('uowevZLjQg==')
    MAGENTA_BOLD = _sec_string('uowevZLiQg==')
    RESET = _sec_string('uowf6w==')
    CLEAR_SCREEN = _sec_string('uowdzLqMZw==')
    STATUS_COLORS = {_sec_string('k+cf'): GREEN_BOLD, _sec_string('k+ce'): GREEN_BOLD, _sec_string('k+cd'): GREEN_BOLD, _sec_string('k+cc'): GREEN_BOLD, _sec_string('k+cb'): GREEN_BOLD, _sec_string('kuce'): YELLOW_BOLD, _sec_string('kucd'): YELLOW_BOLD, _sec_string('kucc'): YELLOW_BOLD, _sec_string('kucb'): YELLOW_BOLD, _sec_string('kucY'): YELLOW_BOLD, _sec_string('kucX'): YELLOW_BOLD, _sec_string('lecf'): RED_BOLD, _sec_string('lece'): RED_BOLD, _sec_string('lecc'): RED_BOLD, _sec_string('lecb'): RED_BOLD, _sec_string('leca'): RED_BOLD, _sec_string('lOcf'): RED_BOLD, _sec_string('lOce'): RED_BOLD, _sec_string('lOcd'): RED_BOLD, _sec_string('lOcc'): RED_BOLD, _sec_string('lOcb'): RED_BOLD}

    def get_status_color(status_code):
        if status_code in STATUS_COLORS:
            return STATUS_COLORS[status_code]
        if status_code.isdigit():
            code = int(status_code)
            if 200 <= code < 300:
                return GREEN_BOLD
            elif 300 <= code < 400:
                return YELLOW_BOLD
            elif 400 <= code < 500:
                return RED_BOLD
            elif 500 <= code < 600:
                return RED_BOLD
        return WHITE_BOLD

    def clear_screen():
        sys.stdout.write(CLEAR_SCREEN)
        sys.stdout.flush()

    def get_terminal_width():
        try:
            return shutil.get_terminal_size().columns
        except:
            return 80

    def get_terminal_height():
        try:
            return shutil.get_terminal_size().lines
        except:
            return 24

    def print_header():
        term_width = get_terminal_width()
        effective_width = max(term_width, 40)
        logo_lines = [_sec_string('Q0G9ZDdFzRAzNbkUQ0G9ZDdFzRAzNbkUQ0GrZDdTzRAlNbkCQ0GrZDdTzRAlNbkCQ0G9ZDdFzRAzNbkUQ0G9ZDdF'), _sec_string('Q0G9ZDdFzRApNbkUQ0G9ZDdFzRAlNbkOQ0GnZDdfzRApNbkOQ0GnZDdfzRApNbkOQ0GnZDdTzRAzNbkUQ0G9ZDdF'), _sec_string('Q0G9ZDdfzRAxNbkUQ0G9ZDdFzRApNbkOQ0GnZDdfzRApNbkOQ0GnZDdfzRApNbkOQ0GnZDdfzRAzNbkUQ0G9ZDdF'), _sec_string('Q0G9ZDdbzRAxNbkUQ0G9ZDdfzRApNbkCQ0GvZDdfzRApNbkOQ0GnZDdfzRApNbkGQ0GrZDdfzRApNbkUQ0G9ZDdF'), _sec_string('Q0G/ZDVrzRAxNbkUQ0G9ZDdfzRApNbkCQ0GrZDdTzRAlNbkOQ0GnZDdTzRAlNbkCQ0GrZDdfzRApNbkUQ0G9ZDdF'), _sec_string('Q0G/ZDVrzRAxNbkUQ0G9ZDdfzRApNbkOQ0GnZDdfzRApNbkOQ0GnZDdfzRApNbkOQ0GnZDdfzRApNbkUQ0G9ZDdF'), _sec_string('Q0G/ZDdTzRAxNbkOQ0GnZDdfzRApNbsGQ0GvZDdHzRAxNbkGQ0GnZDVXzRApNbsGQ0GjZDdHzRApNbkOQ0GrZDdF'), _sec_string('Q0G9ZDdFzRApNbkOQ0GnZDdfzRApNbsGQ0OvZDVXzRIhNbsGQ0OvZDVXzRIhNbsGQ0OvZDdHzRApNbkOQ0GnZDdb'), _sec_string('Q0G9ZDdFzRApNbkGQ0GvZDdfzRApNbkCQ0GnZDVXzRAlNbsGQ0OvZDVXzRAxNbsGQ0GrZDdfzRApNbkOQ0GvZDdF'), _sec_string('Q0G9ZDdFzRApNbkUQ0G9ZDdfzRApNbkOQ0GnZDdfzRApNbkOQ0GrZDdfzRApNbkOQ0GnZDdfzRApNbkUQ0G9ZDdF'), _sec_string('Q0G9ZDdFzRAzNbkUQ0G9ZDdfzRApNbkOQ0GnZDdfzRApNbkOQ0GnZDdfzRApNbkOQ0GnZDdfzRApNbkUQ0G9ZDdF'), _sec_string('Q0G9ZDdFzRAzNbkUQ0G9ZDdfzRApNbkOQ0GnZDdfzRApNbkOQ0GnZDdfzRAxNbkKQ0GnZDdfzRAtNbkUQ0G9ZDdF'), _sec_string('Q0G9ZDdFzRAzNbkUQ0G9ZDdHzRAhNbkWQ0G9ZDdbzRAhNbkOQ0GvZDdFzRAxNbkUQ0GnZDdFzRAzNbkUQ0G9ZDdF'), _sec_string('Q0G9ZDdFzRAzNbkUQ0G9ZDdFzRAzNbkUQ0G9ZDdFzRAzNbkWQ0G9ZDdFzRAzNbkUQ0GjZDdFzRAzNbkUQ0G9ZDdF')]
        title = _sec_string('8oJ/w/P3acfygw/O9YN/pvKUbsjvkn2mQ1e8puqSataBlmPKgZJ3xeSHe6aS5x2mh/dq1POYfdU=')
        subtitle = _sec_string('7b5Z44GFSvXUu1v1gasPx9SjQKvzslzzzLIP+oGaWurVvgLWzqVb')
        print(RED_BOLD + _sec_string('nA==') * effective_width + RESET)
        if len(title) > effective_width - 2:
            title = title[:effective_width - 5] + _sec_string('j/kB')
        print(RED_BOLD + title.center(effective_width) + RESET)
        if len(subtitle) > effective_width - 2:
            subtitle = subtitle[:effective_width - 5] + _sec_string('j/kB')
        print(CYAN_BOLD + subtitle.center(effective_width) + RESET)
        print(RED_BOLD + _sec_string('nA==') * effective_width + RESET)
        for line in logo_lines:
            if len(line) > effective_width - 2:
                line = line[:effective_width - 2]
            print(RED_BOLD + line.center(effective_width) + RESET)
        print(RED_BOLD + _sec_string('nA==') * effective_width + RESET)
        print()

    def find_output_files(input_file):
        input_dir = os.path.dirname(input_file)
        input_basename = os.path.splitext(os.path.basename(input_file))[0]
        output_files = []
        search_dir = input_dir if input_dir else _sec_string('jw==')
        for file in os.listdir(search_dir):
            if file.startswith(f'{input_basename}_results') and file.endswith(_sec_string('j6NX8g==')):
                full_path = os.path.join(search_dir, file)
                output_files.append(full_path)
        output_files.sort(key=lambda x: os.path.getmtime(x), reverse=True)
        return output_files

    def get_host_count_from_file(filename):
        try:
            with open(filename, _sec_string('0w==')) as f:
                return sum((1 for line in f if line.strip()))
        except:
            return 0

    def read_processed_hosts(output_file):
        processed = set()
        try:
            with open(output_file, _sec_string('0w==')) as f:
                for line in f:
                    if _sec_string('mw==') in line and _sec_string('Q1G9') not in line:
                        host = line.split(_sec_string('mw=='), 1)[0].strip()
                        if host:
                            processed.add(host)
        except:
            pass
        return processed

    class FastHTTPChecker:

        def __init__(self, timeout=0.8, port=80):
            self.timeout = timeout
            self.port = port
            self.request_template = _sec_string('5pJ7po73Z9L1hwC3j+YijOm4XPKb91T7rN1s6c+5SuXVvkDom/dM6s6kSour2iU=')

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
                request = self.request_template.format(hostname)
                sock.send(request.encode(_sec_string('wKRM78g='), errors=_sec_string('yLBB6dOy')))
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
                    response = b''.join(response_data).decode(_sec_string('1KNJq5k='), errors=_sec_string('yLBB6dOy'))
                    status_code = _sec_string('1LlE6M6gQQ==')
                    if response.startswith(_sec_string('6YN71o4=')):
                        try:
                            first_line = response.split(_sec_string('qw=='))[0]
                            parts = first_line.split()
                            if len(parts) >= 2:
                                status_code = parts[1]
                        except:
                            pass
                    server = _sec_string('1LlE6M6gQQ==')
                    response_lower = response.lower()
                    if _sec_string('0rJd8MSlFQ==') in response_lower:
                        lines = response.split(_sec_string('qw=='))
                        for line in lines[:10]:
                            if line.lower().startswith(_sec_string('0rJd8MSlFQ==')):
                                server = line.split(_sec_string('mw=='), 1)[1].strip()
                                break
                    return (status_code, server)
                return (_sec_string('z7gC9MSkX+nPpEo='), None)
            except socket.timeout:
                return (_sec_string('1b5C486iWw=='), None)
            except ConnectionRefusedError:
                return (_sec_string('07JJ89KySw=='), None)
            except Exception:
                return (_sec_string('xKVd6dM='), None)
            finally:
                if sock:
                    try:
                        sock.shutdown(socket.SHUT_RDWR)
                        sock.close()
                    except:
                        pass

    def read_file_chunks(filename, processed_hosts, start_line=0, chunk_size=50):
        try:
            with open(filename, _sec_string('0w=='), encoding=_sec_string('1KNJq5k='), errors=_sec_string('yLBB6dOy')) as f:
                for _ in range(start_line):
                    try:
                        next(f)
                    except StopIteration:
                        break
                chunk = []
                current_line = start_line
                for line in f:
                    line = line.strip()
                    if line and (not line.startswith(_sec_string('gg=='))):
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

    def print_update(scanned, total, found, errors, elapsed, last_results, results_display, output_file, port):
        term_width = get_terminal_width()
        effective_width = max(term_width, 40)
        sys.stdout.write(CLEAR_SCREEN)
        print_header()
        percent = scanned / total * 100 if total > 0 else 0
        timestamp = datetime.datetime.now().strftime(_sec_string('hJ8Vo+ztCtU='))
        speed = scanned / elapsed if elapsed > 0 else 0
        bar_length = min(20, effective_width - 60)
        if bar_length < 5:
            bar_length = 5
        filled = int(bar_length * scanned / total) if total > 0 else 0
        bar = _sec_string('Q0Gn') * filled + _sec_string('Q0G9') * (bar_length - filled)
        status_line = f'[{timestamp}] {bar} {scanned}/{total} ({percent:.1f}%) | Found:{found} Errors:{errors} {speed:.1f}/s'
        if len(status_line) > effective_width - 1:
            status_line = status_line[:effective_width - 4] + _sec_string('j/kB')
        print(RED_BOLD + status_line + RESET)
        output_info = f'Output: {output_file} | Port: {port} | Total Results: {len(results_display)}'
        if len(output_info) > effective_width - 1:
            output_info = output_info[:effective_width - 4] + _sec_string('j/kB')
        print(CYAN_BOLD + output_info + RESET)
        print(RED_BOLD + _sec_string('jA==') * min(effective_width, 50) + RESET)
        print(f'{GREEN_BOLD}=== ALL LIVE RESULTS ({len(results_display)} total) ==={RESET}')
        print(f'{YELLOW_BOLD}Scroll up to see all results{RESET}')
        print(RED_BOLD + _sec_string('jA==') * min(effective_width, 50) + RESET)
        if results_display:
            display_results = results_display[-50:] if len(results_display) > 50 else results_display
            for line in display_results:
                if len(line) > effective_width - 2:
                    line = line[:effective_width - 5] + _sec_string('j/kB')
                print(line)
            if len(results_display) > 50:
                print(f'{CYAN_BOLD}... and {len(results_display) - 50} more results (scroll up to see all){RESET}')
        else:
            print(f'{YELLOW_BOLD}Waiting for results...{RESET}')
        print(RED_BOLD + _sec_string('jA==') * min(effective_width, 50) + RESET)
        if last_results:
            h, ip_addr, s, sv = last_results[-1]
            short_h = h[:15] + _sec_string('j/k=') if len(h) > 15 else h
            status_color = get_status_color(s)
            last_line = f'Last: {CYAN_BOLD}{short_h}{RESET}:{YELLOW_BOLD}{port}{RESET} '
            last_line += f'→ {status_color}{s}{RESET}'
            if sv and sv != _sec_string('1LlE6M6gQQ=='):
                last_line += f' [{MAGENTA_BOLD}{sv[:10]}{RESET}]'
            if ip_addr:
                last_line += f' ({BLUE_BOLD}{ip_addr}{RESET})'
            print(YELLOW_BOLD + _sec_string('7bZc8pv3') + last_line + RESET)
        print(RED_BOLD + _sec_string('nA==') * min(effective_width, 40) + RESET)
        print(f'{YELLOW_BOLD}Press Ctrl+C to stop | Scroll up/down to see all results{RESET}')
        sys.stdout.flush()

    def format_result_line(hostname, ip, port, status_code, server):
        status_color = get_status_color(status_code)
        line = f'{CYAN_BOLD}{hostname}{RESET}:{YELLOW_BOLD}{port}{RESET} '
        line += f'→ {status_color}{status_code}{RESET}'
        if ip:
            line += f' ({BLUE_BOLD}{ip}{RESET})'
        if server and server != _sec_string('1LlE6M6gQQ=='):
            line += f' [{MAGENTA_BOLD}{server[:15]}{RESET}]'
        return line

    def count_total_lines(filename):
        try:
            with open(filename, _sec_string('07U=')) as f:
                return sum((1 for _ in f))
        except:
            return 0
    while True:
        clear_screen()
        print_header()
        try:
            workers_input = input(f'{YELLOW_BOLD}Threads (1-50, default 20):{RESET} ').strip()
            workers = int(workers_input) if workers_input else 20
            workers = max(1, min(50, workers))
        except:
            workers = 20
        try:
            timeout_input = input(f'{YELLOW_BOLD}Timeout seconds (0.3-3, default 0.8):{RESET} ').strip()
            timeout = float(timeout_input) if timeout_input else 0.8
            timeout = max(0.3, min(3, timeout))
        except:
            timeout = 0.8
        try:
            port_input = input(f'{YELLOW_BOLD}Port (default 80):{RESET} ').strip()
            port = int(port_input) if port_input else 80
            port = max(1, min(65535, port))
        except:
            port = 80
        while True:
            input_file = input(f'\n{YELLOW_BOLD}Hosts file (hostname IP per line):{RESET} ').strip()
            if os.path.isfile(input_file):
                break
            print(f'{RED_BOLD}File not found{RESET}')
        while True:
            output_file = input(f'\n{YELLOW_BOLD}Output file:{RESET} ').strip()
            if output_file:
                if not output_file.endswith(_sec_string('j6NX8g==')):
                    output_file += _sec_string('j6NX8g==')
                break
            print(f'{RED_BOLD}Please enter an output file name{RESET}')
        if os.path.exists(output_file):
            print(f"\n{CYAN_BOLD}Output file '{os.path.basename(output_file)}' already exists.{RESET}")
            print(f'{YELLOW_BOLD}Choose an option:{RESET}')
            print(f'  1. Resume from where you left off')
            print(f'  2. Start fresh (overwrite file)')
            print(f'  3. Use a different filename')
            while True:
                choice = input(f'\n{YELLOW_BOLD}Enter choice (1, 2, or 3):{RESET} ').strip()
                if choice == _sec_string('kA=='):
                    processed_hosts = read_processed_hosts(output_file)
                    start_line = get_host_count_from_file(output_file)
                    resume_mode = True
                    print(f'\n{GREEN_BOLD}✓ Resuming from existing scan{RESET}')
                    print(f'  Already processed: {len(processed_hosts)} hosts')
                    print(f'  Resume from line: {start_line}')
                    input(f'\n{YELLOW_BOLD}Press Enter to continue...{RESET}')
                    break
                elif choice == _sec_string('kw=='):
                    resume_mode = False
                    start_line = 0
                    processed_hosts = set()
                    print(f'\n{YELLOW_BOLD}Starting fresh scan (overwriting existing file)...{RESET}')
                    input(f'\n{YELLOW_BOLD}Press Enter to continue...{RESET}')
                    break
                elif choice == _sec_string('kg=='):
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
                    print(f'{RED_BOLD}Invalid choice. Please enter 1, 2, or 3.{RESET}')
        else:
            print(f'\n{CYAN_BOLD}New output file: {os.path.basename(output_file)}{RESET}')
            print(f'{YELLOW_BOLD}Choose scan option:{RESET}')
            print(f'  1. Start from beginning (line 0)')
            print(f'  2. Start from specific line number')
            while True:
                choice = input(f'\n{YELLOW_BOLD}Enter choice (1 or 2):{RESET} ').strip()
                if choice == _sec_string('kA=='):
                    resume_mode = False
                    start_line = 0
                    processed_hosts = set()
                    print(f'\n{GREEN_BOLD}Starting from beginning (line 0){RESET}')
                    break
                elif choice == _sec_string('kw=='):
                    while True:
                        try:
                            start_line_input = input(f'{YELLOW_BOLD}Enter line number to start from:{RESET} ').strip()
                            if start_line_input:
                                start_line = int(start_line_input)
                                if start_line >= 0:
                                    resume_mode = False
                                    processed_hosts = set()
                                    print(f'\n{GREEN_BOLD}Starting from line: {start_line}{RESET}')
                                    break
                                else:
                                    print(f'{RED_BOLD}Please enter a positive number or 0{RESET}')
                            else:
                                print(f'{RED_BOLD}Please enter a number{RESET}')
                        except ValueError:
                            print(f'{RED_BOLD}Invalid input. Please enter a valid number.{RESET}')
                    break
                else:
                    print(f'{RED_BOLD}Invalid choice. Please enter 1 or 2.{RESET}')
            input(f'\n{YELLOW_BOLD}Press Enter to continue...{RESET}')
        total_lines = count_total_lines(input_file)
        if start_line > total_lines:
            print(f'{RED_BOLD}Warning: Start line ({start_line}) exceeds total lines ({total_lines}){RESET}')
            start_line = 0
            print(f'{YELLOW_BOLD}Reset to start from beginning (line 0){RESET}')
            input(f'\n{YELLOW_BOLD}Press Enter to continue...{RESET}')
        clear_screen()
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
            out_f = open(output_file, _sec_string('wA==') if resume_mode else _sec_string('1g=='), buffering=1)
        except Exception as e:
            print(f'{RED_BOLD}Error opening output file: {e}{RESET}')
            sys.exit(1)
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
                        unwanted = {_sec_string('kucd'), _sec_string('1b5C486iWw=='), _sec_string('07JJ89KySw=='), _sec_string('xKVd6dM='), _sec_string('z7gC9MSkX+nPpEo=')}
                        if status_code not in unwanted:
                            out_f.write(f"{hostname}:{port} {status_code} : {server or _sec_string('1LlE6M6gQQ==')}\n")
                            out_f.flush()
                            found += 1
                            result_line = format_result_line(hostname, ip, port, status_code, server)
                            results_display.append(result_line)
                        else:
                            errors += 1
                        last_results.append((hostname, ip, status_code, server))
                        current_time = time.time()
                        if current_time - last_update >= 0.2:
                            elapsed = time.time() - start_time
                            print_update(scanned, total_lines, found, errors, elapsed, last_results, results_display, output_file, port)
                            last_update = current_time
                    except queue.Empty:
                        continue
        except KeyboardInterrupt:
            print(f'\n\n{YELLOW_BOLD}⚠ Scan stopped by user{RESET}')
            elapsed = time.time() - start_time
            print(f'{GREEN_BOLD}Results Summary:{RESET}')
            print(f'  Scanned: {scanned} hosts')
            print(f'  Found: {found} hosts')
            print(f'  Errors/Filtered: {errors} hosts')
            if elapsed > 0:
                print(f'  Speed: {scanned / elapsed:.1f}/s')
            print(f'  Resume from line: {scanned}')
            print(f'  Output: {output_file}')
        except Exception as e:
            print(f'\n{RED_BOLD}Error: {e}{RESET}')
        finally:
            for _ in threads:
                task_queue.put(None)
            for t in threads:
                t.join(timeout=1)
            elapsed = time.time() - start_time
            speed = scanned / elapsed if elapsed > 0 else 0
            out_f.close()
            print(f'\n\n{GREEN_BOLD}✓ SCAN COMPLETE{RESET}')
            print(f'{GREEN_BOLD}═══ Results Summary ═══{RESET}')
            print(f'  Total scanned: {scanned} hosts')
            print(f'  Valid found: {found} hosts')
            print(f'  Errors/Filtered: {errors} hosts')
            print(f'  Time: {elapsed:.1f}s')
            print(f'  Speed: {speed:.1f} hosts/s')
            print(f'  Output: {output_file}')
            if results_display:
                print(f'  Total results: {len(results_display)}')
        while True:
            print(f'\n{CYAN_BOLD}Options:{RESET}')
            print(f'{GREEN_BOLD}1. Scan another file{RESET}')
            print(f'{YELLOW_BOLD}2. Return to main menu{RESET}')
            choice = input(f'{CYAN_BOLD}Enter your choice (1-2): {RESET}').strip()
            if choice == _sec_string('kA=='):
                break
            elif choice == _sec_string('kw=='):
                return
            else:
                print(f'{RED_BOLD}Invalid choice. Please enter 1 or 2.{RESET}')

def show_banner():
    print(f'\n{Fore.RED}DOMAIN FINDER ANY COUNTRY V5 @PREMIUM{Style.RESET_ALL}')
    print(f'{Fore.CYAN}')
    print(_sec_string('gfcA+oH3U9qB9w+mgfcPpoH3D6aOqw+m3YsPpg=='))
    print(_sec_string('gfhTpoGrc6aB9w+mgfcPpoH3D6nd9w/6/fc='))
    print(_sec_string('jvdTpoGrD9qB9w+mgfcPpoH3AKbd9w/6gYsP'))
    print(_sec_string('3fdTpoGrD/qB9w+mgfcPpoH3U6bd9w/6gasP'))
    print(_sec_string('/fcP2o73D6mB93DZgfdw2YH3c6aBiwCmgfgP'))
    print(_sec_string('gYsPpoH3AKaB+A+pgfdzpv33D9qB9w+mjvcP'))
    print(_sec_string('gfdzpoH4D6aBiw/a/ogApo73D6b99w+pgfcP'))
    print(_sec_string('gfdzpoH4D6aB+A+mgfcPpv33D6b99w+pgfcP'))
    print(_sec_string('gYgP2oGLcNmO92CmgfcPyYGLcNmO9wCm/vcP'))
    print(_sec_string('gYtzpv2IcNmB9w+mgfcPpoH3cNn++A+pjvcPpg=='))
    print(_sec_string('/vcP2v2IcNmO9w/Z/ohw2f73D9r+iHCpjvcP2Q=='))
    print(_sec_string('/YsPpoz6AquJ9w+mgfcPpoH3D6+M+gKrgfcAqQ=='))
    print(_sec_string('gYtz2f6IcNmJ93DZ/ohw2f6ID6/+iHDZ/vgApg=='))
    print(_sec_string('gfdRq4z6AquJ9w+mgfcPpoH3D6+M+gKrjKkP2Q=='))
    print(_sec_string('gfcP2f6IcNmJ93DZ/ohw2f6ID6/+iHDZ/vcP2v0='))
    print(_sec_string('gfcAqoz6AquJ9w+mgfcPpoH3D6+M+gKrgfdwqY4='))
    print(_sec_string('gfgApoH3D6aJ9w/Z/ohw2f73D6+B9w+mgfgPpv33'))
    print(_sec_string('gakPpoH3D6aBiw+mgfcPpoH3AKaB9w+mgYsPpo73'))
    print(_sec_string('gfcPpoH3D6aB93OmgYhwpoH4D6aB9w+mgfgPqYH3'))
    print(_sec_string('gfcPpoH3D6aB9w/agfcPpo73D6aB9w+mjvcApoH3'))
    print(_sec_string('gfcPpoH3D6aB9w+m/fcPpv33D6aB9w+pgfgPpoH3'))
    print(_sec_string('gfcPpoH3D6aB9w+mgYsPpoGpAquM+lGmjvcPpoH3'))
    print(_sec_string('gfcPpoH3D6aB9w+mgfdz2f6IcNn+iHCpgfcPpoH3'))
    print(f'{Style.RESET_ALL}')

def extract_hostnames(text):
    try:
        text = re.sub(_sec_string('/bNUvo2qU939/XO5hIo='), '', text)
        potential = re.findall(_sec_string('iegVrp7tdOeMrR+rmPpyrf35Bq36tgL8/Kwdqtz+'), text.lower())
        valid = []
        for host in potential:
            host = host.strip(_sec_string('j/o='))
            parts = host.split(_sec_string('jw=='))
            if 4 <= len(host) <= 253 and len(parts) >= 2 and (len(parts[-1]) >= 2) and (not any((p.startswith(_sec_string('jA==')) or p.endswith(_sec_string('jA==')) or len(p) > 63 for p in parts))):
                valid.append(host)
        return list(dict.fromkeys(valid))
    except Exception as e:
        print(f'{Fore.YELLOW}Warning: Error extracting hostnames: {str(e)}{Style.RESET_ALL}')
        return []

def scrape_crtsh(domain_suffix, max_retries=3):
    base_url = _sec_string('yaNb9tLtAKnCpVuo0r8A')
    params = {_sec_string('0A=='): f"%.{domain_suffix.lstrip(_sec_string('jw=='))}", _sec_string('zqJb9tSj'): _sec_string('y6RA6A==')}
    headers = {_sec_string('9KRK9IyWSOPPow=='): _sec_string('7LhV7827TqmU+R+miY8et5r3Y+/Polem2e8Z2ZfjFKbToRW3ke4Btoj3aOPCvECpk+cetpHmH7eBkUb0xLFA/o7mHrOP5w==')}
    for attempt in range(max_retries):
        try:
            response = requests.get(base_url, params=params, headers=headers, timeout=30)
            if response.status_code == 200:
                try:
                    data = response.json()
                    domains = []
                    for item in data:
                        if _sec_string('z7ZC4/6hTurUsg==') in item:
                            domains.extend((d.strip().lower() for d in re.split(_sec_string('+otBqvw='), item[_sec_string('z7ZC4/6hTurUsg==')]) if d.strip()))
                    return domains
                except json.JSONDecodeError:
                    params.pop(_sec_string('zqJb9tSj'), None)
                    continue
            response = requests.get(base_url, params={_sec_string('0A=='): f"%.{domain_suffix.lstrip(_sec_string('jw=='))}"}, headers=headers, timeout=2)
            return re.findall(_sec_string('iegV3cD6VbaM7gLbiosBr4qMTqvbilS0jao='), response.text.lower())
        except requests.RequestException as e:
            print(f'{Fore.YELLOW}Attempt {attempt + 1}/{max_retries} failed: {str(e)}')
            if attempt < max_retries - 1:
                time.sleep(5 * (attempt + 1))
    return []

async def domain_finder():
    while True:
        try:
            clear_screen()
            show_banner()
            while True:
                print(f"\n{Fore.CYAN}Enter domain suffix (e.g., .ke, .org, .com) or 'back': {Style.RESET_ALL}", end='')
                domain_suffix = input().strip().lower()
                if domain_suffix.lower() in [_sec_string('w7ZM7Q=='), _sec_string('xK9G8g=='), _sec_string('0KJG8g=='), _sec_string('0A==')]:
                    return
                if not domain_suffix:
                    print(f'{Fore.RED}Please enter a domain suffix.{Style.RESET_ALL}')
                    continue
                if not domain_suffix.startswith(_sec_string('jw==')):
                    domain_suffix = f'.{domain_suffix}'
                print(f'{Fore.CYAN}Scanning From DATABASE API  for *{domain_suffix} domains...{Style.RESET_ALL}')
                with tqdm(total=100, bar_format=f'{Fore.CYAN}{{l_bar}}{{bar:20}}{{r_bar}}{{bar:-20b}}', ncols=70) as pbar:
                    try:
                        raw_domains = scrape_crtsh(domain_suffix)
                        pbar.update(40)
                        filtered_domains = extract_hostnames(_sec_string('qw==').join(raw_domains))
                        pbar.update(30)
                        final_domains = sorted(set(filtered_domains), key=lambda x: (len(x.split(_sec_string('jw=='))), x))
                        pbar.update(30)
                    except Exception as e:
                        print(f'{Fore.RED}Error during scanning: {str(e)}{Style.RESET_ALL}')
                        final_domains = []
                if not final_domains:
                    print(f'{Fore.YELLOW}No valid domains found for *{domain_suffix}{Style.RESET_ALL}')
                    choice = input(f'{Fore.YELLOW}1. Try another suffix\n2. Return to main menu\nChoose (1-2): {Style.RESET_ALL}').strip()
                    if choice == _sec_string('kw=='):
                        return
                    continue
                while True:
                    print(f'\n{Fore.GREEN}Found {len(final_domains)} domains.{Style.RESET_ALL}')
                    print(f'{Fore.CYAN}1. Save to file')
                    print(_sec_string('k/kP1cK2QabAuUDyybJdpsW4QufIuQ=='))
                    print(_sec_string('kvkP1MSjWvTP91vpgbpO78/3QuPPog=='))
                    print(f'{Style.RESET_ALL}')
                    choice = input(f'{Fore.CYAN}Select option (1-3): {Style.RESET_ALL}').strip()
                    if choice == _sec_string('kA=='):
                        filename = input(f'{Fore.CYAN}Enter filename (e.g., domains.txt): {Style.RESET_ALL}').strip()
                        if not filename:
                            filename = f"domains_{domain_suffix.strip(_sec_string('jw=='))}.txt"
                        try:
                            with open(filename, _sec_string('1g==')) as f:
                                f.write(_sec_string('qw==').join(sorted(final_domains)))
                            print(f'{Fore.GREEN}Successfully saved {len(final_domains)} domains to {filename}{Style.RESET_ALL}')
                        except Exception as e:
                            print(f'{Fore.RED}Error saving file: {str(e)}{Style.RESET_ALL}')
                        input(f'{Fore.YELLOW}Press Enter to continue...{Style.RESET_ALL}')
                        break
                    elif choice == _sec_string('kw=='):
                        break
                    elif choice == _sec_string('kg=='):
                        return
                    else:
                        print(f'{Fore.RED}Invalid choice. Please select 1-3.{Style.RESET_ALL}')
        except KeyboardInterrupt:
            print(f'\n{Fore.YELLOW}Operation cancelled.{Style.RESET_ALL}')
            return
        except Exception as e:
            print(f'{Fore.RED}Unexpected error: {str(e)}{Style.RESET_ALL}')
            input(f'{Fore.YELLOW}Press Enter to continue...{Style.RESET_ALL}')

def load_hostnames_simple(file_path, start_line):
    """Load hostnames starting from a specific line number."""
    try:
        with open(file_path, _sec_string('0w==')) as f:
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
        self.SERVER_MAPPINGS = {_sec_string('4KdO5cmy'): [_sec_string('4KdO5cmy'), _sec_string('4KdO5cmyALQ='), _sec_string('4KdO5cmyALSP5Q=='), _sec_string('4KdO5cmyALSP4w=='), _sec_string('yaNb9sU=')], _sec_string('77BG6Nk='): [_sec_string('z7BG6Nk='), _sec_string('75BmyPk='), _sec_string('9bJB4ci5Sg==')], _sec_string('7L5M9M6kQODV+mbP8g=='): [_sec_string('7L5M9M6kQODV+mbP8g=='), _sec_string('6J58'), _sec_string('7L5M9M6kQODV+mfS9Ydu1ug=')], _sec_string('7b5b4/KnSuPF'): [_sec_string('7b5b4/KnSuPF'), _sec_string('7b5b49KnSuPF'), _sec_string('7b5b4/KnSuPFg0rlyQ==')], _sec_string('7qdK6POyXPLY'): [_sec_string('zqdK6NOyXPLY')], _sec_string('4rZL4tg='): [_sec_string('wrZL4tg=')], _sec_string('5qJB78K4Xeg='): [_sec_string('xqJB78K4Xeg=')], _sec_string('1IB8weg='): [_sec_string('1IB8weg=')], _sec_string('4r9K9M68SuM='): [_sec_string('4r9K9M68SuM=')], _sec_string('9bhC5cCj'): [_sec_string('4KdO5cmyAsXOrkDyxA=='), _sec_string('9bhC5cCj')], _sec_string('67Jb8tg='): [_sec_string('67Jb8tg=')], _sec_string('7b5I7tWjX+I='): [_sec_string('zb5I7tWjX+I=')], _sec_string('4rtA88WxQ+fTsg=='): [_sec_string('wrtA88WxQ+fTsg=='), _sec_string('4pE='), _sec_string('4rtA88WRQ+fTsg==')], _sec_string('6Lpf49OhTg=='): [_sec_string('yLpf49OhTg=='), _sec_string('yLlM59GkWurA')], _sec_string('4LxO68C+'): [_sec_string('4LxO68C+aM7OpFs='), _sec_string('4LxO68C+YePVhFvp07ZI4w=='), _sec_string('4LxO68C+')], _sec_string('57Zc8s2u'): [_sec_string('57Zc8s2u'), _sec_string('x7Zc8s2u')], _sec_string('4IB8puK7QPPFkV3pz6M='): [_sec_string('4rtA88WRXenPow==')], _sec_string('5rhA4c2yD8XNuFrigZRryA=='): [_sec_string('5rhA4c2yD8DTuEHyxLlL'), _sec_string('xqBc')], _sec_string('46JB6NiUa8g='): [_sec_string('w6JB6Ni0S+g='), _sec_string('46JB6NiUa8g=')], _sec_string('4LpO/M65D9WS'): [_sec_string('4LpO/M65fLU='), _sec_string('8uQ=')], _sec_string('77Jb6sixVg=='): [_sec_string('77Jb6sixVg==')], _sec_string('9ocPw8+wRujE'): [_sec_string('9ocPw8+wRujE'), _sec_string('9odqqw==')], _sec_string('6r5B9dW2'): [_sec_string('6r5B9dW2')], _sec_string('6bJd6cqi'): [_sec_string('ybJd6cqi'), _sec_string('6bJd6cqi')], _sec_string('575d48O2XOM='): [_sec_string('575d48O2XOM=')], _sec_string('97Jd5cS7'): [_sec_string('97Jd5cS7')], _sec_string('5b5I79W2Q8nCsk7o'): [_sec_string('5ZhhyeWS')], _sec_string('4K1a9MQ='): [_sec_string('4K1a9MQ='), _sec_string('4IV9'), _sec_string('9pZ41Q==')], _sec_string('7qNH49M='): [_sec_string('8rJd8MSl'), _sec_string('0rJd8MSl')], _sec_string('9LlE6M6gQQ=='): []}

    def detect_server(self, server_header):
        if not server_header:
            return _sec_string('9LlE6M6gQQ==')
        server_header = server_header.lower()
        for server, patterns in self.SERVER_MAPPINGS.items():
            for pattern in patterns:
                if pattern.lower() in server_header:
                    return server
        return _sec_string('7qNH49M=')

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
                return response.decode(errors=_sec_string('yLBB6dOy')).split(_sec_string('rN0ijA=='))[0]
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
        lines = headers.split(_sec_string('rN0='))
        if len(lines) > 0:
            try:
                status_code = int(lines[0].split(_sec_string('gQ=='))[1])
            except:
                pass
        for line in lines[1:]:
            if line.lower().startswith(_sec_string('0rJd8MSlFQ==')):
                server_header = line.split(_sec_string('mw=='), 1)[1].strip()
                break
        server_name = self.detect_server(server_header)
        return (hostname, status_code, server_name)

    def run_scan_fast(self, file_path, results_file, start_line):
        try:
            with open(results_file, _sec_string('1g==')) as outfile:
                hostnames = load_hostnames_simple(file_path, start_line)
                if hostnames is None:
                    print(f'{Fore.RED}Cannot load hostnames from file.{Style.RESET_ALL}')
                    return
                futures = set()
                with ThreadPoolExecutor(max_workers=100) as executor:
                    for _ in range(1000):
                        try:
                            hostname = next(hostnames)
                            if hostname:
                                futures.add(executor.submit(self.scan_host_fast, hostname))
                        except StopIteration:
                            break
                    pbar = tqdm(desc=_sec_string('8rRO6M++QeGBv0D11aQ='), unit=_sec_string('ybhc8tI='))
                    try:
                        while futures:
                            done, _ = wait(futures, return_when=FIRST_COMPLETED)
                            for future in done:
                                futures.remove(future)
                                result = future.result()
                                if result[1] and result[1] != 302:
                                    result_line = f'{result[0]} : {result[1]} : {result[2]}'
                                    outfile.write(result_line + _sec_string('qw=='))
                                    outfile.flush()
                                    append_to_v4(result_line)
                                pbar.update(1)
                                try:
                                    hostname = next(hostnames)
                                    if hostname:
                                        futures.add(executor.submit(self.scan_host_fast, hostname))
                                except StopIteration:
                                    pass
                    except KeyboardInterrupt:
                        print(f'{Fore.YELLOW}\nScan paused by user.{Style.RESET_ALL}')
                        return
                    pbar.close()
        except Exception as e:
            print(f'{Fore.RED}Error in scan: {e}{Style.RESET_ALL}')
            return

async def option_10_advanced_hostname_scanner():
    """
    OPTION 10: Advanced Hostname Scanner with error handling
    """
    while True:
        try:
            clear_screen()
            print(f'\n{Fore.RED}{Style.BRIGHT}ADVANCED HOSTNAME SCANNER (ANTI DPI){Style.RESET_ALL}')
            print(f'{Fore.CYAN}Telegram: @Hacker254prime{Style.RESET_ALL}')
            print(f"{Fore.YELLOW}Type 'back' at any time to return to main menu{Style.RESET_ALL}")
            scanner = AdvancedHostnameScannerSimple()
            while True:
                input_file = input(f"\n{Fore.CYAN}Enter path to hostnames file (or 'back'): {Style.RESET_ALL}").strip()
                if input_file.lower() in [_sec_string('w7ZM7Q=='), _sec_string('xK9G8g=='), _sec_string('0KJG8g=='), _sec_string('0A==')]:
                    return
                if not input_file:
                    print(f'{Fore.YELLOW}Please enter a file path.{Style.RESET_ALL}')
                    continue
                if not os.path.isfile(input_file):
                    print(f'{Fore.RED}File not found: {input_file}{Style.RESET_ALL}')
                    while True:
                        choice = input(f'{Fore.YELLOW}1. Try again\n2. Return to main menu\nChoose (1-2): {Style.RESET_ALL}').strip()
                        if choice == _sec_string('kA=='):
                            break
                        elif choice == _sec_string('kw=='):
                            return
                        else:
                            print(f'{Fore.RED}Invalid choice. Please enter 1 or 2.{Style.RESET_ALL}')
                    continue
                break
            while True:
                results_file = input(f"{Fore.CYAN}Enter results file name (default: host_results.txt, or 'back'): {Style.RESET_ALL}").strip()
                if results_file.lower() in [_sec_string('w7ZM7Q=='), _sec_string('xK9G8g=='), _sec_string('0KJG8g=='), _sec_string('0A==')]:
                    return
                if not results_file:
                    results_file = _sec_string('ybhc8v6lSvXUu1v1j6NX8g==')
                    break
                if not re.match(_sec_string('/4xz8f36Aab8/As='), results_file):
                    print(f'{Fore.RED}Invalid file name. Use only letters, numbers, dots, hyphens, and underscores.{Style.RESET_ALL}')
                    continue
                break
            while True:
                print(f'\n{Fore.CYAN}Choose scan mode:{Style.RESET_ALL}')
                print(f'{Fore.WHITE}1 = NEW scan (start from line 0){Style.RESET_ALL}')
                print(f'{Fore.WHITE}2 = RESUME scan from specific line{Style.RESET_ALL}')
                print(f"{Fore.YELLOW}Type 'back' to return{Style.RESET_ALL}")
                mode = input(f"{Fore.CYAN}Enter choice (1/2 or 'back'): {Style.RESET_ALL}").strip()
                if mode.lower() in [_sec_string('w7ZM7Q=='), _sec_string('xK9G8g=='), _sec_string('0KJG8g=='), _sec_string('0A==')]:
                    return
                if mode == _sec_string('kA=='):
                    start_line = 0
                    print(f'{Fore.GREEN}Starting NEW scan...{Style.RESET_ALL}')
                    break
                elif mode == _sec_string('kw=='):
                    while True:
                        resume_input = input(f"{Fore.CYAN}Enter line number to resume from (or 'back'): {Style.RESET_ALL}").strip()
                        if resume_input.lower() in [_sec_string('w7ZM7Q=='), _sec_string('xK9G8g=='), _sec_string('0KJG8g=='), _sec_string('0A==')]:
                            return
                        if resume_input.isdigit():
                            start_line = int(resume_input)
                            if start_line >= 0:
                                print(f'{Fore.GREEN}Resuming from line {start_line}...{Style.RESET_ALL}')
                                break
                            else:
                                print(f'{Fore.RED}Line number must be 0 or greater.{Style.RESET_ALL}')
                        else:
                            print(f'{Fore.RED}Invalid number. Please enter a valid line number.{Style.RESET_ALL}')
                    break
                else:
                    print(f'{Fore.RED}Invalid choice. Please enter 1 or 2.{Style.RESET_ALL}')
            print(f'\n{Fore.CYAN}Starting scan...{Style.RESET_ALL}')
            scanner.run_scan_fast(input_file, results_file, start_line)
            print(f'\n{Fore.GREEN}Scan completed! Results saved to {results_file}{Style.RESET_ALL}')
            while True:
                print(f'\n{Fore.CYAN}What would you like to do next?{Style.RESET_ALL}')
                print(f'{Fore.GREEN}1. Scan another file{Style.RESET_ALL}')
                print(f'{Fore.YELLOW}2. Return to main menu{Style.RESET_ALL}')
                choice = input(f'{Fore.CYAN}Enter your choice (1-2): {Style.RESET_ALL}').strip()
                if choice == _sec_string('kA=='):
                    break
                elif choice == _sec_string('kw=='):
                    return
                else:
                    print(f'{Fore.RED}Invalid choice. Please enter 1 or 2.{Style.RESET_ALL}')
        except KeyboardInterrupt:
            print(f'\n{Fore.YELLOW}Operation cancelled by user.{Style.RESET_ALL}')
            return
        except Exception as e:
            print(f'{Fore.RED}Unexpected error: {str(e)}{Style.RESET_ALL}')
            print(f'{Fore.YELLOW}Returning to main menu...{Style.RESET_ALL}')
            time.sleep(2)
            return

async def create_anti_dpi_format():
    """DNS Resolver v6.2 - Deduplication & Complete Resolution"""
    RED_BOLD = _sec_string('uowevZLmQg==')
    GREEN_BOLD = _sec_string('uowevZLlQg==')
    YELLOW_BOLD = _sec_string('uowevZLkQg==')
    CYAN_BOLD = _sec_string('uowevZLhQg==')
    RESET = _sec_string('uowf6w==')

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

        def __init__(self, total: int, unique: int):
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

        def show(self, stats: Stats, current: str=''):
            proc, succ, fail, writ, dup = stats.update()
            pct = min(100, int(proc * 100 / self.total)) if self.total else 0
            bar = _sec_string('nA==') * (pct // 5) + _sec_string('nw==') + _sec_string('gQ==') * (20 - pct // 5 - 1)
            if pct == 100:
                bar = _sec_string('nA==') * 20
            rate = stats.rate / 1000
            line = f'\r[{bar}] {pct:3d}% | {self.fmt(proc):>6} | ✓{self.fmt(succ):>5} | ✗{self.fmt(fail):>5} | 🔄{self.fmt(dup):>5} | 💾{self.fmt(writ):>5} | {rate:.1f}K/s | {current[:20]:<20}'
            sys.stdout.write(_sec_string('rA==') + _sec_string('gQ==') * self.last_len + _sec_string('rA=='))
            sys.stdout.write(line)
            sys.stdout.flush()
            self.last_len = len(line)

        def done(self):
            sys.stdout.write(_sec_string('qw=='))

    class ImmediateWriter:

        def __init__(self, filename: str):
            self.filename = filename
            self.file = open(filename, _sec_string('1g=='), buffering=1, encoding=_sec_string('1KNJq5k='), errors=_sec_string('07Jf6sC0Sg=='))
            self.lock = threading.Lock()
            self._closed = False
            self.seen_hostnames = set()

        def write(self, hostname: str, ip: str) -> bool:
            with self.lock:
                if not self._closed:
                    if hostname in self.seen_hostnames:
                        return False
                    line = f'{hostname}\t{ip}\n'
                    self.file.write(line)
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

    def resolve_getaddrinfo(hostname: str) -> str:
        try:
            result = socket.getaddrinfo(hostname, None, socket.AF_INET, socket.SOCK_STREAM)
            if result:
                ip = result[0][4][0]
                return ip
        except socket.gaierror:
            pass
        except Exception:
            pass
        return None

    def count_lines_and_deduplicate(filename: str) -> tuple:
        size = os.path.getsize(filename)
        print(f'📊 Analyzing {size / 1000000000.0:.2f} GB file...')
        total = 0
        unique_hostnames = set()
        with open(filename, _sec_string('0w=='), encoding=_sec_string('1KNJq5k='), errors=_sec_string('07Jf6sC0Sg==')) as f:
            for line in f:
                hostname = line.strip()
                if hostname and (not hostname.startswith(_sec_string('gg=='))):
                    total += 1
                    unique_hostnames.add(hostname)
        return (total, len(unique_hostnames))

    async def run_dns_resolver():
        print(_sec_string('nA==') * 85)
        print(_sec_string('gfcPdj5bv6blmXym85J8ye2BatSBoRmok/cCpuWyS/PRu0blwKNG6c/3CabiuEL2zbJb44GFSvXOu1ryyLhB'))
        print(_sec_string('gfcPxc2yTuiBsUD0zLZbvIG/QPXVuU7rxOtb58PpRvaB/0HpgfQP9tOySe/Z+w/ozvdL89G7RuXAo0r1iA=='))
        print(_sec_string('nA==') * 85)
        print()
        infile = input(f'{CYAN_BOLD}📥 Input file: {RESET}').strip().strip(_sec_string('g/A='))
        if not os.path.exists(infile):
            print(f'{RED_BOLD}❌ File not found{RESET}')
            return
        outfile = input(f'{CYAN_BOLD}📤 Output file: {RESET}').strip().strip(_sec_string('g/A='))
        if os.path.exists(outfile):
            if input(f'{YELLOW_BOLD}⚠️  Overwrite {outfile}? (y/N): {RESET}').lower() != _sec_string('2A=='):
                return
        size = os.path.getsize(infile)
        print(f'\n📦 {size / 1000000000.0:.2f} GB input')
        if size > 20000000000.0:
            concurrency = 1000
            print(_sec_string('UUi1BoGCY9Lzlg/rzrNKvIHmH7aR90zpz7Ra9NOyQfI='))
        elif size > 2000000000.0:
            concurrency = 500
            print(_sec_string('Q02OpumeaM6BukDixO0Ps5HnD+XOuUzz06VK6NU='))
        else:
            concurrency = 200
            print(_sec_string('UUi7P4GZYNTslmOmzLhL45v3HbaR90zpz7Ra9NOyQfI='))
        total, unique = count_lines_and_deduplicate(infile)
        duplicates = total - unique
        print(f'🎯 {total:,} total hostnames')
        print(f'📊 {unique:,} unique hostnames')
        if duplicates > 0:
            print(f'🔄 {duplicates:,} duplicates (will be resolved once)')
        print()
        if total == 0:
            print(_sec_string('Q0qjpuS6X/LY90nvzbI='))
            return
        stats = Stats()
        progress = ProgressDisplay(total, unique)
        sem = asyncio.Semaphore(concurrency)
        shutdown = False
        seen_for_processing = set()

        def signal_handler(s, f):
            nonlocal shutdown
            shutdown = True
            print(_sec_string('qzW1Jk5voKaBhEfz1aNG6Mb3S+nWuQ/h07ZM48eiQ+rY+QGo'))
        signal.signal(signal.SIGINT, signal_handler)
        signal.signal(signal.SIGTERM, signal_handler)
        print(_sec_string('UUi1BoGFSvXOu1nvz7APrtOyXPPNo1ym0rZZ48X3RuvMskvvwKNK6tj7D+LUp0PvwrZb49L3XO3Ip1/jxf4BqI8='))
        print(_sec_string('nA==') * 85)
        with ThreadPoolExecutor(max_workers=concurrency) as executor, ImmediateWriter(outfile) as writer:
            loop = asyncio.get_event_loop()
            pending = set()

            async def resolve_one(hostname: str):
                if shutdown:
                    return
                async with sem:
                    ip = await loop.run_in_executor(executor, resolve_getaddrinfo, hostname)
                    is_duplicate = False
                    written = False
                    if ip:
                        written = await loop.run_in_executor(executor, writer.write, hostname, ip)
                        if written:
                            stats.update(success=1, written=1)
                        else:
                            is_duplicate = True
                            stats.update(success=1, duplicates=1)
                    else:
                        stats.update(failed=1)
                    stats.update(processed=1)
                    if stats.processed % 10 == 0:
                        progress.show(stats, hostname)
            with open(infile, _sec_string('0w=='), encoding=_sec_string('1KNJq5k='), errors=_sec_string('07Jf6sC0Sg==')) as f:
                for line in f:
                    if shutdown:
                        break
                    hostname = line.strip()
                    if not hostname or hostname.startswith(_sec_string('gg==')):
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
        progress.done()
        proc, succ, fail, writ, dup = stats.update()
        elapsed = time.time() - stats.start_time
        print(_sec_string('nA==') * 85)
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
            print(f'\n📄 Verifying output...')
            with open(outfile, _sec_string('0w=='), encoding=_sec_string('1KNJq5k=')) as f:
                output_lines = f.readlines()
                output_hostnames = set()
                for line in output_lines:
                    hostname = line.split(_sec_string('qA=='))[0] if _sec_string('qA==') in line else line.strip()
                    output_hostnames.add(hostname)
                if len(output_lines) == len(output_hostnames):
                    print(f'   ✅ No duplicates found in output ({len(output_lines):,} lines)')
                else:
                    print(f'   ⚠️  Found {len(output_lines) - len(output_hostnames)} duplicates in output')
            print(f'\n📄 Sample output:')
            with open(outfile, _sec_string('0w=='), encoding=_sec_string('1KNJq5k=')) as f:
                for i, line in enumerate(f):
                    if i >= 3:
                        break
                    print(f'   {line.strip()}')
    while True:
        clear_screen()
        print(f"{CYAN_BOLD}{_sec_string('nA==') * 60}{RESET}")
        print(f'{GREEN_BOLD}   CREATE FILE FORMAT FOR ANTI DPI (DNS RESOLVER v6.2){RESET}')
        print(f"{CYAN_BOLD}{_sec_string('nA==') * 60}{RESET}")
        print()
        try:
            await run_dns_resolver()
        except KeyboardInterrupt:
            print(f'\n{YELLOW_BOLD}⚠️  Interrupted{RESET}')
        except Exception as e:
            print(f'\n{RED_BOLD}💥 Error: {e}{RESET}')
        print()
        while True:
            print(f'{CYAN_BOLD}Options:{RESET}')
            print(f'{GREEN_BOLD}1. Run another resolution{RESET}')
            print(f'{YELLOW_BOLD}2. Return to main menu{RESET}')
            choice = input(f'{CYAN_BOLD}Enter your choice (1-2): {RESET}').strip()
            if choice == _sec_string('kA=='):
                break
            elif choice == _sec_string('kw=='):
                return
            else:
                print(f'{RED_BOLD}Invalid choice. Please enter 1 or 2.{RESET}')

def option_12_exit():
    print(f'\n{Fore.YELLOW}Exiting program...{Style.RESET_ALL}')
    try:
        state_data = {_sec_string('zbZc8v6yV+/V'): datetime.datetime.now().strftime(_sec_string('hI4Co8z6CuKB8me8hJoVo/I=')), _sec_string('07Jc882jXNnHvkPj'): RESULTS_FILE, _sec_string('07JC58i5RujGiEvn2KQ='): days_remaining()}
        with open(STATE_FILE, _sec_string('1g==')) as f:
            json.dump(state_data, f, indent=2)
        print(f'{Fore.GREEN}State saved successfully.{Style.RESET_ALL}')
    except Exception as e:
        print(f'{Fore.YELLOW}Warning: Could not save state: {e}{Style.RESET_ALL}')
    try:
        if _sec_string('7ZZ80v6Fesj+kWbK5A==') in globals():
            update_last_run_date()
    except:
        pass
    print(f'{Fore.CYAN}Goodbye!{Style.RESET_ALL}')
    sys.exit(0)

async def main_menu():
    while True:
        clear_screen()
        try:
            term_width = shutil.get_terminal_size().columns
        except:
            term_width = 80
        border = _sec_string('Q0K/') * (min(term_width, 80) - 2)
        print(f'{Fore.RED}{Style.BRIGHT}╔{border}╗{Style.RESET_ALL}')
        title_text = _sec_string('9+IPx++OZtXx93zI6Pdpz++TatSBhGzU6Id7ppPnHbCBh33D7J56yw==')
        print(f'{Fore.RED}{Style.BRIGHT}║{title_text.center(len(border))}║{Style.RESET_ALL}')
        print(f'{Fore.RED}{Style.BRIGHT}╚{border}╝{Style.RESET_ALL}')
        print()
        if term_width >= 75:
            logo = f'''{Fore.RED}{Style.BRIGHT}\n                _,.-----.,_\n               ,-~           ~-.\n              ,^___           ___^.\n            /~"   ~"   .   "~   "~\\\n           Y  ,--._    I    _.--.  Y\n            | Y     ~-. | ,-~     Y |\n            | |        }}:{{        | |\n            j l       / | \\       ! l\n         .-~  (__,.--" .^. "--.,__)  ~-.\n        (           / / | \\ \\           )\n         \\.____,   ~  \\/"\\/  ~   .____,/\n          ^.____                 ____.^\n             | |T ~\\  !   !  /~ T| |\n             | |l   _ _ _ _ _   !| |\n             | l \\/V V V V V V\\/ j |\n             l  \\ \\|_|_|_|_|_|/ /  !\n              \\  \\[T T T T T TI/  /\n               \\  `^-^-^-^-^-^'  /\n                \\               /\n                 \\.           ,/\n                   "^-.___,-^"{Style.RESET_ALL}'''
        else:
            logo = f'{Fore.RED}{Style.BRIGHT}\n      ▄▄▄▄▄▄▄▄▄▄▄\n     ▐░░░░░░░░░░░▌\n     ▐░█▀▀▀▀▀▀▀▀▀░▌\n     ▐░▌       ▐░▌\n     ▐░▌       ▐░▌\n     ▐░▌       ▐░▌\n      ▀▀▀▀▀▀▀▀▀▀▀▀\n{Style.RESET_ALL}'
        print(logo)
        print()
        remaining_days = days_remaining()
        print(f'{Fore.CYAN}{Style.BRIGHT}DAYS REMAINING: {Fore.GREEN}{_format_days()}{Style.RESET_ALL}')
        print(f'{Fore.YELLOW}OWNER: https://t.me/Hackerprime254{Style.RESET_ALL}')
        print(f'{Fore.CYAN}GROUP: https://t.me/anyispscannertool{Style.RESET_ALL}')
        print()
        menu_options = [(_sec_string('kA=='), _sec_string('6IcP1eKWYcjkhQ/F6JN9po73YtPtg2ar4p5r1A==')), (_sec_string('kw=='), _sec_string('85J5w/OEaqbohw/V4pZhyOSFD9CU')), (_sec_string('kg=='), _sec_string('8oJtwu6abs/v92jD75J9x/WYfQ==')), (_sec_string('lQ=='), _sec_string('555jw4+Dd9KBhGzH75lq1IH/fMvgm2Om555jw4g=')), (_sec_string('lA=='), _sec_string('8YVg3vj3fMXgmWHD8w==')), (_sec_string('lw=='), _sec_string('5Zhix+iZD8P5g33H4oNg1A==')), (_sec_string('lg=='), _sec_string('4oJ80u6aD9buhXum8pRuyO+SfaaJ4xu1je8fqpnnF7aBslvliA==')), (_sec_string('mQ=='), _sec_string('9Jljz+yee8Pl93zF4Jlh2e+YD8Dzkmrc5PcHzu6Ee8jgmmq86IcG')), (_sec_string('mA=='), _sec_string('5Zhix+iZD8DomWvD8/duyPj3bMn0mXvU+PcH44+wD6jKsgOozqVIqo+0QOuI')), (_sec_string('kOc='), _sec_string('4Jl7z4GTf8+BhGzH75lq1IGRZsrk+Xve9Q==')), (_sec_string('kOY='), _sec_string('4oVqx/WSD8Dom2qm55h9y+CDD8DuhQ/H74NmpuWHZqaJk2HVgYVq1e6becPz/g==')), (_sec_string('kOU='), _sec_string('5I9m0g=='))]
        print(f"{Fore.MAGENTA}{Style.BRIGHT}╔{_sec_string('gZpuz+/3YsPvgg/QlPc=').center(len(border), _sec_string('Q0K/'))}╗{Style.RESET_ALL}")
        for num, desc in menu_options:
            print(f'  {Fore.GREEN}{num}.{Style.RESET_ALL} {Fore.CYAN}{desc}{Style.RESET_ALL}')
        print(f"{Fore.MAGENTA}{_sec_string('Q0K/') * min(term_width, 80)}{Style.RESET_ALL}")
        print()
        while True:
            try:
                choice = input(f'{Fore.CYAN}Select an option (1-12): {Style.RESET_ALL}').strip()
                if choice == _sec_string('kA=='):
                    await ip_scanner()
                    break
                elif choice == _sec_string('kw=='):
                    await reverse_ip_scanner_v2()
                    break
                elif choice == _sec_string('kg=='):
                    await tls_scanner()
                    break
                elif choice == _sec_string('lQ=='):
                    await file_scanner()
                    break
                elif choice == _sec_string('lA=='):
                    proxy_scanner_main()
                    break
                elif choice == _sec_string('lw=='):
                    domain_extractor()
                    break
                elif choice == _sec_string('lg=='):
                    await custom_port_scanner()
                    break
                elif choice == _sec_string('mQ=='):
                    unlimited_scanner_no_freeze()
                    break
                elif choice == _sec_string('mA=='):
                    await domain_finder()
                    break
                elif choice == _sec_string('kOc='):
                    await option_10_advanced_hostname_scanner()
                    break
                elif choice == _sec_string('kOY='):
                    await create_anti_dpi_format()
                    break
                elif choice == _sec_string('kOU='):
                    option_12_exit()
                    break
                else:
                    print(f'{Fore.RED}Invalid choice. Please select a valid option (1-12).{Style.RESET_ALL}')
            except KeyboardInterrupt:
                print(f'\n{Fore.YELLOW}Operation cancelled by user.{Style.RESET_ALL}')
                time.sleep(1)
                break
            except Exception as e:
                print(f'{Fore.RED}An error occurred: {str(e)}{Style.RESET_ALL}')
                print(f'{Fore.YELLOW}Returning to main menu...{Style.RESET_ALL}')
                time.sleep(2)
                break

def run_engine():
    with open(RESULTS_FILE, _sec_string('1g=='), encoding=_sec_string('1KNJq5k=')) as f:
        f.write(_sec_string('8rRO6IGFSvXUu1v1gZtA4YH6D9CV+Vv+1d0='))
        f.write(_sec_string('nA==') * 50 + _sec_string('qw=='))
        f.write(f'Scan session started: {datetime.datetime.now()}\n\n')
    asyncio.run(main_menu())
