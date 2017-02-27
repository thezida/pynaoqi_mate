#!/usr/bin/env python
# Class autogenerated from ./alaudioplayerproxy.h
# by Sammy Pfeiffer's <Sammy.Pfeiffer at student.uts.edu.au> generator
# You need an ALBroker running

from naoqi import ALProxy


class ALAudioPlayer(object):
    def __init__(self):
        self.proxy = ALProxy("ALAudioPlayer")

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

    def getCurrentPosition(self, playId):
        """Returns the position in the file which is currently played

        :param int playId: Id of the process which is playing the file
        :returns float: Position in the file in seconds
        """
        return self.proxy.getCurrentPosition(playId)

    def getFileLength(self, playId):
        """Returns the length of the file played

        :param int playId: Id of the process which is playing the file
        :returns float: Length of the file in seconds
        """
        return self.proxy.getFileLength(playId)

    def getInstalledSoundSetsList(self):
        """

        :returns std::vector<std::string>: 
        """
        return self.proxy.getInstalledSoundSetsList()

    def getLoadedFilesIds(self):
        """returns an array containing the Ids of the currently loaded files

        :returns std::vector<std::string>: Array containing the Ids of the files which has been loaded
        """
        return self.proxy.getLoadedFilesIds()

    def getLoadedFilesNames(self):
        """returns an array containing the names of the currently loaded files

        :returns std::vector<std::string>: Array containing the names of the files which has been loaded
        """
        return self.proxy.getLoadedFilesNames()

    def getLoadedSoundSetsList(self):
        """

        :returns std::vector<std::string>: 
        """
        return self.proxy.getLoadedSoundSetsList()

    def getMasterVolume(self):
        """Returns the master volume of the player

        :returns float: Volume of the master - range 0.0 to 1.0.
        """
        return self.proxy.getMasterVolume()

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

    def getSoundSetFileNames(self, setName):
        """Return the list of files contained in a sound set

        :param str setName: name of the set
        :returns std::vector<std::string>: 
        """
        return self.proxy.getSoundSetFileNames(setName)

    def getUsage(self, name):
        """Gets the method usage string. This summarises how to use the method.

        :param str name: The name of the method.
        :returns str: A string that summarises the usage of the method.
        """
        return self.proxy.getUsage(name)

    def getVolume(self, playId):
        """Returns the volume of the player

        :param int playId: Id of the process which is playing the file
        :returns float: Volume of the player - range 0.0 to 1.0.
        """
        return self.proxy.getVolume(playId)

    def goTo(self, playId, position):
        """Goes to a given position in a file which is playing.

        :param int playId: Id of the process which is playing the file
        :param float position: Position in the file (in second)
        """
        return self.proxy.goTo(playId, position)

    def isRunning(self, id):
        """Returns true if the method is currently running.

        :param int id: The ID of the method that was returned when calling the method using 'post'
        :returns bool: True if the method is currently running
        """
        return self.proxy.isRunning(id)

    def isSoundSetFileInstalled(self, setName, soundName):
        """

        :param str setName: name of the set
        :param str soundName: name of the sound
        :returns bool: 
        """
        return self.proxy.isSoundSetFileInstalled(setName, soundName)

    def isSoundSetInstalled(self, setName):
        """

        :param str setName: name of the set
        :returns bool: 
        """
        return self.proxy.isSoundSetInstalled(setName)

    def loadFile(self, fileName):
        """Loads a file for ulterior playback

        :param str fileName: Path of the sound file (either mp3 or wav)
        :returns int: Id of the file which has been loaded. This file can then be played with the play function
        """
        return self.proxy.loadFile(fileName)

    def loadSoundSet(self, setName):
        """Load a sound set

        :param str setName: name of the set
        """
        return self.proxy.loadSoundSet(setName)

    def pCall(self):
        """NAOqi1 pCall method.

        :returns AL::ALValue: 
        """
        return self.proxy.pCall()

    def pause(self, id):
        """Pause a play back

        :param int id: Id of the process that is playing the file you want to put in pause
        """
        return self.proxy.pause(id)

    def ping(self):
        """Just a ping. Always returns true

        :returns bool: returns true
        """
        return self.proxy.ping()

    def play(self, id):
        """Starts the playback of a file preloaded with the loadFile function.

        :param int id: Id returned by the loadFile function
        """
        return self.proxy.play(id)

    def play(self, id, volume, pan):
        """Starts the playback of a file preloaded with the loadFile function, with specific volume and audio balance

        :param int id: Id returned by the loadFile function
        :param float volume: volume of the sound file (must be between 0.0 and 1.0)
        :param float pan: audio balance of the sound file (-1.0 : left / 1.0 : right)
        """
        return self.proxy.play(id, volume, pan)

    def playFile(self, fileName):
        """Plays a wav or mp3 file

        :param str fileName: Path of the sound file
        """
        return self.proxy.playFile(fileName)

    def playFile(self, fileName, volume, pan):
        """Plays a wav or mp3 file, with specific volume and audio balance

        :param str fileName: Path of the sound file
        :param float volume: volume of the sound file (must be between 0.0 and 1.0)
        :param float pan: audio balance of the sound file (-1.0 : left / 1.0 : right / 0.0 : centered)
        """
        return self.proxy.playFile(fileName, volume, pan)

    def playFileFromPosition(self, fileName, position):
        """Plays a wav or mp3 file from a given position in the file.

        :param str fileName: Name of the sound file
        :param float position: Position in second where the playing has to begin
        """
        return self.proxy.playFileFromPosition(fileName, position)

    def playFileFromPosition(self, fileName, position, volume, pan):
        """Plays a wav or mp3 file from a given position in the file, with specific volume and audio balance

        :param str fileName: Name of the sound file
        :param float position: Position in second where the playing has to begin
        :param float volume: volume of the sound file (must be between 0.0 and 1.0)
        :param float pan: audio balance of the sound file (-1.0 : left / 1.0 : right)
        """
        return self.proxy.playFileFromPosition(fileName, position, volume, pan)

    def playFileInLoop(self, fileName):
        """Plays a wav or mp3 file in loop

        :param str fileName: Path of the sound file
        """
        return self.proxy.playFileInLoop(fileName)

    def playFileInLoop(self, fileName, volume, pan):
        """Plays a wav or mp3 file in loop, with specific volume and audio balance

        :param str fileName: Path of the sound file
        :param float volume: volume of the sound file (must be between 0.0 and 1.0)
        :param float pan: audio balance of the sound file (-1.0 : left / 1.0 : right)
        """
        return self.proxy.playFileInLoop(fileName, volume, pan)

    def playInLoop(self, id):
        """Starts the playback in loop of a file preloaded with the loadFile function

        :param int id: Id returned by the loadFile function
        """
        return self.proxy.playInLoop(id)

    def playInLoop(self, id, volume, pan):
        """Plays a wav or mp3 file in loop, with specific volume and audio balance

        :param int id: Id returned by the loadFile function
        :param float volume: volume of the sound file (must be between 0.0 and 1.0)
        :param float pan: audio balance of the sound file (-1.0 : left / 1.0 : right)
        """
        return self.proxy.playInLoop(id, volume, pan)

    def playSine(self, frequence, gain, pan, duration):
        """Play a sine wave which specified caracteristics.

        :param int frequence: Frequence in Hertz
        :param int gain: Volume Gain between 0 and 100
        :param int pan: Stereo Pan set to either {-1,0,+1}
        :param float duration: Duration of the sine wave in seconds
        """
        return self.proxy.playSine(frequence, gain, pan, duration)

    def playSoundSetFile(self, fileName):
        """Plays a file contained in one of the sound sets loaded

        :param str fileName: Name of the file without extension
        """
        return self.proxy.playSoundSetFile(fileName)

    def playSoundSetFile(self, soundSetName, fileName):
        """Plays a file contained in a given sound set

        :param str soundSetName: Name of the soundset
        :param str fileName: Name of the file without extension
        """
        return self.proxy.playSoundSetFile(soundSetName, fileName)

    def playSoundSetFile(self, soundSetName, fileName, position, volume, pan, loop):
        """Plays a file contained in a given sound set

        :param str soundSetName: Name of the soundset
        :param str fileName: Name of the file without extension
        :param float position: Position in second where the playing has to begin
        :param float volume: volume of the sound file (must be between 0.0 and 1.0)
        :param float pan: audio balance of the sound file (-1.0 : left / 1.0 : right)
        :param bool loop: specify if the file must be played in loop
        """
        return self.proxy.playSoundSetFile(soundSetName, fileName, position, volume, pan, loop)

    def playSoundSetFile(self, fileName, position, volume, pan, loop):
        """Plays a file contained in a given sound set

        :param str fileName: Name of the file without extension
        :param float position: Position in second where the playing has to begin
        :param float volume: volume of the sound file (must be between 0.0 and 1.0)
        :param float pan: audio balance of the sound file (-1.0 : left / 1.0 : right)
        :param bool loop: specify if the file must be played in loop
        """
        return self.proxy.playSoundSetFile(fileName, position, volume, pan, loop)

    def playWebStream(self, streamName, arg2, arg3):
        """Starts the playback of a wab audio stream

        :param str streamName: Path of the web audio stream
        :param float arg2: arg
        :param float arg3: arg
        """
        return self.proxy.playWebStream(streamName, arg2, arg3)

    def setMasterVolume(self, volume):
        """Sets the master volume of the player

        :param float volume: Volume - range 0.0 to 1.0
        """
        return self.proxy.setMasterVolume(volume)

    def setPanorama(self, arg1):
        """sets the audio panorama : -1 for left speaker / 1 for right speaker

        :param float arg1: arg
        """
        return self.proxy.setPanorama(arg1)

    def setVolume(self, id, volume):
        """Sets the volume of the player

        :param int id: Id of the process that is playing the file you want to put louder or less loud
        :param float volume: Volume - range 0.0 to 1.0
        """
        return self.proxy.setVolume(id, volume)

    def stop(self, id):
        """returns true if the method is currently running

        :param int id: the ID of the method to wait for
        """
        return self.proxy.stop(id)

    def stopAll(self):
        """Stops all the files that are currently playing.
        """
        return self.proxy.stopAll()

    def unloadAllFiles(self):
        """unloads all the files already loaded.
        """
        return self.proxy.unloadAllFiles()

    def unloadFile(self, id):
        """unloads a file previously loaded with the loadFile function

        :param int id: Id returned by the loadFile function
        """
        return self.proxy.unloadFile(id)

    def unloadSoundSet(self, setName):
        """Unload a sound set

        :param str setName: name of the set
        """
        return self.proxy.unloadSoundSet(setName)

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
