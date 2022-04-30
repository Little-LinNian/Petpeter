from .download import download_avatar_to_image
from .utils import circle, resize, load_image, rotate, save_gif


async def rub(qid1: str, qid2: str):

    user_locs = [
        (39, 91, 75, 75),
        (49, 101, 75, 75),
        (67, 98, 75, 75),
        (55, 86, 75, 75),
        (61, 109, 75, 75),
        (65, 101, 75, 75),
    ]
    self_locs = [
        (102, 95, 70, 80, 0),
        (108, 60, 50, 100, 0),
        (97, 18, 65, 95, 0),
        (65, 5, 75, 75, -20),
        (95, 57, 100, 55, -70),
        (109, 107, 65, 75, 0),
    ]
    # fmt: on
    frames = []
    for i in range(6):
        frame = await load_image(f"rub/{i}.png")
        x, y, w, h = user_locs[i]
        user_head = resize(circle(await download_avatar_to_image(qid1)), (w, h))
        frame.paste(user_head, (x, y), mask=user_head)
        x, y, w, h, angle = self_locs[i]
        self_head = rotate(
            resize(circle(await download_avatar_to_image(qid2)), (w, h)), angle
        )
        frame.paste(self_head, (x, y), mask=self_head)
        frames.append(frame)
    return save_gif(frames, 0.05)
