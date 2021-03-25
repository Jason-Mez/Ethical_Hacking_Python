#!/usr/bin/env python
#This scipt will focus on executing system commands on Windows.

import subprocess
#Command will be stored in here.
command = "dir"

subprocess.Popen(command, shell = True)
