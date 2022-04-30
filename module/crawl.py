from .download import download_avatar_to_image
from .utils import circle, resize, load_image, save_gif, BytesIO, save_jpg
import random
from PIL import Image


async def crawl(qid: str, crawl_num: int = 0) -> BytesIO:
    img = await download_avatar_to_image(qid)
    img = resize(circle(img), (100, 100))
    crawl_total = 92
    if not crawl_num and 1 <= crawl_num <= crawl_total:
        crawl_num = random.randint(1, crawl_total)
    frame = await load_image("crawl/{:02d}.jpg".format(crawl_num))
    frame.paste(img, (0, 400), mask=img)
    return save_jpg(frame)
