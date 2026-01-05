Overview

This script is a demonstration keylogging utility created solely for educational and red team learning purposes. Its goal is to illustrate, at a basic level, how keylogging and clipboard capture mechanisms function in real-world malware, without implementing any exfiltration, persistence, or covert deployment techniques.

The script is not intended for surveillance, spying, or unauthorized data collection.

Purpose

The primary objectives of this script are to:

Demonstrate how keystrokes can be captured at the user level

Illustrate clipboard monitoring behavior

Help security practitioners understand:

How such tools operate

What behaviors endpoint security solutions monitor and alert on

Support learning in controlled red team, blue team, or defensive research environments

Scope and Limitations

Local-only execution

No networking or data exfiltration

No persistence mechanisms

No privilege escalation

No stealth or evasion techniques

Output is written locally and visibly to disk

The script runs for a fixed, configurable duration, after which all logging automatically stops. This time limit is intentional and can be adjusted as needed for testing.

Usage

The script can be run directly:

From a terminal using Python, or

From any standard IDE (e.g., VS Code, PyCharm)

No compilation is required, though it may be compiled for experimentation if desired.

Execution should occur only on systems you own or are explicitly authorized to test.

Configuration

The logging duration is controlled by a single variable:

duration = 12  # seconds


This value may be modified to suit your testing requirements.
Also the snippet can be added to a more advance code for red teaming purposes and improved to exfiltrate the logged keys to a remote server

Ethical and Legal Notice

This script must only be used in a controlled environment with explicit authorization.

Unauthorized use of keylogging software may violate:

Local and international laws

Organizational policies

Ethical standards

The author assumes no responsibility for misuse of this code.
