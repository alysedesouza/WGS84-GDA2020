from flask import Flask, request, jsonify
from pyproj import Transformer

app = Flask(__name__)

# Initialize transformers
transformer_gda94_to_gda2020 = Transformer.from_crs("EPSG:28349", "EPSG:7850")  # Example for Zone 49
transformer_wgs84_to_gda2020 = Transformer.from_crs("EPSG:4326", "EPSG:7850")  # WGS84 to GDA2020

@app.route('/convert_coordinates', methods=['POST'])
def convert_coordinates():
    data = request.json
    zone = data['zone']
    eastings = data['eastings']
    northings = data['northings']

    # Use appropriate transformer based on the zone
    transformer = Transformer.from_crs(f"EPSG:283{zone}", "EPSG:785{zone}")
    converted_easting, converted_northing = transformer.transform(eastings, northings)

    # Dummy conversion for WGS84 Lat-Long (replace with actual logic if needed)
    wgs84_lat, wgs84_long = transformer.transform(converted_easting, converted_northing, direction='INVERSE')

    response = {
        'converted_gda2020': {
            'easting': converted_easting,
            'northing': converted_northing
        },
        'wgs84_lat_long': {
            'latitude': wgs84_lat,
            'longitude': wgs84_long
        }
    }
    return jsonify(response)

@app.route('/convert_wgs84_to_gda2020', methods=['POST'])
def convert_wgs84_to_gda2020():
    data = request.json
    latitude = data['latitude']
    longitude = data['longitude']

    # Convert WGS84 to GDA2020
    converted_easting, converted_northing = transformer_wgs84_to_gda2020.transform(latitude, longitude)

    response = {
        'converted_gda2020': {
            'easting': converted_easting,
            'northing': converted_northing
        }
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
