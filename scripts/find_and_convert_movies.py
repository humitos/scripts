#!/usr/bin/env python

import os
import sys

if '--automatic' in sys.argv:
    AUTOMATIC = True
else:
   AUTOMATIC = False
#AUTOMATIC = False
DEBUG = True

JDOWNLOADER_PATH = '/srv/descargas/jdownloader'
#JDOWNLOADER_PATH = '/srv/descargas/peliculas'
EXCLUDE_PATH = '/srv/descargas/jdownloader/exclude'
OUTPUT_PATH = '/srv/descargas/converted'

MENCODER_CMD = 'nice mencoder \
                -ovc xvid  \
                -xvidencopts bitrate=700:threads=2 \
                -oac mp3lame \
                -lameopts br=128:cbr \
                %(subtitle_options)s \
                -o %(output_filename)s \
                %(input_filename)s'

MENCODER_SUB = '-subfont-text-scale 3 -subalign 2 -subpos 90 -subcp iso8859-1 -sub %(subtitle_filename)s'

CONVERTIR_EXTENSIONES = ['avi', 'rmvb', 'mkv']
SUBTITLE_EXTENSIONES = ['sub', 'srt']
MOVIE_EXTENSIONES_CON_SUBS = ['avi', 'mkv']
EXTENSIONES_SIN_SUBS = ['rmvb']

def buscar_subtitle(filename):
    if DEBUG:
        print 'Buscando subtitulo para:', filename
    for root, directories, files in os.walk(JDOWNLOADER_PATH):
        for f in files:
            if f.split('.')[-1] in SUBTITLE_EXTENSIONES:
                if f.split('.')[:-1] == filename.split('.')[:-1]:
                    f = os.path.join(root, f)
                    if DEBUG:
                        print 'Subtitulo encontrado:', f
                    return path_compatible_con_bash(f)
    return False

def ya_fue_convertido(filename, subtitle):
    filename_absolute_path = output_path(filename, subtitle)
    if os.path.exists(filename_absolute_path):
        return True
    else:
        return False

def output_path(filename, subtitle):
    filename_absolute_path = os.path.join(OUTPUT_PATH, filename)
    if subtitle:
        filename_absolute_path = filename_absolute_path + '.Subtitle.avi'
    else:
        filename_absolute_path = filename_absolute_path + '.avi'
    return filename_absolute_path

def path_compatible_con_bash(filename_absolute_path):
    bash_filename = filename_absolute_path.replace(' ', r'\ ')
    bash_filename = bash_filename.replace('(', r'\(')
    bash_filename = bash_filename.replace(')', r'\)')
    bash_filename = bash_filename.replace('[', r'\[')
    bash_filename = bash_filename.replace(']', r'\]')
    return bash_filename


def convertir_video(filename_absolute_path, subtitle):
    filename_absolute_path = path_compatible_con_bash(filename_absolute_path)
    if DEBUG:
        print 'Converting:', filename_absolute_path

    subtitle_options = ''
    if subtitle:
        subtitle_options = MENCODER_SUB % {'subtitle_filename': subtitle}

    kw = {
        'input_filename': filename_absolute_path,
        'output_filename': output_path(os.path.basename(filename_absolute_path), subtitle),
        'subtitle_options': subtitle_options,
    }
    cmd = MENCODER_CMD % kw

    if DEBUG:
        print 'Command:', cmd

    os.system(cmd)

def movie_con_subtitle(filename, subtitle):
    if filename.split('.')[-1] in MOVIE_EXTENSIONES_CON_SUBS and subtitle:
        return True
    else:
        return False

def explorar_directorio():
    for root, directories, files in os.walk(JDOWNLOADER_PATH):
        if root.startswith(EXCLUDE_PATH):
            continue
        for f in files:
            if f.split('.')[-1] in CONVERTIR_EXTENSIONES:
                filename_absolute_path = os.path.join(root, f)
                subtitle = buscar_subtitle(f)
                if not ya_fue_convertido(f, subtitle):
                    if not AUTOMATIC:
                        if movie_con_subtitle(f, subtitle) or f.split('.')[-1] in EXTENSIONES_SIN_SUBS:
                            si = raw_input('Vamos a convertir %s (yes, no): ' % filename_absolute_path)
                            if si in ['y', 'Y', 'yes', 'YES', 'Yes']:
                                convertir_video(filename_absolute_path, subtitle)
                    else:
                        if movie_con_subtitle(f, subtitle):
                            convertir_video(filename_absolute_path, subtitle)

if __name__ == '__main__':
    explorar_directorio()

