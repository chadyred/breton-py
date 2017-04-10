if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition( function (position) {
    var longitude = position.coords.longitude;
    var latitude = position.coords.latitude;
    var altitude = position.coords.altitude;
    document.querySelector('span.location').innerHTML += '<p><b> Longitude </b> : ' + longitude + '<br/><b> Latitude </b> : ' + latitude + '<br/><b> Altitude </b> : ' + altitude + '<br/></p>';

  });
} else {
  alert('Pas accepté !');
}
