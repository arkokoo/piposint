from app.utils.email.light_holehe import run_light_holehe
import trio

def get_holehe(email):
    domain_values = []
    try:
        domain_values = trio.run(run_light_holehe, email)
    except Exception as e:
        pass
    return domain_values
