init();

function init(){
  data = ajax.post('/get_most_populated', '', function(raw_data) {
    //data_json = JSON.parse(raw_data);
    data_json = [];
    data_json.push(JSON.parse(raw_data));
    console.log(data_json);
    var chart;
    nv.addGraph(function() {
        chart = nv.models.multiBarHorizontalChart()
            .x(function(d) { return d.label })
            .y(function(d) { return d.value })
            .barColor(d3.scale.category20().range())
            .duration(250)
            .margin({top: 30,right: 50, left: 175, bottom: 50})
            .stacked(true)
            .showValues(true)           //Show bar value next to each bar.
            .tooltips(true)             //Show tooltips on hover.
            //.transitionDuration(350)
            .showControls(true);

        chart.yAxis.tickFormat(d3.format(',.2f'));

        chart.yAxis.axisLabel('City');

        chart.xAxis.axisLabel('Population').axisLabelDistance(90);
        d3.select('#chart1 svg')
            .datum(data_json)
            .call(chart);
        nv.utils.windowResize(chart.update);
        chart.dispatch.on('stateChange', function(e) { nv.log('New State:', JSON.stringify(e)); });
        chart.state.dispatch.on('change', function(state){
            nv.log('state', JSON.stringify(state));
        });
        return chart;
    });
  });
}
