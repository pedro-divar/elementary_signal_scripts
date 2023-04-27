# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 23:52:16 2023

@author: Marco y Pedro
"""
import numpy as np

def unit_impulse(length, amplitude=1, shift=0):
    """
    Generate a unit impulse signal.

    Parameters
    ----------
    length : int
        Length of the signal.
    amplitude : float, optional
        Amplitude of the impulse (default is 1).
    shift : int, optional
        Amount to shift the impulse (default is 0).

    Returns
    -------
    signal : numpy.ndarray
        A 1D numpy array of length `length` containing the generated
        unit impulse signal.
    """

    signal = np.zeros(length)
    signal[shift] = amplitude

    return signal


def heavy_side(length, amplitude=1, shift=0):
    """
    Generate a unit step signal.

    Parameters
    ----------
    length : int
        Length of the signal.
    amplitude : float, optional
        Amplitude of the step (default is 1).
    shift : int, optional
        Amount to shift the step (default is 0).

    Returns
    -------
    signal : numpy.ndarray
        A 1D numpy array of length `length` containing the generated
        unit step signal.
    """
    signal = np.zeros(length)
    signal[shift:] = amplitude

    return signal


def rectangular_pulse(length, amplitude=1, shift=0, width=1):
    """
    Generate a rectangular pulse signal.

    Parameters
    ----------
    length : int
        Length of the signal.
    amplitude : float, optional
        Amplitude of the pulse (default is 1).
    shift : int, optional
        Amount to shift the pulse (default is 0).
    width : int, optional
        Width of the pulse (default is 1).

    Returns
    -------
    signal : numpy.ndarray
        A 1D numpy array of length `length` containing the generated
        rectangular pulse signal.
    """
    signal = np.zeros(length)
    signal[shift:shift+width] = amplitude

    return signal


def triangular_pulse(length, amplitude=1, shift=0, width=1):
    """
    Generate a triangular pulse signal.

    Parameters
    ----------
    length : int
        Length of the signal.
    amplitude : float, optional
        Amplitude of the pulse (default is 1).
    shift : int, optional
        Amount to shift the pulse (default is 0).
    width : int, optional
        Width of the pulse (default is 1).

    Returns
    -------
    signal : numpy.ndarray
        A 1D numpy array of length `length` containing the generated
        triangular pulse signal.
    """
    signal = np.zeros(length)
    t = np.linspace(-width/2, width/2, width)
    signal[shift:shift+width] = amplitude * (1 - np.abs(t) / (width/2))

    return signal

def exponential_signal(start, end, amplitude = 1, decay_rate = 1):
    """
    Generate an exponential signal.

    Parameters
    ----------
    length : int
        Length of the signal.
    amplitude : float, optional
        Amplitude of the signal (default is 1).
    decay_rate : float, optional
        Decay rate of the exponential function (default is 1).

    Returns
    -------
    signal : numpy.ndarray
        A 1D numpy array of length `length` containing the generated
        exponential signal.
    """
    samples = np.arange(start, end+1, 1)
    signal = amplitude * np.exp(decay_rate * samples)

    return samples, signal

def normal_signal(start, end, mean, std_dev):
 
    samples = np.arange(start,end+1,1)
    signal = np.random.normal(mean, std_dev, size=end-start+1)

    return samples, signal
