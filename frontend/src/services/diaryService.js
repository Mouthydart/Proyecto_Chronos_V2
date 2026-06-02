import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000/api';

export const diaryService = {
    async saveEntry(content) {
        const response = await axios.post(`${API_URL}/save-entry`, { content });
        return response.data;
    },

    async getEntryByDate(date) {
        const response = await axios.get(`${API_URL}/get-entry/${date}`);
        return response.data;
    }
};