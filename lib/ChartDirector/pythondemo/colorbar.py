#!/usr/bin/python

# The ChartDirector for Python module is assumed to be in "../lib"
import sys, os
sys.path.insert(0, os.path.join(os.path.abspath(sys.path[0]), "..", "lib"))

from pychartdir import *

# The data for the bar chart
data = [85, 156, 179, 211, 123, 189, 166]

# The labels for the bar chart
labels = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

# The colors for the bars
colors = [0x5588bb, 0x66bbbb, 0xaa6644, 0x99bb55, 0xee9944, 0x444466, 0xbb5555]

# Create a XYChart object of size 600 x 400 pixels
c = XYChart(600, 400)

# Add a title box using grey (0x555555) 24pt Arial font
c.addTitle("Multi-Color Bar Chart", "Arial", 24, 0x555555)

# Set the plotarea at (70, 60) and of size 500 x 300 pixels, with transparent background and border
# and light grey (0xcccccc) horizontal grid lines
c.setPlotArea(70, 60, 500, 300, Transparent, -1, Transparent, 0xcccccc)

# Set the x and y axis stems to transparent and the label font to 12pt Arial
c.xAxis().setColors(Transparent)
c.yAxis().setColors(Transparent)
c.xAxis().setLabelStyle("Arial", 12)
c.yAxis().setLabelStyle("Arial", 12)

# Add a multi-color bar chart layer with transparent border using the given data
c.addBarLayer3(data, colors).setBorderColor(Transparent)

# Set the labels on the x axis.
c.xAxis().setLabels(labels)

# For the automatic y-axis labels, set the minimum spacing to 40 pixels.
c.yAxis().setTickDensity(40)

# Add a title to the y axis using dark grey (0x555555) 14pt Arial font
c.yAxis().setTitle("Y-Axis Title Placeholder", "Arial", 14, 0x555555)

# Output the chart
c.makeChart("colorbar.png")

