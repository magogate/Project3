let selectFilters = d3.select("#selectFilters");
let accidentData;

d3.csv("\\US_Accidents_Dec19\\US_Accidents_2018.csv").then(function(myData, err) {
    accidentData = myData;  
    renderViolinePlot(myData, "violinePlot", 'TMC')
})//end of d3.csv


selectFilters.on("change", function(d){        
    console.log("hiiiiiii")    
    let colName = selectFilters.property("value");
    renderViolinePlot(accidentData, "violinePlot", colName)    
})//end of cmbLocation