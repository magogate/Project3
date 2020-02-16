//  Created By: 
//      Grettel Canepari
//      Katherine Lee
//      Mandar Gogate
//      Petra Alex
//      Preet Puri
//      Sweta Shekhar
//  Created On: 01/01/2020
//  Updated On: 01/10/2020

function renderScatterChart(myData, id, xAxis, yAxis, col){

    // d3.select(".plot-container.plotly").remove();

    // console.log(myData)
  
    let xVal = [];
    let yVal = [];
    let label = [];
    myData.forEach(function(d){
      xVal.push(d.accidents);
      yVal.push(d.population);
      // console.log(col)
      label.push(d[col])
    })
  
      var trace1 = {
          x: xVal,
          y: yVal,
          mode: 'markers',
          type: 'scatter',
          name: 'Population Vs Accidents (' + col + ')',
          text: label,
          marker: { 
            size: 12,
            color: 'rgb(0, 0, 0)' 
          }
        };
  
        var layout = {
          title:'Population Vs Accidents (' + col + ')',
          xaxis: {
            title: 'Accidents',
            showgrid: true,
            zeroline: true
          },
          yaxis: {
            title: 'Population'            
          },
          width: 1080,
          height: 450
        };
  
      var data = [trace1];
  
      Plotly.newPlot(id, data, layout);
  
  }//end of renderScatterChart