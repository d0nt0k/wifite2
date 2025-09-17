[![GitHub version](https://img.shields.io/badge/version-2.7.2-informational.svg)](#)
[![GitHub issues](https://img.shields.io/github/issues/kimocoder/wifite2.svg)](https://github.com/kimocoder/wifite2/issues)
[![GitHub forks](https://img.shields.io/github/forks/kimocoder/wifite2.svg)](https://github.com/kimocoder/wifite2/network)
[![GitHub stars](https://img.shields.io/github/stars/kimocoder/wifite2.svg)](https://github.com/kimocoder/wifite2/stargazers)
[![Android Supported](https://img.shields.io/badge/Android-Supported-green.svg)](#)
[![GitHub license](https://img.shields.io/github/license/kimocoder/wifite2.svg)](https://github.com/kimocoder/wifite2/blob/master/LICENSE)


Wifite2 - WPA-Only Edition
=========================

This repo is a **specialized WPA-only version** of [`wifite2`](https://github.com/kimocoder/wifite2), a Python script for auditing wireless networks.

**🔒 WPA-ONLY FOCUS**: This version has been specifically modified to **only support WPA/WPA2/WPA3 attacks**, removing all WEP, WPS, and PMKID functionality for a streamlined, focused approach to WPA security testing.

Wifite runs existing wireless-auditing tools for you. Stop memorizing command arguments & switches!

**This WPA-Only Edition supports:**
1. **WPA/WPA2 Handshake Capture** + offline cracking with Hashcat
2. **WPA3-SAE Support** for modern networks
3. **Streamlined Interface** - No confusing attack type selection
4. **Focused Security Testing** - Only WPA-encrypted networks are targeted

**Removed for Simplicity:**
- ❌ WEP attacks (replay, fragment, chopchop, etc.)
- ❌ WPS attacks (PIN, Pixie-Dust)  
- ❌ PMKID attacks
- ❌ All related command line arguments and configuration options 

Run wifite, select your targets, and Wifite will automatically start trying to capture or crack the password.

Supported Operating Systems
---------------------------
Wifite is designed specifically for the latest version of [**Kali** Linux](https://www.kali.org/). [ParrotSec](https://www.parrotsec.org/) is also supported.

NetHunter (Android) is also widely supported by wifite, but it will require a custom kernel with modules support and various
patches for injection in order to work. Tested on Android 10 (Q), Android 11 (R),  Android 12 (S) and Android 13 (T)

More information regarding [ Android: **NetHunter** ](https://gitlab.com/kalilinux/nethunter) is found there and
you should also take a look at the [ **NetHunter WIKI** ](https://www.kali.org/docs/nethunter/) which is more up to date then [ NetHunter.com ](https://nethunter.com).

Other pen-testing distributions (such as BackBox or Ubuntu) have outdated versions of the tools used by Wifite. Do not expect support unless you are using the latest versions of the *Required Tools*, and also [patched wireless drivers that support injection]().

Required Tools
--------------
First and foremost, you will need a wireless card capable of "Monitor Mode" and packet injection (see [this tutorial for checking if your wireless card is compatible](https://www.aircrack-ng.org/doku.php?id=compatible_cards) and also [this guide](https://en.wikipedia.org/wiki/Wi-Fi_Protected_Setup#Offline_brute-force_attack)). There are many cheap wireless cards that plug into USB available from online stores.

Second, only the latest versions of these programs are supported and must be installed for Wifite to work properly:

**Required for WPA-Only Edition:**

* `python3` (Python 3.11+ recommended)
* [`Iw`](https://wireless.wiki.kernel.org/en/users/documentation/iw): For identifying wireless devices already in Monitor Mode.
* [`Ip`](https://packages.debian.org/buster/net-tools): For starting/stopping wireless devices.
* [`Aircrack-ng`](https://aircrack-ng.org/) suite, includes:
   * [`airmon-ng`](https://tools.kali.org/wireless-attacks/airmon-ng): For enumerating and enabling Monitor Mode on wireless devices.
   * [`aireplay-ng`](https://tools.kali.org/wireless-attacks/aireplay-ng): For deauthenticating clients during handshake capture.
   * [`airodump-ng`](https://tools.kali.org/wireless-attacks/airodump-ng): For target scanning & WPA handshake capture.

**Required for WPA Cracking:**

* [`hashcat`](https://hashcat.net/): For cracking WPA handshakes (primary method)
* [`tshark`](https://www.wireshark.org/docs/man-pages/tshark.html): For handshake validation and analysis

**Optional, but Recommended:**

* [`coWPAtty`](https://tools.kali.org/wireless-attacks/cowpatty): For additional handshake validation
* [`john`](https://www.openwall.com/john): Alternative password cracking tool



Install dependencies
--------------------
Either, do it the proper python way with

```sh
$ python3 -m venv venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt
```

## Download and Install

### **Step 1: Clone the Repository**
```sh
git clone https://github.com/d0nt0k/wifite2.git
cd wifite2
```

### **Step 2: Install Dependencies**
```sh
# Install Python dependencies
pip3 install -r requirements.txt

# Install required system tools (Ubuntu/Debian/Kali)
sudo apt update
sudo apt install aircrack-ng hashcat tshark

# Install required system tools (Arch Linux)
sudo pacman -S aircrack-ng hashcat tshark

# Install required system tools (macOS)
brew install aircrack-ng hashcat tshark
```

### **Step 3: Run Wifite2 WPA-Only**
```sh
# Run directly from the cloned directory
sudo python3 wifite2/wifite/wifite.py

# Or install system-wide first, then run
sudo python3 setup.py install
sudo wifite
```



WPA-Only Feature List
---------------------
* **WPA/WPA2 Handshake Capture** - Automatic 4-way handshake capture with client deauthentication
* **WPA3-SAE Support** - Full support for modern WPA3 networks
* **Hashcat Integration** - Primary cracking engine for WPA handshakes
* **Handshake Validation** - Validates captures against `tshark`, `cowpatty`, and `aircrack-ng`
* **Automatic Decloaking** - Reveals hidden access points during scanning
   * Note: Only works when channel is fixed. Use `-c <channel>`
   * Disable this using `--no-deauths`
* **5GHz Support** - Works with 5GHz wireless cards (via `-5` switch)
* **Handshake Storage** - Saves captured handshakes to `hs/` directory
* **Cracked Password Storage** - Stores results in `cracked.json` with network details
* **Wordlist Cracking** - Easy handshake cracking with `--dict` option
* **Streamlined Interface** - No attack type selection needed, focuses on WPA only

TIP! Use `wifite.py -h -v` for a collection of switches and settings
for your own customization, automation, timers and so on ..

What's New in WPA-Only Edition?
-------------------------------
This specialized version focuses exclusively on WPA security testing:

* **🔒 WPA-Only Focus**
   * Removed all WEP, WPS, and PMKID attack functionality
   * Streamlined interface with no attack type selection needed
   * Only scans and attacks WPA-encrypted networks
* **⚡ Simplified Workflow**
   * No confusing attack type menus
   * Automatic WPA handshake capture and cracking
   * Clean, focused user experience
* **🛠️ Optimized for WPA**
   * Hashcat as primary cracking engine
   * Enhanced WPA3-SAE support
   * Improved handshake validation
* **📦 Reduced Dependencies**
   * No need for WPS tools (reaver, bully)
   * No need for PMKID tools (hcxdumptool, hcxpcapngtool)
   * Minimal tool requirements for WPA testing

What's Removed?
---------------
* **WEP Attacks**: All WEP-related functionality (replay, fragment, chopchop, etc.)
* **WPS Attacks**: PIN attacks, Pixie-Dust attacks, and related tools
* **PMKID Attacks**: PMKID hash capture and cracking
* **Related Arguments**: All WEP, WPS, and PMKID command line options
* **Complex Menus**: No more attack type selection screens

What's Preserved?
-----------------
* **Core WPA Functionality**: All WPA handshake capture and cracking features
* **User Interface**: Same familiar text-based interface
* **Python 3 Support**: Full Python 3.11+ compatibility
* **Educational Value**: Verbose mode shows executed commands
* **Process Management**: Clean process handling without background processes

## Quick Start Guide

### **Basic Usage**
```bash
# 1. Download and setup (one-time)
git clone https://github.com/d0nt0k/wifite2.git
cd wifite2
pip3 install -r requirements.txt

# 2. Run the tool
sudo python3 wifite2/wifite/wifite.py
```

### **Advanced Usage Examples**
```bash
# Attack specific WPA network by BSSID
sudo python3 wifite2/wifite/wifite.py -b AA:BB:CC:DD:EE:FF

# Use custom wordlist for cracking
sudo python3 wifite2/wifite/wifite.py --dict /path/to/wordlist.txt

# Attack specific channel only
sudo python3 wifite2/wifite/wifite.py -c 6

# Attack specific ESSID
sudo python3 wifite2/wifite/wifite.py -e "MyNetwork"

# Show verbose output for debugging
sudo python3 wifite2/wifite/wifite.py -v

# Skip cracking, only capture handshakes
sudo python3 wifite2/wifite/wifite.py --skip-crack
```

Expected Output
---------------
```
  .     .     .    
.´  ·  .     .  ·  `.  wifite2 2.7.2
:  :  : (¯)  :  :  :  a wireless auditor by derv82
`.  ·  ` /¯\ ´  ·  .´  maintained by kimocoder
  `     /¯¯¯\     ´    https://github.com/kimocoder/wifite2

[+] option: targeting WPA-encrypted networks only

[+] Scanning for WPA networks...
[+] Found 3 WPA targets
[+] Starting WPA attack against TargetNetwork (AA:BB:CC:DD:EE:FF)
[+] Capturing WPA handshake...
[+] Handshake captured! Cracking with Hashcat...
[+] Password found: MySecurePassword123
```

**Note**: This WPA-Only edition automatically focuses on WPA-encrypted networks and skips all others with a clear message.

## Repository Information

### **Fork Information**
This is a specialized fork of the original [wifite2](https://github.com/kimocoder/wifite2) project, modified to focus exclusively on WPA security testing.

### **Key Differences from Original**
- **Removed**: All WEP, WPS, and PMKID attack functionality
- **Simplified**: Interface and command line arguments
- **Focused**: Only WPA/WPA2/WPA3 handshake capture and cracking
- **Streamlined**: Reduced dependencies and configuration complexity

### **Installation Requirements**
- Python 3.11+
- Wireless card with monitor mode support
- Required tools: `aircrack-ng`, `hashcat`, `tshark`
- Root/sudo privileges for wireless operations

### **Contributing**
This is a specialized fork focused on WPA-only functionality. For general wireless auditing features, please refer to the [original wifite2 repository](https://github.com/kimocoder/wifite2).

### **License**
Same license as the original wifite2 project. See [LICENSE](LICENSE) file for details.

### **Disclaimer**
This tool is for educational and authorized security testing purposes only. Only use on networks you own or have explicit permission to test.
