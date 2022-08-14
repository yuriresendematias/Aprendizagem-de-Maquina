#!/usr/bin/python

# The ChartDirector for Python module is assumed to be in "../lib"
import sys, os
sys.path.insert(0, os.path.join(os.path.abspath(sys.path[0]), "..", "lib"))

from pychartdir import *

# The data for the pie chart
data = [18, 45, 28]

# The labels for the pie chart
labels = ["Marble", "Wood", "Granite"]

# The icons for the sectors
texture = ["marble3.png", "wood.png", "rock.png"]

# Create a PieChart object of size 400 x 330 pixels, with a metallic green (88EE88) background,
# black border and 1 pixel 3D border effect
c = PieChart(400, 330, metalColor(0x88ee88), 0x000000, 1)

# Set donut center at (200, 160), and outer/inner radii as 120/60 pixels
c.setDonutSize(200, 160, 120, 60)

# Add a title box using 15pt Times Bold Italic font and metallic deep green (008000) background
# color
c.addTitle("Material Composition", "Times New Roman Bold Italic", 15).setBackground(metalColor(
    0x008000))

# Set the pie data and the pie labels
c.setData(data, labels)

# Set the colors of the sectors to the 3 texture patterns
c.setColor(DataColor + 0, c.patternColor2(texture[0]))
c.setColor(DataColor + 1, c.patternColor2(texture[1]))
c.setColor(DataColor + 2, c.patternColor2(texture[2]))

# Draw the pie in 3D with a 3D depth of 30 pixels
c.set3D(30)

# Use 12pt Arial Bold Italic as the sector label font
c.setLabelStyle("Arial Bold Italic", 12)

# Output the chart
c.makeChart("texturedonut.png")

