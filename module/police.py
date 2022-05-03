from .utils import (
    BytesIO,
    fit_size,
    load_image,
    resize,
    save_jpg,
    fit_size,
    to_jpg,
    rotate,
    Image,
)
from .download import download_avatar_to_image


async def police(qid: str) -> BytesIO:
    img = await download_avatar_to_image(qid)
    bg = await load_image("police/0.png")
    frame = Image.new("RGBA", bg.size)
    frame.paste(resize(img, (245, 245)), (224, 46))
    frame.paste(bg, mask=bg)
    return save_jpg(frame)


async def police1(qid: str) -> BytesIO:
    img = await download_avatar_to_image(qid)
    img = to_jpg(img).convert("RGBA")
    bg = await load_image("police/1.png")
    frame = Image.new("RGBA", bg.size, (255, 255, 255, 0))
    frame.paste(rotate(fit_size(img, (60, 75)), 16), (37, 291))
    frame.paste(bg, mask=bg)
    return save_jpg(frame)
