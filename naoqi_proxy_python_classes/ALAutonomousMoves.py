#!/usr/bin/env python
# Class autogenerated from ./alautonomousmovesproxy.h
# by Sammy Pfeiffer's <Sammy.Pfeiffer at student.uts.edu.au> generator
# You need an ALBroker running

from naoqi import ALProxy


class ALAutonomousMoves(object):
    def __init__(self):
        self.proxy = ALProxy("ALAutonomousMoves")

    def getGenericProxy(self):
        """Gets the underlying generic proxy

        :returns boost::shared_ptr<ALProxy>: 
        """
        return self.proxy.getGenericProxy()

    def exit(self):
        """Exits and unregisters the module.
        """
        return self.proxy.exit()

    def getBackgroundStrategy(self):
        """Gets the background strategy.

        :returns str: The autonomous background posture strategy. ("none" or "backToNeutral")
        """
        return self.proxy.getBackgroundStrategy()

    def getBrokerName(self):
        """Gets the name of the parent broker.

        :returns str: The name of the parent broker.
        """
        return self.proxy.getBrokerName()

    def getExpressiveListeningEnabled(self):
        """If expressive listening is enabled.

        :returns bool: The boolean value: true means it is enabled, false means it is disabled.
        """
        return self.proxy.getExpressiveListeningEnabled()

    def getMethodHelp(self, methodName):
        """Retrieves a method's description.

        :param str methodName: The name of the method.
        :returns AL::ALValue: A structure containing the method's description.
        """
        return self.proxy.getMethodHelp(methodName)

    def getMethodList(self):
        """Retrieves the module's method list.

        :returns std::vector<std::string>: An array of method names.
        """
        return self.proxy.getMethodList()

    def getModuleHelp(self):
        """Retrieves the module's description.

        :returns AL::ALValue: A structure describing the module.
        """
        return self.proxy.getModuleHelp()

    def getUsage(self, name):
        """Gets the method usage string. This summarises how to use the method.

        :param str name: The name of the method.
        :returns str: A string that summarises the usage of the method.
        """
        return self.proxy.getUsage(name)

    def isRunning(self, id):
        """Returns true if the method is currently running.

        :param int id: The ID of the method that was returned when calling the method using 'post'
        :returns bool: True if the method is currently running
        """
        return self.proxy.isRunning(id)

    def pCall(self):
        """NAOqi1 pCall method.

        :returns AL::ALValue: 
        """
        return self.proxy.pCall()

    def ping(self):
        """Just a ping. Always returns true

        :returns bool: returns true
        """
        return self.proxy.ping()

    def setBackgroundStrategy(self, strategy):
        """The background strategy.

        :param str strategy: The autonomous background posture strategy. ("none" or "backToNeutral")
        """
        return self.proxy.setBackgroundStrategy(strategy)

    def setExpressiveListeningEnabled(self, enable):
        """Enable or disable expressive listening.

        :param bool enable: The boolean value: true to enable, false to disable.
        """
        return self.proxy.setExpressiveListeningEnabled(enable)

    def startSmallDisplacements(self):
        """DEPRECATED since 2.0: do ALBasicAwareness.setTrackingMode("MoveContextually") instead.Start small base moves.
        """
        return self.proxy.startSmallDisplacements()

    def stop(self, id):
        """returns true if the method is currently running

        :param int id: the ID of the method to wait for
        """
        return self.proxy.stop(id)

    def stopSmallDisplacements(self):
        """DEPRECATED since 2.0: do ALBasicAwareness.setTrackingMode instead.Stop small base moves.
        """
        return self.proxy.stopSmallDisplacements()

    def version(self):
        """Returns the version of the module.

        :returns str: A string containing the version of the module.
        """
        return self.proxy.version()

    def wait(self, id, timeoutPeriod):
        """Wait for the end of a long running method that was called using 'post'

        :param int id: The ID of the method that was returned when calling the method using 'post'
        :param int timeoutPeriod: The timeout period in ms. To wait indefinately, use a timeoutPeriod of zero.
        :returns bool: True if the timeout period terminated. False if the method returned.
        """
        return self.proxy.wait(id, timeoutPeriod)
