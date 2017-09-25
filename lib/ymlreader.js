var yaml = require('js-yaml');
var fs   = require('fs');

var YmlReader = module.exports = function YmlReader() {

}

YmlReader.prototype.get = function() {
	return yaml.safeLoad(fs.readFileSync('./packs.yml', 'utf8'));
}

YmlReader.prototype.getModPacks = function() {
	return Object.keys(this.get());
}