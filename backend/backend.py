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

# STARS = []
# for star in named_stars.named_star_dict.keys():
#     s = skyapi.NamedStar(star)
#     STARS.append(s)
#     print("{'name':'"+star+"','ra_hour':"+str(s.ra.hours)+",'dec_deg':"+str(s.dec.degrees)+"}")
STAR_DATA = [
{'name':'Achernar','ra_hour':1.62856849099,'dec_deg':-57.236757486},
{'name':'Acrux','ra_hour':12.4433043895,'dec_deg':-63.099091662},
{'name':'Adhara','ra_hour':6.97709678778,'dec_deg':-28.972083744},
{'name':'Agena','ra_hour':14.0637234673,'dec_deg':-60.3730393096},
{'name':'Albireo','ra_hour':19.5120223853,'dec_deg':27.959681116},
{'name':'Alcor','ra_hour':13.4204272104,'dec_deg':54.9879576653},
{'name':'Aldebaran','ra_hour':4.59867740677,'dec_deg':16.5093013899},
{'name':'Alderamin','ra_hour':21.3096587459,'dec_deg':62.5855726107},
{'name':'Algenib','ra_hour':3.40538065295,'dec_deg':49.8611795912},
{'name':'Algieba','ra_hour':10.332876237,'dec_deg':19.8414887349},
{'name':'Algol','ra_hour':3.13614765679,'dec_deg':40.9556477},
{'name':'Alhena','ra_hour':6.62852808276,'dec_deg':16.3992521672},
{'name':'Alioth','ra_hour':12.9004859519,'dec_deg':55.9598211584},
{'name':'Alkaid','ra_hour':13.792343788,'dec_deg':49.3132650597},
{'name':'Almach','ra_hour':2.06498696435,'dec_deg':42.3297247262},
{'name':'Alnair','ra_hour':22.1372181866,'dec_deg':-46.9609754326},
{'name':'Alnilam','ra_hour':5.60355928949,'dec_deg':-1.20191982639},
{'name':'Alnitak','ra_hour':5.6793130949,'dec_deg':-1.94257223639},
{'name':'Alphard','ra_hour':9.45978979835,'dec_deg':-8.65860253403},
{'name':'Alphecca','ra_hour':15.5781300323,'dec_deg':26.7146930207},
{'name':'Alpheratz','ra_hour':0.13979404756,'dec_deg':29.0904319904},
{'name':'Altair','ra_hour':19.8463886105,'dec_deg':8.86832198407},
{'name':'Aludra','ra_hour':7.40158403734,'dec_deg':-29.3031036025},
{'name':'Ankaa','ra_hour':0.438069714149,'dec_deg':-42.3059815091},
{'name':'Antares','ra_hour':16.4901280308,'dec_deg':-26.4320024932},
{'name':'Arcturus','ra_hour':14.2610200068,'dec_deg':19.1824102958},
{'name':'Arided','ra_hour':20.6905318726,'dec_deg':45.2803379974},
{'name':'Aridif','ra_hour':20.6905318726,'dec_deg':45.2803379974},
{'name':'Aspidiske','ra_hour':9.28483518728,'dec_deg':-59.2752292854},
{'name':'Atria','ra_hour':16.8110819091,'dec_deg':-69.0277150438},
{'name':'Avior','ra_hour':8.37523210699,'dec_deg':-59.5094830677},
{'name':'Becrux','ra_hour':12.7953508702,'dec_deg':-59.6887636195},
{'name':'Bellatrix','ra_hour':5.41885085076,'dec_deg':6.34970223222},
{'name':'Benetnash','ra_hour':13.792343788,'dec_deg':49.3132650597},
{'name':'Betelgeuse','ra_hour':5.91952923974,'dec_deg':7.40706273583},
{'name':'Birdun','ra_hour':13.6647940006,'dec_deg':-53.4663937768},
{'name':'Canopus','ra_hour':6.39919718665,'dec_deg':-52.6956604587},
{'name':'Capella','ra_hour':5.27815529327,'dec_deg':45.9979911065},
{'name':'Caph','ra_hour':0.152968075417,'dec_deg':59.1497795955},
{'name':'Castor','ra_hour':7.57662855631,'dec_deg':31.8882762889},
{'name':'Deneb','ra_hour':20.6905318726,'dec_deg':45.2803379974},
{'name':'Deneb Kaitos','ra_hour':0.72649196011,'dec_deg':-17.9866045956},
{'name':'Denebola','ra_hour':11.8176604374,'dec_deg':14.5720603181},
{'name':'Diphda','ra_hour':0.72649196011,'dec_deg':-17.9866045956},
{'name':'Dschubba','ra_hour':16.0055572947,'dec_deg':-22.6217099275},
{'name':'Dubhe','ra_hour':11.0621301925,'dec_deg':61.7510332011},
{'name':'Durre Menthor','ra_hour':1.73446747585,'dec_deg':-15.9374800618},
{'name':'Elnath','ra_hour':5.4381981661,'dec_deg':28.6074500086},
{'name':'Enif','ra_hour':21.7364328095,'dec_deg':9.87501126416},
{'name':'Etamin','ra_hour':17.9434360755,'dec_deg':51.4888949857},
{'name':'Fomalhaut','ra_hour':22.9608462482,'dec_deg':-29.6222361527},
{'name':'Foramen','ra_hour':19.0049327596,'dec_deg':-55.0155809993},
{'name':'Gacrux','ra_hour':12.5194331392,'dec_deg':-57.1132116887},
{'name':'Gemma','ra_hour':15.5781300323,'dec_deg':26.7146930207},
{'name':'Gienah','ra_hour':20.7701896485,'dec_deg':33.9702560995},
{'name':'Girtab','ra_hour':17.6219807239,'dec_deg':-42.997823859},
{'name':'Gruid','ra_hour':22.7111251877,'dec_deg':-46.8845769008},
{'name':'Hadar','ra_hour':14.0637234673,'dec_deg':-60.3730393096},
{'name':'Hamal','ra_hour':2.11955752884,'dec_deg':23.4624231271},
{'name':'Herschel\'s Garnet Star','ra_hour':21.7251280121,'dec_deg':58.78004608},
{'name':'Izar','ra_hour':14.7497826954,'dec_deg':27.074222441},
{'name':'Kaus Australis','ra_hour':18.4028662008,'dec_deg':-34.3846161104},
{'name':'Kochab','ra_hour':14.8450906704,'dec_deg':74.1555049077},
{'name':'Koo She','ra_hour':8.74506288129,'dec_deg':-54.708821088},
{'name':'Marchab','ra_hour':23.079348273,'dec_deg':15.2052644155},
{'name':'Marfikent','ra_hour':14.5917843904,'dec_deg':-42.1578244672},
{'name':'Markab','ra_hour':9.36856064476,'dec_deg':-55.0106679905},
{'name':'Megrez','ra_hour':12.2571000341,'dec_deg':57.0326169018},
{'name':'Men','ra_hour':14.6988210054,'dec_deg':-47.388200138},
{'name':'Menkalinan','ra_hour':5.99214525921,'dec_deg':44.9474327809},
{'name':'Menkent','ra_hour':14.1113745716,'dec_deg':-36.3699544516},
{'name':'Merak','ra_hour':11.0306879996,'dec_deg':56.3824267864},
{'name':'Miaplacidus','ra_hour':9.21999319072,'dec_deg':-69.7172077347},
{'name':'Mimosa','ra_hour':12.7953508702,'dec_deg':-59.6887636195},
{'name':'Mintaka','ra_hour':5.53344464527,'dec_deg':-0.299092038889},
{'name':'Mira','ra_hour':2.32244241144,'dec_deg':-2.97764261944},
{'name':'Mirach','ra_hour':1.16220099507,'dec_deg':35.6205576976},
{'name':'Mirfak','ra_hour':3.40538065295,'dec_deg':49.8611795912},
{'name':'Mirzam','ra_hour':6.37832924568,'dec_deg':-17.9559177224},
{'name':'Mizar','ra_hour':13.3987619203,'dec_deg':54.9253617524},
{'name':'Muhlifein','ra_hour':12.6919551678,'dec_deg':-48.9598884446},
{'name':'Murzim','ra_hour':6.37832924568,'dec_deg':-17.9559177224},
{'name':'Naos','ra_hour':8.05973518785,'dec_deg':-40.0031476995},
{'name':'Nunki','ra_hour':18.9210904776,'dec_deg':-26.2967222487},
{'name':'Peacock','ra_hour':20.427460509,'dec_deg':-56.7350901024},
{'name':'Phad','ra_hour':11.8971798481,'dec_deg':53.6947600842},
{'name':'Phecda','ra_hour':11.8971798481,'dec_deg':53.6947600842},
{'name':'Polaris','ra_hour':2.5303010235,'dec_deg':89.2641095074},
{'name':'Pollux','ra_hour':7.7552639885,'dec_deg':28.0261986152},
{'name':'Procyon','ra_hour':7.65503286731,'dec_deg':5.22499306341},
{'name':'Ras Alhague','ra_hour':17.5822418217,'dec_deg':12.5600347739},
{'name':'Rasalhague','ra_hour':17.5822418217,'dec_deg':12.5600347739},
{'name':'Regor','ra_hour':8.15887506679,'dec_deg':-47.3365877075},
{'name':'Regulus','ra_hour':10.1395307402,'dec_deg':11.9672070633},
{'name':'Rigel','ra_hour':5.24229787481,'dec_deg':-8.20164055111},
{'name':'Rigel Kent','ra_hour':14.6601377226,'dec_deg':-60.8339746814},
{'name':'Rigil Kentaurus','ra_hour':14.6601377226,'dec_deg':-60.8339746814},
{'name':'Sabik','ra_hour':17.1729687014,'dec_deg':-15.7249102262},
{'name':'Sadira','ra_hour':3.54884560601,'dec_deg':-9.45826215473},
{'name':'Sadr','ra_hour':20.3704727466,'dec_deg':40.2566792396},
{'name':'Saiph','ra_hour':5.79594134878,'dec_deg':-9.66960477667},
{'name':'Sargas','ra_hour':17.6219807239,'dec_deg':-42.997823859},
{'name':'Scheat','ra_hour':23.0629048673,'dec_deg':28.0827890878},
{'name':'Schedar','ra_hour':0.675122365203,'dec_deg':56.5373310888},
{'name':'Scutulum','ra_hour':9.28483518728,'dec_deg':-59.2752292854},
{'name':'Shaula','ra_hour':17.5601444405,'dec_deg':-37.1038211451},
{'name':'Sirius','ra_hour':6.75247702577,'dec_deg':-16.7161158193},
{'name':'Sirrah','ra_hour':0.13979404756,'dec_deg':29.0904319904},
{'name':'South Star','ra_hour':21.1463460105,'dec_deg':-88.9564989967},
{'name':'Spica','ra_hour':13.419883134,'dec_deg':-11.1613220315},
{'name':'Suhail','ra_hour':9.13326623837,'dec_deg':-43.4325893516},
{'name':'Thuban','ra_hour':14.0731527143,'dec_deg':64.3758505109},
{'name':'Toliman','ra_hour':14.6601377226,'dec_deg':-60.8339746814},
{'name':'Tseen She','ra_hour':19.0049327596,'dec_deg':-55.0155809993},
{'name':'Tsih','ra_hour':0.945147702604,'dec_deg':60.7167403752},
{'name':'Turais','ra_hour':9.28483518728,'dec_deg':-59.2752292854},
{'name':'Vega','ra_hour':18.6156490071,'dec_deg':38.7836917958},
{'name':'Wei','ra_hour':16.8360591595,'dec_deg':-34.2932317131},
{'name':'Wezen','ra_hour':7.13985673788,'dec_deg':-26.3931996662},

]

STARS = [skyapi.Star(ra_hours=s['ra_hour'], dec_degrees=s['dec_deg']) for s in STAR_DATA]


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
    dt = datetime.fromtimestamp(time // 1000)
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
