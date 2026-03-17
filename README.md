# 🔐 Ethical Keylogger

> **Educational use only — local machine, explicit consent required.**  
> A Python-based keystroke logger built to understand how malware captures input, designed for cybersecurity project
---

## 📌 Overview

This project simulates a basic keylogger in a **controlled, transparent, and ethical environment**. The goal is not to create malware — it's to understand the mechanics behind one of the most common attack vectors in the wild, so you can **defend against it**.

Understanding how keyloggers work is a fundamental skill for:
- 🛡️ SOC Analysts monitoring endpoint behaviour
- 🔍 Malware Analysts reverse-engineering threats
- 🧪 Penetration Testers assessing device security
- 📚 Cybersecurity Students learning offensive fundamentals to build defensive intuition

---

## 📁 Project Structure

```
ethical-keylogger/
│
├── keylogger.py        # Main keylogger — starts the listener session
├── analyze_log.py      # Log parser — generates keystroke statistics
├── requirements.txt    # Python dependencies
├── .gitignore          # Excludes log files from version control
└── README.md           # You're reading it
```

> ⚠️ The `logs/` directory is excluded from version control via `.gitignore`.  
> **Never commit captured keystroke data to a public repository.**

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/your-username/ethical-keylogger.git
cd ethical-keylogger

# 2. (Recommended) Create a virtual environment
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows

# 3. Install dependencies
pip install -r requirements.txt
```

### Running the Keylogger

```bash
python keylogger.py
```

The logger will:
1. Create a `logs/keylog.txt` file automatically
2. Begin capturing keystrokes with timestamps
3. Auto-save every 60 seconds (configurable)
4. **Press `ESC` to stop the session gracefully**

### Analyzing the Log

```bash
python analyze_log.py
```

Outputs a full report including:
- Total keystroke count
- Top 10 most-typed characters
- Top 10 most-typed words
- Special key breakdown (ENTER, BACKSPACE, SHIFT, etc.)
- Captured text preview

---

## ⚙️ Configuration

All settings are at the top of `keylogger.py`:

```python
LOG_DIR         = "logs"       # Directory to store logs
LOG_FILE        = "logs/keylog.txt"
REPORT_INTERVAL = 60           # Auto-save every N seconds (None = disable)
MAX_BUFFER_SIZE = 500          # Flush after N keystrokes
SESSION_TIMEOUT = None         # Auto-stop after N seconds (None = manual ESC)
```

---

## 📊 Sample Output

**Terminal (live):**
```
============================================================
   ETHICAL KEYLOGGER — Educational Use Only
============================================================
   Log file   : /home/user/ethical-keylogger/logs/keylog.txt
   Started at : 2026-03-16 14:32:01
   Press [ESC] to stop the session.
============================================================

  [14:32:05] Key: H
  [auto-save] 2026-03-16 14:33:01 — 87 keystrokes logged so far.
```

**Log file (`logs/keylog.txt`):**
```
============================================================
  SESSION STARTED
  Timestamp : 2026-03-16 14:32:01
  Platform  : Windows 11
  Python    : 3.11.4
============================================================

Hello world[ENTER]
This is a test[BACKSPACE][BACKSPACE]
```

**Analyzer output:**
```
═══════════════════════════════════════════════════════
   KEYSTROKE ANALYSIS REPORT
═══════════════════════════════════════════════════════
  Total keystrokes logged  : 142
  Printable characters     : 118
  Special key presses      : 24

─── Top 10 Characters ───────────────────────────────
  'e'  ████████████ (12)
  't'  ██████████ (10)
  's'  ████████ (8)
```

---

## 🛡️ Defensive Takeaways

After building this, you'll understand why defenders recommend:

- **Endpoint Detection & Response (EDR)** tools that monitor for suspicious process hooks
- **Application whitelisting** to prevent unauthorized scripts from running
- **Multi-factor authentication (MFA)** so stolen passwords alone aren't enough
- **Privileged Access Workstations (PAWs)** for sensitive administrative tasks
- **Security awareness training** to reduce the risk of phishing-delivered keyloggers

---

## 🛠️ Built With

- [Python 3](https://www.python.org/) — Core language
- [pynput](https://pynput.readthedocs.io/) — Keyboard listener library
- `threading`, `collections`, `datetime` — Python standard library

---

## 🗺️ Roadmap

- [ ] AES-encrypted log output
- [ ] Email-based log delivery simulation (for lab environments)
- [ ] GUI dashboard for log analysis
- [ ] Cross-platform stealth mode toggle (for malware analysis labs)
- [ ] Screenshot capture integration
---
