# DNS / Hosts File Manipulation (Windows)

This script demonstrates a basic DNS redirection technique by modifying the Windows `hosts` file to override domain name resolution.

## What the script does
- Changes the working directory to the Windows hosts file location  
  (`C:\Windows\System32\drivers\etc`)
- Appends a static IP-to-domain mapping to the `hosts` file
- Flushes the local DNS cache to apply changes immediately

In its current form, the script redirects `www.google.com` to a specified IP address by adding a hosts file entry.

## Purpose
This code is intended for **defensive evasion research and security testing**, illustrating how local name resolution can be manipulated without interacting with external DNS infrastructure. It is useful for:
- Understanding DNS resolution order on Windows
- Testing detection and monitoring controls
- Demonstrating the impact of hosts file tampering

## Requirements
- Windows operating system
- Administrator privileges (required to modify the hosts file)

## Warning

BEFORE
 ![Image Alt]([https://github.com/cybernight646/defensive-evasion-research/blob/08168fa6285373f5f573e21dd1cc757f9c5ca54a/dns-poisoner/screenshots/Screenshot%20(97).png])
 
 AFTER 
![Image Alt]([https://github.com/cybernight646/defensive-evasion-research/blob/f37ad2ed225b2cfc3fad63f48d85cd12bfaf287d/dns-poisoner/screenshots/Screenshot%20(98).png])

Modifying the hosts file can disrupt normal network behavior. This script should only be executed in controlled environments (e.g., labs, VMs) and for authorized testing purposes.
