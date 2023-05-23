import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
import socket
import threading
import sys
import termios
import tty

class LedPublisher(Node):
    def __init__(self):
        super().__init__('led_publisher')
        self.publisher_ = self.create_publisher(Int32, 'led_status', 10)
        self.timer_ = self.create_timer(0.1, self.publish_led_status)
        self.led_status_ = 0
        self.is_key_pressed = False
        self.esp32_ip = '172.20.10.2'  # Replace with the actual IP address of the ESP32
        self.esp32_port = 5000
        self.get_logger().info('LED Publisher Node Initialized')

    def publish_led_status(self):
        msg = Int32()
        msg.data = self.led_status_
        self.publisher_.publish(msg)

    def getch(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            char = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return char

    def check_user_input(self):
        while True:
            char = self.getch()
            if char == 'w' and not self.is_key_pressed:
                self.is_key_pressed = True
                self.led_status_ = 1
                self.send_to_esp32(1)
            elif char == 's' and not self.is_key_pressed:
                self.is_key_pressed = True
                self.led_status_ = 2
                self.send_to_esp32(2)
            elif char != ' ' and self.is_key_pressed:
                self.is_key_pressed = False
                self.led_status_ = 0
                self.send_to_esp32(0)

    def send_to_esp32(self, user_input):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((self.esp32_ip, self.esp32_port))
            sock.sendall(str(user_input).encode())
            sock.close()
        except socket.error as e:
            self.get_logger().info(f'Error connecting to ESP32: {e}')

    def run(self):
        thread = threading.Thread(target=self.check_user_input)
        thread.start()

def main(args=None):
    rclpy.init(args=args)
    led_publisher = LedPublisher()
    led_publisher.run()
    rclpy.spin(led_publisher)
    led_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

