# 🔍 Subdomain Finder

A Python-based subdomain enumeration tool for reconnaissance and security testing. It discovers active subdomains of a target domain using DNS resolution and a built-in wordlist.

## 🚀 Features
- Scans 60+ common subdomains automatically
- Uses DNS resolution to verify if subdomain is live
- Shows real-time progress during scan
- Displays IP address of each found subdomain
- Saves results to a `.txt` file automatically
- No external libraries required

## 🛠️ Requirements
- Python 3.x
- Internet connection
- No pip installs needed (uses built-in modules only)

## ▶️ How to Run

```bash
python subdomain_finder.py
```

Then enter a domain when prompted:
```
Enter target domain: example.com
```

## 📸 Example Output

```
==================================================
        🔍 Subdomain Finder
        Recon & Enumeration Tool
==================================================

🎯 Target  : example.com
📋 Wordlist: 60 subdomains

--------------------------------------------------
[+] FOUND  : www.example.com              -> 93.184.216.34
[+] FOUND  : mail.example.com             -> 93.184.216.50
--------------------------------------------------

📊 Scan Complete!
  Total Checked    : 60
  Subdomains Found : 2

💾 Results saved to: example.com_subdomains.txt
```

## 🧠 What I Learned
- DNS resolution using Python's `socket` module
- Subdomain enumeration techniques used in real pentesting
- Building wordlist-based recon tools
- File handling and result saving in Python
- Real-time terminal progress display

## ⚠️ Disclaimer
This tool is intended for **educational purposes only**.  
Only use it on domains you **own** or have **explicit permission** to test.  
Unauthorized scanning may be illegal in your country.

## 📚 Tech Used
- Python 3.x
- `socket` module (DNS resolution)
- `urllib` module
- `datetime` module

## 👨‍💻 Author
Parveen Kumar

---
⭐ If you found this useful, give it a star!
