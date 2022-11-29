#!/usr/bin/node

num = parseInt(process.argv[2]);
if (!num) {
    console.log("Missing number of occurrences");
    return;
}
else {
    for (let i= 0; i < num; i++) {
        console.log("C is fun");
    }
}
