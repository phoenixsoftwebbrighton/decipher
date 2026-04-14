# 💡 Decipher — Future Ideas Log
> Dump ideas here as they come. No wrong answers. No pressure to build them now.
> These are the seeds for what Decipher becomes next.

---

## 💡 Idea 1 — Screenshot Error Submission
**Date:** April 2026
**Where it came from:** Ash noticed that sending screenshots gives developers a view of exactly what the user sees on their screen

**The idea:**
Instead of users typing or pasting an error, they take a screenshot of their screen and submit it directly to Decipher. Decipher reads the error from the image automatically using OCR (optical character recognition) and either:
- Matches it to a known error in the database
- OR saves it to the unknown errors queue with the full screenshot attached

**Why this is powerful:**
- Removes typing friction entirely — massive win for neurodivergent users
- Captures the FULL context (not just the error line, but everything around it)
- Screenshot queue becomes a goldmine of real-world error data
- Developers can see exactly what the user saw — no guessing

**What it would need:**
- OCR library (pytesseract or similar) to read text from images
- Screenshot upload button in the web interface
- Image stored alongside the unknown error entry
- Admin view to review screenshots and add them to the database

**Difficulty:** Medium — needs web interface first, then image upload, then OCR
**Priority:** High — this could be the killer feature that makes Decipher different from everything else

---

## 💡 Idea 2 — Community Error Database
**Date:** April 2026

**The idea:**
Unknown errors submitted by users across all installations feed into a shared database. When Decipher learns a new error from one user, everyone benefits.

**What it would need:**
- Central server to receive submissions (could be a simple API)
- Review system so bad/spam submissions don't get added automatically
- Version system so the database can be updated and pushed to all users

---

## 💡 Idea 3 — "Health First" Pre-Check
**Date:** April 2026
**From:** PAIN_POINTS.md item 3

**The idea:**
Before Decipher even tries to diagnose an error, it runs a quick health check:
- Is your disk full? (df -h)
- Is your RAM maxed out? (free -h)
- Is the relevant service actually running?

90% of mystery errors are caused by one of those three things.

**Why this matters:**
Stops users spending hours debugging code when the real problem is the disk is full.

---

## 💡 Idea 4 — Error Severity Rating
**Date:** April 2026

**The idea:**
Every error gets a severity label so users know how worried to be:
- 🟢 Minor — easy fix, 2 minutes
- 🟡 Medium — needs attention, might take a while
- 🔴 Critical — stop what you're doing, fix this first
- ⚫ Unknown — we haven't seen this before

---

## 💡 Idea 5 — "What Were You Doing?" Context Memory
**Date:** April 2026

**The idea:**
Decipher remembers what the user was working on when they hit an error. Over time it spots patterns — "every time you run Ansible against this server, you get this error" — and flags them proactively.

---

*Add ideas here whenever they come — even half-formed ones.*
*The best ideas usually start as a sentence at 4am.*
