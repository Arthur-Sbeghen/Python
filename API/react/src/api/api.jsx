import axios from 'axios';

const api = axios.create({
    baseURL: 'localhost:3000',
    timeout: 1000,
    headers: {'Content-Type': 'application/json'}
})

export default api;