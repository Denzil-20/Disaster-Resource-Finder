let map = L.map('map').setView([12.9716, 77.5946], 12);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  maxZoom: 19
}).addTo(map);

function loadResources(query = "") {
  fetch(`/api/resources${query ? "?type=" + query : ""}`)
    .then(res => res.json())
    .then(data => {
      data.forEach(resource => {
        L.marker([resource.latitude, resource.longitude])
          .addTo(map)
          .bindPopup(`<b>${resource.name}</b><br>${resource.type}`);
      });
    });
}

function searchResource() {
  let search = document.getElementById("searchBox").value;
  map.eachLayer(layer => {
    if (layer instanceof L.Marker) map.removeLayer(layer);
  });
  loadResources(search);
}

loadResources();