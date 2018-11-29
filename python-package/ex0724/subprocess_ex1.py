# -*- coding: utf-8 -*-
import subprocess
proc = subprocess.Popen(["dir"],
                    shell=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE)

out, err = proc.communicate()
print out
