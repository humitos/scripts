# Variables
FILENAME=`basename $AVI_FULLNAME`
FILENAME=${FILENAME%.*}

mencoder \
 -ovc xvid \
 -xvidencopts bitrate=1200 \
 -oac pcm \
 -o $BASENAME.Subtitles.avi \
  $AVI_FULLNAME

