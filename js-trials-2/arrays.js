"use strict";


// 1. printIndices
function printIndices(items) {
  // Replace this with your code
  for (const i in items) {
    console.log(`${(i)}. ${(items[i])}`);
    // console.log(message)
  }
  // console.log(`${i}. ${item}`);
}

// printIndices(['apple', 'berry', 'cherry']))

// 2. everyOtherItem
function everyOtherItem(items) {
  // Replace this with your code
  const everyOtherItem = [];

  for (let i in items) {
    if (i % 2 === 0) {
      everyOtherItem.push(items[i]);
    }
  
  }
  return everyOtherItem;  
  // No longer prints "undefined"
}


// 3. smallestNItems * BRING BACK THE N
function smallestNItems(items, n) {
  // Replace this with your code
  // const items = [2, 5, 4, 1, 3];
  
  items.sort(function (a, b) {
    return a - b;
  });
  // console.log(items);
  return items.slice(0, n);
}

