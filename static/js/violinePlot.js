// Plotly.d3.json("https://usacity-accidents-population.herokuapp.com/allcities", function(err, rows){

function renderViolinePlot2(myData, id, col1, col2){

  function unpack(myData, key) {
    return myData.map(function(myData) { return myData[key]; });
  }

var data = [{
  type: 'violin',
  x: unpack(myData, col1),
  y: unpack(myData, col2),
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
  transforms: [{
    type: 'groupby',
  groups: unpack(myData, col1),
  styles: [
   {target: '1', value: {line: {color: 'blue'}}},
   {target: '2', value: {line: {color: 'orange'}}},
   {target: '3', value: {line: {color: 'green'}}},
   {target: '4', value: {line: {color: 'red'}}}
  ]
 }]
  // x0: column
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