from datetime import datetime

from flask import Flask, jsonify, abort
from skyfield import api as skyapi
from skyfield import named_stars

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


load = skyapi.Loader('./data')
ts = load.timescale()
planets = load('de405.bsp')
earth = planets['earth']
PRINCETON_EARTH = skyapi.Topos('40.3440 N', '74.6514 W')

STARS = [skyapi.NamedStar(star) for star in named_stars.named_star_dict.keys()]


def star_data(stars, loc, time):
    altaz = [loc.at(time).observe(s).apparent().altaz() for s in stars]
    return [(altaz_[0].degrees, altaz_[1].degrees) for altaz_ in altaz]
    # data = []
    # for star in stars:
    #     obs = princeton.at(now).observe(s)
    #     alt, az, d = obs.apparent().altaz()
    #     data.append((alt.radians, az.radians))

    # return data


@app.route('/data/<int:time>/<string:lat>/<string:long>')
# TODO: /<float:azi>/<float:alt>/<float:radius>')
def get_data(time, lat, long):  # , azi, alt, radius):
    """Returns star data near a certain position"""
    # As of yet, does literally none of that.
    try:
        lat = float(lat)
        long = float(long)
    except ValueError:
        print('wow')
        abort(404)

    location = earth + skyapi.Topos(lat, long)
    dt = datetime.fromtimestamp(time)
    dt = dt.replace(tzinfo=skyapi.utc)
    t = ts.utc(dt)

    return jsonify({
        'type': 'FeatureCollection',
        'features': [{
            'geometry': {
                'type': 'Point',
                'coordinates': [star_az, star_alt],
            },
            'type': 'Feature',
            'properties': {'mag': 1.337}
        } for star_az, star_alt in star_data(STARS, location, t)]
    })


if __name__ == '__main__':
    app.run()
