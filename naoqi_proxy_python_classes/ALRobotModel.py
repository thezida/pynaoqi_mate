#!/usr/bin/env python
# Class autogenerated from /home/sam/Downloads/aldebaran_sw/nao/naoqi-sdk-2.1.4.13-linux64/include/alproxies/alrobotmodelproxy.h
# by Sammy Pfeiffer's <Sammy.Pfeiffer at student.uts.edu.au> generator
# You need an ALBroker running

from naoqi import ALProxy



class ALRobotModel(object):
    def __init__(self):
        self.proxy = None

    def force_connect(self):
        self.proxy = ALProxy("ALRobotModel")

    def getConfig(self):
        """Return the RobotConfig key/value pairs serialized in xml format

        :returns str: the RobotConfig key/value pairs in xml format
        """
        if not self.proxy:
            self.proxy = ALProxy("ALRobotModel")
        return self.proxy.getConfig()

    def ping(self):
        """Just a ping. Always returns true

        :returns bool: returns true
        """
        if not self.proxy:
            self.proxy = ALProxy("ALRobotModel")
        return self.proxy.ping()

    def version(self):
        """Returns the version of the module.

        :returns str: A string containing the version of the module.
        """
        if not self.proxy:
            self.proxy = ALProxy("ALRobotModel")
        return self.proxy.version()
