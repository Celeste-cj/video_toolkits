import os
import sys

import av
import cv2


class VideoReader(object):
    def __init__(self, file_name):
        self.file_name = file_name
        try:
            self.file_name = int(file_name)
        except ValueError:
            pass

    def __iter__(self):
        try:
            self.container = av.open(self.file_name)
        except av.error.FileNotFoundError:
            raise IOError('Video {} not found'.format(self.file_name))
        return self

    def __next__(self):
        try:
            img = next(self.container.decode(video=0))
            frame = img.to_ndarray(format='bgr24')
        except Exception as e:
            raise StopIteration
        return frame


class VideoReaderCV2(object):
    def __init__(self, file_name):
        self.file_name = file_name
        try:  # OpenCV needs int to read from webcam
            self.file_name = int(file_name)
        except ValueError:
            pass

    def __iter__(self):
        self.cap = cv2.VideoCapture(self.file_name)
        if not self.cap.isOpened():
            raise IOError('Video {} cannot be opened'.format(self.file_name))
        return self

    def __next__(self):
        was_read, img = self.cap.read()
        if not was_read:
            raise StopIteration
        return img


class VideoWriter:
    @staticmethod
    def imgseq2video(img_seq, out_path, fps=30):
        img_num = len(img_seq)
        frameSize = (img_seq[0].shape[1], img_seq[0].shape[0])

        if out_path[-3:] == "avi":
            fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
        elif out_path[-3:] == "mp4":
            fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        else:
            sys.stderr.write('Format {} not implemented'.format(out_path[-3:]))
            return False
        video_writer = cv2.VideoWriter(filename=out_path, fourcc=fourcc, fps=fps, frameSize=frameSize)

        sys.stdout.write('Converting img sequences into video...')

        for i in range(img_num):
            video_writer.write(img_seq[i])
        video_writer.release()

        print('Done')
        return True



def flv2mp4(vid_path, out_folder=''):
    '''
    convert flv format video to mp4

    :param vid_path: path to input video in flv format
    :param out_folder: output folder
    :return: True - succeed; False - failed
    '''
    try:
        reader = VideoReaderCV2(vid_path)
        imgs = []
        shape = (1080, 960)
        for img in reader:
            imgs.append(img)
            shape = img.shape[:2] if img.shape[0] * img.shape[1] < shape[0] * shape[1] else shape
        imgs = [cv2.resize(img, shape) for img in imgs]

        out_path = os.path.join(out_folder, os.path.basename(vid_path)[:-3] + "mp4") if out_folder == '' else vid_path[:-3] + "mp4"
        VideoWriter.imgseq2video(imgs, out_path)
        return True
    except:
        return False


__all__ = ['VideoReader', 'VideoReaderCV2', 'VideoWriter', 'flv2mp4']