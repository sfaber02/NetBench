import express from 'express';
import { spawn } from 'child_process';
import bodyParser from 'body-parser';
import cors from 'cors';

const app = express();
const port = 8000;

app.use(bodyParser.json());
app.use(cors()); // Enable CORS for all routes

// Spawn the Netbench process once when the server starts
const pythonProcess = spawn('python3', ['../../../backend/src/netbench/init_netbench_backend.py']);
console.log("Python process spawned");

pythonProcess.stdout.on('data', (data) => {
    const rawData = data.toString();
    console.log(`Raw data received from Python: ${rawData}`);
});

pythonProcess.stderr.on('data', (data) => {
    console.error(`stderr: ${data}`);
});

pythonProcess.on('close', (code) => {
    console.log(`Express: Python process exited with code ${code}`);
});

app.post('/api/test', (req, res) => {
    const message = req.body.message;
    console.log(`Received message: ${message}`);

    // Send message to Python process
    pythonProcess.stdin.write(JSON.stringify({ action: 'communicate', message }) + '\n');

    // Listen for response from Python process
    pythonProcess.stdout.once('data', (data) => {
        const rawData = data.toString();
        console.log(`Express: Raw data received from Python: ${rawData}`);
        try {
            const jsonData = JSON.parse(rawData);
            res.json(jsonData);
        } catch (error) {
            console.error(`Error parsing JSON: ${error.message}`);
            res.status(500).send('Invalid JSON received from Python process');
        }
    });

    pythonProcess.stderr.once('data', (data) => {
        console.error(`stderr: ${data}`);
        res.status(500).send(data.toString());
    });

    pythonProcess.once('close', (code) => {
        if (code !== 0) {
            res.status(500).send(`Python process exited with code ${code}`);
        }
    });
});

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});

export {};
