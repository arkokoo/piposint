import trio
from app.utils.light_holehe import run_light_holehe

def get_holehe(email):
    domain_values = []
    try:
        domain_values = trio.run(run_light_holehe, email)
    except Exception as e:
        pass
    return domain_values
