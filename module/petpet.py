from .download import download_avatar_to_image
from .utils import circle, resize, load_image, save_gif
from PIL import Image


async def petpet(qid: str):
    frames = []
    locs = [
        (14, 20, 98, 98),
        (12, 33, 101, 85),
        (8, 40, 110, 76),
        (10, 33, 102, 84),
        (12, 20, 98, 98),
    ]
    img = await download_avatar_to_image(qid)
    img = circle(img)
    for i in range(5):
        frame = Image.new("RGBA", (112, 112), (255, 255, 255, 0))
        x, y, w, h = locs[i]
        new_img = resize(img, (w, h))
        frame.paste(new_img, (x, y), mask=new_img)
        hand = await load_image(f"petpet/{i}.png")
        frame.paste(hand, mask=hand)
        frames.append(frame)
    return save_gif(frames, 0.06)
