from .download import download_avatar_to_image
from .utils import (
    circle,
    resize,
    load_image,
    save_gif,
    BytesIO,
    to_jpg,
    make_jpg_or_gif,
)
from PIL.Image import Image as IMG
from PIL import Image


async def always(qid: str, **kwargs) -> BytesIO:
    img = await download_avatar_to_image(qid)
    always = await load_image("always/0.png")
    w, h = img.size
    h1 = int(h / w * 300)
    h2 = int(h / w * 60)
    height = h1 + h2 + 10

    async def make(img: IMG) -> IMG:
        img = to_jpg(img)
        frame = Image.new("RGBA", (300, height), (255, 255, 255, 0))
        frame.paste(always, (0, h1 - 300 + int((h2 - 60) / 2)))
        frame.paste(resize(img, (300, h1)), (0, 0))
        frame.paste(resize(img, (60, h2)), (165, h1 + 5))
        return frame

    return await make_jpg_or_gif(img, make)
