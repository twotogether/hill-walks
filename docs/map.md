# Interactive Map

All hills climbed are marked with green dots on the map below.

```{raw} html

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.min.css" />
<script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.min.js"></script>

<div id="map" style="height: 600px; margin: 20px 0; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);"></div>

<script>
// Initialize map centered on Scotland
const map = L.map('map').setView([55.5, -3.5], 7);

// OS Maps API - Ordnance Survey
// Get free API key at: https://osdatahub.os.uk/
const osApiKey = 'YOUR_OS_API_KEY_HERE'; // Replace with your OS Maps API key

if (osApiKey !== 'YOUR_OS_API_KEY_HERE') {
  L.tileLayer(`https://api.os.uk/maps/raster/v1/zxy/Light_3857/{z}/{x}/{y}.png?key=${osApiKey}`, {
    attribution: '&copy; Crown copyright and database right ' + new Date().getFullYear() + ' Ordnance Survey',
    maxZoom: 20
  }).addTo(map);
} else {
  // Fallback to OpenTopoMap if no API key
  L.tileLayer('https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png', {
    attribution: 'Map data: &copy; OpenStreetMap contributors | Rendering: &copy; OpenTopoMap',
    maxZoom: 17
  }).addTo(map);
  console.warn('OS Maps API key not set. Using OpenTopoMap as fallback. Get a free key at https://osdatahub.os.uk/');
}

// Green triangle marker for hills - enhanced visibility
const greenTriangleSVG = 'data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><circle cx="16" cy="16" r="14" fill="%2322c55e" stroke="white" stroke-width="2"/><polygon points="16,8 24,22 8,22" fill="white"/></svg>';
const hillIcon = L.icon({
  iconUrl: greenTriangleSVG,
  iconSize: [32, 32],
  iconAnchor: [16, 22],  // Position triangle point at coordinate
  popupAnchor: [0, -22]
});

// Hill data
const hillsData = {
  "hills": [
    {
      "name": "North Berwick Law",
      "region": "East Lothian",
      "latitude": 56.048825,
      "longitude": -2.713749,
      "elevation": 187,
      "difficulty": "Easy",
      "type": "Volcanic cone",
      "url": "regions/east-lothian/north-berwick-law.html"
    },
    {
      "name": "Eildon Mid Hill",
      "region": "East Lothian",
      "latitude": 55.582169,
      "longitude": -2.718219,
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
