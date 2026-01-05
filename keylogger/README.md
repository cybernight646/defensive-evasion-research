I wrote this script as a simple keylogging and clipboard monitoring demo to better understand how this type of behavior works in the wild. The goal is learning and experimentation—not building a fully weaponized tool.

It’s intentionally basic and stripped down so the mechanics are easy to follow. There’s no stealth, no persistence, and no data leaving the system. Everything stays local and visible.

This is strictly a learning artifact.

The main reasons for this script are to:

See how keystrokes can be captured at the user level
Observe how clipboard monitoring works in practice
Understand the kinds of behaviors that EDRs and AV products tend to flag
Use it as a reference when thinking about attacker tradecraft and defensive detection
It’s meant to be used in controlled red team / blue team labs or personal research environments.

What it does

Logs keystrokes locally
Logs copied clipboard content
Writes output to disk in a visible directory
Stops automatically after a fixed amount of time

Usage

You can run the script:
Directly with Python from the terminal, or
From any IDE (VS Code, PyCharm, etc.)
There’s no special setup required beyond the dependencies. You should only run it on systems you own or have explicit permission to test.

The code itself is also simple enough to be embedded into more advanced red team tooling later, depending on your lab goals. Any extensions beyond local logging should only be explored in authorized environments.
