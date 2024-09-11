#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import String


class aggregator_node(Node):
    def __init__(self):
        super().__init__("aggregator_node")
        self.temp_subscriber=self.create_subscription(String,"temperature",self.temperature_recieval,10)
        self.humid_subscriber=self.create_subscription(String,"humidity",self.humidity_recieval,10)
        self.press_subscriber=self.create_subscription(String,"pressure",self.pressure_recieval,10)
        self.get_logger().info("aggregator node started")

    def temperature_recieval(self,msg):
        self.temperature=msg.data
        self.get_logger().info("Temperature: "+msg.data)

    def humidity_recieval(self,msg):
        self.humidity=msg.data
        self.get_logger().info("Humidity: "+ msg.data)

    def pressure_recieval(self,msg):
        self.pressure=msg.data
        self.get_logger().info("Pressure: "+msg.data)


def main(args=None):
    rclpy.init(args=args)

    node=aggregator_node()
    rclpy.spin(node)

    rclpy.shutdown()