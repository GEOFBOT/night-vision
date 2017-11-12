import numpy as np

class Almanac(object):
    """Handles retrieving data about stars."""

    stars = {}

    def __init__(self):
        pass

    def add_star(self, id, star):
        """

        :param id: identifier for this star
        :param star: Skyfield Star object
        :return:
        """
        self.stars[id] = BallOfGas(id, star)

class BallOfGas(object):
    """Wrapper for star data."""
    def __init__(self, id, star):
        self._id = id
        self._star = star

    def observe(self, time, location):
        """
        Returns x,y,z coordinates on a unit sphere of the star, relative
        to the viewer's location at a certain time.
        """
        obs = location.at(time).observe(self._star)
        altaz = obs.apparent().altaz()
        return BallOfGas._altaz_to_spherical(altaz)

    @staticmethod
    def _altaz_to_spherical(altaz):
        """Converts from altitude/azimuth to Cartesian coordinates."""
        alt = altaz[0].radians
        az = altaz[1].radians

        # Interpret as spherical coordinates
        phi = np.pi / 2.0 - alt  # spherical is measured from top, not horizon
        theta = az
        rho = 1

        r = rho * np.sin(phi)
        x = r * np.cos(theta)
        y = r * np.sin(theta)
        z = rho * np.cos(phi)

        return x, y, z
