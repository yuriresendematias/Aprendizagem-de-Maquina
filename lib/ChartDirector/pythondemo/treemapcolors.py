#!/usr/bin/python

# The ChartDirector for Python module is assumed to be in "../lib"
import sys, os
sys.path.insert(0, os.path.join(os.path.abspath(sys.path[0]), "..", "lib"))

from pychartdir import *

# The first level nodes of the tree map. There are 3 nodes.
allRegions = ["Alpha", "Beta", "Gamma"]

# Each first level node branches to become 7 second level nodes.
energy_types = ["Coal", "Oil", "Gas", "Nuclear", "Hydro", "Solar", "Wind"]

# Colors for the second level nodes.
colors = [0x222222, 0x666666, 0x884488, 0xcc0000, 0x3366cc, 0x33cc33, 0x77bbff]

# The data for the 3 groups of second level nodes
region0 = [0, 50, 70, 0, 60, 120, 140]
region1 = [200, 50, 30, 65, 60, 40, 40]
region2 = [0, 100, 70, 100, 60, 35, 40]

# Create a Tree Map object of size 600 x 520 pixels
c = TreeMapChart(600, 520)

# Add a title to the chart
c.addTitle("Energy Usage by Region", "Arial Bold Italic", 18)

# Set the plotarea at (10, 35) and of size 480 x 480 pixels
c.setPlotArea(10, 35, 480, 480)

# Obtain the root of the tree map, which is the entire plot area
root = c.getRootNode()

# Add first level nodes to the root. We do not need to provide data as they will be computed as the
# sum of the second level nodes.
root.setData(None, allRegions)

# Add second level nodes to each of the first level node
root.getNode(0).setData(region0, energy_types, colors)
root.getNode(1).setData(region1, energy_types, colors)
root.getNode(2).setData(region2, energy_types, colors)

# Get the prototype (template) for the first level nodes.
nodeConfig = c.getLevelPrototype(1)

# Set the label format for the nodes to show the label with 8pt Arial Bold font in semi-transparent
# black color (0x77000000). Put the text at the top left corner of the cell.
nodeConfig.setLabelFormat("{label}", "Arial Bold", 18, 0x77ffffff, TopLeft)

# Set the border color to white (ffffff). Use 2 pixel thick flat border style.
nodeConfig.setColors(-1, 0xffffff, flatBorder(2))

# Get the prototype (template) for the second level nodes.
nodeConfig2 = c.getLevelPrototype(2)

# Set the label format for the nodes to show the label and value with 8pt Arial Bold font. Put the
# text at the center of the cell.
nodeConfig2.setLabelFormat("{label}<*br*>{value}MW", "Arial Bold", 8, 0xffffff, Center)

# Set the border color to white (ffffff)
nodeConfig2.setColors(-1, 0xffffff)

# Add a legend box at (500, 35) with 12pt Arial font and transparent background and border.
b = c.addLegend(500, 35, 1, "Arial", 12)
b.setBackground(Transparent, Transparent)

# Add the legend keys for the colors
for i in range(0, len(energy_types)) :
    b.addKey(energy_types[i], colors[i])

# Output the chart
c.makeChart("treemapcolors.png")

