#!/usr/bin/python

# The ChartDirector for Python module is assumed to be in "../lib"
import sys, os
sys.path.insert(0, os.path.join(os.path.abspath(sys.path[0]), "..", "lib"))

from pychartdir import *

def createChart(chartIndex) :

    # The value to display on the meter
    value = 74.25

    # The background and border colors of the meters
    bgColor = [0xbbddff, 0xccffcc, 0xffccff, 0xffffaa, 0xffdddd, 0xeeeeee]
    borderColor = [0x000088, 0x006600, 0x6600aa, 0xee6600, 0x880000, 0x666666]

    # Create a LinearMeter object of size 70 x 260 pixels with a 3-pixel thick rounded frame
    m = LinearMeter(70, 260, bgColor[chartIndex], borderColor[chartIndex])
    m.setRoundedFrame(Transparent)
    m.setThickFrame(3)

    # Set the scale region top-left corner at (28, 30), with size of 20 x 200 pixels. The scale
    # labels are located on the left (default - implies vertical meter)
    m.setMeter(28, 30, 20, 200)

    # Set meter scale from 0 - 100, with a tick every 10 units
    m.setScale(0, 100, 10)

    # Demostrate different types of color scales and putting them at different positions
    smoothColorScale = [0, 0x6666ff, 25, 0x00bbbb, 50, 0x00ff00, 75, 0xffff00, 100, 0xff0000]
    stepColorScale = [0, 0x33ff33, 50, 0xffff33, 80, 0xff3333, 100]
    highLowColorScale = [0, 0x6666ff, 70, Transparent, 100, 0xff0000]

    if chartIndex == 0 :
        # Add the smooth color scale at the default position
        m.addColorScale(smoothColorScale)
    elif chartIndex == 1 :
        # Add the step color scale at the default position
        m.addColorScale(stepColorScale)
    elif chartIndex == 2 :
        # Add the high low scale at the default position
        m.addColorScale(highLowColorScale)
    elif chartIndex == 3 :
        # Add the smooth color scale starting at x = 28 (left of scale) with zero width and ending
        # at x = 28 with 20 pixels width
        m.addColorScale(smoothColorScale, 28, 0, 28, 20)
    elif chartIndex == 4 :
        # Add the smooth color scale starting at x = 38 (center of scale) with zero width and ending
        # at x = 28 with 20 pixels width
        m.addColorScale(smoothColorScale, 38, 0, 28, 20)
    else :
        # Add the smooth color scale starting at x = 48 (right of scale) with zero width and ending
        # at x = 28 with 20 pixels width
        m.addColorScale(smoothColorScale, 48, 0, 28, 20)

    # Add a blue (0x0000cc) pointer at the specified value
    m.addPointer(value, 0x0000cc)

    # Add a title using white (0xffffff) 8pt Arial Bold font with a border color background
    m.addTitle("Temp C", "Arial Bold", 8, 0xffffff).setBackground(borderColor[chartIndex])

    # Add a bottom title using white (0xffffff) 8pt Arial Bold font with a border color background
    # to display the value
    m.addTitle2(Bottom, m.formatValue(value, "2"), "Arial Bold", 8, 0xffffff).setBackground(
        borderColor[chartIndex])

    # Output the chart
    m.makeChart("colorvlinearmeter%s.png" % chartIndex)


createChart(0)
createChart(1)
createChart(2)
createChart(3)
createChart(4)
createChart(5)

