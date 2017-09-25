var fs = require('fs');
var exec = require('child_process').execSync;
var Action = require('argparse').Action;
var YmlReader = require('./ymlreader');
var util = require('util');
var Handlebars = require('handlebars');

var ActionBuild = module.exports = function ActionBuild(options) {
	options = options || {};
	template = Handlebars.compile(fs.readFileSync('Dockerfile.template','utf8'));
	genpropfile = fs.readFileSync('gen_server_properties.sh', 'utf8');

	Action.call(this, options);
}
util.inherits(ActionBuild, Action);

function buildModPack(name, data) {
	console.log("## Building "+name);
	var baseDir = 'output/'+name;

	if (!fs.existsSync(baseDir)) fs.mkdirSync(baseDir);

	data.forEach(function(d) {
		var mcVerDir = baseDir+'/'+d.mc_version;
		var packVerDir = mcVerDir+'/'+d.pack_version;
		var dockerfile = packVerDir+'/Dockerfile';
		var genPropScript = packVerDir+'/gen_server_properties.sh';

		d.name = name;

		if (!fs.existsSync(mcVerDir)) fs.mkdirSync(mcVerDir);
		if (!fs.existsSync(packVerDir)) fs.mkdirSync(packVerDir);

		fs.writeFileSync(dockerfile, template(d));
		fs.writeFileSync(genPropScript, genpropfile);

		dockerTag = 'feedthebeast/'+name+':'+d.mc_version+'_'+d.pack_version

		console.log("## Run command:", 'docker build '+packVerDir);
		exec('docker build --rm --tag '+dockerTag+' '+packVerDir, {stdio:[0,1,2]});
		exec('docker push '+dockerTag);
	});
}

ActionBuild.prototype.call = function(p, ns, nargs) {
	var reader = new YmlReader();
	var modpacks = [];

	if(nargs != null && nargs.length > 0) {
		for (i = 0; i < nargs.length; ++i) {
			if(reader.getModPacks().indexOf(nargs[i]) == -1) {
				console.log("No such modpack: "+nargs[i]);
				return;
			}
		}
		modpacks = nargs;
	}

	if(modpacks.length == 0)
		modpacks = reader.getModPacks();

	modpackData = reader.get();

	if (!fs.existsSync('output')) fs.mkdirSync('output');
	
	modpacks.forEach(function(m) {
		buildModPack(m, modpackData[m]);
	});
}