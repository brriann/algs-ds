// CLI expected format "node myprog.js 1-2-3/4-5-6/7-8-9"
// to represent the file format:
// 1 2 3
// 4 5 6
// 7 8 9

const rowDelimiter = '/';
const cellDelimiter = '-';

methods = {
  readArgTo2DArray: function(cliInput, callBack) {
    var array2D = [];
    let lines = cliInput.split(rowDelimiter);
    lines.map(i => {
        array2D.push(
            i.split(cellDelimiter).map(i => {
                return parseInt(i, 10);
            }));
    });
    callBack(array2D);
  }
}

module.exports = methods;
