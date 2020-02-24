const fs = require('fs');
const readline = require('readline');

methods = {
  readLinesTo2DArray: function(filePath, callBack) {
    var inputs = [];
    const rl = readline.createInterface({
      input: fs.createReadStream(filePath),
      crlfDelay: Infinity
    });
    rl.on('line', (line) => {
        var lineArray = [];
        var strings = line.split(' ');
        for (var i = 0; i < strings.length; i++) {
            lineArray.push(Number(strings[i]));
        }
      inputs.push(lineArray);
    }).on('close', () => {
        callBack(inputs);
    });
  }
}

module.exports = methods;

