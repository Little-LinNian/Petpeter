from typing import Union
from io import BytesIO

from .download import download_avatar_to_image
from .utils import (
    load_image,
    DEFAULT_FONT,
    fit_font_size,
    load_font,
    to_jpg,
    rotate,
    perspective,
    draw_text,
    fit_size,
    make_jpg_or_gif,
)
from PIL.Image import Image as IMG
from PIL import Image


async def play_game(qid: str, text: str = "来玩休闲游戏啊") -> Union[str, BytesIO]:
    img = await download_avatar_to_image(qid)
    bg = await load_image("play_game/1.png")
    fontname = DEFAULT_FONT
    fontsize = await fit_font_size(text, 520, 110, fontname, 35, 25)
    if not fontsize:
        return "描述太长了哦，改短点再试吧~"
    font = await load_font(fontname, fontsize)
    text_w = font.getsize(text)[0]

    async def make(img: IMG) -> IMG:
        img = to_jpg(img)
        frame = Image.new("RGBA", bg.size, (255, 255, 255, 0))
        points = [(0, 5), (227, 0), (216, 150), (0, 165)]
        screen = rotate(perspective(fit_size(img, (220, 160)), points), 9)
        frame.paste(screen, (161, 117))
        frame.paste(bg, mask=bg)

        await draw_text(
            frame,
            (263 - text_w / 2, 430),
            text,
            font=font,
            fill="#000000",
            stroke_fill="#FFFFFF",
            stroke_width=2,
        )
        return frame

    return await make_jpg_or_gif(img, make)
