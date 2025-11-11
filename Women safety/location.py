import geocoder

# Get location based on your IP
g = geocoder.ip('me')

if g.ok:
    lat, lng = g.latlng
    print(f"Latitude: {lat}")
    print(f"Longitude: {lng}")
    print(f"Google Maps link: https://maps.google.com/?q={lat},{lng}")
else:
    print("Unable to fetch location")
