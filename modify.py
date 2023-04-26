# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 11:49:09 2023

@author: luca
"""
import numpy as np

def invert_signal(signal, invert_time=False, invert_amp=False):
    """Applies time and/or amplitude inversion to a discrete-time signal.
    
    Args:
    signal (np.array): Discrete-time signal.
    invert_time (bool, optional): If True, the signal is inverted in time. Default is False.
    invert_amp (bool, optional): If True, the signal is inverted in amplitude. Default is False.
    
    Returns:
    np.array: The inverted signal.
    """
    # Invert signal in time if specified
    if invert_time == True:
        signal = np.flip(signal)
    
    # Invert signal in amplitude if specified
    if invert_amp == True:
        signal = -1 * signal
        
    return signal

def shift_signal(signal, sample_shift, amp_shift, shift_sample = False, shift_amp = False):
    """
    Shifts a discrete-time signal in samples and/or amplitude.

    Args:
        signal (numpy.ndarray): The input signal to shift.
        sample_shift (int): The number of samples to shift the signal in time.
        amp_shift (float): The amplitude value to shift the signal.
        shift_sample (bool, optional): If True, shift the signal in time. Default is False.
        shift_amp (bool, optional): If True, shift the signal in amplitude. Default is False.

    Returns:
        numpy.ndarray: The shifted signal.
    """
    # Shift sample
    if shift_sample == True:
        signal = np.roll(signal, sample_shift)
    
    # Shift amplitude
    if shift_amp == True:
        signal = shift_amp*signal
    
    return signal

def operate_signal(signal_1, signal_2, operator):
    """
    Apply the selected mathematical operation between two signals of equal length.
    
    Args:
    signal_1 (np.array): First signal.
    signal_2 (np.array): Second signal.
    operator (str): Mathematical operator. Options are "add" for addition, "mult" for multiplication, and "convo" for convolution.
    
    Returns:
    np.array: The result of applying the selected operator to the input signals.
    """
    # Add
    if operator == "add":
        output = signal_1+signal_2
    
    # Multiply
    if operator == "mult":
        output = signal_1*signal_2
        
    # Convolution
    if operator == "convo":
        output = np.convolve(signal_1, signal_2)
    
    return output