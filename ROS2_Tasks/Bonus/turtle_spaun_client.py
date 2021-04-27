#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.srv import Spawn

class my_server(Node):
    def __init__(self):
        super().__init__("Client_spawn_node")
        self.service_client(8,9,4)
        self.service_client(0,0,1)



    def service_client(self,x,y,theta):
        client=self.create_client(Spawn,"/spawn")
        while client.wait_for_service(4)==False:
            self.get_logger().warn("wating for server")

        request=Spawn.Request()
        request.x=float(x)
        request.y=float(y)
        request.theta=float(theta)
        futur_obj=client.call_async(request)
        futur_obj.add_done_callback(self.future_call)

    def future_call(self,future_msg):
        #self.get_logger().info(str(future_msg.result().sum))
        self.get_logger().info("Done !")
        


       


def main (args=None):
    rclpy.init(args=args)
    node1=my_server()
    rclpy.spin(node1)
    rclpy.shutdown()

if __name__ == "__main__":
    main()