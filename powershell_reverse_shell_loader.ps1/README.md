Description

This script is provided strictly for educational and research purposes.

The goal of this project is to understand how loader-style malware operates in real-world scenarios, specifically how an initial script can retrieve and execute additional payloads at runtime. PowerShell was intentionally chosen because it allows in‑memory execution, meaning code can run without being written to disk, which is a common technique observed in modern malware.

The script demonstrates:

How a basic loader functions

How persistence can be implemented via repeated connection attempts

How remote code can be retrieved and executed dynamically

No malicious payloads are included in this repository. Anything beyond the loader mechanism itself is explicitly out of scope for this project.

This work is intended to support learning, defensive research, and detection engineering, not offensive misuse.

Usage (Educational Lab Only)

Prepare a remote server to host a test script.

A simple Python HTTP server is sufficient.

The hosted script should be non‑malicious and used only for demonstration purposes.

Configure the loader to point to your controlled server.

When executed, the loader will attempt to retrieve the hosted script.

Upon successful download, a confirmation will be returned.

Observe the behavior.

This allows learners and defenders to study loader mechanics, execution flow, and detection opportunities.

The behavior and outcome depend entirely on the script hosted on the remote server. This repository does not provide or endorse malicious payloads.

Disclaimer

This project is intended solely for educational, research, and defensive purposes.

The author does not condone misuse of this code and is not responsible for any damage, disruption, or legal consequences resulting from improper or unauthorized use. Users are responsible for ensuring that all testing is conducted in isolated lab environments and in compliance with applicable laws and policies.
