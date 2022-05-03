from .download import download_avatar_to_image
from .utils import resize, load_image, save_gif
from io import BytesIO
from PIL import Image


async def eat(qid: str, **kwargs) -> BytesIO:
    img = resize(await download_avatar_to_image(qid), (32, 32))
    frames = []
    for i in range(3):
        frame = Image.new("RGBA", (60, 67), (255, 255, 255, 0))
        frame.paste(img, (1, 38))
        bg = await load_image(f"eat/{i}.png")
        frame.paste(bg, mask=bg)
        frames.append(frame)
    return save_gif(frames, 0.05)
