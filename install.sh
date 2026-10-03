#!/data/data/com.termux/files/usr/bin/bash
set -e

echo "[+] Updating package list..."
pkg update -y

echo "[+] Installing Python..."
pkg install -y python

echo "[+] Upgrading pip..."
python -m pip install --upgrade pip

if [ -f requirements.txt ]; then
    echo "[+] Installing Python dependencies..."
    python -m pip install -r requirements.txt
else
    echo "[+] No requirements.txt found; skipping dependency install."
fi

echo "[+] Installation complete."
