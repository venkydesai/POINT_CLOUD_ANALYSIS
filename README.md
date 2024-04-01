# POINT CLOUD ANALYSIS

This repository is my Assignment for a course CS5335 @ Northeastern University

## Results

1) You are given a set P of 100 points and asked to fit a plane to these points. The output of these functions should be a point intercept of the plane (a vector called “center”) and the plane surface normal (a vector called “normal”)

![](https://github.com/venkydesai/RANSAC_cloud_points/blob/main/Results/Figure_1(a).png)
![](https://github.com/venkydesai/RANSAC_cloud_points/blob/main/Results/Figure_1(b).png)
![](https://github.com/venkydesai/RANSAC_cloud_points/blob/main/Results/Figure_1(c).png)

2) You must use RANSAC to localize a sphere given point cloud data. The point cloud contains a ball that is only partially visible to the sensor. The position of the center of the ball is unknown. The radius is unknown but between 5cm (0.05m) and 11cm (0.11m)

![Sphere point cloud](https://github.com/venkydesai/RANSAC_cloud_points/blob/main/Results/Figure_2.png)

3) This question is harder because you need to calculate the center, the orientation, and the radius (between 0.05m and 0.1m). The orientation should be returned in the form of a unit vector pointing along the axis of the cylinder (either direction is fine)

![Cylinder point cloud](https://github.com/venkydesai/RANSAC_cloud_points/blob/main/Results/Figure_3.png)


4) Given a set of points M, and another a set of points D with a different pose, ICP algorithm could be used to find a 4-by-4 transformation matrix T so that D = TM

![](https://github.com/venkydesai/RANSAC_cloud_points/blob/main/Results/Figure_4(a).png)

(b) Noise and Shuffle

![](https://github.com/venkydesai/RANSAC_cloud_points/blob/main/Results/Figure_4(b).png)

(c) when the order of the points is shuffled

![](https://github.com/venkydesai/RANSAC_cloud_points/blob/main/Results/Figure_4(c).png)


