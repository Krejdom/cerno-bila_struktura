from PIL import Image
import numpy as np
import random

SIZE = int(input("Set the size: "))


def pil_grid(images, max_horiz=np.iinfo(int).max):
    """https://stackoverflow.com/a/46877433"""
    n_images = len(images)
    n_horiz = min(n_images, max_horiz)
    h_sizes, v_sizes = [0] * n_horiz, [0] * (n_images // n_horiz)
    for i, im in enumerate(images):
        h, v = i % n_horiz, i // n_horiz
        h_sizes[h] = max(h_sizes[h], im.size[0])
        v_sizes[v] = max(v_sizes[v], im.size[1])
    h_sizes, v_sizes = np.cumsum([0] + h_sizes), np.cumsum([0] + v_sizes)
    im_grid = Image.new('RGB', (h_sizes[-1], v_sizes[-1]), color='white')
    for i, im in enumerate(images):
        im_grid.paste(im, (h_sizes[i % n_horiz], v_sizes[i // n_horiz]))
    return im_grid

source = ['img/1.bmp', 'img/2.bmp', 'img/3.bmp', 'img/4.bmp', 'img/5.bmp',
          'img/6.bmp', 'img/7.bmp', 'img/8.bmp', 'img/9.bmp', 'img/10.bmp',
          'img/11.bmp', 'img/12.bmp', 'img/13.bmp', 'img/14.bmp', 'img/15.bmp',
          'img/16.bmp', 'img/17.bmp', 'img/18.bmp', 'img/19.bmp', 'img/20.bmp',
          'img/21.bmp', 'img/22.bmp', 'img/23.bmp', 'img/24.bmp', 'img/25.bmp',
          'img/26.bmp', 'img/27.bmp', 'img/28.bmp', 'img/29.bmp', 'img/30.bmp',
          'img/31.bmp', 'img/32.bmp', 'img/33.bmp', 'img/34.bmp', 'img/35.bmp',
          'img/36.bmp', 'img/37.bmp', 'img/38.bmp', 'img/39.bmp', 'img/40.bmp',
          'img/41.bmp', 'img/42.bmp', 'img/43.bmp', 'img/44.bmp', 'img/45.bmp',
          'img/46.bmp', 'img/47.bmp']
img_list = []

for i in range(SIZE**2):
    src_img = random.choice(source)
    im = Image.open(src_img)
    img_list.append(im)

result = pil_grid(img_list, SIZE)

result.save("output.jpg")
