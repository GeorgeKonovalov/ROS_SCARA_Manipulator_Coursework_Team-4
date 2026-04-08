#! /usr/bin/env python3
 
"""
Description:
    This ROS node periodically publishes "Hello World" messages on a topic according to timer.
-------
Publishing Topics:
    /py_example_topic - std_msgs/String
-------
Subscription Topics:
    None
"""
 
import rclpy  # ros 2 client library for python
from rclpy.node import Node  # ros 2 node class
from std_msgs.msg import String  # import sting message library
 
 
class ExamplePyPublisher(Node):
    """Create ExamplePyPublisher node"""
 
    def __init__(self):
        """ Create a custom node class for publishing messages"""
 
        super().__init__('example_py_publisher') # initialize the node 
 
        # creates a publisher on the topic "py_example_topic" with a queue size of 5 messages
        self.publisher_1 = self.create_publisher(String, '/py_example_topic', 5)
 
        # timer to trigger the callback function (it is in seconds)
        timer_period = 0.5 
        self.timer = self.create_timer(timer_period, self.timer_callback)
 
        self.i = 0 # initialise a counter variable for message content

    def timer_callback(self):
        """Callback function executed periodically by the timer"""

        msg = String() # string object message 
        msg.data = 'Hello World: %d' % self.i
 
        self.publisher_1.publish(msg) # publish the message on the topic
 
        self.get_logger().info('Publishing: "%s"' % msg.data) # log a message
 
        self.i = self.i + 1 # increment counter
 
 
def main(args=None):
    """Main function to start the ROS 2 node"""
 
    rclpy.init(args=args) # initialise ROS 2 communication
 
    example_py_publisher = ExamplePyPublisher() # create an instance of the ExamplePyPublisher node
 
    rclpy.spin(example_py_publisher) # keep the node running and processing events
 
    example_py_publisher.destroy_node() # destroy the node explicitly
 
    rclpy.shutdown() # shutdown ROS 2 communication
 
 
if __name__ == '__main__':
    main() # Run main