#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request(url, (error, response) => {
    console.log('code:' response.statusCode);
});
