import numpy as np

def is_rotation_matrix(R, tol=1e-5):

    #  R^T * R should be close to the identity matrix
    should_be_identity = np.dot(R.T, R)
    I = np.identity(3)
    if not np.allclose(should_be_identity, I, atol=tol):
        return False
    
    #  if the determinant is +1
    det = np.linalg.det(R)
    if not np.isclose(det, 1.0, atol=tol):
        return False
    
    return True

#  matrix example
R = np.array([[0.8660254, -0.5, 0],
              [0.5, 0.8660254, 0],
              [0, 0, 1]])

#  if the matrix is a valid rotation matrix
print(is_rotation_matrix(R)) 