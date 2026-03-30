<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Strategic Geospatial Ecosystem</title>

<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css"/>

<style>
body{font-family:'Poppins',sans-serif;margin:0;background:#f4f7fb;}
header{
color:white;text-align:center;padding:140px 20px;
background:linear-gradient(rgba(0,20,10,0.75), rgba(0,40,20,0.85)),
url('https://eoimages.gsfc.nasa.gov/images/imagerecords/57000/57730/mali_amo_2009240_lrg.jpg');
background-size:cover;
}
h1{font-size:42px;}
nav{background:white;padding:15px;text-align:center;position:sticky;top:0;}
nav a{margin:10px;cursor:pointer;font-weight:500;}
section{display:none;padding:60px;}
section.active{display:block;}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:20px;}
.card{background:white;padding:20px;border-radius:10px;}
#map{height:500px;}
footer{background:#003d1f;color:white;text-align:center;padding:20px;}
</style>
</head>

<body>

<header>
<h1 id="title">STRATEGIC GEOSPATIAL ECOSYSTEM</h1>
<p id="subtitle">Geospatial Data Scientist | Remote Sensing | AI</p>
</header>

<nav>
<a onclick="show('home')">Home</a>
<a onclick="show('projects')">Projects</a>
<a onclick="show('mapSection')">Map</a>
<a onclick="show('contact')">Contact</a>
</nav>

<section id="home" class="active">
<h2>Portfolio</h2>
<p>International geospatial research platform.</p>
</section>

<section id="projects">
<h2>Projects</h2>
<div class="cards">
<div class="card">Geospatial Ecosystem</div>
<div class="card">Population Mapping Mali</div>
</div>
</section>

<section id="mapSection">
<h2>Interactive Map</h2>
<div id="map"></div>
</section>

<section id="contact">
<h2>Contact</h2>
<p>Email: mahamadoucamaramoc@outlook.com</p>
</section>

<footer>
© 2026 Dr Mahamadou CAMARA
</footer>

<script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>

<script>
// Navigation
function show(id){
document.querySelectorAll('section').forEach(s=>s.classList.remove('active'));
document.getElementById(id).classList.add('active');
}

// Map
var map = L.map('map').setView([17,-3],6);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);

L.marker([12.6,-7.7]).addTo(map).bindPopup("Bamako");
</script>

</body>
</html>
