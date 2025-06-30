# Arduino Code for Pan-Tilt Control via rosserial

This Arduino sketch receives pan and tilt angles from ROS topics via `rosserial` and controls two PWM-based servo motors.

## Connections
- Pan Servo → Pin 9
- Tilt Servo → Pin 10

## ROS Topics Subscribed
- `/pan_controller/command` – (std_msgs/Float64)
- `/tilt_controller/command` – (std_msgs/Float64)

## Setup Instructions
1. Install `rosserial_arduino`
2. Generate `ros_lib` with:
   ```
   rosrun rosserial_arduino make_libraries.py ~/Arduino/libraries
   ```
3. Upload sketch to Arduino
4. Run ROS serial node:
   ```
   rosrun rosserial_python serial_node.py _port:=/dev/ttyUSB0 _baud:=57600
   ```
