let selectFilters = d3.select("#selectFilters");
let accidentData;

d3.csv("\\US_Accidents_Dec19\\US_Accidents_2018.csv").then(function(myData, err) {
    accidentData = myData;  
    renderViolinePlot2(myData, "violinePlot", "Severity", 'TMC')
})//end of d3.csv


selectFilters.on("change", function(d){             
    let colName = selectFilters.property("value");
    renderViolinePlot2(accidentData, "violinePlot", "Severity", colName)    
})//end of cmbLocation