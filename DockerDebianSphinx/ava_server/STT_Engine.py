"""
    Speech-To-Text class handling for AVA

    STT: We are using CMUSphinx opensource library
    CMUSphinx:
        - English language model
        - Customize dictionnary
"""

from pocketsphinx.pocketsphinx import *
from sphinxbase.sphinxbase import *

import os
import pyaudio

# Class used to connect and send informations to Watson
class STT_Engine():

    # PocketSphinx folder
    def __init__(self):
        # Microphone stream config.
        self.RATE = 16000
        self.FPB = 2048
        self.CHUNK = 1024
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
	self.MODELDIR = "/usr/local/share/pocketsphinx/model"
        self.THRESHOLD = 4500
        self.num_phrases = -1

        # Create a decoder with certain model
        config = Decoder.default_config()
        config.set_string('-hmm', os.path.join(self.MODELDIR, 'en-us/en-us'))
        config.set_string('-lm', os.path.join(self.MODELDIR, 'en-us/en-us.lm.bin'))
        config.set_string('-dict', os.path.join(self.MODELDIR, 'en-us/cmudict-en-us.dict'))
        config.set_string('-logfn', '/dev/null')

        # Creaders decoder object for streaming data.
        self.decoder = Decoder(config)


    def recognize(self, stream):
        self.decoder.start_utt()
        self.decoder.process_raw(stream, False, False)
        in_speech_bf = self.decoder.get_in_speech()
        self.decoder.end_utt()
        result = self.decoder.hyp().hypstr
        if result == "":
            return "No Result"
        return result
