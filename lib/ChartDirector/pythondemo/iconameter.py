#!/usr/bin/python

# The ChartDirector for Python module is assumed to be in "../lib"
import sys, os
sys.path.insert(0, os.path.join(os.path.abspath(sys.path[0]), "..", "lib"))

from pychartdir import *

# The value to display on the meter
value = 85

# Create an AugularMeter object of size 70 x 90 pixels, using black background with a 2 pixel 3D
# depressed border.
m = AngularMeter(70, 90, 0, 0, -2)

# Use white on black color palette for default text and line colors
m.setColors(whiteOnBlackPalette)

# Set the meter center at (10, 45), with radius 50 pixels, and span from 135 to 45 degrees
m.setMeter(10, 45, 50, 135, 45)

# Set meter scale from 0 - 100, with the specified labels
labels = ["E", " ", " ", " ", "F"]
m.setScale2(0, 100, labels)

# Set the angular arc and major tick width to 2 pixels
m.setLineWidth(2, 2)

# Add a red zone at 0 - 15
m.addZone(0, 15, 0xff3333)

# Add an icon at (25, 35)
m.addText(25, 35, "<*img=gas.png*>")

# Add a yellow (ffff00) pointer at the specified value
m.addPointer(value, 0xffff00)

# Output the chart
m.makeChart("iconameter.png")

