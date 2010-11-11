#!/usr/bin/env python

import urllib
import commands

URL = 'http://la.nvidia.com/Download/processDriver.aspx?psid=51&pfid=312&rpf=1&osid=11&lid=11&lang=la&lastupdate='

def local_driver_version():
    nvidia_version = commands.getoutput('nvidia-settings --version')
    return nvidia_version.splitlines()[1].split('  ')[1].split(' ')[1]

def internet_driver_url():
    urlopen = urllib.urlopen(URL)
    return urlopen.read()

if __name__ == '__main__':
    local = local_driver_version()
    url = internet_driver_url()

    # print local
    # print url

    if local in url:
        # not update needed
        pass
    else:
        # update needed
        print 'A new version of NVIDIA drivers is available'
        print '    * Your version: %s' % local
        print
        print url


