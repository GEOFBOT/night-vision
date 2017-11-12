# pieced together from example code; plots the azimuth and altitude of Mars
# as viewed from Princeton over time.
# matplotlib polar plot example;
# skyfield alt/az example

# at the moment this 3D plots the paths of celestial bodies, and implements
# a little bit of vector math for projecting positions of celestial bodies
# onto a plane (for rendering into an image as would be viewed from the ground_

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from skyfield.api import load, Star
import skyfield

def altaz_to_spherical(alt, az):
    # horizon = alt>=0
    # alt = alt[horizon]
    # az = az[horizon]

    phi = np.pi / 2.0 - alt  # spherical is measured from top, not horizon
    theta = az
    rho = 1

    r = rho * np.sin(phi)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    z = rho * np.cos(phi)

    return x, y, z


def project(center_point, project_point):
    OP = center_point
    OQ = project_point
    PQ = np.subtract(OQ, OP)
    mag = lambda x: np.linalg.norm(x)
    proj_PQ_on_OP = np.multiply(np.dot(PQ, OP) / np.power(mag(OP), 2), OP)
    omega = np.subtract(PQ, proj_PQ_on_OP)
    omega_hat = np.divide(omega, mag(omega))
    theta = np.arccos(np.divide(np.dot(OP, OQ), mag(OP) * mag(OQ)))
    PQ_prime = np.multiply(mag(OP) * np.tan(theta), omega_hat)
    OP_prime = OP + PQ_prime
    return OP_prime

if __name__ == "__main__":
    planets = load('de421.bsp')
    # p = ['mercury', 'venus', 'mars',
    p = []#'jupiter barycenter', 'saturn barycenter']
    for i, p_ in enumerate(p):
        p[i] = planets[p_]
    earth, mars = planets['earth'], planets['mars']

    betelgeuse = skyfield.api.NamedStar('Betelgeuse')
    p.append(betelgeuse)
    polaris = skyfield.api.NamedStar('Polaris')
    p.append(polaris)
    ts = load.timescale()

    from skyfield.api import Topos

    PRINCETON_EARTH = Topos('40.3440 N', '74.6514 W')
    princeton = earth + PRINCETON_EARTH

    ax = plt.subplot(111, projection='3d')
    ax.set_aspect('equal')
    ax.set_xlim([-1.0,1.0])
    ax.set_ylim([-1.0,1.0])
    ax.set_zlim([-1.0,1.0])


    alt__ = np.repeat([0.0], 20)
    az__ = np.arange(0.0, 2*np.pi, 2.0/20.0*np.pi)
    ax.plot(*altaz_to_spherical(alt__, az__))
    ax.plot(*altaz_to_spherical(az__, alt__))
    ax.plot(*altaz_to_spherical(az__, alt__ + np.pi/2.0))

    # generate a field of view
    center_point = altaz_to_spherical(np.pi / 6, np.pi / 4.0) # point on sphere that is the center of our field of view
    ax.scatter(*center_point, marker='^')
    project_point = altaz_to_spherical(np.pi/3, np.pi / 4.0 + 0.2)
    ax.scatter(*project_point, marker='x')

    for planet in p:
        xs = []
        ys = []
        zs = []
        obs = princeton.at(ts.utc(2010, 1, range(1, 100))).observe(planet)

        alt, az, d = obs.apparent().altaz()

        alt_ = alt.radians
        az_ = az.radians
        pt = altaz_to_spherical(alt_, az_)
        # xs.append(pt[0])
        # ys.append(pt[1])
        # zs.append(pt[2])
        for pt__ in zip(*pt):
            ax.scatter(*project(center_point, pt__))
        ax.scatter(*pt)


    # project vector from project_point to center_point on vector from origin to center_point
    # QP = np.subtract(center_point, project_point)
    # dot = np.dot(QP, center_point)
    # projected = np.multiply(center_point,dot / np.power(np.linalg.norm(center_point), 2))
    # ax.scatter(*(project_point + projected), marker='+')
    # this projection is incorrect^

    ax.scatter(*project(center_point, project_point), marker='+')
    ax.scatter(0, 0, 0, marker='o')



    plt.show()
