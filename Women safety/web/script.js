document.getElementById("sosBtn").addEventListener("click", () => {
  if (confirm("Do you want to send an SOS alert with your location?")) {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition((position) => {
        const lat = position.coords.latitude;
        const lng = position.coords.longitude;

        document.getElementById("status").innerText =
          `📍 Location: ${lat.toFixed(4)}, ${lng.toFixed(4)} — Sending...`;

        // Call backend Python function
        eel.send_sos(lat, lng)((response) => {
          alert(response);
          document.getElementById("status").innerText = response;
        });

      }, (err) => {
        alert("❌ Could not get location: " + err.message);
      }, { enableHighAccuracy: true });
    } else {
      alert("❌ Geolocation not supported by this browser.");
    }
  }
});

  $("#sosBtn").click(function () {
    eel.trigger_sos();
  })