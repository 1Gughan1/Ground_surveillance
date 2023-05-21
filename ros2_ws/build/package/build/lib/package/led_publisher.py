import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class LedController(Node):
    def __init__(self):
        super().__init__('led_controller')
        self.publisher_ = self.create_publisher(Int32, 'led_status', 10)
        self.get_logger().info('LED Controller Node Initialized')
        
    def get_user_input(self):
        while rclpy.ok():
            user_input = int(input("Enter 1 to turn on the LED or 0 to turn it off: "))
            if user_input == 0 or user_input == 1:
                msg = Int32()
                msg.data = user_input
                self.publisher_.publish(msg)
            else:
                self.get_logger().info('Invalid input. Please enter either 0 or 1.')

def main(args=None):
    rclpy.init(args=args)
    led_controller = LedController()
    led_controller.get_user_input()
    rclpy.spin(led_controller)
    led_controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

