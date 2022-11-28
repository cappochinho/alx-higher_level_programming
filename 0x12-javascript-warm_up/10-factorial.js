#!/usr/bin/env node

function factorial(a) {
    if (a === 0 || a === 1 || a === NaN) {
        return 1;
    }
    else {
        return a * factorial((a - 1));
    }
}

a = parseInt(process.argv[2]);
let answer;
if (a) {
    answer = factorial(a);
    console.log(answer);
}