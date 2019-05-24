import axios from 'axios'

const server = axios.create({
    baseURL: 'http://localhost:5000/',
})

const getData = () => server.get('')

const api = {
    getData,
}

export default api

