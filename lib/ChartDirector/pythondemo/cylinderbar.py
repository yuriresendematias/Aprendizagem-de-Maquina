#!/usr/bin/python

# The ChartDirector for Python module is assumed to be in "../lib"
import sys, os
sys.path.insert(0, os.path.join(os.path.abspath(sys.path[0]), "..", "lib"))

from pychartdir import *

# The data for the bar chart
data = [85, 156, 179.5, 211, 123]

# The labels for the bar chart
labels = ["Mon", "Tue", "Wed", "Thu", "Fri"]

# Create a XYChart object of size 400 x 240 pixels.
c = XYChart(400, 240)

# Add a title to the chart using 14pt Times Bold Italic font
c.addTitle("Weekly Server Load", "Times New Roman Bold Italic", 14)

# Set the plotarea at (45, 40) and of 300 x 160 pixels in size. Use alternating light grey (f8f8f8)
# / white (ffffff) background.
c.setPlotArea(45, 40, 300, 160, 0xf8f8f8, 0xffffff)

# Add a multi-color bar chart layer
layer = c.addBarLayer3(data)

# Set layer to 3D with 10 pixels 3D depth
layer.set3D(10)

# Set bar shape to circular (cylinder)
layer.setBarShape(CircleShape)

# Set the labels on the x axis.
c.xAxis().setLabels(labels)

# Add a title to the y axis
c.yAxis().setTitle("MBytes")

# Add a title to the x axis
c.xAxis().setTitle("Work Week 25")

# Output the chart
c.makeChart("cylinderbar.png")

