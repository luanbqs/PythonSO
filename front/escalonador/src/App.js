
import './App.css';
import service from '../src/services/service'
import React, { Component } from 'react';

// import { Container } from './styles';

export default class App extends Component {
  constructor(props) {
    super(props)
      this.state = {
        mensagem: 'oi'
      }    
  }
  async testerota(){

      const {data} = await service.post("/create-process",{nome:'oi'});
      this.setState({
        teste:data.mensagem
      })
      
  }

  teste = async () => {
    const {data} = await service.post("/teste");
    console.log('data',data)
  }

  componentDidMount(){
    this.teste()
  }

  render() {
    return (
      <div >
        {this.state.mensagem}
      </div>
    );
  }
}
