from fontTools.misc.fixedTools import strToFixed
from .download import download_avatar_to_image
from .utils import (
    circle,
    resize,
    load_image,
    save_jpg,
    BytesIO,
    rotate,
    BOLD_FONT,
    fit_font_size,
    load_font,
    draw_text,
)
from PIL import Image
from typing import Union
from pydantic import BaseModel


class RIP(BaseModel):
    qid1: str
    qid2: str
    huaji: bool = True
    text: str = ""


async def rip(data: RIP) -> Union[str, BytesIO]:
    self_img = await download_avatar_to_image(data.qid1)
    user_img = await download_avatar_to_image(data.qid2)

    if data.huaji:
        rip = await load_image("rip/0.png")
    else:
        rip = await load_image("rip/1.png")
    text = data.text

    frame = Image.new("RGBA", rip.size, (255, 255, 255, 0))
    left = rotate(resize(user_img, (385, 385)), 24)
    right = rotate(resize(user_img, (385, 385)), -11)
    frame.paste(left, (-5, 355))
    frame.paste(right, (649, 310))
    frame.paste(resize(self_img, (230, 230)), (408, 418))
    frame.paste(rip, mask=rip)

    if text:
        fontname = BOLD_FONT
        fontsize = await fit_font_size(text, rip.width - 50, 300, fontname, 150, 25)
        if not fontsize:
            return "text too long"
        font = await load_font(fontname, fontsize)
        text_w = font.getsize(text)[0]
        await draw_text(
            frame,
            ((rip.width - text_w) / 2, 40),
            text,
            font=font,
            fill="#FF0000",
        )
    return save_jpg(frame)
