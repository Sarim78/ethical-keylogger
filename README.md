# 🔐 Ethical Keylogger

> **Educational use only — local machine, explicit consent required.**  
> A Python-based keystroke logger built to understand how malware captures input, designed for cybersecurity learning.

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
├── keylogger.py        # Main keylogger — listens for keypresses and saves to file
├── analyze_log.py      # Log parser — prints character and word stats
├── requirements.txt    # Python dependencies
├── .gitignore          # Excludes log file from version control
└── README.md           # You're reading it
```

> ⚠️ `log.txt` is excluded from version control via `.gitignore`.  
> **Never commit captured keystroke data to a public repository.**

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation
```bash
# 1. Clone the repository
git clone https://github.com/Sarim78/ethical-keylogger.git
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
1. Start capturing every keypress immediately
2. Save each keystroke to `log.txt` in real time
3. **Press `ESC` to stop the session**

### Analyzing the Log
```bash
python analyze_log.py
```

Outputs:
- Total characters typed
- Top 10 most-typed characters
- Top 10 most-typed words

---

## 📊 Sample Output

**Log file (`log.txt`):**
```
Hello world [enter] This is a test [backspace] [backspace]
```

**Analyzer output:**
```
Total characters typed: 38

Top 10 keys:
  'e' — 4 times
  's' — 3 times
  't' — 3 times

Top 10 words:
  'this' — 1 times
  'is' — 1 times
  'a' — 1 times
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
- `collections`, `re` — Python standard library
