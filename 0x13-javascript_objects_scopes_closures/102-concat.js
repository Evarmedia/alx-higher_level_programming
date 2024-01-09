#!/usr/bin/node

// a script that concats two files
const fs = require('fs');

const sourceFilePath1 = process.argv[2];
const sourceFilePath2 = process.argv[3];
const destinationFilePath = process.argv[4];

const readStream1 = fs.createReadStream(sourceFilePath1);
const readStream2 = fs.createReadStream(sourceFilePath2);
const writeStream = fs.createWriteStream(destinationFilePath, { flags: 'a' });

readStream1.pipe(writeStream, { end: false });

readStream1.on('end', () => {
  readStream2.pipe(writeStream);
});
