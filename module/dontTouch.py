from io import BytesIO
from .utils import load_image, resize, save_jpg
from .download import download_avatar_to_image, download_url, download_url_to_image


async def dont_touch(url: str) -> BytesIO:
    img = await download_url_to_image(url)
    frame = await load_image("dont_touch/0.png")
    frame.paste(resize(img, (170, 170)), (23, 231))
    return save_jpg(frame)
