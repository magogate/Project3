// Plotly.d3.json("https://usacity-accidents-population.herokuapp.com/allcities", function(err, rows){


function renderViolinePlot(myData, id, column){

  function unpack(myData, key) {
    return myData.map(function(myData) { return myData[key]; });
  }


var data = [{
  type: 'violin',
  y: unpack(myData, column),
  points: 'none',
  box: {
    visible: true
  },
  boxpoints: false,
  line: {
    color: 'black'
  },
  fillcolor: '#8dd3c7',
  opacity: 0.6,
  meanline: {
    visible: true
  },
  x0: column
}]

var layout = {
    width: 1080,
    height: 450,
    title: "",
    yaxis: {
        zeroline: false
    }
}

  Plotly.newPlot(id, data, layout);

}