#!/usr/bin/python

# The ChartDirector for Python module is assumed to be in "../lib"
import sys, os
sys.path.insert(0, os.path.join(os.path.abspath(sys.path[0]), "..", "lib"))

from pychartdir import *

# The x-axis and y-axis labels
xLabels = ["Alpha", "Beta", "Gamma", "Delta", "Epsilon", "Zeta", "Eta", "Theta", "Iota", "Kappa"]
yLabels = ["Ant", "Bear", "Cat", "Dog", "Elephant", "Fox", "Goat", "Horse", "Insect", "Jellyfish"]

# Random data for the 10 x 10 cells
rand = RanSeries(2)
zData = rand.getSeries(len(xLabels) * len(yLabels), 0, 10)

# The coordinates for the first set of scatter symbols
symbolX = [2.5, 6.5, 3.5, 8.5]
symbolY = [4.5, 7.5, 9.5, 8.5]

# The coordinates for the second set of scatter symbols
symbol2X = [6.5, 3.5, 7.5, 1.5]
symbol2Y = [0.5, 7.5, 3.5, 2.5]

# Create an XYChart object of size 600 x 500 pixels.
c = XYChart(600, 500)

# Set the plotarea at (80, 80) and of size 400 x 400 pixels. Set the background, border, and grid
# lines to transparent.
p = c.setPlotArea(80, 80, 400, 400, -1, -1, Transparent, Transparent)

# Add the first set of scatter symbols. Use grey (0x555555) cross shape symbols.
c.addScatterLayer(symbolX, symbolY, "Disputed", Cross2Shape(0.2), 15, 0x555555)

# Add the first set of scatter symbols. Use yellow (0xffff66) star shape symbols.
c.addScatterLayer(symbol2X, symbol2Y, "Audited", StarShape(5), 19, 0xffff66)

# Create a discrete heat map with 10 x 10 cells
layer = c.addDiscreteHeatMapLayer(zData, len(xLabels))

# Set the x-axis labels. Use 10pt Arial Bold font rotated by 90 degrees. Set axis stem to
# transparent, so only the labels are visible. Set 0.5 offset to position the labels in between the
# grid lines. Position the x-axis at the top of the chart.
c.xAxis().setLabels(xLabels)
c.xAxis().setLabelStyle("Arial Bold", 10, TextColor, 90)
c.xAxis().setColors(Transparent, TextColor)
c.xAxis().setLabelOffset(0.5)
c.setXAxisOnTop()

# Set the y-axis labels. Use 10pt Arial Bold font. Set axis stem to transparent, so only the labels
# are visible. Set 0.5 offset to position the labels in between the grid lines. Reverse the y-axis
# so that the labels are flowing top-down instead of bottom-up.
c.yAxis().setLabels(yLabels)
c.yAxis().setLabelStyle("Arial Bold", 10)
c.yAxis().setColors(Transparent, TextColor)
c.yAxis().setLabelOffset(0.5)
c.yAxis().setReverse()

# Set the color stops and scale
colorScale = [0, 0xff0000, 1, 0xff8800, 3, 0x4488cc, 7, 0x99ccff, 9, 0x00ff00, 10]
colorLabels = ["Poor", "Fair", "Good", "Very Good", "Excellent"]
layer.colorAxis().setColorScale(colorScale)

# Position the legend box 20 pixels to the right of the plot area. Use 10pt Arial Bold font. Set the
# key icon size to 15 x 15 pixels. Set vertical key spacing to 8 pixels.
b = c.addLegend(p.getRightX() + 20, p.getTopY(), 1, "Arial Bold", 10)
b.setBackground(Transparent, Transparent)
b.setKeySize(15, 15)
b.setKeySpacing(0, 8)

# Add the color scale label to the legend box
for i in range(len(colorLabels) - 1, -1, -1) :
    b.addKey(colorLabels[i], int(colorScale[i * 2 + 1]))

# Output the chart
c.makeChart("heatmapcellsymbols.png")

