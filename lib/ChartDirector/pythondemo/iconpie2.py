#!/usr/bin/python

# The ChartDirector for Python module is assumed to be in "../lib"
import sys, os
sys.path.insert(0, os.path.join(os.path.abspath(sys.path[0]), "..", "lib"))

from pychartdir import *

# The data for the pie chart
data = [28, 45, 5, 1, 12]

# The labels for the pie chart
labels = ["Excellent", "Good", "Bad", "Very Bad", "Neutral"]

# The icons for the sectors
icons = ["laugh.png", "smile.png", "sad.png", "angry.png", "nocomment.png"]

# Create a PieChart object of size 560 x 300 pixels, with a silver background, black border, 1 pxiel
# 3D border effect and rounded corners
c = PieChart(560, 300, silverColor(), 0x000000, 1)
c.setRoundedFrame()

# Set the center of the pie at (280, 150) and the radius to 120 pixels
c.setPieSize(280, 150, 120)

# Add a title box with title written in CDML, on a sky blue (A0C8FF) background with glass effect
c.addTitle(
    "<*block,valign=absmiddle*><*img=doc.png*> Customer Survey: <*font=Times New Roman " \
    "Italic,color=000000*>Do you like our <*font,color=dd0000*>Hyper<*super*>TM<*/font*> " \
    "molecules?", "Times New Roman Bold Italic", 15, 0x000080).setBackground(0xa0c8ff, 0x000000,
    glassEffect())

# Add a logo to the chart written in CDML as the bottom title aligned to the bottom right
c.addTitle2(BottomRight,
    "<*block,valign=absmiddle*><*img=molecule.png*> <*block*><*color=FF*><*font=Times New Roman " \
    "Bold Italic,size=12*>Molecular Engineering\n<*font=Arial,size=10*>Creating better molecules")

# Set the pie data and the pie labels
c.setData(data, labels)

# Set 3D style
c.set3D()

# Use the side label layout method
c.setLabelLayout(SideLayout)

# Set the label background color to transparent
c.setLabelStyle().setBackground(Transparent)

# Add icons to the chart as a custom field
c.addExtraField(icons)

# Configure the sector labels using CDML to include the icon images
c.setLabelFormat("<*block,valign=absmiddle*><*img={field0}*> {label} ({percent|0}%)")

# Explode the 3rd and 4th sectors as a group (index = 2 and 3)
c.setExplodeGroup(2, 3)

# Set the start angle to 135 degrees may improve layout when there are many small sectors at the end
# of the data array (that is, data sorted in descending order). It is because this makes the small
# sectors position near the horizontal axis, where the text label has the least tendency to overlap.
# For data sorted in ascending order, a start angle of 45 degrees can be used instead.
c.setStartAngle(135)

# Output the chart
c.makeChart("iconpie2.png")

