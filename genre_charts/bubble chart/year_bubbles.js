(function() {
  var width = 1000,
    height = 1000;
  
  var svg = d3.select("#chart")
    .append("svg")
    .attr("height", height)
    .attr("width", width)
    .append("g")
    .attr("transform", "translate(0,0)")

  var simulation = d3.forceSimulation()
    .force("x", d3.forceX(width / 2).strength(0.005))

  d3.queue()
    .defer(d3.csv, "genres_2010.csv")
    .await(ready)

  function ready (error, datapoints) {

    var circles = svg.selectAll(".artist")
      .data(datapoints)
      .enter().append("circle")
      .attr("class", "artist")
      .attr("r", 10)
      .attr("fill", "lightblue")
      .attr("cx, "cy")

    simulation.nodes(datapoints)
      .on('tick', ticked)

    function ticked() {
      circles
      .attr("cx", function(d) {
        return d.x
      .attr("cy", function(d) {
        return d.y
      })
    }


  }
})();


 
 
