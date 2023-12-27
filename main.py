import numpy as np
from PIL import Image

for H in range(1, 6): #1
    for W in range(1, 6): #1
        #평행이동
        for x_ in range(6 - W): #1
            for y_ in range(6 - H): #4
                #캔버스 만들기
                data = np.zeros((5, 5, 3), dtype=np.uint8)
                data[0:256, 0:256] = [255, 255, 255]

                #그리기
                for x in range(x_, x_ + W):
                    for y in range(y_, y_ + H):
                        data[x, y] = [0,0,0]

                #저장
                img = Image.fromarray(data, 'RGB')
                img.save(f"./image/img_{H}-{W}_{x_}-{y_}.jpg")
                