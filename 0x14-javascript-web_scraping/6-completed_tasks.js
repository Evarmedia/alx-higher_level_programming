#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (err, response, body) => {
  err ?
    console.log(err) :
    response.statusCode === 200 ?
      (() => {
        const completed = {};
        const tasks = JSON.parse(body);
        for (const i in tasks) {
          const task = tasks[i];
          task.completed === true ?
            completed[task.userId] === undefined ?
              completed[task.userId] = 1 :
              completed[task.userId]++ :
            null;
        }
        console.log(completed);
      })() :
      console.log('An error occured. Status code: ' + response.statusCode);
});
