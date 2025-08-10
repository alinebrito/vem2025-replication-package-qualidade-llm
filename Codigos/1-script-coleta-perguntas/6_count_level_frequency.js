const fs = require('fs');

function countLevelFrequency(jsonFile, outputFile) {
    fs.readFile(jsonFile, 'utf8', (err, data) => {
        if (err) {
            console.error('Error reading the file:', err);
            return;
        }

        const items = JSON.parse(data);
        const frequency = {};

        items.forEach(item => {
            const level = item.difficulty.level;
            if (frequency[level]) {
                frequency[level]++;
            } else {
                frequency[level] = 1;
            }
        });

        fs.writeFile(outputFile, JSON.stringify(frequency, null, 2), 'utf8', (err) => {
            if (err) {
                console.error('Error writing the file:', err);
                return;
            }
            console.log(`Frequency data saved to ${outputFile}`);
        });
    });
}

// Example usage
countLevelFrequency('./data/dataUpdatedWithSolutions.json', './data/frequencyOutput.json');