from .download import download_avatar_to_image
from .utils import circle, resize, load_image, save_gif, save_jpg, BytesIO, rotate
import random


async def throw(qid: str, **kwargs) -> BytesIO:
    img = await download_avatar_to_image(qid)
    img = resize(rotate(circle(img), random.randint(1, 360), expand=False), (143, 143))
    frame = await load_image("throw/0.png")
    frame.paste(img, (15, 178), mask=img)
    return save_jpg(frame)


async def throw_gif(qid: str, **kwargs) -> BytesIO:
    img = await download_avatar_to_image(qid)
    locs = [
        [(32, 32, 108, 36)],
        [(32, 32, 122, 36)],
        [],
        [(123, 123, 19, 129)],
        [(185, 185, -50, 200), (33, 33, 289, 70)],
        [(32, 32, 280, 73)],
        [(35, 35, 259, 31)],
        [(175, 175, -50, 220)],
    ]
    frames = []
    for i in range(8):
        frame = await load_image(f"throw_gif/{i}.png")
        for w, h, x, y in locs[i]:
            new_img = resize(circle(img), (w, h))
            frame.paste(new_img, (x, y), mask=new_img)
        frames.append(frame)
    return save_gif(frames, 0.1)
