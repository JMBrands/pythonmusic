from enum import Enum, IntEnum
import math
import matplotlib.pyplot as plt
import numpy as np

class freq(Enum):
    C0 = 16.35
    Cs0 = 17.32
    D0 = 18.35
    Ds0 = 19.45
    E0 = 20.60
    F0 = 21.83
    Fs0 = 23.12
    G0 = 24.50
    Gs0 = 25.96
    A0 = 27.50
    As0 = 29.14
    B0 = 30.87
    C1 = 16.35*2
    Cs1 = 17.32*2
    D1 = 18.35*2
    Ds1 = 19.45*2
    E1 = 20.60*2
    F1 = 21.83*2
    Fs1 = 23.12*2
    G1 = 24.50*2
    Gs1 = 25.96*2
    A1 = 27.50*2
    As1 = 29.14*2
    B1 = 30.87*2
    C2 = 16.35*4
    Cs2 = 17.32*4
    D2 = 18.35*4
    Ds2 = 19.45*4
    E2 = 20.60*4
    F2 = 21.83*4
    Fs2 = 23.12*4
    G2 = 24.50*4
    Gs2 = 25.96*4
    A2 = 27.50*4
    As2 = 29.14*4
    B2 = 30.87*4
    C3 = 16.35*8
    Cs3 = 17.32*8
    D3 = 18.35*8
    Ds3 = 19.45*8
    E3 = 20.60*8
    F3 = 21.83*8
    Fs3 = 23.12*8
    G3 = 24.50*8
    Gs3 = 25.96*8
    A3 = 27.50*8
    As3 = 29.14*8
    B3 = 30.87*8
    C4 = 16.35*16
    Cs4 = 17.32*16
    D4 = 18.35*16
    Ds4 = 19.45*16
    E4 = 20.60*16
    F4 = 21.83*16
    Fs4 = 23.12*16
    G4 = 24.50*16
    Gs4 = 25.96*16
    A4 = 27.50*16
    As4 = 29.14*16
    B4 = 30.87*16
    C5 = 16.35*32
    Cs5 = 17.32*32
    D5 = 18.35*32
    Ds5 = 19.45*32
    E5 = 20.60*32
    F5 = 21.83*32
    Fs5 = 23.12*32
    G5 = 24.50*32
    Gs5 = 25.96*32
    A5 = 27.50*32
    As5 = 29.14*32
    B5 = 30.87*32
    C6 = 16.35*64
    Cs6 = 17.32*64
    D6 = 18.35*64
    Ds6 = 19.45*64
    E6 = 20.60*64
    F6 = 21.83*64
    Fs6 = 23.12*64
    G6 = 24.50*64
    Gs6 = 25.96*64
    A6 = 27.50*64
    As6 = 29.14*64
    B6 = 30.87*64
    C7 = 16.35*128
    Cs7 = 17.32*128
    D7 = 18.35*128
    Ds7 = 19.45*128
    E7 = 20.60*128
    F7 = 21.83*128
    Fs7 = 23.12*128
    G7 = 24.50*128
    Gs7 = 25.96*128
    A7 = 27.50*128
    As7 = 29.14*128
    B7 = 30.87*128
    C8 = 16.35*256
    Cs8 = 17.32*256
    D8 = 18.35*256
    Ds8 = 19.45*256
    E8 = 20.60*256
    F8 = 21.83*256
    Fs8 = 23.12*256
    G8 = 24.50*256
    Gs8 = 25.96*256
    A8 = 27.50*256
    As8 = 29.14*256
    B8 = 30.87*256

midi = [(440*(2**(1/12))**(x-69)) for x in range(128)]

class length(IntEnum):
    sixtyforth = 1
    thirtysecond = 2
    sixteenth = 4
    eighth = 8
    quarter = 16
    half = 32
    whole = 64

class waveforms(Enum):
    sin = lambda t, freq, amp: math.sin(t*2*math.pi*freq)*amp
    cos = lambda t, freq, amp: math.cos(t*2*math.pi*freq)*amp
    square = lambda t, freq, amp: ((-1)**int(2*freq*t))*amp
    triangle = lambda t, freq, amp: (2*amp)/math.pi*math.asin(math.sin((2*math.pi)/(1/freq)*t))
    sawtooth = lambda t, freq , amp: (((2*math.atan(math.tan((2*math.pi*t*freq)/2)))/math.pi)*amp)

class note:
    def __init__(self, pitch: int, length: length):
        """
a class for a note

Attributes
----------

pitch : int
    the midi pitch of the note
length : length
    the length of the note
        """
        self.pitch = pitch
        self.length = length
        self.freq = midi[pitch]

class rest:
    def __init__(self, length: length):
        """
a class for a rest

Attributes
----------
length : length
    the length of the rest
        """
        self.length = length

class chord:
    def __init__(self):
        """a class representing a chord"""
        self.notes = []
        pass
    
    def add_note(self, note: note):
        self.notes.append(note)


class voice:
    def __init__(self, volume, wave):
        """
a class representing a musical score to be used in a score
        """
        self.chords = []
        self.volume = volume
        self.wave = wave
        pass

    def add_chord(self, chord: chord):
        """add a note to the voice"""
        self.chords.append(note)

class score:
    def __init__(self, bpm: int):
        """
a class for a musical score

Attributes
----------
bpm : int
    the bpm of the score
        """
        self.bpm = bpm
        self.voices = []
    
    def add_voice(self, voice: voice):
        """add a voice to the score"""
        self.voices.append(voice)