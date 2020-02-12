d3.csv("https://usacity-accidents-population.herokuapp.com/gacities").then(function(myData, err) {
    ga_cities = myData
    renderScatterChart(myData, "scatterPlotGA", "value", "population", "City")
    renderViolinePlot(myData, "violinePlotGA", 'accidents')
    renderUSAScatterPlot()
})//end of d3.csv