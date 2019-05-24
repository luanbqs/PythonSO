import React, { Component } from 'react'
import * as am4core from "@amcharts/amcharts4/core"
import * as am4charts from "@amcharts/amcharts4/charts"
import am4themes_animated from "@amcharts/amcharts4/themes/animated"

class Chart extends Component {
    constructor(props) {
        super(props)
    }

    componentDidMount() {
        this.buildChart()
    }    

    buildChart() {        
        am4core.useTheme(am4themes_animated)

        let chart = am4core.create("chartdiv", am4charts.XYChart)

        // Add percent sign to all numbers
        chart.numberFormatter.numberFormat = "#.3'%'"

        // Add data
        chart.data = [{
            "country": "USA",
            "year2004": 3.5,
            "year2005": 4.2
        }, {
            "country": "UK",
            "year2004": 1.7,
            "year2005": 3.1
        }, {
            "country": "Canada",
            "year2004": 2.8,
            "year2005": 2.9
        }, {
            "country": "Japan",
            "year2004": 2.6,
            "year2005": 2.3
        }, {
            "country": "France",
            "year2004": 1.4,
            "year2005": 2.1
        }, {
            "country": "Brazil",
            "year2004": 2.6,
            "year2005": 4.9
        }]

        // Create axes
        let categoryAxis = chart.xAxes.push(new am4charts.CategoryAxis())
        categoryAxis.dataFields.category = "country"
        categoryAxis.renderer.grid.template.location = 0
        categoryAxis.renderer.minGridDistance = 30

        let valueAxis = chart.yAxes.push(new am4charts.ValueAxis())
        valueAxis.title.text = "GDP growth rate"
        valueAxis.title.fontWeight = 800

        // Create series
        let series = chart.series.push(new am4charts.ColumnSeries())
        series.dataFields.valueY = "year2004"
        series.dataFields.categoryX = "country"
        series.clustered = false
        series.tooltipText = "GDP grow in {categoryX} (2004): [bold]{valueY}[/]"

        let series2 = chart.series.push(new am4charts.ColumnSeries())
        series2.dataFields.valueY = "year2005"
        series2.dataFields.categoryX = "country"
        series2.clustered = false
        series2.columns.template.width = am4core.percent(50)
        series2.tooltipText = "GDP grow in {categoryX} (2005): [bold]{valueY}[/]"

        chart.cursor = new am4charts.XYCursor()
        chart.cursor.lineX.disabled = true
        chart.cursor.lineY.disabled = true
    }

    render() {        
        return(
            <div>
                <div id="chartdiv" style={{width: "100%", height: "500px"}}></div>          
            </div>
        )
    }
}

export default Chart