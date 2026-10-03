#!/data/data/com.termux/files/usr/bin/bash
set -e

cd "$(dirname "$0")"

if command -v python >/dev/null 2>&1; then
    PYTHON=python
elif command -v python3 >/dev/null 2>&1; then
    PYTHON=python3
else
    echo "[-] Python is not installed. Run ./install.sh first."
    exit 1
fi

echo "[+] Starting scanner..."
exec "$PYTHON" scanner.py "$@"
