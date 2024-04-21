from app.utils.email.light_holehe import run_light_holehe
from flask import abort
import trio

def get_holehe(email: str) -> list:
    domain_values = []
    try:
        domain_values = trio.run(run_light_holehe, email)
    except Exception as e:
        abort(500, f"Failed to fetch data from Holehe: {e}")
    return domain_values