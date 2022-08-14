#!/usr/bin/python

# The ChartDirector for Python module is assumed to be in "../lib"
import sys, os
sys.path.insert(0, os.path.join(os.path.abspath(sys.path[0]), "..", "lib"))

from pychartdir import *

# Data for the tree map
data = [25, 18, 15, 12, 8, 30, 35]

# Labels for the tree map
labels = ["Alpha", "Beta", "Gamma", "Delta", "Epsilon", "Zeta", "Eta"]

# Colors for the tree map
colors = [0xff5555, 0xff9933, 0xffff44, 0x66ff66, 0x44ccff, 0x6699ee, 0xdd99dd]

# Create a Tree Map object of size 400 x 400 pixels
c = TreeMapChart(400, 400)

# Set the plotarea at (10, 10) and of size 380 x 380 pixels
c.setPlotArea(10, 10, 380, 380)

# Obtain the root of the tree map, which is the entire plot area
root = c.getRootNode()

# Add first level nodes to the root.
root.setData(data, labels, colors)

# Get the prototype (template) for the first level nodes.
nodeConfig = c.getLevelPrototype(1)

# Set the label format for the nodes to show the label and value with 8pt Arial Bold font in black
# color (000000) and center aligned in the node.
nodeConfig.setLabelFormat("{label}<*br*>{value}", "Arial Bold", 8, 0x000000, Center)

# Set the node fill color to the provided color and the border color to white (ffffff)
nodeConfig.setColors(-1, 0xffffff)

# Output the chart
c.makeChart("simpletreemap.png")

