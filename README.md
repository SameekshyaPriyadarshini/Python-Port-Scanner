# 🔎 Python Port Scanner

A lightweight TCP Port Scanner built in Python using the socket module.

## 📌 Overview

This project scans a target host for commonly used TCP ports and identifies which ports are open. It was built to understand TCP connections, socket programming, and basic network reconnaissance.

---

## 🚀 Features

- Scan multiple common TCP ports
- Detect open ports
- Display total scan time
- User-friendly terminal output
- Beginner-friendly implementation

---

## 🛠 Technologies Used

- Python 3
- Socket Module
- TCP Networking

---

## 📂 Ports Scanned

| Service | Port |
|---------|------|
| FTP | 21 |
| SSH | 22 |
| Telnet | 23 |
| SMTP | 25 |
| DNS | 53 |
| HTTP | 80 |
| POP3 | 110 |
| NetBIOS | 139 |
| IMAP | 143 |
| HTTPS | 443 |
| SMB | 445 |
| RDP | 3389 |

---

## ▶️ How to Run

```bash
python scanner_v2.py
```

---

## 📸 Sample Output

```text
========================================
Python Port Scanner V2
========================================

Scanning scanme.nmap.org...

[+] Port 21 (FTP) is OPEN
[+] Port 22 (SSH) is OPEN
[+] Port 80 (HTTP) is OPEN

========================================
Scan Complete
========================================

Open Ports Found: 3

Time Taken: 2.34 seconds
```

---

## 📚 What I Learned

- Python Socket Programming
- TCP Handshake
- Common Network Ports
- Network Reconnaissance
- Git & GitHub Workflow

---

## 🔮 Future Improvements

- Multithreading
- Custom Port Range
- Banner Grabbing
- Service Detection
- Save Scan Results to CSV
- GUI Version