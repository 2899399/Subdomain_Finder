# ============================================
#   Subdomain Finder
#   Beginner Cybersecurity / Recon Tool
# ============================================

import urllib.request
import socket
import datetime
import os

# Terminal colors
RED    = "\033[91m"
YELLOW = "\033[93m"
GREEN  = "\033[92m"
CYAN   = "\033[96m"
BOLD   = "\033[1m"
RESET  = "\033[0m"

# Common subdomains wordlist
WORDLIST = [
    "www", "mail", "ftp", "admin", "webmail", "smtp", "pop", "ns1", "ns2",
    "blog", "dev", "staging", "api", "app", "cdn", "cpanel", "shop", "store",
    "portal", "forum", "support", "help", "m", "mobile", "test", "beta",
    "vpn", "secure", "login", "dashboard", "status", "docs", "wiki",
    "media", "images", "img", "static", "assets", "remote", "cloud",
    "git", "gitlab", "jenkins", "jira", "confluence", "monitor",
    "mx", "mx1", "mx2", "email", "smtp2", "imap", "pop3",
    "server", "server1", "server2", "host", "host1", "web", "web1", "web2",
    "old", "new", "demo", "preview", "v1", "v2", "internal", "intranet"
]


def check_subdomain(subdomain, domain):
    """
    Check if a subdomain exists by resolving its DNS.
    Returns IP if found, None if not.
    """
    full = f"{subdomain}.{domain}"
    try:
        ip = socket.gethostbyname(full)
        return full, ip
    except socket.gaierror:
        return None, None


def save_results(domain, found):
    """Save found subdomains to a text file."""
    filename = f"{domain}_subdomains.txt"
    with open(filename, "w") as f:
        f.write(f"Subdomain Finder Results\n")
        f.write(f"Domain  : {domain}\n")
        f.write(f"Scanned : {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Found   : {len(found)} subdomains\n")
        f.write("=" * 45 + "\n\n")
        for sub, ip in found:
            f.write(f"[+] {sub:<35} -> {ip}\n")
    return filename


def main():
    print(f"\n{CYAN}{BOLD}{'='*50}")
    print("        🔍 Subdomain Finder")
    print(f"        Recon & Enumeration Tool")
    print(f"{'='*50}{RESET}")

    print(f"\n{YELLOW}⚠️  For educational and authorized use only!{RESET}\n")

    domain = input(f"{BOLD}Enter target domain (e.g. example.com): {RESET}").strip()

    # Remove http/https if user pastes full URL
    domain = domain.replace("https://", "").replace("http://", "").replace("www.", "").strip("/")

    if not domain:
        print(f"{RED}No domain entered. Exiting.{RESET}")
        return

    print(f"\n{CYAN}🎯 Target  : {domain}")
    print(f"📋 Wordlist: {len(WORDLIST)} subdomains{RESET}")
    print(f"\n{BOLD}Starting scan...{RESET}\n")
    print("-" * 50)

    found = []
    total = len(WORDLIST)

    for i, word in enumerate(WORDLIST, 1):
        # Progress indicator
        print(f"\r{YELLOW}[{i}/{total}] Checking: {word}.{domain}...{RESET}    ", end="", flush=True)

        sub, ip = check_subdomain(word, domain)

        if sub:
            found.append((sub, ip))
            print(f"\r{GREEN}[+] FOUND  : {sub:<35} -> {ip}{RESET}          ")

    print(f"\r{' '*60}\r", end="")  # Clear last progress line
    print("-" * 50)

    # Summary
    print(f"\n{BOLD}📊 Scan Complete!{RESET}")
    print(f"  Total Checked : {total}")
    print(f"  {GREEN}Subdomains Found : {len(found)}{RESET}")

    if found:
        filename = save_results(domain, found)
        print(f"\n{CYAN}💾 Results saved to: {filename}{RESET}")
        print(f"\n{BOLD}Found Subdomains:{RESET}")
        for sub, ip in found:
            print(f"  {GREEN}✅ {sub:<35} -> {ip}{RESET}")
    else:
        print(f"\n{RED}No subdomains found for {domain}{RESET}")

    print(f"\n{CYAN}{'='*50}{RESET}\n")


if __name__ == "__main__":
    main()
