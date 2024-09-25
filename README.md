# STL_CONTROL_EXPERIMENT

&ensp;&ensp;This experiment demonstrates the controller design for nonholonomic vehicles in finishing Signal Temporal Logic (STL) tasks. It is conducted in a ROS (Noetic) environment on Linux (Ubuntu 18.04) and uses Vicon for motion tracking and positioning.

## Related Configuration

1.Nonholonomic Car Configuration

&ensp;&ensp;The experiment uses a differential drive robot with dimensions of 266 × 230 × 206 mm. The Raspberry Pi 4B acts as the ROS master, receiving commands and sending them to the STM32F407VET6 microcontroller through a serial connection. This microcontroller calculates and issues control commands for the robot's chassis. The robot is powered by MG513 metal gear reduction motors, allowing it to navigate around obstacles and complete Signal Temporal Logic (STL) tasks effectively.

<div align=center>  <img src=".\image\nonholonomic car.png" width=50%>

<div align=left>
2.Environment Configuration

&ensp;&ensp;The VICON coordinates: ENU; Car local coordinates: ENU.
&ensp;&ensp;The experimental area has dimensions of 8 × 11 meters. The nonholonomic mobile robot designates the starting point as the origin and acquires global positioning data through wireless telemetry from the Vicon system.

&ensp;&ensp;First, activate the chassis control node.

&ensp;&ensp;The following images depict the environmental setup for the obstacle scene. In contrast, the unobstructed scene is created by removing the obstacles.

<div align=center>  <img src=".\image\experiment environment.png" width=90%>

<div align=left>
  
## Launch

1.Formulating Signal Temporal Logic (STL) Tasks
```
roslaunch stl_control set_param.py
```

&ensp;&ensp;**Remark:**  Load the relevant parameters, including the specifications of the signal temporal logic tasks, as well as information regarding the positions and velocities of obstacles.

2.Run the Control Script:
```
rosrun stl_control stl_control_car.py
```
&ensp;&ensp;**Remark:**  Activate the control node. When the program begins, it will prompt you to confirm whether there are obstacles in the scene. You can press 'Y' or 'y' to indicate their presence, 'N' or 'n' to indicate their absence, and 'Q' or 'q' to exit.

## Data

1.Experiment with Obstacle Free Scenarios

[2024-09-22-15-36-25.bag](https://github.com/hzy-ui/Unicycle_STL_ROS/blob/main/data/2024-09-22-15-36-25.bag) is the correct data.

2.Experiment with Obstacle Scenarios

[2024-06-27-13-27-33.bag](https://github.com/hzy-ui/Unicycle_STL_ROS/blob/main/data/2024-06-27-13-27-33.bag) is the correct data.

## Videos
1.Experiment with Obstacle Free Scenarios

<!-- [Experiment Video](https://).
<video width="320" height="240" controls>
  <source src="[.mp4](https://)" type="video/mp4">
  Your browser does not support the video tag.
</video>-->

<iframe 
src="https://github.com/hzy-ui/Unicycle_STL_ROS/blob/main/videos/obstacles%20free%20scence.mp4" 
scrolling="no" 
border="0" 
frameborder="no" 
framespacing="0" 
allowfullscreen="true" 
height=600 
width=800> 
</iframe>

&ensp;&ensp;Please click the [link](https://github.com/hzy-ui/Unicycle_STL_ROS/blob/main/videos/obstacles%20free%20scence.mp4) to get access to the video with higher resolution.


2.Experiment with Obstacle Scenarios

<!-- [Experiment Video](https://).
<video width="320" height="240" controls>
  <source src="[mp4](https://)" type="video/mp4">
  Your browser does not support the video tag.
</video>-->

&ensp;&ensp;Please click the [link](https://github.com/hzy-ui/Unicycle_STL_ROS/blob/main/videos/Obstacle%20Scence.mp4) to get access to the video with higher resolution.





