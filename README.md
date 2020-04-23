# klipper-os-commands

Klipper can't send commands to OS terminal by default

This plugin adds to Klipper this functionality.

## Setup

```
 git clone https://github.com/morgan55555/klipper-os-commands.git
 ln -s ~/klipper-os-commands/os_commands.py ~/klipper/klippy/extras/os_commands.py
```

## Klipper configuration

```ini
[os_commands]
```

## Usage

```
[gcode_macro TEST]
gcode:
    {printer.gcode.action_respond_info(printer.os_commands.run("ls"))}
```
