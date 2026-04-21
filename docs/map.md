# Interactive Map

All hills climbed are marked with green dots on the map below.

```{raw} html

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.min.css" />
<script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.min.js"></script>

<div id="map" style="height: 600px; margin: 20px 0; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);"></div>

<script>
// Initialize map centered on Scotland
const map = L.map('map').setView([55.5, -3.5], 7);

L.tileLayer('https://{s}.basemaps.cartocdn.com/positron/{z}/{x}/{y}{r}.png', {
  attribution: '© OpenStreetMap contributors | © CARTO',
  maxZoom: 19
}).addTo(map);

// Green marker for hills
const hillIcon = L.icon({
  iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-green.png',
  shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
  iconSize: [25, 41],
  iconAnchor: [12, 41],
  popupAnchor: [1, -34],
  shadowSize: [41, 41]
});

// Load hills from JSON
fetch('region-metadata.json')
  .then(response => response.json())
  .then(data => {
    data.hills.forEach(hill => {
      const marker = L.marker([hill.latitude, hill.longitude], { icon: hillIcon })
        .bindPopup(`
          <div style="font-weight: bold; margin-bottom: 5px;">${hill.name}</div>
          <div><strong>Region:</strong> ${hill.region}</div>
          <div><strong>Elevation:</strong> ${hill.elevation}m</div>
          <div><strong>Difficulty:</strong> ${hill.difficulty}</div>
          <div><strong>Type:</strong> ${hill.type}</div>
          <div style="margin-top: 8px;"><a href="${hill.url}">View details →</a></div>
        `)
        .addTo(map);
    });
  })
  .catch(error => console.error('Error loading hills:', error));
</script>

```
