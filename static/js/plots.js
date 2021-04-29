var trace1 = {
<<<<<<< HEAD
  x: data.kobe.kb_year_index,
  y: data.kobe.kb_pts_yr,
  name: "Kobe",
  mode: 'lines+markers',
  type: 'scatter'
=======
    x: kb_year_index,
    y: data.kobe.kb_pts_yr,
    name: "Kobe",
    mode: 'lines+markers',
    type: 'scatter'
>>>>>>> cb53a816777b55c8dd84677bbfe781927361d55e
  };
var trace2 = {
  x: data.lebron.Plotlylj_year_index,
  y: data.lebron.lj_pts_yr,
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
  
var data = [trace1, trace2];

console.log(data.kobe.kb_pts_yr)

Plotly.newPlot('myDiv', data);
