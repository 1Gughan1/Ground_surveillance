import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class LedSubscriber(Node):
    def __init__(self):
        super().__init__('led_subscriber')
        self.subscription = self.create_subscription(
            Int32,
            'led_status',
            self.callback,
            10
        )
        self.subscription

    def callback(self, msg):
        if msg.data == 1:
            self.turn_on_led()
        elif msg.data == 0:
            self.turn_off_led()
        else:
            self.get_logger().warn('Invalid LED status received: {}'.format(msg.data))

    def turn_on_led(self):
        # Code to turn on the LED
        self.get_logger().info('LED turned on')

    def turn_off_led(self):
        # Code to turn off the LED
        self.get_logger().info('LED turned off')

def main(args=None):
    rclpy.init(args=args)
    led_subscriber = LedSubscriber()
    rclpy.spin(led_subscriber)
    led_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

