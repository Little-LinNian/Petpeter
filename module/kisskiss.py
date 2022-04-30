from io import BytesIO
from .download import download_avatar_to_image
from .utils import circle, resize, load_image, save_gif


async def kiss(user1: str, user2: str) -> BytesIO:
    user_locs = [
        (58, 90),
        (62, 95),
        (42, 100),
        (50, 100),
        (56, 100),
        (18, 120),
        (28, 110),
        (54, 100),
        (46, 100),
        (60, 100),
        (35, 115),
        (20, 120),
        (40, 96),
    ]
    self_locs = [
        (92, 64),
        (135, 40),
        (84, 105),
        (80, 110),
        (155, 82),
        (60, 96),
        (50, 80),
        (98, 55),
        (35, 65),
        (38, 100),
        (70, 80),
        (84, 65),
        (75, 65),
    ]
    # fmt: on
    frames = []
    for i in range(13):
        frame = await load_image(f"kiss/{i}.png")
        user_head = resize(circle(await download_avatar_to_image(user1)), (50, 50))
        frame.paste(user_head, user_locs[i], mask=user_head)
        self_head = resize(circle(await download_avatar_to_image(user2)), (40, 40))
        frame.paste(self_head, self_locs[i], mask=self_head)
        frames.append(frame)
    return save_gif(frames, 0.05)
