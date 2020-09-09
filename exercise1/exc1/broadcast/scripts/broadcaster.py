#!/usr/bin/env python
import rospy
from std_msgs.msg import Int16

def talker():
    pub = rospy.Publisher('xamin', Int16, queue_size=10)
    rospy.init_node('broadcaster', anonymous=True)
    rate = rospy.Rate(20) # 10hz
    k = 1
    while not rospy.is_shutdown():
        pub.publish(k)
        rate.sleep()
        k+=4

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass