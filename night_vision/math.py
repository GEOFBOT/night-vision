import numpy as np

def project(center_point, project_point):
    """
    Projects project_point onto the
    plane tangent to the sphere at center_point.
    """
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
