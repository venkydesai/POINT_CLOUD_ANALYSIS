from typing import Tuple
import numpy as np

import utils


def q1_a(P: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    '''
    Fit a least squares plane by taking the Eigen values and vectors
    of the sample covariance matrix

    Attributes
    ----------
    P : np.ndarray
        Nx3 matrix denoting points in 3D space

    Returns
    -------
    normal : np.ndarray
        array of shape (3,) denoting surface normal of the fitting plane
    center : np.ndarray
        array of shape (3,) denoting center of the points
    '''

    ### Enter code below
    # c = np.array([0,1,0])
    # normal = np.array([0,0,1])
    c=np.mean(P,axis=0)
    c_P=P-c
    covar=np.cov(c_P,rowvar=False)
    eigen_val,eigen_vector=np.linalg.eigh(covar)
    
    normal=eigen_vector[:,0] #Assuimg  that the first column is the one with smallest eign value
    
    return normal, c


def q1_c(P: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    '''
    Fit a plane using RANSAC

    Attributes
    ----------
    P : np.ndarray
        Nx3 matrix denoting points in 3D space

    Returns
    -------
    normal : np.ndarray
        array of shape (3,) denoting surface normal of the fitting plane
    center : np.ndarray
        array of shape (3,) denoting center of the points
    '''
    
    ### Enter code below
    # center = np.array([0,1,0])
    # normal = np.array([0,0,1])
    iter=10^3
    num_samples=3
    delta=0.01
    max=0
    for i in range(iter):
        sample_set=P[np.random.choice(P.shape[0],num_samples, replace=False)]
        normal, center=q1_a(sample_set)
        dist=np.abs((P-center)@ normal)
        inliners=np.sum(dist < delta)
        
        if inliners > max:
            result=(normal,center)
            max=inliners
    return result