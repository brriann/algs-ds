// invoke this script with an int array from CLI as "node 0Intro.js 0,1,2,3,4"

if (process.argv.length < 3) {
    console.log('usage: node 0Intro.js x,y,z,a,b,c');
} else {
    let arrayArgument = process.argv[2].split(',');
    let arraySum = arrayArgument.reduce((a,b) => parseInt(a, 10) + parseInt(b, 10), 0);
    console.log(arrayArgument);
    console.log('your array sum is:');
    console.log(arraySum);

}