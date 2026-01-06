Defender Status Awareness (Research PoC)

Overview
This script is a research proof-of-concept designed to demonstrate how user-interface–based social engineering prompts can be triggered conditionally based on the status of a local security service.
Specifically, it:
Checks whether the Windows Defender Network Inspection Service (WdNisSvc) is running
Displays a graphical popup message only if the service is active

The project is intended to support red team research and defensive awareness, particularly around how attackers may attempt to influence user behavior through deceptive notifications—and how such tactics can be detected, mitigated, or trained against.

What the Script Does
Queries the Windows service WdNisSvc using psutil
Determines whether the service state is running
If running, displays a Tkinter-based informational popup message

Does not:
Disable any security services
Modify system settings
Execute payloads
Persist on the system

All actions are user-space only and require no elevated privileges.

Intended Use
Security research
Red team training exercises
Blue team awareness and user training
Studying social engineering indicators and UX-based deception

All usage must be limited to controlled lab environments on systems owned by, or explicitly authorized for testing by, the user.

Limitations
The script relies on user interaction; it does not enforce any action
Modern endpoint security solutions may flag or monitor misleading security prompts
This PoC does not include evasion, persistence, or privilege escalation mechanisms
