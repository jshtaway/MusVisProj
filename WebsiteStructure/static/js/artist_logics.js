function createMap (conserts) {
    var basemap = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
        attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap </a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox </a>",
        maxZoom: 18,
        id: "mapbox.outdoors",
        accessToken: API_KEY
    });
    var darkmap = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
        attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
        maxZoom: 18,
        id: "mapbox.dark",
        accessToken: API_KEY
    });
    var baseMaps = {
        "Street Map": basemap,
        "Dark Map": darkmap
    };
    var overlayMaps = {
        Artist: conserts
    };
    var map = L.map("map", {
                center: [37.09, -95.71],
                zoom: 5,
                layers: [basemap, conserts]
    });
    L.control.layers(baseMaps, overlayMaps, {
        collapsed: false
    }).addTo(map);
}

function createFeatures(data) {
    function onEachFeature(feature, layer) {
        layer.bindPopup("<h3>" + feature.properties.name + "</h3>");
    }
    var events = L.geoJSON(data, {
        onEachFeature: onEachFeature        
    });
    createMap(events);
};

var slider = 
{
    'type': "FeatureCollection",
    'features': 
    [
        {
            'geometry': 
            {
                'coordinates': [-116.19518, 33.72221],
                'type': 'Point'
            },
            'properties': 
            {
                'City': 'Indio, CA, US',
                'Date': '2018-07-21',
                'Name': 'Pitbull at Special Events Center, Fantasy Springs Resort & Casino (July 21, 2018)',
                'Popularity': 0.500202
            },
            'type': 'Feature'
        },
        {
            'geometry': 
            {
                'coordinates': [-117.124, 33.5033],
                'type': 'Point'
            },
            'properties': 
            {
                'City': 'Temecula, CA, US',
                'Date': '2018-07-20',
                'Name': 'Pitbull at Pechanga Summit (July 20, 2018)',
                'Popularity': 0.500201
            },
            'type': 'Feature'
        },
        {
            'geometry': 
            {
                'coordinates': [-118.7995455, 45.6700263],
                'type': 'Point'
            },
            'properties': 
            {
                'City': 'Pendleton, OR, US',
                'Date': '2018-07-14',
                'Name': 'Pendleton Whisky Music Fest 2018',
                'Popularity': 0.500222
            },
            'type': 'Feature'
        }
    ]
};

var geojsonMarkerOptions = {
    radius: 8,
    fillColor: "#ff7800",
    color: "#000",
    weight: 1,
    opacity: 1,
    fillOpacity: 0.8
};

console.log("HERE");
var artistName
var EventData = function () {
    artistName = d3.select('input').property('value')
    console.log(artistName)
};

var link = "/api_geojson/" + artistName;

d3.json(link, function (data) {
    // console.log(error);
    console.log(data);
    // Creating a GeoJSON layer with the retrieved data
    createFeatures(data);
});
