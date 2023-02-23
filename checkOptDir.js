import fs from 'fs';

export const handler = async(event) => {
    fs.readdir('/opt/nodejs/node_modules', (err, files) => {
        files.forEach(file => {
            console.log("this is: ", file);
        });
    });

    // TODO implement
    const response = {
        statusCode: 200,
        body: JSON.stringify('Hello from Lambda!'),
    };
    return response;
};
