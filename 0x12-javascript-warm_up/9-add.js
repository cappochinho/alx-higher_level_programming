#!/usr/bin/env node

function add(a, b) {
    let result = a + b;
    return result;
}

a = parseInt(process.argv[2]);
b = parseInt(process.argv[3]);
let answer;
if (a && b) {
    answer = add(a, b);
    console.log(answer);
}