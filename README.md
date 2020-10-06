:movie_camera: video_toolkits
=======================

This repo provides functions to read/write a video and draw keypoints.

** Defult BGR **

Installation
-----

```bash
git clone https://github.com/Celeste-cj/video_toolkits.git
cd video_toolkits
python setup.py install
```

How To Use
-----

### VideoReader  

```python
from video_toolkits import VideoReader, VideoReaderCV2

video_path = 'path to video'
reader = VideoReader(video_path)            # VideoReader - pyav, only support video file/stream
# reader = VideoReader(0)                   # webcam 0   VideoReaderCV2 support
for img in reader:
    pass
```


### VideoReader  

```python
from video_toolkits import VideoWriter

img_seqs = []
out_path = '{VIDEO_NAME}.mp4'                     # currently support .mp4/.avi
succeed = VideoWriter.imgseq2video(img_seqs, out_path, fps=30)
```

### Visualization

```python
from video_toolkits import show, visualize

img = None
kpts = []                       # default (22, 4)
show(img)                       # plot image with matplotlib.pyplot
visualize(img, kpts, color=None, sklts=None)          # draw skeletons
```

### Easy Import  

```python
from video_toolkits.easy_import import *       # this will import os, math, cv2, plt, numpy
```


License
-------

This is free and unencumbered software released into the public domain.

Anyone is free to copy, use, compile this software, either in source code form or as a compiled binary, for any purpose, commercial or non-commercial, and by any means.
