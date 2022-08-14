#!/usr/bin/python

# The ChartDirector for Python module is assumed to be in "../lib"
import sys, os
sys.path.insert(0, os.path.join(os.path.abspath(sys.path[0]), "..", "lib"))

from pychartdir import *

# The data for the bar chart
data = [85, 156, 179, 211, 123, 189, 166]

# The labels for the bar chart
labels = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

# Create a XYChart object of size 600 x 400 pixels
c = XYChart(600, 400)

# Add a title box using grey (0x555555) 24pt Arial Bold font
c.addTitle("    Bar Chart Demonstration", "Arial Bold", 24, 0x555555)

# Set the plotarea at (70, 60) and of size 500 x 300 pixels, with transparent background and border
# and light grey (0xcccccc) horizontal grid lines
c.setPlotArea(70, 60, 500, 300, Transparent, -1, Transparent, 0xcccccc)

# Set the x and y axis stems to transparent and the label font to 12pt Arial
c.xAxis().setColors(Transparent)
c.yAxis().setColors(Transparent)
c.xAxis().setLabelStyle("Arial", 12)
c.yAxis().setLabelStyle("Arial", 12)

# Add a blue (0x6699bb) bar chart layer with transparent border using the given data
c.addBarLayer(data, 0x6699bb).setBorderColor(Transparent)

# Set the labels on the x axis.
c.xAxis().setLabels(labels)

# For the automatic y-axis labels, set the minimum spacing to 40 pixels.
c.yAxis().setTickDensity(40)

# Add a title to the y axis using dark grey (0x555555) 14pt Arial Bold font
c.yAxis().setTitle("Y-Axis Title Placeholder", "Arial Bold", 14, 0x555555)

# Output the chart
c.makeChart("simplebar2.png")

