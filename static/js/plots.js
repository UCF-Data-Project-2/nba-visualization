var trace1 = {
  x: data.kobe.index_year,
  y: data.kobe.pts_year,
  name: "Kobe",
  mode: 'lines+markers',
  type: 'scatter'
  };
var trace2 = {
  x: data.kobe.index_year,
  y: data.lebron.pts_year,
  name: 'Lebron',
  mode: 'lines+markers',
  type: 'scatter'
  };
// var trace3 = {
//   x: [1, 2, 3, 4],
//   y: [12, 9, 15, 12],
//   mode: 'lines+markers',
//   type: 'scatter'
//   };
var layout = {
  title: "Kobe vs Lebron - Points",
  yaxis: { title: "Points"},
  xaxis: { title: "Year Index"}
  };
  
var chart1 = [trace1, trace2];

console.log(data)

Plotly.newPlot('interactive', chart1, layout);
