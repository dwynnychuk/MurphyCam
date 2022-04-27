# Main code
# April 2022

# import
from tabnanny import check
import cv2
import RPi.GPIO as GPIO
import time

from treat import Treat

class Murphycam:
    """Main class for project"""

    def __init__(self):
        """Initialize the project"""
        Treat(1)
