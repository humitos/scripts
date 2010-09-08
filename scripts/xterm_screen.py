#!/usr/bin/python

import commands
import os
import sys

DEBUG = False
#DEBUG = True

output = commands.getoutput('ps -f -u humitos')
program = sys.argv[1]
R_XTERM = 'xterm -fa monospace -fs 10 -132 -bdc -geometry 120x30 -title %(program)s -e screen -r %(program)s'
S_XTERM = 'xterm -fa monospace -fs 10 -132 -bdc -geometry 120x30 -title %(program)s -e screen -S %(program)s %(program)s'
CHANGE = 'wmctrl -a %(program)s'

def log(string):
    if DEBUG:
        os.system('echo "%s" | aosd_cat' % string)

def main():
    if program == 'firefox':
        if 'firefox-bin' in output:
            os.system(CHANGE % {'program': 'iceweasel'})
            log(CHANGE)
            return
        else:
            os.system('iceweasel')
            return
    elif ('SCREEN -S %s' % program in output) and not ('screen -r %s' % program in output):
        # esta detachado
        os.system(R_XTERM % {'program': program})
        log(R_XTERM)
        return
    elif ('screen -r %s' % program in output) or ('SCREEN -S %s' % program in output):
        # ya existe una ventana switcheo a esa mediante un comando
        os.system(CHANGE % {'program': program.split('-')[0]})
        log(CHANGE)
        return
    else:
        # no se esta ejecutando
        os.system(S_XTERM % {'program': program})
        log(S_XTERM)
        return

if __name__ == '__main__':
    main()
