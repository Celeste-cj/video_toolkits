:movie_camera: video_toolkits
=======================

This repo provides functions to read/write a video.

Installation
-----

```bash
git clone git@github.com:Celeste-cj/video_toolkits.git
cd video_toolkits
python setup.py install
```

How To Use
-----

### VideoReader  

```python
from video_toolkits import VideoReader

video_path = 'path to video'
reader = VideoReader(video_path)            # video path
reader = VideoReader(0)            # webcam 0
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

License
-------

This is free and unencumbered software released into the public domain.

Anyone is free to copy, use, compile this software, either in source code form or as a compiled binary, for any purpose, commercial or non-commercial, and by any means.