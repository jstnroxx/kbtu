const fs = require('fs');

fs.readFile('*INSERT INPUT FILENAME HERE*.json', 'utf-8', (err, dataReceived) => {
    if (err) {
        console.error('There was an error while reading file:', err);
        return;
    } else {
        console.log('File read successfully.');

        const jsonDataFormatted = JSON.stringify(JSON.parse(dataReceived), null, 4);

        fs.writeFile('*INSERT INPUT FILENAME HERE*.json', jsonDataFormatted, err => {
        if (err) {
            console.error('There was an error while writing file:', err);
            return;
        } else {
            console.log('File written successfully.');
        };
    });
    }; 
});