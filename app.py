from flask import Flask, request, jsonify, render_template
from pyproj import Transformer

app = Flask(__name__)

# Initialize transformers
transformer_wgs84_to_gda2020_zone54 = Transformer.from_crs("EPSG:4326", "EPSG:7855")  # WGS84 to GDA2020 Zone 54

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/convert_wgs84_to_gda2020', methods=['POST'])
def convert_wgs84_to_gda2020():
    data = request.json
    latitude = data['latitude']
    longitude = data['longitude']

    # Convert WGS84 to GDA2020 Zone 54
    converted_easting, converted_northing = transformer_wgs84_to_gda2020_zone54.transform(latitude, longitude)

    response = {
        'converted_gda2020': {
            'easting': converted_easting,
            'northing': converted_northing
        }
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
