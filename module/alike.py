from io import BytesIO
from .utils import save_jpg, resize, load_image
from .download import download_url_to_image
from PIL.Image import Image




async def alike(url: str) -> BytesIO:
    img = await download_url_to_image(url)
    frame = await load_image("alike/0.png")
    frame.paste(resize(img, (90, 90)), (131, 14))
    return save_jpg(frame)
