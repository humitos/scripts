import os
import sys
import imdb
import glob
import time

HTTP = 'http://www.imdb.com/title/tt%s/'

ia = imdb.IMDb()

def mount(mountpoint):
    os.system('eject -t')
    time.sleep(2)
    os.system('sudo mount %s /cdrom' % mountpoint)

def umount(mountpoint):
    os.system('sudo umount %s' % mountpoint)
    time.sleep(2)
    os.system('eject')

def parse_dvd(mountpoint, dvd_number):
    mount(mountpoint)
    print '= %s =\n' % dvd_number

    filelist = glob.glob('/cdrom/*.avi')

    umount(mountpoint)

    for filename in filelist:
        parse_file(filename)


def parse_file(filename):

    film = filename.split('.avi')[0].replace('/cdrom/', '')
    try:
        s_result = ia.search_movie(film)[0]
        url = HTTP % s_result.getID()
    except:
        pass
        url = False

    if url:
        print ' * [%s %s]' % (url, film)
    else:
        print ' * %s' % film

def command_handler(line):
    if line == 'quit':
        sys.exit(0)
    elif line.isdigit():
        parse_dvd('/dev/hdb', line)

def prompt():
    line = sys.stdin.readline()
    while line:
        command_handler(line.strip())
        print 'Ingrese el numero de DVD: ',
        line = sys.stdin.readline()

if __name__ == '__main__':
    prompt()

