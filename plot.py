# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 12:25:11 2023

@author: luca
"""
import matplotlib.pyplot as plt
import numpy as np

def plot_signal(signal, title=f"{signal}", color="b", xl="Samples", yl="Amplitude", png_save=False, png_name, npy_load=False, npy_save=False, npy_file):
    """
    Plots a given signal and saves it in .png and/or .npy format if requested.
    
    Args:
        signal (np.array): Discrete-time signal.
        title (str, optional): Plot title. Default is f"{signal}".
        color (str, optional): Plot color. Default is "b" (blue).
        xl (str, optional): Label for x-axis. Default is "Samples".
        yl (str, optional): Label for y-axis. Default is "Amplitude".
        png_save (bool, optional): If True, saves the plot as a .png file. Default is False.
        png_name (str, optional): Name of the .png file. Only used if png_save is True. Default is None.
        npy_load (bool, optional): If True, loads a signal from a .npy file. Default is False.
        npy_save (bool, optional): If True, saves the signal as a .npy file. Default is False.
        npy_file (str, optional): Name of the .npy file. Only used if npy_load or npy_save are True. Default is None.
    
    Returns:
        None
    """
    # Load the signal from a .npy file if requested
    if npy_input == True:
        signal = np.load(f"{npy_file}")
    
    # Plot the signal
    plt.figure()
    plt.plot(signal, f"{color}")
    plt.title(title)
    plt.xlabel(xl)
    plt.ylabel(yl)
    
    # Save as .png
    if png_save == True:
        plt.savefig(f"{png_name}")
    
    # Save as .npy
    if npy_save == True:
        np.save(f"{npy_file}", signal)