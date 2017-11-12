from flask import Flask, jsonify
from skyfield import api as skyapi
from skyfield import named_stars

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


PRINCETON_EARTH = skyapi.Topos('40.3440 N', '74.6514 W')


def star_data(stars):
    load = skyapi.Loader('./data')
    planets = load('de405.bsp')
    earth = planets['earth']
    princeton = earth + PRINCETON_EARTH
    ts = load.timescale()
    now = ts.now()

    data = []

    for star in stars:
        s = skyapi.NamedStar(star)
        obs = princeton.at(now).observe(s)
        alt, az, d = obs.apparent().altaz()
        data.append((alt.radians, az.radians))

    return data


STARS = ['Polaris', 'Betelgeuse']
STAR_DATA = star_data(named_stars.named_star_dict.keys())


@app.route('/data/<float:azi>/<float:alt>/<float:radius>')
def get_data(azi, alt, radius):
    """Returns star data near a certain position"""
    # As of yet, does literally none of that.

    return jsonify({
        'type': 'FeatureCollection',
        'features': [{
            'geometry': {
                'type': 'Point',
                'coordinates': [star_az * 360.0 / 2.0 / 3.141592,
                                star_alt * 360.0 / 2.0 / 3.141592],
            },
            'type': 'Feature',
            'properties': {'mag': 1.337}
        } for star_az, star_alt in STAR_DATA]  # STARS)]
    })


if __name__ == '__main__':
    app.run()
