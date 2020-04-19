# klipper-os-commands

Klipper can't send commands to OS terminal by default

This plugin adds to Klipper this functionality.

## Setup

```
 git clone https://github.com/morgan55555/klipper-os-commands.git
 ln -s ~/klipper-os-commands/os_commands.py ~/klipper/klippy/extras/os_commands.py
```

## Klipper configuration

Just copy that code and change parameters to any that you need.

```ini
[os_commands]
# new command, run it with OS_RUN COMMAND="command1"
command1: ls /bin
```
