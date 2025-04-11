# this is a new node inside our package
import rclpy    # Import the rclpy library
from rclpy.node import Node  # Import the Node class from rclpy
from std_msgs.msg import String  # Import the String message type from std_msgs

class SimpleSubscriber(Node):
    def __init__(self):
        super().__init__('simple_subscriber')
        self.sub_ = self.create_subscription(String, "chatter", self.listenerCallback, 10)        
        self.get_logger().info("Simple subscriber initialized")
        
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
    
