#!/usr/bin/env python3

import rclpy
import random
from rclpy.node import Node
from example_interfaces.msg import String

class h_publisher_node(Node):
    def __init__(self):
        super().__init__("humidity_node")
        self.humidity_publisher=self.create_publisher(String,"humidity",10)
        self.get_logger().info("humidity node started")
        self.value=random.randint(-50,200)
        msg=String()
        msg.data=str(self.value)
        self.humidity_publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)

    node=h_publisher_node()
    rclpy.spin(node)

    rclpy.shutdown()