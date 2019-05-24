import React, { Component } from 'react'
import api from '../../utils/api'

class Home extends Component {
    constructor(props) {
        super(props)        
        this.state = {
            dataList: []
        }
    }

    componentDidMount() {
        // this.loadDataList()
        this.setState({ dataList: [1,2,3,4,5,6,7]})

    }

    loadDataList = async () => {
        const response = api.getData()
        this.setState({ dataList: response.data })
    }

    render() {
        const { dataList } = this.state
        return(
            <div>
                {dataList.map((item) => (
                    <p>{item}</p>
                ))}
            </div>
        )
    }
}

export default Home