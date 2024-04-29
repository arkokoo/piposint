from app.utils.username.light_blackbird import run_light_blackbird
from flask import abort
import asyncio

loop = asyncio.get_event_loop()

def get_blackbird(username: str)->dict:
    """
    Get information about a username via blackbird tool
    """
    output_dict = {}
    try:
        output_dict = loop.run_until_complete(run_light_blackbird(username))
    except Exception as e:
        abort(500, description=f"Failed to fetch data from Blackbird: {e}")
    return output_dict