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
from PIL import ImageFilter


async def loading(qid: str, **kwargs) -> BytesIO:
    img = await download_avatar_to_image(qid)
    bg = await load_image("loading/0.png")
    icon = await load_image("loading/1.png")
    w, h = img.size
    h1 = int(h / w * 300)
    h2 = int(h / w * 60)
    height = h1 + h2 + 10

    def make_static(img: IMG) -> IMG:
        img = to_jpg(img)
        frame = Image.new("RGBA", (300, height), (255, 255, 255, 0))
        frame.paste(bg, (0, h1 - 300 + int((h2 - 60) / 2)))
        img = resize(img, (300, h1))
        img = img.filter(ImageFilter.GaussianBlur(radius=2))
        frame.paste(img, (0, 0))
        mask = Image.new("RGBA", (300, h1), (0, 0, 0, 128))
        frame.paste(mask, (0, 0), mask=mask)
        frame.paste(icon, (100, int(h1 / 2) - 50), mask=icon)
        return frame

    frame = make_static(img)

    async def make(img: IMG) -> IMG:
        new_img = frame.copy()
        new_img.paste(resize(img, (60, h2)), (60, h1 + 5))
        return new_img

    return await make_jpg_or_gif(img, make)
