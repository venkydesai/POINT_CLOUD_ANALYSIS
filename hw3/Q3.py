from typing import Tuple
import numpy as np


def q3(P: np.ndarray, N: np.ndarray) -> Tuple[np.ndarray, np.ndarray, float]:
    '''
    Localize a cylinder in the point cloud. Given a point cloud as
    input, this function should locate the position, orientation,
    and radius of the cylinder

    Attributes
    ----------
    P : np.ndarray
        Nx3 matrix denoting 100 points in 3D space
    N : np.ndarray
        Nx3 matrix denoting normals of pointcloud

    Returns
    -------
    center : np.ndarray
        array of shape (3,) denoting cylinder center
    axis : np.ndarray
        array of shape (3,) pointing along cylinder axis
    radius : float
        scalar radius of cylinder
    '''

    
    ### Enter code below
    # center = np.array([1,0.5,0.1])
    # axis = np.array([0,0,1])
    # radius = 0.05
    itr=5000
    delta=0.001
    max=0
    for i in range(itr):
        #(a) Sample a radius for the candidate cylinder between 5 and 10 cm.
        radius=np.random.uniform(0.05,0.10)
        
        # (b) Sample two points from the cloud.
        sample_Idx=np.random.choice(P.shape[0], 2, replace=False)
        sample_pt=P[sample_Idx]
        sample_normal=N[sample_Idx]
        
        #(c) Set the cylinder axis direction equal to the direction of the cross product between the surface normals associated with the two sampled points.
        cyl_axis=np.cross(sample_normal[0], sample_normal[1])
        cyl_axis/=np.linalg.norm(cyl_axis)
        
        #(d) Pick one of the sampled points from the cloud and use it to estimate a candidate center, just as you did in Q1.
        vector=radius*sample_normal
        choice = np.random.choice([0, 1])
        center=sample_pt[choice] + vector[choice]
        
        # (e) Project the points in the cloud onto the plane orthogonal to the axis you just calculated. You can do this projection by multiplying the points in the cloud by this matrix: I − aˆaˆT , where aˆ is equal to the axis of the cylinder. Also project the candidate center into this plane in the same way.
        
        I=np.identity(3)
        proj=I-np.dot(cyl_axis.reshape(3,1),cyl_axis.reshape(3,1).T)
        proj_points=np.dot(P,proj)
        proj_center=np.dot(center,proj)
        
        #(f) Evaluate number of inliers in the plane for a circle with the given projected center and the sampled radius.
        
        dist=np.linalg.norm(proj_points-proj_center,axis=1)
        inliners_idx=np.where((dist < (radius+delta))& (dist > (radius-delta)))[0]
        inliners=len(inliners_idx)
        
        if inliners>max:
            max=inliners
            result=(center,cyl_axis, radius)
    return result