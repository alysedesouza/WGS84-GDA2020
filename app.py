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
    source_crs = 4326
    destination_crs = 7800 + zone

    # Perform WGS84 to GDA2020 conversion
    transformer_wgs84_to_gda2020 = Transformer.from_crs(source_crs, destination_crs)
    transformed_point_gda2020 = transformer_wgs84_to_gda2020.transform(longitude, latitude)


    return jsonify({
        'converted_gda2020': {
            'easting': transformed_point_gda2020[0],
            'northing': transformed_point_gda2020[1]
        },
     
        }
    )

if __name__ == '__main__':
    app.run(debug=True)
