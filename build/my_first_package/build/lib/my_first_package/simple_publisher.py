# Contain the logic

import rclpy    # Import the rclpy library
from rclpy.node import Node  # Import the Node class from rclpy
from std_msgs.msg import String  # Import the String message type from std_msgs

class SimplePublisher(Node):    # Define a class that inherits from Node
    def __init__(self):  # Constructor method
        super().__init__('simple_publisher')  # Call the constructor of the parent class with the node name
        self.pub_ = self.create_publisher(String, "chatter", 10)
        self.counter_ = 0 # Initialize a counter
        self.frequency_ = 1.0 # Set the frequency to 1 Hz
        self.get_logger().info("Publishing at %d Hz" % self.frequency_)  # Log the frequency
        self.timer_ = self.create_timer(self.frequency_, self.timerCallback)
        
    def timerCallback(self):
        msg = String()
        msg.data = "Hello ROS2 - counter: %d" % self.counter_
        self.pub_.publish(msg)
        self.counter_ += 1

def main():
    rclpy.init()  # Initialize the rclpy library
    simple_publisher = SimplePublisher()  # Create an instance of the SimplePublisher class
    rclpy.spin(simple_publisher)  # Keep the node running until it is shut down
    simple_publisher.destroy_node()  # Destroy the node
    rclpy.shutdown()  # Shutdown the rclpy library
        
if __name__ == "__main__":
    main()
    