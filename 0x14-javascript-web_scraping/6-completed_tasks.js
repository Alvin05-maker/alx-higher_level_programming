#!/usr/bin/node
// computes the number of tasks completed by user id.

const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
    return;
  }

  const allTodos = JSON.parse(body);
  const allUsers = {};

  allTodos.forEach(task => {
    if (!Object.prototype.hasOwnProperty.call(allUsers, task.userId)) {
      allUsers[task.userId] = 0;
    }

    if (task.completed) {
      allUsers[task.userId]++;
    }
  });

  Object.keys(allUsers).forEach(key => {
    if (!allUsers[key]) { // users with no completed tasks
      delete allUsers[key];
    }
  });
  console.log(allUsers);
});
