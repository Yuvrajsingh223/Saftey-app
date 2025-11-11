import eel
from backend import trigger_sos

eel.init("web")

@eel.expose
def send_sos(lat, lng):
    print(f"📍 Location received: {lat}, {lng}")
    result = trigger_sos(lat, lng)
    return result

if __name__ == "__main__":
    eel.start("index.html", size=(500, 500))
