import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class LedSubscriber(Node):
    def __init__(self):
        super().__init__('led_subscriber')
        self.subscription = self.create_subscription(
            Int32,
            'led_status',
            self.led_status_callback,
            10
        )
        self.subscription

    def led_status_callback(self, msg):
        led_status = msg.data
        if led_status == 1:
            self.turn_on_led()
        elif led_status == 0:
            self.turn_off_led()

    def turn_on_led(self):
        # Perform the action to turn on the LED
        print("LED turned on")

    def turn_off_led(self):
        # Perform the action to turn off the LED
        print("LED turned off")

def main(args=None):
    rclpy.init(args=args)
    led_subscriber = LedSubscriber()
    rclpy.spin(led_subscriber)
    led_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

