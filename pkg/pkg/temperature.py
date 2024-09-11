#!/usr/bin/env python3

import rclpy
import random
from rclpy.node import Node
from example_interfaces.msg import String

class publisher_node(Node):
    def __init__(self):
        super().__init__("temperature_node")
        self.temperature_publisher=self.create_publisher(String,"temperature",10)
        self.get_logger().info("temperature node started")
        self.value=random.randint(-50,200)
        msg=String()
        msg.data=str(self.value)
        self.temperature_publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)

    node=publisher_node()
    rclpy.spin(node)

    rclpy.shutdown()