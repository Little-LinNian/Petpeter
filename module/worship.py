from io import BytesIO
from .utils import perspective, resize, load_image, save_gif
from .download import download_avatar_to_image
from PIL import Image


async def worship(qid: str) -> BytesIO:
    img = await download_avatar_to_image(qid)
    points = [(0, -30), (135, 17), (135, 145), (0, 140)]
    paint = perspective(resize(img, (150, 150)), points)
    frames = []
    for i in range(10):
        frame = Image.new("RGBA", (300, 169), (255, 255, 255, 0))
        frame.paste(paint)
        bg = await load_image(f"worship/{i}.png")
        frame.paste(bg, mask=bg)
        frames.append(frame)
    return save_gif(frames, 0.04)
