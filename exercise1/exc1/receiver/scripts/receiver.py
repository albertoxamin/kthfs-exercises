#!/usr/bin/env python
import rospy
from std_msgs.msg import Int16, Float32


class Receiver:
    pub = None
    rate = None

    def callback(self, data):
        self.pub.publish(data.data/0.15)

    def init(self):
        rospy.init_node('receiver', anonymous=True)
        rospy.Subscriber("xamin", Int16, self.callback)
        self.pub = rospy.Publisher('/kthfs/result', Float32, queue_size=10)
        self.rate = rospy.Rate(20)
        rospy.spin()


if __name__ == '__main__':
    rec = Receiver()
    rec.init()
