#!/usr/bin/node
const express = require('express');
const axios = require('axios');

const app = express();
const port = 3000;

// Add the necessary CORS header to allow all origins (for testing purposes)
app.use((req, res, next) => {
    res.setHeader('Access-Control-Allow-Origin', '*');
    next();
});

app.get('/hello', async (req, res) => {
    try {
        const response = await axios.get('https://stefanbohacek.com/hellosalut/?lang=fr');
        res.json({ hello: response.data.hello });
    } catch (error) {
        console.error(error.message);
        res.status(500).json({ error: 'Error fetching data' });
    }
});

app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});

