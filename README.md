# 🔍 Decipher

> **Errors in plain English.**

Part of the [ADHDeveloper Toolkit](https://github.com/phoenixsoftwebbrighton/adhddeveloper-toolkit) — CLI tools for developers whose brains work differently.

[![License: MIT](https://img.shields.io/badge/License-MIT-amber.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-amber.svg)](https://www.python.org/downloads/)

---

## 🤔 What is it?

You get an error. It's written in machine language. You have no idea what it means.

Decipher translates it into plain English — what it means, why it happened, and exactly how to fix it. No Stack Overflow required.

---

## ⚡ Quick Start

```bash
# Install dependency
pip install rich

# Run Decipher
python3 decipher.py
```

Add an alias to your shell for instant access:

```bash
echo 'alias decipher="python3 ~/decipher/decipher.py"' >> ~/.zshrc
source ~/.zshrc

# Now just type:
decipher
```

---

## 🛠️ How it works

```bash
$ decipher

Paste error here: Permission denied (publickey)

╭─── 🔍 Decipher knows this one ───╮
│ What this means:                  │
│   Wrong username — the system is  │
│   trying to log in as the wrong   │
│   person.                         │
│                                   │
│ How to fix it:                    │
│   1. Check your SSH config        │
│   2. Specify the right username   │
│   3. Try: ssh -u YOUR_USERNAME    │
╰───────────────────────────────────╯
```

---

## 🌍 Community Database

When Decipher doesn't recognise an error, it asks if you want to submit it to the community queue. Every submission makes Decipher smarter for the next person.

```
✅ Known error    → instant translation
❓ Unknown error  → submit to community queue
📬 Submitted      → helps the next developer
```

---

## 🔧 Errors Currently Covered

- SSH connection errors
- Git errors (push, pull, auth, repo not found)
- Ansible/YAML errors
- Docker errors
- Disk space errors
- DNS/network errors
- Python errors
- ...and growing every day

---

## 🎨 Design Philosophy

- **No jargon** — every translation in plain English
- **Community powered** — gets smarter with every user
- **Works offline** — local database, nothing phones home
- **Integrated with GitSpeak** — errors translated automatically

---

## 📄 License

MIT — free forever.

---

*Part of the ADHDeveloper Toolkit — made for brains that work differently* 🧠
