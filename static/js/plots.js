<<<<<<< HEAD
// // function init() {
//   // d3.json("../../data/kobe_data.json").then(data => {
//   //     console.log(data);
//   // Getting id from dropdown
//   // let input = d3.select("#selDataset");
//   // data.names.forEach(element => {
//       // input.append("option").attr("value", element).text(element)
//   // });    
//   // Call updatePlots function to build plots
//   // updatePlots(data, "940");
//   // });
// // };

// // d3.json("../../data/kobe_data.json").then(data => {
// //   console.log(data);
// // var trace1 = {
// //     x: [Kobe_stats["Year"]],
// //     y: [Kobe_stats["pts"]],
// //     mode: 'markers',
// //     type: 'scatter'
// //   };
// //   var trace2 = {
// //     x: [2, 3, 4, 5],
// //     y: [16, 5, 11, 9],
// //     mode: 'lines',
// //     type: 'scatter'
// //   };
// //   var trace3 = {
// //     x: [1, 2, 3, 4],
// //     y: [12, 9, 15, 12],
// //     mode: 'lines+markers',
// //     type: 'scatter'
// //   };
// //   var data = [trace1];
// //   Plotly.newPlot('plot', data);

// df = pd.read_csv('')
// df_external_source = FF.create_table(df.head())
// py.iplot(df_external_source, filename='df-external-source-table')
// trace = go.Scatter(x = df[''], y = df[''],
//                   name='Stats')
// layout = go.Layout(title='Kobe',
//                    plot_bgcolor='rgb(230, 230,230)',
//                    showlegend=True)
// fig = go.Figure(data=[trace], layout=layout)
// py.iplot(fig, filename='kobe_data')

=======
var trace1 = {
    x: kb_year_index,
    y: data.kobe.kb_pts_yr,
    name: "Kobe",
    mode: 'lines+markers',
    type: 'scatter'
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
  
var data = [trace1, trace2;
console.log(data.kobe.kb_pts_yr)
Plotly.newPlot('myDiv', data);
>>>>>>> d9769a4faffec7b94882ee5ca1333e7508d5ddde
