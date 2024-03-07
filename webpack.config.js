const path = require('path');

module.exports = {
  // The entry point file described above
  entry: './middleware/static/js/index.js',
  // The location of the build folder described above
  output: {
    path: path.resolve(__dirname, 'middleware/static/dist'),
    filename: 'bundle.js'
  },
};

