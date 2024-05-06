import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.srv import Spawn, Kill, SetPen
import time

class Estrelinha(Node):
    def __init__(self):
        super().__init__('estrelinha')
        self.spawn_client = self.create_client(Spawn, '/spawn')
        self.kill_client = self.create_client(Kill, '/kill')
        self.pen_client = self.create_client(SetPen, '/turtle1/set_pen')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        time.sleep(2)  # Timerzin

    def desenhandinho(self):
        # Trazendo uma nova tartaruguinha ao mundo
        spawn_future = self.spawn_client.call_async(Spawn.Request(x=8.0, y=8.0, theta=0.0, name='turtle2'))
        rclpy.spin_until_future_complete(self, spawn_future)
        new_turtle_name = spawn_future.result().name

        # Usando o setpen para definir a cor e a largura da linha
        set_pen = SetPen.Request(r=218, g=165, b=32, width=2, off=0)
        self.pen_client.call_async(set_pen)

        # Lista de coordenadas para fazer a estrela
        starPoints = starPoints = [(3.0, 0.0, 0.0), (0.0, 0.0, 10.0), (3.0, 0.0, 0.0), (0.0, 0.0, 10.0), (3.0, 0.0, 0.0), (0.0, 0.0, 10.0), (3.0, 0.0, 0.0), (0.0, 0.0, 10.0), (3.0, 0.0, 0.0)]

        # Movendo a tartaruga para desenhar a estrela
        for point in starPoints:
            x, y, z = point
            msg = Twist()
            msg.linear.x = x
            msg.linear.y = y
            msg.angular.z = z
            self.publisher_.publish(msg)
            time.sleep(1)  # Espera um pouco antes de ir para o próximo ponto

        # Mandando a tartaruguinha embora
        kill_future = self.kill_client.call_async(Kill.Request(name=new_turtle_name))
        rclpy.spin_until_future_complete(self, kill_future)

def main(args=None):
    rclpy.init(args=args)
    turtle_art = Estrelinha()
    turtle_art.desenhandinho()
    turtle_art.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

