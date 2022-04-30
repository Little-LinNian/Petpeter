from enum import Flag
from .download import download_avatar_to_image
from .utils import (
    circle,
    resize,
    load_image,
    save_gif,
    BytesIO,
    to_jpg,
    save_jpg,
    BOLD_FONT,
    limit_size,
    draw_text,
    load_font,
    FitSizeMode,
    fit_font_size,
)
from typing import Union
from PIL import Image


async def littleangel(
    qid: str, text: str = "非常可爱！简直就是小天使", ta: str = "它", name: str = "霖念"
) -> Union[str, BytesIO]:
    img = await download_avatar_to_image(qid)
    img = to_jpg(img).convert("RGBA")
    img = limit_size(img, (500, 500), FitSizeMode.INSIDE)
    img_w, img_h = img.size

    bg = Image.new("RGB", (600, img_h + 230), (255, 255, 255))
    bg.paste(img, (int(300 - img_w / 2), 110))
    fontname = BOLD_FONT

    font = await load_font(fontname, 48)
    text_w, _ = font.getsize(text)
    await draw_text(
        bg, (300 - text_w / 2, img_h + 120), text, font=font, fill=(0, 0, 0)
    )

    font = await load_font(fontname, 26)
    text = f"{ta}没失踪也没怎么样  我只是觉得你们都该看一下"
    text_w, _ = font.getsize(text)
    await draw_text(
        bg, (300 - text_w / 2, img_h + 180), text, font=font, fill=(0, 0, 0)
    )

    text = f"请问你们看到{name}了吗?"
    fontsize = await fit_font_size(text, 560, 110, fontname, 70, 25)
    if not fontsize:
        return "名字太长了哦，改短点再试吧~"

    font = await load_font(fontname, fontsize)
    text_w, text_h = font.getsize(text)
    x = 300 - text_w / 2
    y = 55 - text_h / 2
    await draw_text(bg, (x, y), text, font=font, fill=(0, 0, 0))
    return save_jpg(bg)
