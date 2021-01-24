// Initialize and add the mapfunction 
function initMap() {

    // Map options 
    var options = {
        zoom: 13,
        center: {
            lat: 53.3498,
            lng: -6.2603
        }
    }

    // New Map
    var map = new google.maps.Map(document.getElementById('map'), options);

    //Marker
    var marker = new google.maps.Marker({
        position: {
            lat: 53.341389,
            lng: -6.260278
        },
        map: map,
        icon: 'http://maps.google.com/mapfiles/kml/paddle/B.png'
    });

    var infowindow = new google.maps.InfoWindow({
        content: ('<h5>Banyan Ayurveda</h5> <p class="my-2"><i class="fas fa-map-marker"></i>&nbsp Grafton Street | DUBLIN</p><p><i class="fas fa-phone-alt"></i>&nbsp 1234567890</p>')
    });

    marker.addListener('click', function () {
        infowindow.open(map, marker);
    });
}