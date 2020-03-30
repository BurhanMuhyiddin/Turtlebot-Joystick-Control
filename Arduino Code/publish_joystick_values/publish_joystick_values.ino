//sudo chmod a+rw /dev/ttyUSB0
//rosrun rosserial_python serial_node.py /dev/ttyUSB0

#include <ros.h>
#include <joystick_msgs/JoystickMsg.h>

// Connection of Joystick pins to the Arduino Uno Board
// key - digital pin 2
// x   - analog  pin 0
// y   - analog  pin 1
// VCC - 5V pin
// GND - GND pin

#define x_dir A0
#define y_dir A1
#define buttn 2

ros::NodeHandle  nh;

joystick_msgs::JoystickMsg j_msg; // user defined message for the joystick

ros::Publisher joystick_publisher("joystick_publisher", &j_msg); // topic to publish the joystick values

void setup()
{
  pinMode(buttn, INPUT);
  nh.initNode();
  nh.advertise(joystick_publisher);
}

void loop()
{
  // Read the Joystick x and y values and publish to the "joystick_publisher" topic

  int x_val = analogRead(x_dir);
  int y_val = analogRead(y_dir);
  
  j_msg.x = x_val;
  j_msg.y = y_val;
  j_msg.is_pressed = false;

  joystick_publisher.publish(&j_msg);
  nh.spinOnce();
  delay(50);
}
