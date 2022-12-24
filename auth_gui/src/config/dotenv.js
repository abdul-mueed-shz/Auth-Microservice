const dotEnvConf = require("dotenv").config();

module.exports = function dotEnvParsed() {
  return dotEnvConf.parsed;
};
