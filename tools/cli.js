// CLI expected format "node myprog.js 1-2-3/4-5-6/7-8-9"
// to represent the file format:
// 1 2 3
// 4 5 6
// 7 8 9

const rowDelimiter = '/';
const cellDelimiter = '-';

methods = {
  readArgTo2DArray: function(cliInput, callBack) {
    var pivotedInputs = [];
    let lines = cliInput.split(rowDelimiter);
    lines.map( i => {
        pivotedInputs.push(i.split(cellDelimiter));
    });
    callBack(pivotedInputs);
  }
}

module.exports = methods;
