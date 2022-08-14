#!/usr/bin/python

# The ChartDirector for Python module is assumed to be in "../lib"
import sys, os
sys.path.insert(0, os.path.join(os.path.abspath(sys.path[0]), "..", "lib"))

from pychartdir import *

# The data for the pie chart
data = [21, 18, 15, 12, 8, 24]

# The labels for the pie chart
labels = ["Labor", "Licenses", "Taxes", "Legal", "Facilities", "Production"]

# The colors to use for the sectors
colors = [0x66aaee, 0xeebb22, 0xbbbbbb, 0x8844ff, 0xdd2222, 0x009900]

# Create a PieChart object of size 600 x 320 pixels. Use a vertical gradient color from light blue
# (99ccff) to white (ffffff) spanning the top 100 pixels as background. Set border to grey (888888).
# Use rounded corners. Enable soft drop shadow.
c = PieChart(600, 320)
c.setBackground(c.linearGradientColor(0, 0, 0, 100, 0x99ccff, 0xffffff), 0x888888)
c.setRoundedFrame()
c.setDropShadow()

# Add a title using 18pt Times New Roman Bold Italic font. Add 16 pixels top margin to the title.
c.addTitle("Pie Chart With Legend Demonstration", "Times New Roman Bold Italic", 18).setMargin2(0,
    0, 16, 0)

# Set the center of the pie at (160, 165) and the radius to 110 pixels
c.setPieSize(160, 165, 110)

# Draw the pie in 3D with a pie thickness of 25 pixels
c.set3D(25)

# Set the pie data and the pie labels
c.setData(data, labels)

# Set the sector colors
c.setColors2(DataColor, colors)

# Use local gradient shading for the sectors
c.setSectorStyle(LocalGradientShading)

# Use the side label layout method, with the labels positioned 16 pixels from the pie bounding box
c.setLabelLayout(SideLayout, 16)

# Show only the sector number as the sector label
c.setLabelFormat("{={sector}+1}")

# Set the sector label style to Arial Bold 10pt, with a dark grey (444444) border
c.setLabelStyle("Arial Bold", 10).setBackground(Transparent, 0x444444)

# Add a legend box, with the center of the left side anchored at (330, 175), and using 10pt Arial
# Bold Italic font
b = c.addLegend(330, 175, 1, "Arial Bold Italic", 10)
b.setAlignment(Left)

# Set the legend box border to dark grey (444444), and with rounded conerns
b.setBackground(Transparent, 0x444444)
b.setRoundedCorners()

# Set the legend box margin to 16 pixels, and the extra line spacing between the legend entries as 5
# pixels
b.setMargin(16)
b.setKeySpacing(0, 5)

# Set the legend box icon to have no border (border color same as fill color)
b.setKeyBorder(SameAsMainColor)

# Set the legend text to show the sector number, followed by a 120 pixels wide block showing the
# sector label, and a 40 pixels wide block showing the percentage
b.setText(
    "<*block,valign=top*>{={sector}+1}.<*advanceTo=22*><*block,width=120*>{label}<*/*>" \
    "<*block,width=40,halign=right*>{percent}<*/*>%")

# Output the chart
c.makeChart("legendpie2.png")

