from app.utils.username.light_blackbird import run_light_blackbird
import asyncio

loop = asyncio.get_event_loop()

def get_blackbird(username):
    result = {}
    try:
        result = loop.run_until_complete(run_light_blackbird(username))
    except Exception as e:
        pass
    return result