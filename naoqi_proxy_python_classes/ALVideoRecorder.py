#!/usr/bin/env python
# Class autogenerated from ./alvideorecorderproxy.h
# by Sammy Pfeiffer's <Sammy.Pfeiffer at student.uts.edu.au> generator
# You need an ALBroker running

from naoqi import ALProxy


class ALVideoRecorder(object):
    def __init__(self):
        self.proxy = ALProxy("ALVideoRecorder")

    def getGenericProxy(self):
        """Gets the underlying generic proxy

        :returns boost::shared_ptr<ALProxy>: 
        """
        return self.proxy.getGenericProxy()

    def exit(self):
        """Exits and unregisters the module.
        """
        return self.proxy.exit()

    def getBrokerName(self):
        """Gets the name of the parent broker.

        :returns str: The name of the parent broker.
        """
        return self.proxy.getBrokerName()

    def getCameraID(self):
        """Returns current camera ID.

        :returns int: Current camera ID.
        """
        return self.proxy.getCameraID()

    def getColorSpace(self):
        """Returns current color space.

        :returns int: Current color space.
        """
        return self.proxy.getColorSpace()

    def getFrameRate(self):
        """Returns current frame rate.

        :returns int: Current frame rate.
        """
        return self.proxy.getFrameRate()

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

    def getResolution(self):
        """Returns current resolution.

        :returns int: Current resolution.
        """
        return self.proxy.getResolution()

    def getUsage(self, name):
        """Gets the method usage string. This summarises how to use the method.

        :param str name: The name of the method.
        :returns str: A string that summarises the usage of the method.
        """
        return self.proxy.getUsage(name)

    def getVideoFormat(self):
        """Returns current video format.

        :returns str: Current video format.
        """
        return self.proxy.getVideoFormat()

    def isRecording(self):
        """Are we currently recording a video

        :returns bool: True/False
        """
        return self.proxy.isRecording()

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

    def setCameraID(self, cameraID):
        """Sets camera ID.

        :param int cameraID: ID of the camera to use.
        """
        return self.proxy.setCameraID(cameraID)

    def setColorSpace(self, colorSpace):
        """Sets color space.

        :param int colorSpace: New color space.
        """
        return self.proxy.setColorSpace(colorSpace)

    def setFrameRate(self, frameRate):
        """Sets frame rate.

        :param float frameRate: New frame rate.
        """
        return self.proxy.setFrameRate(frameRate)

    def setResolution(self, resolution):
        """Sets resolution.

        :param int resolution: New frame resolution.
        """
        return self.proxy.setResolution(resolution)

    def setVideoFormat(self, videoFormat):
        """Sets video format.

        :param str videoFormat: New video format.
        """
        return self.proxy.setVideoFormat(videoFormat)

    def startRecording(self, folderPath, fileName):
        """Starts recording a video. Please note that only one record at a time can be made.

        :param str folderPath: Folder where the video is saved.
        :param str fileName: Filename used to save the video.
        """
        return self.proxy.startRecording(folderPath, fileName)

    def startRecording(self, folderPath, fileName, overwrite):
        """Starts recording a video. Please note that only one record at a time can be made.

        :param str folderPath: Folder where the video is saved.
        :param str fileName: Filename used to save the video.
        :param bool overwrite: If false and the filename already exists, an exception is thrown.
        """
        return self.proxy.startRecording(folderPath, fileName, overwrite)

    def stop(self, id):
        """returns true if the method is currently running

        :param int id: the ID of the method to wait for
        """
        return self.proxy.stop(id)

    def stopRecording(self):
        """Stops a video record that was launched with startRecording(). The function returns the number of frames that were recorded, as well as the video absolute file name.

        :returns AL::ALValue: Array of two elements [numRecordedFrames, recordAbsolutePath]
        """
        return self.proxy.stopRecording()

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
