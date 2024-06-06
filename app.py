from flask import Flask, request, jsonify, render_template
from pyproj import Transformer

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/convert_coordinates', methods=['POST'])
def convert_coordinates():
    data = request.json
    zone = int(data['zone'])
    latitude = float(data['latitude'])
    longitude = float(data['longitude'])

    # Define source and destination CRS codes for WGS84 to GDA2020 conversion
    source_crs = 'EPSG:4326'
    destination_crs = f'EPSG:{7800 + zone}'

    # Perform WGS84 to GDA2020 conversion
    transformer_wgs84_to_gda2020 = Transformer.from_crs(source_crs, destination_crs, always_xy=True)
    transformed_point_gda2020 = transformer_wgs84_to_gda2020.transform(longitude, latitude)

    return jsonify({
        'converted_gda2020': {
            'easting': round(transformed_point_gda2020[0], 1),
            'northing': round(transformed_point_gda2020[1], 1)
        }
    })

if __name__ == '__main__':
    app.run(debug=True)
