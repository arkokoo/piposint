from app.utils.light_holehe import run_light_blackbird
import trio

def get_blackbird(username) :
    try:
        userJson = trio.run(run_light_blackbird, username)
    except Exception as e:
        pass
    return userJson