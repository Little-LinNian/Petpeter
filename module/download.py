import httpx
import hashlib
import aiofiles
from pathlib import Path
from aiocache import cached
from loguru import logger
from PIL import Image
import io

data_path = Path() / "resources"


class DownloadError(Exception):
    pass


class ResourceError(Exception):
    pass


network_resource: bool = False


async def download_url(url: str) -> bytes:
    async with httpx.AsyncClient() as client:
        for i in range(3):
            try:
                resp = await client.get(url)
                if resp.status_code != 200:
                    continue
                return resp.content
            except Exception as e:
                logger.warning(f"Error downloading {url}, retry {i}/3: {e}")
    raise DownloadError


async def get_resource(path: str, name: str) -> bytes:
    file_path = data_path / path / name
    if not file_path.exists():
        raise ResourceError
    if network_resource:
        url = f"https://cdn.jsdelivr.net/gh/MeetWq/nonebot-plugin-petpet@master/resources/{path}/{name}"
        data = await download_url(url)
        return data
    async with aiofiles.open(str(file_path), "rb") as f:
        return await f.read()


@cached(ttl=600)
async def get_image(name: str) -> bytes:
    return await get_resource("images", name)


@cached(ttl=600)
async def get_font(name: str) -> bytes:
    return await get_resource("fonts", name)


@cached(ttl=60)
async def download_avatar(user_id: str) -> bytes:
    url = f"http://q1.qlogo.cn/g?b=qq&nk={user_id}&s=640"
    data = await download_url(url)
    if not data or hashlib.md5(data).hexdigest() == "acef72340ac0e914090bd35799f5594e":
        url = f"http://q1.qlogo.cn/g?b=qq&nk={user_id}&s=100"
        data = await download_url(url)
        if not data:
            raise DownloadError
    return data


async def download_avatar_to_image(user_id: str):
    return Image.open(io.BytesIO(await download_avatar(user_id)))
