var Action = require('argparse').Action;
var YmlReader = require('./ymlreader');
var util = require('util');

var ActionList = module.exports = function ActionList(options) {
	options = options || {};

	Action.call(this, options);
}
util.inherits(ActionList, Action);

ActionList.prototype.call = function() {
	var reader = new YmlReader();
	reader.getModPacks().forEach(function(p){console.log(p)});
}