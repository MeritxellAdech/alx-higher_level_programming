#!/usr/bin/node

// Add the incr() function to increments the integer value of the given object
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);

myObject.incr = function () {
  myObject.value++;
};

myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
