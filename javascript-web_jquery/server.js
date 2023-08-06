const express = require('express');
const https = require('https');

const app = express();
const port = 3000;

app.use((req, res, next) => {
    res.setHeader('Access-Control-Allow-Origin', '*');
    next();
});

app.get('/hello', (req, res) => {
    const options = {
        hostname: 'stefanbohacek.com',
        path: '/hellosalut/?lang=fr',
        method: 'GET'
    };

    const request = https.request(options, (response) => {
        let data = '';
        response.on('data', (chunk) => {
            data += chunk;
        });

        response.on('end', () => {
            const hello = JSON.parse(data).hello;
            res.json({ hello });
        });
    });

    request.on('error', (error) => {
        console.error(error.message);
        res.status(500).json({ error: 'Error fetching data' });
    });

    request.end();
});

app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
