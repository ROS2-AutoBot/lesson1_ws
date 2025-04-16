# This is a another node inside our package. 
# This is a node that subscribes to messages from the "chatter" topic.
import rclpy    # Import the rclpy library
from rclpy.node import Node  # Import the Node class from rclpy
from std_msgs.msg import String  # Import the String message type from std_msgs

class SimpleSubscriber(Node): # Define a class that inherits from Node class
    def __init__(self): # Constructor method
        super().__init__('simple_subscriber') # Call the constructor of the parent class with the node name
        self.sub_ = self.create_subscription(String, "chatter", self.listenerCallback, 10) # Create a subscription to the "chatter" topic        
        self.get_logger().info("Simple subscriber initialized") # Log that the subscriber has been initialized
        
    def listenerCallback(self, msg):
        self.get_logger().info("I heard: %s" % msg.data)
        
def main():
    rclpy.init()
    simple_subscriber = SimpleSubscriber()
    rclpy.spin(simple_subscriber)
    simple_subscriber.destroy_node()
    rclpy.shutdown()
    
if __name__ == "__main__":
    main()
    
