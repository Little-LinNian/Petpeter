from fastapi import FastAPI
from fastapi.responses import Response
from module.download import download_avatar_to_image
from module.petpet import petpet
from module.kisskiss import kiss
from module.rub import rub
from module.play import play
from module.pat import pat
from module.rip import RIP, rip
from module.throw import throw, throw_gif

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
