from typing import Tuple
import numpy as np
import utils


def q4_a(M: np.ndarray, D: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    '''
    Find transformation T such that D = T @ M. This assumes that M and D are
    corresponding (i.e. M[i] and D[i] correspond to same point)

    Attributes
    ----------
    M : np.ndarray
        Nx3 matrix of points
    D : np.ndarray
        Nx3 matrix of points

    Returns
    -------
    T : np.ndarray
        4x4 homogenous transformation matrix

    Hint
    ----
    use `np.linalg.svd` to perform singular value decomposition
    '''
    
    ### Enter code below
    # T = np.eye(4)
    M_mean=np.mean(M,axis=0)
    D_mean=np.mean(D,axis=0)
    
    # Subtract the corresponding center of mass from every point in the two sets
    centered_M=M-M_mean
    centered_D=D-D_mean
    
    # Computing the SVD of the centred matrices
    A=centered_M.T @ centered_D
    U,S,Vt=np.linalg.svd(A)
    R=U @ Vt
    t=M_mean-np.dot(R,D_mean)
    
    T=np.eye(4)
    T[0:3,0:3]=R
    T[0:3,3]=t
    return np.linalg.inv(T)


def q4_c(M: np.ndarray, D: np.ndarray) -> np.ndarray:
    '''
    Solves iterative closest point (ICP) to generate transformation T to best
    align the points clouds: D = T @ M

    Attributes
    ----------
    M : np.ndarray
        Nx3 matrix of points
    D : np.ndarray
        Nx3 matrix of points

    Returns
    -------
    T : np.ndarray
        4x4 homogenous transformation matrix

    Hint
    ----
    you should make use of the function `q4_a`
    '''

    ### Enter code below
    T = np.eye(4)
    itr = 100
    margin = 1e-8
    for i in range(itr):
        trans_M=utils.apply_transform(M,T)

        # Find the closest points in the destination cloud to each transformed point in the source cloud
        closestPts = []
        for j in range(M.shape[0]):
            distances = np.linalg.norm(D-trans_M[j, :3], axis=1)
            closestIdx = np.argmin(distances)
            closestPts.append(D[closestIdx])
        closestPts = np.array(closestPts)
        T_prev = T
        T = q4_a(M,closestPts)
        
        diff = np.abs(T - T_prev)
        if np.all(diff<margin):
            break
    return T
