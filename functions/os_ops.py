import os
import subprocess as sp


def open_camera():
    sp.Popen(["open", "-a", "Photo Booth"])

def open_notepad():
    sp.Popen(["open", "-a", "TextEdit"])

def open_discord():
    sp.Popen(["open", "-a", "Discord"])

def open_cmd():
    sp.Popen(["open", "-a", "Terminal"])

def open_calculator():
    sp.Popen(["open","-a","Calculator"])
