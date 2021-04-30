


var trace1 = {
<<<<<<< HEAD
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
=======
    x: data.kobe.index_year,
    y: data.kobe.pts_year,
    name: 'Kobe',
>>>>>>> 6137e27ce8cbb9b17aa64a851c4518f0570a150f
    mode: 'lines+markers',
    type: 'scatter'
>>>>>>> cb53a816777b55c8dd84677bbfe781927361d55e
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
<<<<<<< HEAD

console.log(data.kobe.kb_pts_yr)

Plotly.newPlot('myDiv', data);
=======
Plotly.newPlot('interactive', data, layout);


// static charts

>>>>>>> 6137e27ce8cbb9b17aa64a851c4518f0570a150f
