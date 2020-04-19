# -*- coding: utf-8 -*-
# Klipper OS commands support
#
# Copyright (C) 2020  Alex Morgan <alxmrg55@gmail.com>
#
# This file may be distributed under the terms of the GNU GPLv3 license.
#
# Install:
#
# git clone https://github.com/morgan55555/klipper-os-commands.git
# ln -s ~/klipper-os-commands/os_commands.py ~/klipper/klippy/extras/os_commands.py
#
from subprocess import check_output

class OS_Commands:
    def __init__(self, config):
        self.printer = config.get_printer()
        self.config = config
        self.gcode = self.printer.lookup_object('gcode')
        self.gcode.register_command(
            'OS_RUN', self.cmd_OS_RUN, when_not_ready=True, desc=self.cmd_OS_RUN_desc)
    cmd_OS_RUN_desc = 'Run OS commands'
    def cmd_OS_RUN(self, params):
        command_id = self.gcode.get_str('COMMAND', params, None)
        if command_id is None:
            self.gcode.respond_info('Usage: OS_RUN COMMAND="command_name", define command_name: command in config')
            return
        command = self.config.get(command_id, '')
        if not command:
            self.gcode.respond_error('Command "%s" is not defined in config' % command_id )
            return
        output = check_output(command, shell=True, universal_newlines=True)
        if output:
            self.gcode.respond_info(output)


def load_config(config):
    return OS_Commands(config)
    