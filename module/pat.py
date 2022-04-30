from .download import download_avatar_to_image
from .utils import circle, resize, load_image, save_gif, BytesIO
from PIL import Image


async def pat(qid: str, **kwargs) -> BytesIO:
    img = await download_avatar_to_image(qid)
    locs = [(11, 73, 106, 100), (8, 79, 112, 96)]
    img_frames = []
    for i in range(10):
        frame = Image.new("RGBA", (235, 196), (255, 255, 255, 0))
        x, y, w, h = locs[1] if i == 2 else locs[0]
        frame.paste(resize(img, (w, h)), (x, y))
        raw_frame = await load_image(f"pat/{i}.png")
        frame.paste(raw_frame, mask=raw_frame)
        img_frames.append(frame)
    # fmt: off
    seq = [0, 1, 2, 3, 1, 2, 3, 0, 1, 2, 3, 0, 0, 1, 2, 3, 0, 0, 0, 0, 4, 5, 5, 5, 6, 7, 8, 9]
    # fmt: on
    frames = [img_frames[n] for n in seq]
    return save_gif(frames, 0.085)
