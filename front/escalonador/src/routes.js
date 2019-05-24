import React from 'react'
import { 
    BrowserRouter, 
    Switch, 
    Route } from 'react-router-dom'
import Home from './pages/Home'
import Chart from './pages/Chart'

const Routes = () => (
    <BrowserRouter>
        <Switch>
            <Route exact path='/' component={Chart}/>
            <Route path='/Home' component={Home} />
        </Switch>
    </BrowserRouter>
)

export default Routes