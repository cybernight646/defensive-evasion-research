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
 ![Image Alt]([image_url](https://github.com/cybernight646/defensive-evasion-research/blob/e7b66274729e4863695ba11df7946c5181ed807d/dns-poisoner/screenshots/Screenshot%20(98).png))

 AFTER 
![Image Alt]([image_url]

Modifying the hosts file can disrupt normal network behavior. This script should only be executed in controlled environments (e.g., labs, VMs) and for authorized testing purposes.
