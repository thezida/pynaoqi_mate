#!/usr/bin/env python
# Class autogenerated from ./alvideodeviceproxy.h
# by Sammy Pfeiffer's <Sammy.Pfeiffer at student.uts.edu.au> generator
# You need an ALBroker running

from naoqi import ALProxy


class ALVideoDevice(object):
    def __init__(self):
        self.proxy = ALProxy("ALVideoDevice")

    def getGenericProxy(self):
        """Gets the underlying generic proxy

        :returns boost::shared_ptr<ALProxy>: 
        """
        return self.proxy.getGenericProxy()

    def closeCamera(self, arg1):
        """

        :param int arg1: arg
        :returns bool: 
        """
        return self.proxy.closeCamera(arg1)

    def exit(self):
        """Exits and unregisters the module.
        """
        return self.proxy.exit()

    def getActiveCamera(self):
        """Tells which camera is the default one

        :returns int: 0: top camera - 1: bottom camera
        """
        return self.proxy.getActiveCamera()

    def getActiveCamera(self, name):
        """

        :param str name: Name of the subscribing vision module
        :returns int: 
        """
        return self.proxy.getActiveCamera(name)

    def getActiveCameras(self, name):
        """

        :param str name: Name of the subscribing vision module
        :returns AL::ALValue: 
        """
        return self.proxy.getActiveCameras(name)

    def getAngPosFromImgPos(self, arg1):
        """

        :param std::vector<float> arg1: arg
        :returns std::vector<float>: 
        """
        return self.proxy.getAngPosFromImgPos(arg1)

    def getAngSizeFromImgSize(self, arg1):
        """

        :param std::vector<float> arg1: arg
        :returns std::vector<float>: 
        """
        return self.proxy.getAngSizeFromImgSize(arg1)

    def getAngularPositionFromImagePosition(self, arg1, arg2):
        """

        :param int arg1: arg
        :param std::vector<float> arg2: arg
        :returns std::vector<float>: 
        """
        return self.proxy.getAngularPositionFromImagePosition(arg1, arg2)

    def getAngularSizeFromImageSize(self, arg1, arg2):
        """

        :param int arg1: arg
        :param std::vector<float> arg2: arg
        :returns std::vector<float>: 
        """
        return self.proxy.getAngularSizeFromImageSize(arg1, arg2)

    def getBrokerName(self):
        """Gets the name of the parent broker.

        :returns str: The name of the parent broker.
        """
        return self.proxy.getBrokerName()

    def getCameraIndexes(self):
        """

        :returns AL::ALValue: 
        """
        return self.proxy.getCameraIndexes()

    def getCameraModel(self, cameraIndex):
        """

        :param int cameraIndex: Camera requested.
        :returns int: 1(kOV7670): VGA camera - 2(kMT9M114): HD camera
        """
        return self.proxy.getCameraModel(cameraIndex)

    def getCameraModelID(self):
        """

        :returns int: 
        """
        return self.proxy.getCameraModelID()

    def getCameraName(self, cameraIndex):
        """

        :param int cameraIndex: Camera requested.
        :returns str: CameraTop - CameraBottom - CameraDepth
        """
        return self.proxy.getCameraName(cameraIndex)

    def getCameraParameter(self, name, parameterId):
        """

        :param str name: Name of the subscribing vision module
        :param int parameterId: Camera parameter requested.
        :returns int: 
        """
        return self.proxy.getCameraParameter(name, parameterId)

    def getCameraParameterInfo(self, name, parameterId):
        """

        :param str name: Name of the subscribing vision module
        :param int parameterId: Camera parameter requested.
        :returns AL::ALValue: 
        """
        return self.proxy.getCameraParameterInfo(name, parameterId)

    def getCameraParameterRange(self, name, parameterId):
        """

        :param str name: Name of the subscribing vision module
        :param int parameterId: Camera parameter requested.
        :returns AL::ALValue: 
        """
        return self.proxy.getCameraParameterRange(name, parameterId)

    def getCamerasParameter(self, name, parameterId):
        """

        :param str name: Name of the subscribing vision module
        :param int parameterId: Camera parameter requested.
        :returns AL::ALValue: 
        """
        return self.proxy.getCamerasParameter(name, parameterId)

    def getColorSpace(self, cameraIndex):
        """

        :param int cameraIndex: Camera requested.
        :returns int: 
        """
        return self.proxy.getColorSpace(cameraIndex)

    def getColorSpace(self, name):
        """

        :param str name: Name of the subscribing vision module
        :returns int: 
        """
        return self.proxy.getColorSpace(name)

    def getColorSpaces(self, name):
        """

        :param str name: Name of the subscribing vision module
        :returns AL::ALValue: 
        """
        return self.proxy.getColorSpaces(name)

    def getDirectRawImageLocal(self, name):
        """Retrieves the latest image from the video source and returns a pointer to the locked ALImage, with data array pointing directly to raw data. There is no format conversion and no copy of the raw buffer. Warning: When image is not necessary anymore, a call to releaseDirectRawImage() is requested. Warning: When using this mode for several vision module, if they need raw data for more than 25ms check that you have strictly less modules in this mode than the amount of kernel buffers!! Warning: Release all kernel buffers before any action requesting a modification in camera running mode (e.g. resolution, switch between cameras).

        :param str name: Name of the subscribing vision module Warning, image pointer is valid only for C++ dynamic library.
        """
        return self.proxy.getDirectRawImageLocal(name)

    def getDirectRawImageRemote(self, name):
        """Fills an ALValue with data coming directly from raw buffer (no format conversion).

        :param str name: Name of the subscribing vision module     [0] : width;     [1] : height;     [2] : number of layers;     [3] : ColorSpace;     [4] : time stamp (highest 32 bits);     [5] : time stamp (lowest 32 bits);     [6] : array of size height * width * nblayers containing image data;     [7] : cameraID;     [8] : left angle;     [9] : top angle;     [10] : right angle;     [11] : bottom angle;
        :returns AL::ALValue: Array containing image informations :
        """
        return self.proxy.getDirectRawImageRemote(name)

    def getDirectRawImagesLocal(self, name):
        """Retrieves the latest image from the video source and returns a pointer to the locked ALImage, with data array pointing directly to raw data. There is no format conversion and no copy of the raw buffer. Warning: When image is not necessary anymore, a call to releaseDirectRawImage() is requested. Warning: When using this mode for several vision module, if they need raw data for more than 25ms check that you have strictly less modules in this mode than the amount of kernel buffers!! Warning: Release all kernel buffers before any action requesting a modification in camera running mode (e.g. resolution, switch between cameras).

        :param str name: Name of the subscribing vision module Warning, image pointer is valid only for C++ dynamic library.
        :returns AL::ALValue: Array of pointer to the locked image buffer, NULL if error.
        """
        return self.proxy.getDirectRawImagesLocal(name)

    def getDirectRawImagesRemote(self, name):
        """Fills an ALValue with data coming directly from raw buffer (no format conversion).

        :param str name: Name of the subscribing vision module     [0] : width;     [1] : height;     [2] : number of layers;     [3] : ColorSpace;     [4] : time stamp (highest 32 bits);     [5] : time stamp (lowest 32 bits);     [6] : array of size height * width * nblayers containing image data;     [7] : cameraID;     [8] : left angle;     [9] : top angle;     [10] : right angle;     [11] : bottom angle;
        :returns AL::ALValue: Array containing image informations :
        """
        return self.proxy.getDirectRawImagesRemote(name)

    def getExpectedImageParameters(self, cameraIndex):
        """called by the simulator to know expected image parameters

        :param int cameraIndex: Camera requested.
        :returns AL::ALValue: ALValue of expected parameters, [int resolution, int framerate]
        """
        return self.proxy.getExpectedImageParameters(cameraIndex)

    def getExpectedImageParameters(self):
        """called by the simulator to know expected image parameters

        :returns AL::ALValue: ALValue of expected parameters, [int resolution, int framerate]
        """
        return self.proxy.getExpectedImageParameters()

    def getFrameRate(self, cameraIndex):
        """

        :param int cameraIndex: Camera requested.
        :returns int: 
        """
        return self.proxy.getFrameRate(cameraIndex)

    def getFrameRate(self, name):
        """

        :param str name: Name of the subscribing vision module
        :returns int: 
        """
        return self.proxy.getFrameRate(name)

    def getGVMColorSpace(self, arg1):
        """

        :param str arg1: arg
        :returns int: 
        """
        return self.proxy.getGVMColorSpace(arg1)

    def getGVMFrameRate(self, arg1):
        """

        :param str arg1: arg
        :returns int: 
        """
        return self.proxy.getGVMFrameRate(arg1)

    def getGVMResolution(self, arg1):
        """

        :param str arg1: arg
        :returns int: 
        """
        return self.proxy.getGVMResolution(arg1)

    def getHorizontalAperture(self, cameraIndex):
        """

        :param int cameraIndex: Camera requested.
        :returns float: 
        """
        return self.proxy.getHorizontalAperture(cameraIndex)

    def getHorizontalFOV(self, cameraIndex):
        """

        :param int cameraIndex: Camera requested.
        :returns float: 
        """
        return self.proxy.getHorizontalFOV(cameraIndex)

    def getImageInfoFromAngularInfo(self, arg1, arg2):
        """

        :param int arg1: arg
        :param std::vector<float> arg2: arg
        :returns std::vector<float>: 
        """
        return self.proxy.getImageInfoFromAngularInfo(arg1, arg2)

    def getImageInfoFromAngularInfoWithResolution(self, arg1, arg2, arg3):
        """

        :param int arg1: arg
        :param std::vector<float> arg2: arg
        :param int arg3: arg
        :returns std::vector<float>: 
        """
        return self.proxy.getImageInfoFromAngularInfoWithResolution(arg1, arg2, arg3)

    def getImageLocal(self, name):
        """Applies transformations to the last image from video source and returns a pointer to a locked ALImage. When image is not necessary anymore, a call to releaseImage() is requested.

        :param str name: Name of the subscribing vision module
        """
        return self.proxy.getImageLocal(name)

    def getImagePositionFromAngularPosition(self, arg1, arg2):
        """

        :param int arg1: arg
        :param std::vector<float> arg2: arg
        :returns std::vector<float>: 
        """
        return self.proxy.getImagePositionFromAngularPosition(arg1, arg2)

    def getImageRemote(self, name):
        """Applies transformations to the last image from video source and fills pFrameOut.

        :param str name: Name of the subscribing vision module     [0] : width;     [1] : height;     [2] : number of layers;     [3] : ColorSpace;     [4] : time stamp (highest 32 bits);     [5] : time stamp (lowest 32 bits);     [6] : array of size height * width * nblayers containing image data;     [7] : cameraID;     [8] : left angle;     [9] : top angle;     [10] : right angle;     [11] : bottom angle;
        :returns AL::ALValue: Array containing image informations :
        """
        return self.proxy.getImageRemote(name)

    def getImageSizeFromAngularSize(self, arg1, arg2):
        """

        :param int arg1: arg
        :param std::vector<float> arg2: arg
        :returns std::vector<float>: 
        """
        return self.proxy.getImageSizeFromAngularSize(arg1, arg2)

    def getImagesLocal(self, name):
        """Applies transformations to the last image from video source and returns a pointer to a locked ALImage. When image is not necessary anymore, a call to releaseImage() is requested.

        :param str name: Name of the subscribing vision module
        :returns AL::ALValue: Array of pointer of the locked image buffer, NULL if error.Warning, image pointer is valid only for C++ dynamic library.
        """
        return self.proxy.getImagesLocal(name)

    def getImagesRemote(self, name):
        """Applies transformations to the last image from video source and fills pFrameOut.

        :param str name: Name of the subscribing vision module     [0] : width;     [1] : height;     [2] : number of layers;     [3] : ColorSpace;     [4] : time stamp (highest 32 bits);     [5] : time stamp (lowest 32 bits);     [6] : array of size height * width * nblayers containing image data;     [7] : cameraID;     [8] : left angle;     [9] : top angle;     [10] : right angle;     [11] : bottom angle;
        :returns AL::ALValue: Array containing image informations :
        """
        return self.proxy.getImagesRemote(name)

    def getImgInfoFromAngInfo(self, arg1):
        """

        :param std::vector<float> arg1: arg
        :returns std::vector<float>: 
        """
        return self.proxy.getImgInfoFromAngInfo(arg1)

    def getImgInfoFromAngInfoWithRes(self, arg1, arg2):
        """

        :param std::vector<float> arg1: arg
        :param int arg2: arg
        :returns std::vector<float>: 
        """
        return self.proxy.getImgInfoFromAngInfoWithRes(arg1, arg2)

    def getImgPosFromAngPos(self, arg1):
        """

        :param std::vector<float> arg1: arg
        :returns std::vector<float>: 
        """
        return self.proxy.getImgPosFromAngPos(arg1)

    def getImgSizeFromAngSize(self, arg1):
        """

        :param std::vector<float> arg1: arg
        :returns std::vector<float>: 
        """
        return self.proxy.getImgSizeFromAngSize(arg1)

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

    def getParam(self, pParam):
        """

        :param int pParam: Camera parameter requested.
        :returns int: 
        """
        return self.proxy.getParam(pParam)

    def getParam(self, pParam, pCameraIndex):
        """

        :param int pParam: Camera parameter requested.
        :param int pCameraIndex: Camera requested.
        :returns int: 
        """
        return self.proxy.getParam(pParam, pCameraIndex)

    def getParameter(self, cameraIndex, parameterId):
        """

        :param int cameraIndex: Camera requested.
        :param int parameterId: Camera parameter requested.
        :returns int: 
        """
        return self.proxy.getParameter(cameraIndex, parameterId)

    def getParameterInfo(self, cameraIndex, parameterId):
        """

        :param int cameraIndex: Camera requested.
        :param int parameterId: Camera parameter requested.
        :returns AL::ALValue: 
        """
        return self.proxy.getParameterInfo(cameraIndex, parameterId)

    def getParameterRange(self, cameraIndex, parameterId):
        """

        :param int cameraIndex: Camera requested.
        :param int parameterId: Camera parameter requested.
        :returns AL::ALValue: 
        """
        return self.proxy.getParameterRange(cameraIndex, parameterId)

    def getResolution(self, cameraIndex):
        """

        :param int cameraIndex: Camera requested.
        :returns int: 
        """
        return self.proxy.getResolution(cameraIndex)

    def getResolution(self, name):
        """

        :param str name: Name of the subscribing vision module
        :returns int: 
        """
        return self.proxy.getResolution(name)

    def getResolutions(self, name):
        """

        :param str name: Name of the subscribing vision module
        :returns AL::ALValue: 
        """
        return self.proxy.getResolutions(name)

    def getSubscribers(self):
        """

        :returns AL::ALValue: 
        """
        return self.proxy.getSubscribers()

    def getUsage(self, name):
        """Gets the method usage string. This summarises how to use the method.

        :param str name: The name of the method.
        :returns str: A string that summarises the usage of the method.
        """
        return self.proxy.getUsage(name)

    def getVIMColorSpace(self):
        """

        :returns int: 
        """
        return self.proxy.getVIMColorSpace()

    def getVIMFrameRate(self):
        """

        :returns int: 
        """
        return self.proxy.getVIMFrameRate()

    def getVIMResolution(self):
        """

        :returns int: 
        """
        return self.proxy.getVIMResolution()

    def getVerticalAperture(self, cameraIndex):
        """

        :param int cameraIndex: Camera requested.
        :returns float: 
        """
        return self.proxy.getVerticalAperture(cameraIndex)

    def getVerticalFOV(self, cameraIndex):
        """

        :param int cameraIndex: Camera requested.
        :returns float: 
        """
        return self.proxy.getVerticalFOV(cameraIndex)

    def hasDepthCamera(self):
        """

        :returns bool: 
        """
        return self.proxy.hasDepthCamera()

    def isCameraOpen(self, arg1):
        """

        :param int arg1: arg
        :returns bool: 
        """
        return self.proxy.isCameraOpen(arg1)

    def isCameraStarted(self, arg1):
        """

        :param int arg1: arg
        :returns bool: 
        """
        return self.proxy.isCameraStarted(arg1)

    def isFrameGrabberOff(self, cameraIndex):
        """

        :param int cameraIndex: Camera requested.
        :returns bool: 
        """
        return self.proxy.isFrameGrabberOff(cameraIndex)

    def isFrameGrabberOff(self):
        """Advanced method that asks if the framegrabber is off.

        :returns int: true if off
        """
        return self.proxy.isFrameGrabberOff()

    def isRunning(self, id):
        """Returns true if the method is currently running.

        :param int id: The ID of the method that was returned when calling the method using 'post'
        :returns bool: True if the method is currently running
        """
        return self.proxy.isRunning(id)

    def onClientDisconnected(self, eventName, eventContents, message):
        """Callback when client is disconnected

        :param str eventName: The echoed event name
        :param AL::ALValue eventContents: The name of the client that has disconnected
        :param str message: The message give when subscribing.
        """
        return self.proxy.onClientDisconnected(eventName, eventContents, message)

    def openCamera(self, arg1):
        """

        :param int arg1: arg
        :returns bool: 
        """
        return self.proxy.openCamera(arg1)

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

    def putImage(self, cameraIndex, width, height, imageBuffer):
        """Allow image buffer pushing

        :param int cameraIndex: Camera requested.
        :param int width: int width of image among 1280*960, 640*480, 320*240, 240*160
        :param int height: int height of image
        :param AL::ALValue imageBuffer: Image buffer in bitmap form
        :returns bool: true if the put succeeded
        """
        return self.proxy.putImage(cameraIndex, width, height, imageBuffer)

    def putImage(self, imageBuffer):
        """Allow image buffer pushing

        :param AL::ALValue imageBuffer: Image buffer in bitmap form
        :returns bool: true if the put succeeded
        """
        return self.proxy.putImage(imageBuffer)

    def recordVideo(self, id, path, totalNumber, period):
        """Background record of an .arv raw format video from the images processed by a vision module Actualy it take picture each time the vision module call getDirectRawImageRemote().

        :param str id: Name under which the G.V.M. is known from the V.I.M.
        :param str path: path/name of the video to be recorded
        :param int totalNumber: number of images to be recorded. 0xFFFFFFFF for "unlimited"
        :param int period: one image recorded every pPeriod images
        :returns bool: true if success
        """
        return self.proxy.recordVideo(id, path, totalNumber, period)

    def releaseDirectRawImage(self, name):
        """Release image buffer locked by getDirectRawImageLocal().

        :param str name: Name of the subscribing vision module
        :returns bool: true if success
        """
        return self.proxy.releaseDirectRawImage(name)

    def releaseDirectRawImages(self, name):
        """Release image buffer locked by getDirectRawImagesLocal().

        :param str name: Name of the subscribing vision module
        :returns AL::ALValue: true if success
        """
        return self.proxy.releaseDirectRawImages(name)

    def releaseImage(self, name):
        """Release image buffer locked by getImageLocal(). If G.V.M. had no locked image buffer, does nothing.

        :param str name: Name of the subscribing vision module
        :returns bool: true if success
        """
        return self.proxy.releaseImage(name)

    def releaseImages(self, name):
        """Release image buffer locked by getImageLocal(). If G.V.M. had no locked image buffer, does nothing.

        :param str name: Name of the subscribing vision module
        :returns AL::ALValue: true if success
        """
        return self.proxy.releaseImages(name)

    def resetCamera(self, arg1):
        """

        :param int arg1: arg
        :returns bool: 
        """
        return self.proxy.resetCamera(arg1)

    def resolutionToSizes(self, arg1):
        """

        :param int arg1: arg
        :returns AL::ALValue: 
        """
        return self.proxy.resolutionToSizes(arg1)

    def setActiveCamera(self, activeCamera):
        """Set the active camera

        :param int activeCamera: 0: top camera - 1: bottom camera
        :returns bool: 
        """
        return self.proxy.setActiveCamera(activeCamera)

    def setActiveCamera(self, name, cameraIndex):
        """

        :param str name: Name of the subscribing vision module
        :param int cameraIndex: Camera requested.
        :returns bool: 
        """
        return self.proxy.setActiveCamera(name, cameraIndex)

    def setActiveCameras(self, name, cameraIndexes):
        """

        :param str name: Name of the subscribing vision module
        :param AL::ALValue cameraIndexes: Cameras requested.
        :returns AL::ALValue: 
        """
        return self.proxy.setActiveCameras(name, cameraIndexes)

    def setAllCameraParametersToDefault(self, name):
        """

        :param str name: Name of the subscribing vision module
        :returns bool: 
        """
        return self.proxy.setAllCameraParametersToDefault(name)

    def setAllParametersToDefault(self, cameraIndex):
        """

        :param int cameraIndex: Camera requested.
        :returns bool: 
        """
        return self.proxy.setAllParametersToDefault(cameraIndex)

    def setCameraParameter(self, name, parameterId, value):
        """

        :param str name: Name of the subscribing vision module
        :param int parameterId: Camera parameter requested.
        :param int value: value requested.
        :returns bool: 
        """
        return self.proxy.setCameraParameter(name, parameterId, value)

    def setCameraParameterToDefault(self, name, parameterId):
        """

        :param str name: Name of the subscribing vision module
        :param int parameterId: Camera parameter requested.
        :returns bool: 
        """
        return self.proxy.setCameraParameterToDefault(name, parameterId)

    def setCamerasParameter(self, name, parameterId, values):
        """

        :param str name: Name of the subscribing vision module
        :param int parameterId: Camera parameter requested.
        :param AL::ALValue values: values requested.
        :returns AL::ALValue: 
        """
        return self.proxy.setCamerasParameter(name, parameterId, values)

    def setCamerasParameterToDefault(self, name, parameterId):
        """

        :param str name: Name of the subscribing vision module
        :param int parameterId: Camera parameter requested.
        :returns AL::ALValue: 
        """
        return self.proxy.setCamerasParameterToDefault(name, parameterId)

    def setColorSpace(self, name, colorSpace):
        """

        :param str name: Name of the subscribing vision module
        :param int colorSpace: Color Space requested.
        :returns bool: 
        """
        return self.proxy.setColorSpace(name, colorSpace)

    def setColorSpaces(self, name, colorSpaces):
        """

        :param str name: Name of the subscribing vision module
        :param AL::ALValue colorSpaces: Color Spaces requested.
        :returns AL::ALValue: 
        """
        return self.proxy.setColorSpaces(name, colorSpaces)

    def setFrameRate(self, name, frameRate):
        """

        :param str name: Name of the subscribing vision module
        :param int frameRate: Frame Rate requested.
        :returns bool: 
        """
        return self.proxy.setFrameRate(name, frameRate)

    def setParam(self, pParam, pNewValue):
        """Sets the value of a specific parameter for the video source.

        :param int pParam: Camera parameter requested.
        :param int pNewValue: value requested.
        """
        return self.proxy.setParam(pParam, pNewValue)

    def setParam(self, pParam, pNewValue, pCameraIndex):
        """Sets the value of a specific parameter for the video source.

        :param int pParam: Camera parameter requested.
        :param int pNewValue: value requested.
        :param int pCameraIndex: Camera requested.
        """
        return self.proxy.setParam(pParam, pNewValue, pCameraIndex)

    def setParamDefault(self, arg1):
        """

        :param int arg1: arg
        """
        return self.proxy.setParamDefault(arg1)

    def setParameter(self, cameraIndex, parameterId, value):
        """

        :param int cameraIndex: Camera requested.
        :param int parameterId: Camera parameter requested.
        :param int value: value requested.
        :returns bool: 
        """
        return self.proxy.setParameter(cameraIndex, parameterId, value)

    def setParameterToDefault(self, cameraIndex, parameterId):
        """

        :param int cameraIndex: Camera requested.
        :param int parameterId: Camera parameter requested.
        :returns bool: 
        """
        return self.proxy.setParameterToDefault(cameraIndex, parameterId)

    def setResolution(self, name, resolution):
        """

        :param str name: Name of the subscribing vision module
        :param int resolution: Resolution requested.
        :returns bool: 
        """
        return self.proxy.setResolution(name, resolution)

    def setResolutions(self, name, resolutions):
        """

        :param str name: Name of the subscribing vision module
        :param AL::ALValue resolutions: Resolutions requested.
        :returns AL::ALValue: 
        """
        return self.proxy.setResolutions(name, resolutions)

    def setSimCamInputSize(self, width, height):
        """called by the simulator to know expected image parameters

        :param int width: int width of image among 1280*960, 640*480, 320*240, 240*160
        :param int height: int height of image among 1280*960, 640*480, 320*240, 240*160
        :returns bool: true if setSize worked
        """
        return self.proxy.setSimCamInputSize(width, height)

    def sizesToResolution(self, arg1, arg2):
        """

        :param int arg1: arg
        :param int arg2: arg
        :returns int: 
        """
        return self.proxy.sizesToResolution(arg1, arg2)

    def startCamera(self, arg1):
        """

        :param int arg1: arg
        :returns bool: 
        """
        return self.proxy.startCamera(arg1)

    def startFrameGrabber(self, cameraIndex):
        """

        :param int cameraIndex: Camera requested.
        :returns bool: 
        """
        return self.proxy.startFrameGrabber(cameraIndex)

    def startFrameGrabber(self):
        """Advanced method that opens and initialize video source device if it was not before. Note that the first module subscribing to ALVideoDevice will launch it automatically.

        :returns bool: true if success
        """
        return self.proxy.startFrameGrabber()

    def stop(self, id):
        """returns true if the method is currently running

        :param int id: the ID of the method to wait for
        """
        return self.proxy.stop(id)

    def stopCamera(self, arg1):
        """

        :param int arg1: arg
        :returns bool: 
        """
        return self.proxy.stopCamera(arg1)

    def stopFrameGrabber(self, cameraIndex):
        """

        :param int cameraIndex: Camera requested.
        :returns bool: 
        """
        return self.proxy.stopFrameGrabber(cameraIndex)

    def stopFrameGrabber(self):
        """Advanced method that close video source device. Note that the last module unsubscribing to ALVideoDevice will launch it automatically.

        :returns bool: true if success
        """
        return self.proxy.stopFrameGrabber()

    def stopVideo(self, id):
        """Stop writing the video sequence

        :param str id: Name under which the G.V.M. is known from ALVideoDevice.
        :returns bool: true if success
        """
        return self.proxy.stopVideo(id)

    def subscribe(self, gvmName, resolution, colorSpace, fps):
        """Register to ALVideoDevice (formerly Video Input Module/V.I.M.). When a General Video Module(G.V.M.) registers to ALVideoDevice, a buffer of the requested image format is added to the buffers list. Returns the name under which the G.V.M. is registered to ALVideoDevice (useful when two G.V.M. try to register using the same name

        :param str gvmName: Name of the subscribing G.V.M.
        :param int resolution: Resolution requested. { 0 = kQQVGA, 1 = kQVGA, 2 = kVGA }
        :param int colorSpace: Colorspace requested. { 0 = kYuv, 9 = kYUV422, 10 = kYUV, 11 = kRGB, 12 = kHSY, 13 = kBGR }
        :param int fps: Fps (frames per second) requested. { 5, 10, 15, 30 }
        :returns str: Name under which the G.V.M. is known from ALVideoDevice, 0 if failed.
        """
        return self.proxy.subscribe(gvmName, resolution, colorSpace, fps)

    def subscribeCamera(self, name, cameraIndex, resolution, colorSpace, fps):
        """

        :param str name: Name of the subscribing vision module
        :param int cameraIndex: Camera requested.
        :param int resolution: Resolution requested.{0=kQQVGA, 1=kQVGA, 2=kVGA, 3=k4VGA}
        :param int colorSpace: Colorspace requested.{0=kYuv, 9=kYUV422, 10=kYUV, 11=kRGB, 12=kHSY, 13=kBGR}
        :param int fps: Fps (frames per second) requested.{5, 10, 15, 30}
        :returns str: Name under which the vision module is known from ALVideoDevice
        """
        return self.proxy.subscribeCamera(name, cameraIndex, resolution, colorSpace, fps)

    def subscribeCameras(self, name, cameraIndexes, resolutions, colorSpaces, fps):
        """

        :param str name: Name of the subscribing vision module
        :param AL::ALValue cameraIndexes: Cameras requested.
        :param AL::ALValue resolutions: Resolutions requested.{0=kQQVGA, 1=kQVGA, 2=kVGA, 3=k4VGA}
        :param AL::ALValue colorSpaces: Colorspaces requested.{0=kYuv, 9=kYUV422, 10=kYUV, 11=kRGB, 12=kHSY, 13=kBGR}
        :param int fps: Fps (frames per second) requested.{5, 10, 15, 30}
        :returns str: Name under which the vision module is known from ALVideoDevice
        """
        return self.proxy.subscribeCameras(name, cameraIndexes, resolutions, colorSpaces, fps)

    def unsubscribe(self, nameId):
        """

        :param str nameId: Name under which the vision module is known from ALVideoDevice.
        :returns bool: True if success, false otherwise
        """
        return self.proxy.unsubscribe(nameId)

    def unsubscribeAllInstances(self, id):
        """Used to unsubscribe all instances for a given G.V.M. (e.g. VisionModule and VisionModule_5) from ALVideoDevice.

        :param str id: Root name of the G.V.M. (e.g. with the example above this will be VisionModule).
        """
        return self.proxy.unsubscribeAllInstances(id)

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
