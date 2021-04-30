


var trace1 = {
    x: data.kobe.index_year,
    y: data.kobe.pts_year,
    name: 'Kobe',
    mode: 'lines+markers',
    type: 'scatter'
  };
var trace2 = {
  x: data.lebron.index_year,
  y: data.lebron.pts_year,
  name: 'Lebron',
  mode: 'lines+markers',
  type: 'scatter'
  };

var layout = {
  title: "Kobe vs Lebron - Points",
  yaxis: { title: "Points"},
  xaxis: { title: "Year Index"}
  };
  
var data = [trace1, trace2];
Plotly.newPlot('interactive', data, layout);


// static charts

