import os.path,subprocess
from subprocess import STDOUT,PIPE
import shlex, subprocess
def Christofide(filename):
    #print filename
    cmd = "java -jar Chris.jar "+filename
    #print cmd
    args = shlex.split(cmd)
    proc = subprocess.Popen(args, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
    stdout,stderr = proc.communicate()
    path = [int(e) for e in stdout.split()]
    return path
