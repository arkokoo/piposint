import asyncio
import json
import os
import sys
import time
import warnings
from datetime import datetime
import base64
from app.utils.Requester import Requester, get_user_agent
import aiohttp
from bs4 import BeautifulSoup
import requests

req = "https://raw.githubusercontent.com/p1ngul1n0/blackbird/master/data.json"
response = requests.get(url=req)
searchData = response.json()
warnings.filterwarnings("ignore")

#useragents = open(os.path.join(os.path.abspath(__file__),'..','useragent.txt'),'w').read().splitlines()

async def run_light_blackbird(username):
    timeout = aiohttp.ClientTimeout(total=20)

    async with aiohttp.ClientSession(timeout=timeout) as session:
        tasks = []
        for u in searchData["sites"]:
            task = asyncio.ensure_future(
                makeRequest(session, u, username)
            )
            tasks.append(task)

        results = await asyncio.gather(*tasks)
        userJson = {
            "search-params": {
                "username": username,
            },
            "sites": [],
        }
        
        for x in results:
            if x["response-status"] == "200 OK" and x["status"] == "FOUND" :
                del x["status"]
                del x["response-status"]
                userJson["sites"].append(x)

        return userJson

async def makeRequest(session, u, username):
    url = u["url"].format(username=username)
    jsonBody = None
    useragent = get_user_agent()
    headers = {"User-Agent": useragent}
    metadata = []
    if "headers" in u:
        headers.update(json.loads(u["headers"]))
    if "json" in u:
        jsonBody = u["json"].format(username=username)
        jsonBody = json.loads(jsonBody)
    try:
        async with session.request(
            u["method"], url, json=jsonBody, proxy=None, headers=headers, ssl=False
        ) as response:
            responseContent = await response.text()
            if (
                "content-type" in response.headers
                and "application/json" in response.headers["Content-Type"]
            ):
                jsonData = await response.json()
            else:
                soup = BeautifulSoup(responseContent, "html.parser")

            if eval(u["valid"]):
                if "metadata" in u:
                    metadata = []
                    for d in u["metadata"]:
                        try:
                            value = eval(d["value"]).strip("\t\r\n")
                            metadata.append(
                                {"type": d["type"], "key": d["key"], "value": value}
                            )
                        except Exception as e:
                            pass
                return {
                    "app": u["app"],
                    "url": url,
                    "response-status": f"{response.status} {response.reason}",
                    "status": "FOUND",
                    "metadata": metadata,
                }
            else:
                return {
                    "id": u["id"],
                    "app": u["app"],
                    "url": url,
                    "response-status": f"{response.status} {response.reason}",
                    "status": "NOT FOUND",
                    "error-message": None,
                    "metadata": metadata,
                }
    except Exception as e:
        return {
            "id": u["id"],
            "app": u["app"],
            "url": url,
            "response-status": None,
            "status": "ERROR",
            "error-message": repr(e),
            "metadata": metadata,
        }