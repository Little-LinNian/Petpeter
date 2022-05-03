from module.download import download_avatar_to_image
from .utils import (
    BytesIO,
    to_jpg,
    limit_size,
    Image,
    ImageFilter,
    load_font,
    BOLD_FONT,
    draw_text,
    ImageDraw,
    save_jpg,
    DEFAULT_FONT,
)
from typing import Union


async def ask(
    qid: str,
    ta: str = "它",
    name: str = "",
) -> Union[str, BytesIO]:
    img = await download_avatar_to_image(qid)
    img = to_jpg(img).convert("RGBA")
    img = limit_size(img, (640, 0))
    img_w, img_h = img.size
    mask_h = 150
    start_t = 180
    gradient = Image.new("L", (1, img_h))
    for y in range(img_h):
        t = 0 if y < img_h - mask_h else img_h - y + start_t - mask_h
        gradient.putpixel((0, y), t)
    alpha = gradient.resize((img_w, img_h))
    mask = Image.new("RGBA", (img_w, img_h))
    mask.putalpha(alpha)
    mask = mask.filter(ImageFilter.GaussianBlur(radius=3))
    img = Image.alpha_composite(img, mask)
    if not name:
        return "找不到名字，加上名字再试吧~"

    font = await load_font(BOLD_FONT, 25)
    start_h = img_h - mask_h
    start_w = 30
    text_w = font.getsize(name)[0]
    line_w = text_w + 200
    await draw_text(
        img,
        (start_w + (line_w - text_w) / 2, start_h + 5),
        name,
        font=font,
        fill="orange",
    )
    draw = ImageDraw.Draw(img)
    draw.line(
        (start_w, start_h + 45, start_w + line_w, start_h + 45), fill="orange", width=2
    )
    text_w = font.getsize(f"{name}不知道哦")[0]
    await draw_text(
        img,
        (start_w + (line_w - text_w) / 2, start_h + 50),
        f"{name}不知道哦。",
        font=font,
        fill="white",
    )

    sep_w = 30
    sep_h = 80
    bg = Image.new("RGBA", (img_w + sep_w * 2, img_h + sep_h * 2), "white")
    font = await load_font(DEFAULT_FONT, 35)
    if font.getsize(name)[0] > 600:
        return "名字太长了哦，改短点再试吧~"
    await draw_text(bg, (sep_w, 10), f"让{name}告诉你吧", font=font, fill="black")
    await draw_text(
        bg, (sep_w, sep_h + img_h + 10), f"啊这，{ta}说不知道", font=font, fill="black"
    )
    bg.paste(img, (sep_w, sep_h))
    return save_jpg(bg)
