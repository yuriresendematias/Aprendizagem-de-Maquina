#!/usr/bin/python

# The ChartDirector for Python module is assumed to be in "../lib"
import sys, os
sys.path.insert(0, os.path.join(os.path.abspath(sys.path[0]), "..", "lib"))

from pychartdir import *

# The x-axis and y-axis labels
xLabels = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
yLabels = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

# Random data for the 10 x 10 cells
r = RanSeries(2)
zData = r.get2DSeries(len(xLabels), len(yLabels), 0, 100)

# Create an XYChart object of size 520 x 470 pixels.
c = XYChart(520, 470)

# Set the plotarea at (50, 30) and of size 400 x 400 pixels.
p = c.setPlotArea(50, 30, 400, 400)

# Create a discrete heat map with 10 x 10 cells
layer = c.addDiscreteHeatMapLayer(zData, len(xLabels))

# Set the x-axis labels. Use 8pt Arial Bold font. Set axis stem to transparent, so only the labels
# are visible. Set 0.5 offset to position the labels in between the grid lines.
c.xAxis().setLabels(xLabels)
c.xAxis().setLabelStyle("Arial Bold", 8)
c.xAxis().setColors(Transparent, TextColor)
c.xAxis().setLabelOffset(0.5)
c.xAxis().setTitle("X Axis Title Placeholder", "Arial Bold", 12)

# Set the y-axis labels. Use 8pt Arial Bold font. Set axis stem to transparent, so only the labels
# are visible. Set 0.5 offset to position the labels in between the grid lines.
c.yAxis().setLabels(yLabels)
c.yAxis().setLabelStyle("Arial Bold", 8)
c.yAxis().setColors(Transparent, TextColor)
c.yAxis().setLabelOffset(0.5)
c.yAxis().setTitle("Y Axis Title Placeholder", "Arial Bold", 12)

# Position the color axis 20 pixels to the right of the plot area and of the same height as the plot
# area. Put the labels on the right side of the color axis. Use 8pt Arial Bold font for the labels.
cAxis = layer.setColorAxis(p.getRightX() + 20, p.getTopY(), TopLeft, p.getHeight(), Right)
cAxis.setLabelStyle("Arial Bold", 8)

# Output the chart
c.makeChart("discreteheatmap.png")

