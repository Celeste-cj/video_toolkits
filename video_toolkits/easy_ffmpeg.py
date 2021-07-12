import os

import ffmpeg


def trim_video(input_path: str, output_path: str, start_at: int, end_at: int=None, duration: int=None):
    """
    trim a video clip from given video. if both end_at and duration are not given, it will trim to the end by default.

    :param input_path: path to the raw input video
    :param output_path: path to the output video
    :param start_at: trim video start second
    :param end_at: trim video end second
    :param duration: maximum video clip duration, the actual end = min(start + duration, video length)
    """
    args = {
        "start": start_at
    }
    if end_at is not None:
        args["end"] = end_at
    if duration is not None:
        args["duration"] = duration

    (
        ffmpeg
        .input(input_path)
        .trim(**args)
        .output(output_path)
        .run(overwrite_output=True)
    )


def push_rtmp(input_path, output_path, loop=False):
    """
    push input video to RTMP server in the raw video format and fps

    :param input_path: input video path
    :param output_path: RTMP play url
    :param loop: [boolean] whether push stream in a loop
    :return: None
    """
    loop_num = -1 if loop else 0
    os.system(f"ffmpeg -re -stream_loop {loop_num} -i {input_path} -vcodec copy -acodec copy -f flv -y {output_path}")


__all__ = ["trim_video", "push_rtmp"]
