// Function to format metadata for panel
dropdown = ["Points", "Assists", "Rebounds", "Blocks", "Defensive Rebounds", "Steals"]

function init() {

    d3.json("api/all").then(data => {
        console.log(data);

    // Getting input from dropdown
    let input = d3.select("#input");
    dropdown.forEach(element => {
        input.append("option").attr("value", element).text(element)
    });    

    console.log(d3.sum(data.kobe.pts_year));
    

    // Build static-chart1
    var trace1 = {
        x: 'Kobe Bryant',
        y: [d3.sum(data.kobe.pts_year.slice(0, 18))],
        name: "Kobe Bryant",
        marker: {color: 'rgb(85, 37, 130)'},
        type: 'bar'
    };

    var trace2 = {
        x: 'LeBron James',
        y: [d3.sum(data.lebron.pts_year)],
        name: "LeBron James",
        marker: {color: 'rgb(253 185 39)'},
        type: 'bar'
    };

    var staticChart1 = [trace1, trace2];

    var layout = {
        barmode: 'group',
        showlegend: true,
        legend: {
            x: 0,
            y: -.2,
            "orientation": "h"
        }
    };

    Plotly.newPlot('static-chart1', staticChart1, layout);

    // Build static-chart2
    var trace1 = {
        x: 'Kobe Bryant',
        y: [d3.sum(data.kobe.ast_year.slice(0, 18))],
        name: "Kobe Bryant",
        marker: {color: 'rgb(85, 37, 130)'},
        type: 'bar'
    };

    var trace2 = {
        x: 'LeBron James',
        y: [d3.sum(data.lebron.ast_year)],
        name: "LeBron James",
        marker: {color: 'rgb(253 185 39)'},
        type: 'bar'
    };

    var staticChart2 = [trace1, trace2];

    var layout = {
        barmode: 'group',
        showlegend: true,
        legend: {
            x: 0,
            y: -.2,
            "orientation": "h"
        }
    };

    Plotly.newPlot('static-chart2', staticChart2, layout);

    // Build static-chart3
    var trace1 = {
        x: 'Kobe Bryant',
        y: [d3.sum(data.kobe.reb_year.slice(0, 18))],
        name: "Kobe Bryant",
        marker: {color: 'rgb(85, 37, 130)'},
        type: 'bar'
    };

    var trace2 = {
        x: 'LeBron James',
        y: [d3.sum(data.lebron.reb_year)],
        name: "LeBron James",
        marker: {color: 'rgb(253 185 39)'},
        type: 'bar'
    };

    var staticChart3 = [trace1, trace2];

    var layout = {
        barmode: 'group',
        showlegend: true,
        legend: {
            x: 0,
            y: -.2,
            "orientation": "h"
        }
    };

    Plotly.newPlot('static-chart3', staticChart3, layout);
    
    // Build static-chart4
    var trace1 = {
        x: 'Kobe Bryant',
        y: [d3.sum(data.kobe.blk_year.slice(0, 18))],
        name: "Kobe Bryant",
        marker: {color: 'rgb(85, 37, 130)'},
        type: 'bar'
    };

    var trace2 = {
        x: 'LeBron James',
        y: [d3.sum(data.lebron.blk_year)],
        name: "LeBron James",
        marker: {color: 'rgb(253 185 39)'},
        type: 'bar'
    };

    var staticChart4 = [trace1, trace2];

    var layout = {
        barmode: 'group',
        showlegend: true,
        legend: {
            x: 0,
            y: -.2,
            "orientation": "h"
        }
    };

    Plotly.newPlot('static-chart4', staticChart4, layout);

    // Build static-chart5
    var trace1 = {
        x: 'Kobe Bryant',
        y: [d3.sum(data.kobe.dreb_year.slice(0, 18))],
        name: "Kobe Bryant",
        marker: {color: 'rgb(85, 37, 130)'},
        type: 'bar'
    };

    var trace2 = {
        x: 'LeBron James',
        y: [d3.sum(data.lebron.dreb_year)],
        name: "LeBron James",
        marker: {color: 'rgb(253 185 39)'},
        type: 'bar'
    };

    var staticChart5 = [trace1, trace2];

    var layout = {
        barmode: 'group',
        showlegend: true,
        legend: {
            x: 0,
            y: -.2,
            "orientation": "h"
        }
    };

    Plotly.newPlot('static-chart5', staticChart5, layout);

    // Build static-chart6
    var trace1 = {
        x: 'Kobe Bryant',
        y: [d3.sum(data.kobe.stl_year.slice(0, 18))],
        name: "Kobe Bryant",
        marker: {color: 'rgb(85, 37, 130)'},
        type: 'bar'
    };

    var trace2 = {
        x: 'LeBron James',
        y: [d3.sum(data.lebron.stl_year)],
        name: "LeBron James",
        marker: {color: 'rgb(253 185 39)'},
        type: 'bar'
    };

    var staticChart6 = [trace1, trace2];

    var layout = {
        barmode: 'group',
        showlegend: true,
        legend: {
            x: 0,
            y: -.2,
            "orientation": "h"
        }
    };

    Plotly.newPlot('static-chart6', staticChart6, layout);
  
    // Call updatePlots function to build plots
    updatePlots(data, "Points");
    });
};

// Code to build plot chosen in dropdown menu
updatePlots = (data, input) => {
    console.log(data)
    console.log(input)

    // Determine y axis values
    if (input == "Points") {
        yKobe = data.kobe.pts_year
        yLeBron = data.lebron.pts_year
    }
    else if (input == "Assists") {
        yKobe = data.kobe.ast_year
        yLeBron = data.lebron.ast_year
    }
    else if (input == "Rebounds") {
        yKobe = data.kobe.reb_year
        yLeBron = data.lebron.reb_year
    }
    else if (input == "Blocks") {
        yKobe = data.kobe.blk_year
        yLeBron = data.lebron.blk_year
    }
    else if (input == "Defensive Rebounds") {
        yKobe = data.kobe.dreb_year
        yLeBron = data.lebron.dreb_year
    }
    else {
        yKobe = data.kobe.stl_year
        yLeBron = data.lebron.stl_year
    }

    console.log(yKobe);
    console.log(yLeBron);
 
    // Build responsive chart
    var trace1 = {
        x: data.kobe.index_year,
        y: yKobe,
        name: "Kobe",
        marker: {color: 'rgb(85, 37, 130)'},
        mode: 'lines+markers',
        type: 'scatter'
        };
    var trace2 = {
        x: data.kobe.index_year,
        y: yLeBron,
        name: 'Lebron',
        marker: {color: 'rgb(253 185 39)'},
        mode: 'lines+markers',
        type: 'scatter'
        };

    var layout = {
        title: `Kobe vs Lebron - ${input}`,
        yaxis: { title: input},
        xaxis: { title: "Year Index"}
        };

    var config = {responsive: true}
        
    var chart1 = [trace1, trace2];
      
    console.log(data)
      
    Plotly.newPlot('responsive-chart', chart1, layout, config);

    // Function for handling new input from dropdown
    optionChanged = (input) => {
        topbar.show()
        topbar.hide()
        d3.json("api/all").then (data => {
            console.log(data);
            updatePlots(data, input);
        })
    };
};

init();