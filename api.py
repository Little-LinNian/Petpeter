from io import BytesIO
from os import walk
from typing import Awaitable, Callable
from fastapi import FastAPI
from fastapi.responses import Response
from module.download import download_avatar_to_image, download_url_to_image
from module.petpet import petpet
from module.kisskiss import kiss
from module.rub import rub
from module.play import play
from module.pat import pat
from module.rip import RIP, rip
from module.throw import throw, throw_gif
from module.crawl import crawl
from module.always import always
from module.loading import loading
from module.support import support
from module.turn import turn as _turn
from module.littleangel import littleangel, LittleAngel
from module.ASK import ask
from module.bite import bite
from module.alike import alike
from module.dontTouch import dont_touch
from module.playGame import play_game
from module.police import police, police1
from module.roll import roll
from module.eat import eat
from module.worship import worship


import sys


app = FastAPI(
    title="图图图 API", docs_url="/", openapi_url="/api/openapi.json", redoc_url=None
)






@app.post("/rua")
async def rua(qid: str):
    img = await petpet(qid)
    return Response(img.getvalue(), media_type="image/png")


@app.get("/kisskiss")
async def kisskiss(qid1: str, qid2: str):
    img = await kiss(qid1, qid2)
    return Response(img.getvalue(), media_type="image/png")


@app.get("/rub")
async def api_rub(qid: str, qid2: str):
    img = await rub(qid, qid2)
    return Response(img.getvalue(), media_type="image/png")


@app.get("/play")
async def api_play(qid: str):
    img = await play(qid)
    return Response(img.getvalue(), media_type="image/png")


@app.get("/pat")
async def api_pat(qid: str):
    img = await pat(qid)
    return Response(img.getvalue(), media_type="image/png")


@app.post("/rip")
async def api_rip(rip_data: RIP):
    resp = await rip(rip_data)
    if isinstance(resp, str):
        return resp
    return Response(resp.getvalue(), media_type="image/png")


@app.get("/throw")
async def api_throw(qid: str, gif: bool = False):
    if gif:
        img = await throw_gif(qid)
    else:
        img = await throw(qid)
    return Response(img.getvalue(), media_type="image/png")


@app.get("/crawl")
async def api_crawl(qid: str, crawl_num: int = 0):
    img = await crawl(qid, crawl_num)
    return Response(img.getvalue(), media_type="image/png")


@app.get("/always")
async def api_always(qid: str):
    img = await always(qid)
    return Response(img.getvalue(), media_type="image/png")


@app.get("/support")
async def api_support(qid: str):
    img = await support(qid)
    return Response(img.getvalue(), media_type="image/png")


@app.post("/littleangel")
async def little_eangel(data: LittleAngel):
    resp = await littleangel(data)
    if isinstance(resp, str):
        return resp
    return Response(resp.getvalue(), media_type="image/png")


@app.get("/loading")
async def loadddddd(source_image_url: str):
    img = await loading(source_image_url)
    return Response(img.getvalue(), media_type="image/png")


@app.get("/turn")
async def turn(qid: str):
    img = await _turn(qid)
    return Response(img.getvalue(), media_type="image/png")


@app.get("/playgame")
async def playgame(qid: str, text: str = "来玩休闲游戏啊"):
    img = await play_game(qid, text)
    if isinstance(img, str):
        return img
    return Response(img.getvalue(), media_type="image/png")


@app.get("/worship")
async def api_worship(qid: str):
    img = await worship(qid)
    return Response(img.getvalue(), media_type="image/png")


@app.get("/ask")
async def _ask(qid: str, ta: str = "它", name: str = ""):
    img = await ask(qid, ta, name)
    if isinstance(img, str):
        return img
    return Response(img.getvalue(), media_type="image/png")


@app.get("/eat")
async def _eat(qid: str):
    img = await eat(qid)
    return Response(img.getvalue(), media_type="image/png")


@app.get("/roll")
async def _roll(qid: str):
    img = await roll(qid)
    return Response(img.getvalue(), media_type="image/png")


@app.get("/police")
async def _police(qid: str, police_num: int = 0):
    if police_num == 0:
        img = await police(qid)
    elif police_num == 1:
        img = await police1(qid)
    else:
        return "1 or 0"
    return Response(img.getvalue(), media_type="image/png")


@app.get("/donttouch")
async def donttouch(source_image_url: str):
    img = await dont_touch(source_image_url)
    return Response(img.getvalue(), media_type="image/png")


@app.get("/alike")
async def _alike(source_image_url: str):
    img = await alike(source_image_url)
    return Response(img.getvalue(), media_type="image/png")


@app.get("/bite")
async def _bite(qid: str):
    img = await bite(qid)
    return Response(img.getvalue(), media_type="image/png")
