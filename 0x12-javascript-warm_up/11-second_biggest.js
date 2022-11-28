#!/usr/bin/env node

list = process.argv.sort();
count = 0;
for (element of list) {
    count++;
}
console.log(list[count - 2]);