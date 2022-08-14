#!/usr/bin/python

# The ChartDirector for Python module is assumed to be in "../lib"
import sys, os
sys.path.insert(0, os.path.join(os.path.abspath(sys.path[0]), "..", "lib"))

from pychartdir import *

#
# Data for 4 scatter layers to demonstrate various tooltip styles
#

dataX0 = [1, 1, 2, 2]
dataY0 = [3, 4, 3, 4]

dataX1 = [3, 3, 4, 4]
dataY1 = [3, 4, 3, 4]

dataX2 = [1, 1, 2, 2]
dataY2 = [1, 2, 1, 2]

dataX3 = [3, 3, 4, 4]
dataY3 = [1, 2, 1, 2]

# Create a XYChart object of size 550 x 390 pixels
c = XYChart(550, 390)

# Set the plotarea at (30, 40) and size 300 x 300 pixels. Use a gradient color background, light
# grey (c0c0c0) border, and light grey horizontal and vertical grid lines.
c.setPlotArea(30, 40, 300, 300, c.linearGradientColor(0, 30, 0, 330, 0xf9fcff, 0xaaccff), -1,
    0xc0c0c0, 0xc0c0c0, 0xc0c0c0)

# Add a legend box at the right side of the plot area. Use 10pt Arial Bold font and set background
# and border colors to Transparent.
c.addLegend(c.getPlotArea().getRightX() + 20, c.getPlotArea().getTopY(), 1, "Arial Bold Italic", 10
    ).setBackground(Transparent)

# Add a title to the chart using 18pt Times Bold Itatic font
c.addTitle("CDML Tooltip Demonstration", "Times New Roman Bold Italic", 18)

# Set the axes line width to 3 pixels, and ensure the auto axis labels are integers.
c.xAxis().setWidth(3)
c.yAxis().setWidth(3)
c.yAxis().setMinTickInc(1)
c.yAxis().setMinTickInc(1)

# Add a scatter chart layer with 19 pixel red (ff3333) sphere symbols. Use default CDML tooltip
# style.
layer0 = c.addScatterLayer(dataX0, dataY0, "Default CDML Tooltip", GlassSphere2Shape, 19, 0xff3333)
layer0.setHTMLImageMap("", "", "title='<*cdml*>{dataSetName}<*br*>X = {x}, Y = {value}'")

# Add a scatter chart layer with 19 pixel green (33ff33) sphere symbols. Cconfigure the CDML tooltip
# to use a background background with text of different colors and fonts.
layer1 = c.addScatterLayer(dataX1, dataY1, "Dark Style Tooltip", GlassSphere2Shape, 19, 0x33ff33)
layer1.setHTMLImageMap("", "",
    "title='<*block,bgcolor=000000,margin=5,roundedCorners=3*><*font=Arial Bold " \
    "Italic,color=FFFF00*>{dataSetName}<*/font*><*br*><*font=Arial Bold,size=8,color=FFFFFF*>X = " \
    "{x}, Y = {value}'")

# Add a scatter chart layer with 19 pixels sky blue (66ccff) symbols. Configure the CDML tooltip to
# ue a translucent background.
layer2 = c.addScatterLayer(dataX2, dataY2, "Translucent Tooltip", GlassSphere2Shape, 19, 0x66ccff)
layer2.setHTMLImageMap("", "",
    "title='<*block,bgcolor=5fffff00,margin=5,roundedCorners=3*><*font=Arial Bold*>" \
    "<*font,underline=1*>{dataSetName}<*/font*><*br*>X = {x}, Y = {value}'")

# Add a scatter chart layer with 19 pixels sky blue (ffff00) symbols. Use standard tooltips provided
# by the GUI framework.
layer3 = c.addScatterLayer(dataX3, dataY3, "Classical Tooltip", GlassSphere2Shape, 19, 0xffff00)
layer3.setHTMLImageMap("", "", "title='[{dataSetName}] X = {x}, Y = {value}'")

# Output the chart
c.makeChart("cdmltooltip.png")

