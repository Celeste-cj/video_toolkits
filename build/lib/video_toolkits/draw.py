import cv2
import numpy as np
import matplotlib.pyplot as plt


def display(img):
    """
    Plot image with matplotlib, support 3-channel or 1-channel input

    :param img: BGR
    :return: None
    """
    if img.shape[-1] == 3:
        plt.imshow(img[..., ::-1])
    else:
        plt.imshow(img)
    plt.show()


color_default = np.array([
    [255, 128, 0, 0.5],
    [255, 153, 51, 0.5],
    [255, 153, 153, 0.5],
    [255, 102, 102, 0.5],
    [255, 51, 51, 0.5],
    [153, 255, 153, 0.5],
    [102, 255, 102, 0.5],
    [51, 255, 51, 0.5],
    [255, 153, 255, 0.5],
    [255, 102, 255, 0.5],
    [255, 51, 255, 0.5],
    [153, 204, 255, 0.5],
    [102, 178, 255, 0.5],
    [51, 153, 255, 0.5],
    [230, 230, 0, 0.5],
    [255, 178, 102, 0.5],
    [102, 178,255, 0.5],
    [0, 230, 230, 0.5],
    [255, 204, 153, 0.5],
    [0, 128, 255, 0.5]
    ])

sklts_simbase_foot = [
    [0, 1], [1, 2], [3, 4], [4, 5], [2, 6], [3, 6],
    [6, 7], [7, 8], [8, 9],
    [10, 11], [11, 12], [13, 14], [14, 15], [8, 12], [8, 13],
    [0, 19], [0, 21],
    [5, 16], [5, 18]
]


def draw_sklts(img, kpts, color=None, sklts=None, inplace=False):
    '''
    Draw keypoints and skeletons on the given image

    :param img:
    :param kpts:
    :param color: None for predefined color
    :param sklts: default skeleton with 22 keypoints
    :param inplace: whether cover or return a copy of raw image
    :return: img: a copy of raw image, so you do not need to worry about overwriting raw image
    '''
    img = img.copy() if not inplace else img
    color = color_default if color is None else color
    sklts = sklts_simbase_foot if sklts is None else sklts
    num_kpts = kpts.shape[0]
    for i in range(num_kpts):
        cv2.circle(img, (int(kpts[i][0]), int(kpts[i][1])), 3, color[i % len(color)], 3)

    for i, (pt_a, pt_b) in enumerate(sklts):
        if kpts[pt_a][0] < 0 or kpts[pt_b][0] < 0:
            continue
        cv2.line(img, (int(kpts[pt_a][0]), int(kpts[pt_a][1])), (int(kpts[pt_b][0]), int(kpts[pt_b][1])), color[i % len(color)], 4)
    return img


color_dict = {'r': (0, 0, 255), 'g': (0, 255, 0), 'b': (255, 0, 0), 'd': (0, 0, 0), 'y': (0, 255, 255)}

def put_text(img, text: str, pos=(15, 35), color='y', inplace=False):
    '''
    put text on the given image (default not inplace)
    :param img:
    :param text: str
    :param pos:
    :param color: r, g, b, d(black), y(yellow)
    :param inplace: whether cover or return a copy of raw image
    :return: img (raw image or copy)
    '''
    img = img.copy() if not inplace else img
    if isinstance(color, str):
        color = 'y' if color not in color_dict else color
        color = color_dict[color]
    else:
        assert len(color) == 3, "color should be char or 3-tuple"
    cv2.putText(img, text, pos, cv2.FONT_HERSHEY_SIMPLEX, 1.2, color, 2)
    return img


def draw_bbox(img, bbox, color='y', inplace=False):
    '''
    draw bbox on the given image (default not inplace)
    :param img:
    :param bbox: lefttop_x, lefttop_y, width, height
    :param color: r, g, b, d(black), y(yellow)
    :param inplace: whether cover or return a copy of raw image
    :return: img (raw image or copy)
    '''
    img = img.copy() if not inplace else img
    x, y, w, h = np.array(bbox, dtype=np.int_)
    color = 'y' if color not in color_dict else color
    img = cv2.rectangle(img, (x, y), (x + w, y + h), color_dict[color], 2)
    return img


__all__ = ["display", "draw_sklts", "put_text", "draw_bbox"]