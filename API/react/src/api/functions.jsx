import api from './api';

export const functions = {
  getAll: async () => {
    try {
      const response = await api.get('/notes/');
      return response.data;
    } catch (error) {
      throw error.response?.data || error.message;
    }
  },
  create: async (data) => {
    try {
      const response = await api.post('/notes/', data);
      return response.data;
    } catch (error) {
      throw error.response?.data || error.message;
    }
  },
  update: async (id, data) => {
    try {
      const response = await api.put(`/notes/${id}/`, data);
      return response.data;
    } catch (error) {
      throw error.response?.data || error.message;
    }
  },
  delete: async (id) => {
    try {
      const response = await api.delete(`/notes/${id}/`);
      return response.data;
    } catch (error) {
      throw error.response?.data || error.message;
    }
  }
};