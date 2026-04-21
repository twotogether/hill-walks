# Interactive Map

All hills climbed are marked with green dots on the map below.

```{raw} html

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.min.css" />
<script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.min.js"></script>

<div id="map" style="height: 600px; margin: 20px 0; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);"></div>

<script>
// Initialize map centered on Scotland
const map = L.map('map').setView([55.5, -3.5], 7);

L.tileLayer('https://tile.openstreetmap.de/tiles/osmde/{z}/{x}/{y}.png', {
  attribution: '© OpenStreetMap contributors',
  maxZoom: 18,
  maxNativeZoom: 18
}).addTo(map);

// Green triangle marker for hills
const greenTriangleSVG = 'data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="%2322c55e"><polygon points="12,2 22,20 2,20"/></svg>';
const hillIcon = L.icon({
  iconUrl: greenTriangleSVG,
  iconSize: [20, 20],
  iconAnchor: [10, 16],
  popupAnchor: [0, -16]
});

// Hill data
const hillsData = {
  "hills": [
    {
      "name": "North Berwick Law",
      "region": "East Lothian",
      "latitude": 56.049224,
      "longitude": -2.719218,
      "elevation": 187,
      "difficulty": "Easy",
      "type": "Volcanic cone",
      "url": "regions/east-lothian/north-berwick-law.html"
    },
    {
      "name": "Eildon Mid Hill",
      "region": "East Lothian",
      "latitude": 55.582432,
      "longitude": -2.7177954,
      "elevation": 422,
      "difficulty": "Medium",
      "type": "Moorland",
      "url": "regions/east-lothian/eildon-mid-hill.html"
    }
  ]
};

// Load hills and add markers
if (hillsData.hills && hillsData.hills.length > 0) {
  console.log('Adding', hillsData.hills.length, 'hills to map');
  
  hillsData.hills.forEach(hill => {
    console.log(`Adding marker: ${hill.name} at [${hill.latitude}, ${hill.longitude}]`);
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
  
  // Center map on first hill
  if (hillsData.hills[0]) {
    map.setView([hillsData.hills[0].latitude, hillsData.hills[0].longitude], 10);
  }
} else {
  console.error('No hills data found');
}
</script>

```
