from .download import download_avatar_to_image
from .utils import circle, resize, load_image, save_gif, BytesIO, save_jpg, rotate
from PIL import Image


async def support(qid: str, **kwargs) -> BytesIO:
    img = await download_avatar_to_image(qid)
    support = await load_image("support/0.png")
    frame = Image.new("RGBA", support.size, (255, 255, 255, 0))
    img = rotate(resize(img, (815, 815)), 23)
    frame.paste(img, (-172, -17))
    frame.paste(support, mask=support)
    return save_jpg(frame)
