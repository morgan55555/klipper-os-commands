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
    def get_status(self, eventtime):
        return {'run': self._run}
    def _run(self, command):
        output = check_output(command, shell=True, universal_newlines=True)
        if output:
            return str(output)
        else:
            return ""


def load_config(config):
    return OS_Commands(config)
    
