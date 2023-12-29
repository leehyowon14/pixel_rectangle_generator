"""주어진 가로 세로 픽셀의 사각형에서 만들 수 있는 모든 사각형을 만들어서 사진으로 저장해주는 프로그램.
"""
import itertools
import numpy as np
from PIL import Image

for H, W in itertools.product(range(1, 6), range(1, 6)):
    #평행이동
    for x_ in range(6 - W): #1
        for y_ in range(6 - H): #4
            #캔버스 만들기
            data = np.zeros((5, 5, 3), dtype=np.uint8)
            data[0:256, 0:256] = [255, 255, 255]

            #그리기
            for x, y in itertools.product(range(x_, x_ + W), range(y_, y_ + H)):
                data[x, y] = [0,0,0]

            #저장
            img = Image.fromarray(data, 'RGB')
            img.save(f"./image/img_{H}-{W}_{x_}-{y_}png")
                