

function renderMap(Lat, Lng, Severity){

    let lat_lng = [];

    lat_lng.push(Lat)
    lat_lng.push(Lng)

    console.log("Lat & Long")
    console.log(lat_lng)

    var map = L.map('map').setView(lat_lng, 9);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    L.marker(lat_lng).addTo(map)
        .bindPopup('Severity Is - ' + Severity)
        .openPopup();

}

// renderMap("35.191669", "-114.06745900000001", "4")