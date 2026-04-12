# 🚩 Pain Point Log: The "Why" Behind the Toolkit

This log documents the specific technical and psychological barriers encountered during the build of the homelab. These points serve as the requirements for the Guided Formatter Toolkit.

## 1. The "Invisible" Syntax Wall (YAML/Ansible)
- **The Symptom:** Errors like `Colons in unquoted values must be followed by a non-space character` or `did not find expected key`.
- **The Pain:** The error tells you a "column number" (e.g., Column 10), but it doesn't show you a visual marker of *where* the space is. 
- **The Need:** A tool that highlights the exact character causing the break and explains it in plain English (e.g., "You have a hidden space after this colon").

## 2. The "Wrong Identity" Loop (SSH/Ansible)
- **The Symptom:** `Permission denied (publickey, password)` despite having the right password.
- **The Pain:** The system assumes the local username (e.g., 'phoenix') is the server username. The error doesn't explicitly say "You are using the wrong username"; it just says "Access Denied."
- **The Need:** A pre-flight check that asks: "Are you sure your local username is the same as your server username?"

## 3. The "Invisible Resource" Gap (Disk/RAM)
- **The Symptom:** `Internal Server Error` or apps crashing without explanation.
- **The Pain:** The app tells you it's broken, but it doesn't tell you *why* (e.g., the disk is 100% full). The user spends hours fixing the app when the problem is actually the hardware.
- **The Need:** A "Health First" check that scans Disk and RAM before attempting to diagnose software errors.

## 4. The "Passphrase vs. Password" Confusion
- **The Symptom:** Entering a passphrase during `ssh-keygen` and then being unable to automate the connection.
- **The Pain:** The prompt is ambiguous. "Passphrase" sounds like "Password," leading the user to add a security layer that actually blocks the automation they are trying to build.
- **The Need:** Clear, bold warnings in the tool: "STOP: Adding a passphrase here will break your automation. Leave this blank for a 'VIP Pass'."

## 5. The "LVM" Space Paradox
- **The Symptom:** Creating a 20GB VM but only seeing 10GB available in Ubuntu.
- **The Pain:** The OS does not automatically use the space provided by the hypervisor. This is a "hidden" setting that isn't mentioned in basic install guides.
- **The Need:** An automated "Disk Expansion" check that tells the user: "Your VM has 20GB, but Ubuntu is only using 10GB. Click here to expand."

## 6. The "Wall of Text" Overwhelm
- **The Symptom:** Large logs with mixed colors and technical jargon.
- **The Pain:** When an error occurs, the most important information is buried in the middle of 50 lines of text.
- **The Need:** An "Error Summarizer" that strips away the jargon and gives a 1-sentence explanation and a 3-step fix.