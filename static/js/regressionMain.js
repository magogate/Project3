let selectFilters = d3.select("#selectFilters");

let ga_cities;
let usa_cities;

d3.json("https://usacity-accidents-population.herokuapp.com/allcities").then(function(myData, err) {
    ga_cities = myData
    renderScatterChart(myData, "scatterPlotGA", "value", "population", "city")
    renderViolinePlot(myData, "violinePlotGA", 'accidents')
    renderUSAScatterPlot()
})//end of d3.csv


function renderUSAScatterPlot(){

    d3.json("https://usacity-accidents-population.herokuapp.com/allcounties").then(function(myData, err) {
        usa_cities = myData
        renderScatterChart(myData, "scatterPlotUS", "value", "population", "county")
        renderViolinePlot(myData, "violinePlotUS", 'accidents')
    })//end of d3.csv

}

selectFilters.on("change", function(d){        
    console.log("hiiiiiii")    
    let colName = selectFilters.property("value");
    renderViolinePlot(ga_cities, "violinePlotGA", colName)
    renderViolinePlot(usa_cities, "violinePlotUS", colName)
})//end of cmbLocation