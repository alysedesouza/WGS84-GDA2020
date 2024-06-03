# Coordinate Conversion App

This is a Flask-based web application for converting coordinates between GDA94 and GDA2020 systems, specifically designed for Australian geographic zones 49 to 56. It provides a simple HTML interface to input Easting and Northing values and select a specific zone for the conversion.

## Features

- User-friendly web interface.
- Supports coordinate conversion for zones 49 to 56.
- Displays converted coordinates on the same page.

## Prerequisites

Before running this application, you need to have Python installed on your machine along with the Flask framework and the `pyproj` library.

### Installing Python

Download and install Python from [python.org](https://www.python.org/downloads/).

### Installing Flask and pyproj

After installing Python, you can install Flask and pyproj using pip:

```bash
pip install flask pyproj
```

### Project Structure

Copy code
/your_project_directory
│   app.py
|   readme.md

└───templates/
    │   index.html

### Running the Application

To run the application, navigate to the project directory and execute the following command in your terminal:

```bash
python app.py
```

The application will start running on http://127.0.0.1:5000/. Open this URL in your web browser to interact with the application.

### Usage

Select the zone for the coordinate conversion using the dropdown menu.
Enter the Easting and Northing values.
Click the "Submit" button to see the converted coordinates displayed below the input fields.

### API Endpoints

POST /convert_coordinates: This endpoint accepts JSON containing zone, eastings, and northings and returns the transformed easting and northing.

### Development

If you wish to further develop or contribute to this project, you can clone the repository and follow the setup steps outlined above.

### License

This project is open-sourced under the MIT license.

```bash
This Markdown text provides a comprehensive guide for users to set up, run, and understand your project. It can be placed in a `README.md` file in the root directory of your project. This file will be displayed on the main page of your repository on platforms like GitHub, providing a first point of contact for anyone who finds your project.
```
