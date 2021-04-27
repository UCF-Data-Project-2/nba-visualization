// Function to format metadata for panel
function init() {
    d3.json("http://localhost:5000/api/all").then(data => {
        console.log(data);

    // Getting id from dropdown
    let input = d3.select("#input");
    data.name.forEach(element => {
        input.append("option").attr("value", element).text(element)
    });

    // Call updatePlots function to build plots
    updatePlots(data, "Danny Green");
    });
};

// Code to build plots
updatePlots = (data, name) => {
    console.log(data)
    console.log(name)

//     let sample = data.samples.filter(sample => sample.id === id);
//     let metadata = data.metadata.filter(metadatum => metadatum.id === +id);

//     console.log(sample);

//     //Populate demographic info
//     d3.select("#sample-metadata").html("");
//     d3.select("#sample-metadata").html(make_meta(metadata));

//     // X & Y variables for charts
//     let otuID = sample[0].otu_ids;
//     let sampleVal = sample[0].sample_values;
//     let otuLabel = sample[0].otu_labels;

//     console.log(otuID);
//     console.log(sampleVal);

//     xy = otuID.map((val, i) => ({
//         otuID: val,
//         sampleVal: sampleVal[i],
//         otuLabel: otuLabel[i],
//         }));

//     xy.sort((a, b) => b - a);
//     xy = (xy.slice(0, 10));
    
//     console.log(xy);

//     x = [];
//     y = [];
//     labels = [];
    
//     for (let i = 0; i < xy.length; i ++) {
//         x.push(xy[i].sampleVal);
//         y.push(xy[i].otuID);
//         labels.push(xy[i].otuLabel);
//       };

//     console.log(x);
//     console.log(y);
//     console.log(labels);

//     // Build bar chart:
//     let barData = [{
//         x: x,
//         y: y,
//         type: 'bar',
//         orientation: 'h',
//         hovertext: labels,
//         marker: {color: 'rgb(52, 192, 235)'},
//         width: .8
//     }];

//     let barLayout = {
//         title: `Top 10 OTUs for Test Subject ${id}`,
//         yaxis: {
//             autorange: "reversed",
//             type: 'category',
//             // ticktext: 'OTU ' + y,
//             showticklabels: true,
//         },
//     };

//     var barConfig = {responsive: true}

//     // Plot bar chart
//     Plotly.newPlot("bar", barData, barLayout, barConfig);

//     // Build bubble chart:
//     let bubbleData = [{
//         x: y,
//         y: x,
//         mode: 'markers',
//         marker: {
//             color: y,
//             size: x,
//         }
//     }];

//     let bubbleLayout = {
//         title: 'Bio Bubbles',
//         xaxis: {
//             title: {
//                 text: "OTU IDs"
//             }
//         }
//     };

//     var bubbleConfig = {responsive: true}

//     // Plot bubble chart
//     Plotly.newPlot("bubble", bubbleData, bubbleLayout, bubbleConfig);
// };

// // Function for handling new ID input from dropdown
// optionChanged = (id) => {
//     d3.json("samples.json").then (data => {
//         console.log(data);
//         updatePlots(data, id);
//     });
};

init();