from .download import download_avatar_to_image
from .utils import (
    circle,
    resize,
    load_image,
    save_gif,
    BytesIO,
    to_jpg,
    make_jpg_or_gif,
    rotate,
)
from PIL import Image
import random


async def turn(qid: str, **kwargs) -> BytesIO:
    img = await download_avatar_to_image(qid)
    img = circle(img)
    frames = []
    for i in range(0, 360, 10):
        frame = Image.new("RGBA", (250, 250), (255, 255, 255, 0))
        frame.paste(resize(rotate(img, i, False), (250, 250)), (0, 0))
        frames.append(to_jpg(frame))
    if random.randint(0, 1):
        frames.reverse()
    return save_gif(frames, 0.05)
