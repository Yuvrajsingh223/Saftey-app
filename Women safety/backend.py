from shlex import quote
import subprocess
import time
import pyautogui
from playsound import playsound
import geocoder
import eel
@eel.expose
def send_whatsapp_message(message,phone_number="+919259274909", name="Family"):
    encoded_message = quote(message)
    whatsapp_url = f"whatsapp://send?phone={phone_number}&text={encoded_message}"
    subprocess.run(f'start "" "{whatsapp_url}"', shell=True)

    time.sleep(6)  # wait for WhatsApp to open
    pyautogui.press('enter')

    print(f"✅ Message sent to {name}")
    return True
g = geocoder.ip('me')
if g.ok:
    lat, lng = g.latlng


def trigger_sos(lat, lng):
    
    try:
        playsound("emergency-alarm-69780.mp3")  # play alert sound
    except Exception as e:
        print(f"⚠️ Could not play alert sound: {e}")

    maps_link = f"https://maps.google.com/?q={lat},{lng}"
    message = f"🚨 SOS! I need help! My live location: {maps_link}"

    phone_number = "+919259274909"  # your emergency contact

    send_whatsapp_message( message,phone_number, "Mom")

    return "✅ SOS alert sent successfully!"
