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
    eastings = float(data['eastings'])
    northings = float(data['northings'])

    # Define source and destination CRS codes for GDA94 to GDA2020 conversion
    source_crs = 28300 + zone
    destination_crs = 7800 + zone

    # Perform GDA94 to GDA2020 conversion
    transformer_gda94_to_gda2020 = Transformer.from_crs(source_crs, destination_crs)
    transformed_point_gda2020 = transformer_gda94_to_gda2020.transform(eastings, northings)

    # Convert GDA2020 coordinates to WGS84 lat-long
    transformer_gda2020_to_wgs84 = Transformer.from_crs(destination_crs, 4326)
    wgs84_lat_long = transformer_gda2020_to_wgs84.transform(transformed_point_gda2020[0], transformed_point_gda2020[1])

    return jsonify({
        'converted_gda2020': {
            'easting': transformed_point_gda2020[0],
            'northing': transformed_point_gda2020[1]
        },
        'wgs84_lat_long': {
            'latitude': wgs84_lat_long[0],
            'longitude': wgs84_lat_long[1]
        }
    })

if __name__ == '__main__':
    app.run(debug=True)
