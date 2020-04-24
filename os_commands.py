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
import subprocess

class OS_Commands:
    def __init__(self, config):
        self.printer = config.get_printer()
        self.config = config
    def get_status(self, eventtime):
        return {'run': self._run}
    def _run(self, command):
        output = None
        try:
            output = subprocess.check_output(command, shell=True, universal_newlines=True, stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as e:
            output = 'Error: ' + e.output
        if output != None:
            return str(output)


def load_config(config):
    return OS_Commands(config)
    
