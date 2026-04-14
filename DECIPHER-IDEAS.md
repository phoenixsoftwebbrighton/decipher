# 💡 Decipher — Future Ideas Log
> Dump ideas here as they come. No wrong answers. No pressure to build them now.
> These are the seeds for what Decipher becomes next.

---

## 💡 Idea 1 — Screenshot Error Submission
**Date:** April 2026
**Where it came from:** Ash noticed that sending screenshots gives developers a view of exactly what the user sees on their screen

**The idea:**
Instead of users typing or pasting an error, they take a screenshot and submit it directly. Decipher reads the error from the image automatically using OCR and either matches it or saves it to the unknown queue.

**Why this is powerful:**
- Removes typing friction entirely — massive win for neurodivergent users
- Captures full context, not just the error line
- Screenshot queue becomes a goldmine of real-world error data
- Developers see exactly what the user saw

**What it would need:** pytesseract (OCR), web interface, image upload, admin review view
**Priority:** High — potential killer feature

---

## 💡 Idea 2 — Submission Threshold Notifications
**Date:** April 2026
**Where it came from:** Ash — "what if we set up a ping that lets us know after so many errors have been uploaded"

**The idea:**
When the unknown_errors.json queue reaches a certain number of pending submissions, Decipher automatically sends a notification to the developer (Ash) so they know it's time to review and add new errors to the database.

**How it would work:**
- Set a threshold — e.g. every 10 new submissions triggers a ping
- Notification options (cheapest first):
  1. **Email** — simple SMTP notification, free
  2. **Ntfy.sh** — free self-hosted push notification, works on phone too
  3. **Slack/Discord webhook** — one line of code, instant message to a channel
  4. **Uptime Kuma** — already in your stack, can be repurposed for this

**Why this matters:**
As users grow, you can't manually check the queue every day. This makes the database grow itself — users submit, you get pinged, you review and add, everyone benefits faster.

**What it would need:** A background check script that counts pending entries and fires a notification when the threshold is hit
**Difficulty:** Easy — this is maybe 20 lines of Python
**Priority:** Medium — build when user count starts growing

---

## 💡 Idea 3 — Community Error Database
**Date:** April 2026

Unknown errors submitted across all installations feed into a shared database. When Decipher learns from one user, everyone benefits.

---

## 💡 Idea 4 — "Health First" Pre-Check
**Date:** April 2026

Before diagnosing, run a quick health check — disk full? RAM maxed? Service running? Stops users debugging code when the real problem is hardware.

---

## 💡 Idea 5 — Error Severity Rating
**Date:** April 2026

Every error gets a label: 🟢 Minor / 🟡 Medium / 🔴 Critical / ⚫ Unknown

---

## 💡 Idea 6 — Context Memory
**Date:** April 2026

Decipher remembers what the user was working on when they hit errors. Over time it spots patterns and flags them proactively.

---

*Add ideas here whenever they come — even half-formed ones.*
*The best ideas usually start as a sentence at 4am.*
