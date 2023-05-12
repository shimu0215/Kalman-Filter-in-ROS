# Kalman-Filter-in-ROS
An simple implement of Kalman filter in ROS

This repo is construct based on topic covered by Tufts SP-23-CS-193-03 Intro to ROS.

This repo mainly covered two topics:
1. the use of server, client and message.
2. implement a Kalman Filter.

<img width="222" alt="ep1" src="https://github.com/shimu0215/Kalman-Filter-in-ROS/assets/67790259/af13647a-43c7-4c34-9f5e-7d077565ec64">

A server could implement complex functions and complete complex computational requests. It should be dedined as a sever and can use a custom message type as its return message type. And the client could be used to send a request.

The example of usage of server, client and message in sowed in msg and script file.

The method of Kalman filter is showing following. It is very useful in estimation in a robot with sensor and noises.

<img width="699" alt="截屏2023-05-11 21 41 43" src="https://github.com/shimu0215/Kalman-Filter-in-ROS/assets/67790259/d6554ff4-113f-4547-88dc-bb2cc93b3753">

In ROS, we can use a node to get input from user or get signal from sensors as an observation, than we can pass the information to a node or a server, and run the Kalman algorithm to update a new prediction, which is usually more accuracy than the old prediction. And the output can be pass to another node to help the following processing.

An example of the implement in ROS is also the script folder.

<img width="689" alt="截屏2023-05-11 21 51 12" src="https://github.com/shimu0215/Kalman-Filter-in-ROS/assets/67790259/1df44905-ffdf-4fe0-bf21-5c97ba281a45">

The structure of the nodes is on above.
