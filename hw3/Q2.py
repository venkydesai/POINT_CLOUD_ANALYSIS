from typing import Tuple
import numpy as np


def q2(P: np.ndarray, N: np.ndarray) -> Tuple[np.ndarray, float]:
    '''
    Localize a sphere in the point cloud. Given a point cloud as
    input, this function should locate the position and radius
    of a sphere

    Attributes
    ----------
    P : np.ndarray
        Nx3 matrix denoting points in 3D space
    N : np.ndarray
        Nx3 matrix denoting normals of pointcloud

    Returns
    -------
    center : np.ndarray
        array of shape (3,) denoting sphere center
    radius : float
        scalar radius of sphere
    '''

    ### Enter code below
    # center = np.array([1,0.5,0.1])
    # radius = 0.05
    delta=0.01
    max=0
    
    for i in range(5000):
        #(a) sample a point from the cloud;
        sample_Idx=np.random.choice(P.shape[0], 1, replace=False)
        sample_pt=P[sample_Idx]
        sample_normal=N[sample_Idx]
        
        #(b) sample a radius of the candidate sphere between 5 and 11cm;
        radius=np.random.uniform(0.05,0.11)
        
        # (c) project a vector from the sampled point in the direction of the associated surface normal for a distance equal to the sampled radius. This point would be at the center of the candidate sphere
        center=sample_pt[0]+(radius*sample_normal)[0]

        #RANSAC        
        dist=np.linalg.norm(P-center,axis=1)
        inliners_idx=np.where((dist < (radius+delta))& (dist > (radius-delta)))[0]
        inliners=len(inliners_idx)
        
        if inliners>max:
            max=inliners
            result=(center,radius)
    # print(result)
    return result