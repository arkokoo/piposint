from app.utils.username.light_blackbird import run_light_blackbird
import asyncio

loop = asyncio.get_event_loop()

def get_blackbird(username):
    output_dict = {}
    try:
        output_dict = loop.run_until_complete(run_light_blackbird(username))
    except Exception as e:
        pass
    return output_dict