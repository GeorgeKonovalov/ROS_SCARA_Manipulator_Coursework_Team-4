#! /usr/bin/env python3
 
"""
Description:
    Node that subscribes to the Hello World topic.
-------
Publishing Topics:
    None
-------
Subscription Topics:
    /py_example_topic - std_msgs/String
"""
 
import rclpy  # ros 2 client library for python
from rclpy.node import Node  # ros 2 node class
from std_msgs.msg import String  # import sting message library
 
 
class ExampleSubscriber(Node):
    """Create Example Subscriber node"""
 
    def __init__(self):
        """ Create a custom node class for subscribing"""

        super().__init__('example_py_subscriber') #initialise node
 
        # create a subscriber
        self.subscriber_1 = self.create_subscription(
            String,
            '/py_example_topic',
            self.listener_callback,
            10)
 
    def listener_callback(self, msg):
        """Call this function every time a new message is published on the topic."""
        self.get_logger().info(f'I heard: "{msg.data}"') #log a message
 
 
def main(args=None):
    """Main function to start the ROS 2 node"""
 
    rclpy.init(args=args) # initialise ros2 communication
 
    minimal_py_subscriber = ExampleSubscriber() # create instance of subscriber node
 
    rclpy.spin(minimal_py_subscriber) # keep node running
 
    minimal_py_subscriber.destroy_node() #get rid of node

    rclpy.shutdown() #close communication
 
 
if __name__ == '__main__':
    main() # run main