# 🔍 Decipher

---

> **"Built for the developers who kept being told the problem was them. It wasn't."**

> **Decipher is part of a wider project to build tech tools for neurodivergent people. Finally, built by someone with lived experience.**

For too long, tech tools have been built by people without lived experience of what it feels like to be neurodivergent and lost in a wall of error messages. Decipher exists because that changes now. If you've ever stared at a terminal and felt completely alone — this was built for you, by someone who knows exactly how that feels.

---

## What is Decipher?

Error messages are written for machines — not humans. They're cryptic, cold, and often point at the wrong thing entirely.

Decipher translates those robot messages into plain English. It tells you what the error actually means, and gives you clear step-by-step instructions to fix it.

**No jargon. No assumptions. No making you feel stupid.**

---

## Who is it for?

Decipher was built by a neurodivergent developer, for neurodivergent developers — and anyone else who's ever felt left behind by tools that weren't designed for their brain.

It's especially useful if you:
- Are just getting started with Linux, Docker, Ansible, or Git
- Have ADHD or Autism and find walls of technical text overwhelming
- Keep hitting the same errors and can't remember how you fixed them last time
- Want a tool that treats you like a human being

---

## Current Error Database

Decipher currently knows how to translate **14 errors** across the following categories:

| Category | Errors covered |
|---|---|
| SSH | Wrong username, passphrase traps, keygen mistakes |
| Ansible | Inventory format, sudo issues, wrong module parameters |
| YAML | Colon spacing, indentation problems |
| Docker | Wrong parameter names |
| Git | Repository not found, authentication failed, refspec errors |
| Disk | Full disk, LVM not expanded, no space left |
| Network | Connection refused, hostname not found |

Every error entry contains:
- **The robot error** — exactly what the terminal shows you
- **The human truth** — what it actually means in plain English
- **Fix steps** — numbered, clear, no assumptions

---

## How to run it

**Requirements:** Python 3 and the `rich` library

```bash
pip install rich
```

**Run Decipher:**
```bash
cd decipher
python3 translator.py
```

**Paste your error when prompted:**
```
Paste error here: Permission denied (publickey,password)
```

**Decipher responds:**
```
✅ Translation Found

What this means:
  The system is trying to log in with the wrong username —
  it's using your Mac's username instead of your server username.

How to fix it:
  1. Check what username your server expects (e.g. ubuntu or phoenix)
  2. Add ansible_user=YOUR_USERNAME to your inventory file
  3. Or use the -u flag: ansible-playbook playbook.yml -u ubuntu
```

---

## What happens when Decipher doesn't recognise an error?

If you paste an error it hasn't seen before, Decipher asks you two questions:

1. What were you trying to do when this happened?
2. Which tool is this error from?

Your answer gets saved to a queue of new errors waiting to be added to the database. Every submission makes Decipher smarter for the next person.

---

## Project structure

```
decipher/
├── translator.py          ← the main app
├── errors.json            ← the error database (human translations live here)
├── unknown_errors.json    ← queue of unrecognised errors submitted by users
├── config.json            ← user settings (local vs cloud mode)
├── PAIN_POINTS.md         ← the real problems that inspired this tool
├── DECIPHER-IDEAS.md      ← future features and ideas log
└── README.md              ← you are here
```

---

## Roadmap

- [ ] Web interface — so anyone can use it without touching a terminal
- [ ] Screenshot submission — paste a screenshot, Decipher reads the error from the image
- [ ] Submission threshold notifications — get pinged when enough new errors are in the queue
- [ ] AI-assisted translation — use local AI (Ollama) to auto-generate translations for unknown errors
- [ ] Community database — submissions from all users feed one shared database
- [ ] Health check — scan disk, RAM and services before diagnosing software errors
- [ ] Error severity ratings — 🟢 Minor / 🟡 Medium / 🔴 Critical

---

## Contributing

Found an error that Decipher doesn't know yet? Just run the tool and it'll ask you to submit it. That's all you need to do.

If you want to add translations directly, open `errors.json` and follow the existing format:

```json
{
  "id": "unique_id",
  "robot_error": "exact text from the terminal",
  "human_truth": "what it actually means in plain English",
  "fix_steps": [
    "Step 1",
    "Step 2",
    "Step 3"
  ],
  "tags": ["category", "tool"]
}
```

---

## Built by

Ash Baguley — Brighton, UK

Built from 3 years of hitting walls, getting frustrated, figuring it out, and deciding that nobody else should have to feel as lost as I did. If this tool helps even one person feel less alone in front of a terminal — it was worth every hour.
