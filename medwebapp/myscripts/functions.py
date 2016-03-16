import serial
import numpy as np
from array import array
from matplotlib import pyplot as plt
import pylab as pl
import math
import cmath
from multiprocessing import Process
import thinkdspf.thinkdsp as thinkdsp
import adaptfilt as adf
from pybrain.datasets import SupervisedDataSet
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
import pickle
import scipy as sp
import pandas as pd
import csv as csv
from sklearn.ensemble import RandomForestClassifier
import os

##................................................................##
Fs=4.167#sampling frequency in Hz, e.g. sampling interval=80 ms Fs=12.5Hz
def estimate(data):
    length=len(data)
    wave=thinkdsp.Wave(ys=data,framerate=Fs)
    spectrum=wave.make_spectrum()
    spectrum_heart=wave.make_spectrum()
    spectrum_resp=wave.make_spectrum()

    fft_mag=list(np.absolute(spectrum.hs))
    fft_length= len(fft_mag)

    spectrum_heart.high_pass(cutoff=0.8,factor=0.001)
    spectrum_heart.low_pass(cutoff=2,factor=0.001)
    fft_heart=list(np.absolute(spectrum_heart.hs))

    max_fft_heart=max(fft_heart)
    heart_sample=fft_heart.index(max_fft_heart)
    hr=heart_sample*Fs/length*60

    spectrum_resp.high_pass(cutoff=0.15,factor=0)
    spectrum_resp.low_pass(cutoff=0.4,factor=0)
    fft_resp=list(np.absolute(spectrum_resp.hs))

    max_fft_resp=max(fft_resp)
    resp_sample=fft_resp.index(max_fft_resp)
    rr=resp_sample*Fs/length*60

    return hr,rr