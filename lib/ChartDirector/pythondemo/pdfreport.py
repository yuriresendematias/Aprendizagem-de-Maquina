#!/usr/bin/python

# The ChartDirector for Python module is assumed to be in "../lib"
import sys, os
sys.path.insert(0, os.path.join(os.path.abspath(sys.path[0]), "..", "lib"))

from pychartdir import *

#
# 5 years of random data series
#
r = RanSeries(127)
timeStamps = r.getDateSeries(1827, chartTime(2015, 1, 1), 86400)
dataSeriesA = r.getSeries(1827, 150, -10, 10)
dataSeriesB = r.getSeries(1827, 200, -10, 10)
dataSeriesC = r.getSeries(1827, 250, -8, 8)

#
# Draw an XYChart using data from startDate to endDate
#
def drawXYChart(startDate, endDate) :

    startIndex = int(bSearch(timeStamps, startDate))
    endIndex = int(bSearch(timeStamps, endDate) + 0.999999)

    #================================================================================
    # Configure overall chart appearance.
    #================================================================================

    # Create an XYChart object of size 640 x 350 pixels
    c = XYChart(640, 350)

    # Set the plotarea at (55, 50) with width 80 pixels less than chart width, and height 85 pixels
    # less than chart height. Use a vertical gradient from light blue (f0f6ff) to sky blue (a0c0ff)
    # as background. Set border to transparent and grid lines to white (ffffff).
    c.setPlotArea(55, 50, c.getWidth() - 80, c.getHeight() - 85, c.linearGradientColor(0, 50, 0,
        c.getHeight() - 35, 0xf0f6ff, 0xa0c0ff), -1, Transparent, 0xffffff, 0xffffff)

    # As the data can lie outside the plotarea in a zoomed chart, we need enable clipping.
    c.setClipping()

    # Add a legend box at (55, 25) using horizontal layout. Use 8pts Arial Bold as font. Set the
    # background and border color to Transparent and use line style legend key.
    b = c.addLegend(55, 25, 0, "Arial Bold", 8)
    b.setBackground(Transparent)
    b.setLineStyleKey()

    # Set the axis stem to transparent
    c.xAxis().setColors(Transparent)
    c.yAxis().setColors(Transparent)

    # Add axis title using 10pts Arial Bold Italic font
    c.yAxis().setTitle("Ionic Temperature (C)", "Arial Bold Italic", 10)

    #================================================================================
    # Add data to chart
    #================================================================================

    #
    # In this example, we represent the data by lines. You may modify the code below to use other
    # representations (areas, scatter plot, etc).
    #

    # Add a line layer for the lines, using a line width of 2 pixels
    layer = c.addLineLayer2()
    layer.setLineWidth(2)

    # Now we add the 3 data series to a line layer, using the color red (ff33333), green (008800)
    # and blue (3333cc)
    layer.setXData(timeStamps[startIndex:endIndex + 1])
    layer.addDataSet(dataSeriesA[startIndex:endIndex + 1], 0xff3333, "Alpha")
    layer.addDataSet(dataSeriesB[startIndex:endIndex + 1], 0x008800, "Beta")
    layer.addDataSet(dataSeriesC[startIndex:endIndex + 1], 0x3333cc, "Gamma")

    #================================================================================
    # Configure axis scale and labelling
    #================================================================================

    # Set the x-axis scale
    c.xAxis().setDateScale(timeStamps[startIndex], timeStamps[endIndex])
    c.xAxis().setMultiFormat(StartOfYearFilter(), "<*font=bold*>{value|mmm yyyy}", AllPassFilter(),
        "{value|mmm}")

    return c

#
# Create the report
#

# The MultiPagePDF object can create PDF from multiple pages, each with one chart object. Since a
# chart object can contain text (eg. using BaseChart.addText) and other charts (eg. using
# MultiChart), that means each page can contain text and multiple charts.
doc = MultiPagePDF()

# Page configuration - A4 = 210 x 297mm. The PDF default is 96 dpi (dot per inch), so the A4 size is
# equal to 794 x 1123 dots.
pageConfig = "pagewidth = 794; pageHeight = 1123"

# In this example, we include a cover page with only text. This is by creating an empty pie chart
# with text only.
firstPage = PieChart(720, 960)
firstPage.addText(360, 320,
    "<*size=50*>ChartDirector<*br*><*size=30*>PDF Report Demonstration<*/*>", "Arial Bold", 30,
    0x000000, Center)
firstPage.setOutputOptions(pageConfig)
doc.addPage(firstPage)

# We include 2 charts per page, with each chart showing one year of data. Each page will also have a
# header and page number
startYear = int(getChartYMD(timeStamps[0]) / 10000)
endYear = int(getChartYMD(timeStamps[len(timeStamps) - 1] - 1) / 10000)
pageNumber = 0

for yyyy in range(startYear, endYear + 1, 2) :
    # A page contains up to two charts
    m = MultiChart(760, 920)

    # Use addTitle to add a header
    m.addTitle("ChartDirector PDF Report Demonstration", "Arial Bold", 20)

    # Create the first chart
    c = drawXYChart(chartTime(yyyy, 1, 1), chartTime(yyyy + 1, 1, 1))
    c.addTitle("Year %s" % (yyyy))
    m.addChart((m.getWidth() - c.getWidth()) / 2, 100, c)

    if yyyy < endYear :
        # Create the second chart
        c2 = drawXYChart(chartTime(yyyy + 1, 1, 1), chartTime(yyyy + 2, 1, 1))
        c2.addTitle("Year %s" % (yyyy + 1))
        m.addChart((m.getWidth() - c2.getWidth()) / 2, 500, c2)

    # Add the page number
    pageNumber = pageNumber + 1
    m.addTitle2(BottomCenter, str(pageNumber), "Arial Bold", 8)

    m.setOutputOptions(pageConfig)
    doc.addPage(m)

doc.outPDF("pdfreport.pdf")

