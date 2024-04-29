from app.utils.Requester import Requester, get_user_agent
import asyncio
import json
import aiohttp
from bs4 import BeautifulSoup

async def run_light_blackbird(username):
    """Run the light version of the blackbird tool."""

    # Get the sites data from the blackbird repository
    github_request = "https://raw.githubusercontent.com/p1ngul1n0/blackbird/master/data.json"
    response = Requester(url=github_request).get()
    search_data = response.json()

    timeout = aiohttp.ClientTimeout(total=20)
    output_dict = {
            "search-params": {
                "username": username,
            },
            "sites": [],
        }

    async with aiohttp.ClientSession(timeout=timeout) as session:
        tasks = []
        # Make a request to each site
        for site_data in search_data["sites"]:
            task = asyncio.ensure_future(
                make_request(session, site_data, username)
            )
            tasks.append(task)

        results = await asyncio.gather(*tasks)
        
        # Add the results to the output
        for result in results:
            if result["response-status"] == "200 OK" and result["status"] == "FOUND" :
                del result["status"]
                del result["response-status"]
                output_dict["sites"].append(result)

        return output_dict
    
async def make_request(session, site_data, username):
    """ Check if the username exists on a specific site and return the result."""

    url = site_data["url"].format(username=username)
    json_body = None
    useragent = get_user_agent()
    headers = {"User-Agent": useragent}
    metadata = []

    # Add headers and json body if they exist
    if "headers" in site_data:
        headers.update(json.loads(site_data["headers"]))
    if "json" in site_data:
        json_body = site_data["json"].format(username=username)
        json_body = json.loads(json_body)

    try:
        async with session.request(
            site_data["method"], url, json=json_body, proxy=None, headers=headers, ssl=False
        ) as response:
            responseContent = await response.text() # Used on fetched github's "data.json" properties
            if (
                "content-type" in response.headers
                and "application/json" in response.headers["Content-Type"]
            ):
                jsonData = await response.json() # Used on fetched github's "data.json" properties
            else:
                soup = BeautifulSoup(responseContent, "html.parser") # Used on fetched github's "data.json" properties

            if eval(site_data["valid"]):
                if "metadata" in site_data:
                    metadata = []
                    for metadata_item in site_data["metadata"]:
                        try:
                            value = eval(metadata_item["value"]).strip("\t\r\n")
                            metadata.append(
                                {"type": metadata_item["type"], "key": metadata_item["key"], "value": value}
                            )
                        except Exception as e:
                            pass
                out_status = "FOUND"
            else:
                out_status = "NOT FOUND"
        out_response_status = f"{response.status} {response.reason}"
    except Exception as e:
        out_status = "ERROR"
        out_response_status = None

    return {
        "app": site_data["app"],
        "url": url,
        "response-status": out_response_status,
        "status": out_status,
        "metadata": metadata,
    }