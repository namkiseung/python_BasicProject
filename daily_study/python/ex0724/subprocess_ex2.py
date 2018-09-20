# -*- coding: utf-8 -*-
import subprocess
proc = subprocess.Popen(["ping", "8.8.8.8"],
                    shell=True,                    
                    stdout=subprocess.PIPE)
                    

out = proc.communicate()
print out[0]
