import api from './api';

const functions = {
  getAll: async () => {
    try {
      const response = await api.get('/notas');
      return response.data;
    } catch (error) {
      return Promise.reject(
        error.response?.data?.detail || 
        error.response?.data || 
        error.message
      );
    }
  },

  create: async (data) => {
    try {
      const response = await api.post('/notas', data);
      return response.data;
    } catch (error) {
      return Promise.reject(
        error.response?.data?.detail || 
        error.response?.data || 
        error.message
      );
    }
  },

  update: async (id, data) => {
    try {
      const response = await api.put(`/notas/${id}`, data);
      return response.data;
    } catch (error) {
      return Promise.reject(
        error.response?.data?.detail || 
        error.response?.data || 
        error.message
      );
    }
  },

  delete: async (id) => {
    try {
      const response = await api.delete(`/notas/${id}`);
      return response.data;
    } catch (error) {
      return Promise.reject(
        error.response?.data?.detail || 
        error.response?.data || 
        error.message
      );
    }
  }
};

export default functions;
