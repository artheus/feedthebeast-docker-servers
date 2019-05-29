import argparse
import os
import bs4
import requests
import subprocess


DYNMAP_URLS = {
    "1.4.7": "https://minecraft.curseforge.com/projects/dynmapforge/files/2216525/download",
    "1.5.2": "https://minecraft.curseforge.com/projects/dynmapforge/files/2216526/download",
    "1.6.4": "https://minecraft.curseforge.com/projects/dynmapforge/files/2307077/download",
    "1.7.10": "https://minecraft.curseforge.com/projects/dynmapforge/files/2380586/download",
    "1.8.0": "https://minecraft.curseforge.com/projects/dynmapforge/files/2380592/download",
    "1.8.9": "https://minecraft.curseforge.com/projects/dynmapforge/files/2380593/download",
    "1.9": "https://minecraft.curseforge.com/projects/dynmapforge/files/2380594/download",
    "1.9.4": "https://minecraft.curseforge.com/projects/dynmapforge/files/2380600/download",
    "1.10.2": "https://minecraft.curseforge.com/projects/dynmapforge/files/2380601/download",
    "1.11": "https://minecraft.curseforge.com/projects/dynmapforge/files/2380602/download",
    "1.11.2": "https://minecraft.curseforge.com/projects/dynmapforge/files/2380603/download",
    "1.12": "https://minecraft.curseforge.com/projects/dynmapforge/files/2436596/download",
    "1.12.2": "https://minecraft.curseforge.com/projects/dynmapforge/files/2645936/download"
}


class Modpack:
    def __init__(self, name, description, dir, version, old_versions,
                 mc_version, min_jre, image, logo, server_pack, repo_version):
        self.name = name
        self.description = description
        self.dir = dir
        self.version = version
        self.old_versions = old_versions
        self.mc_version = mc_version
        self.min_jre = min_jre
        self.image = image
        self.logo = logo
        self.server_pack = server_pack
        self.repo_version = repo_version

    def __repr__(self):
        from pprint import pformat
        return "<" + type(self).__name__ + "> " + pformat(vars(self), indent=4, width=1)


def do_build(docker_tag, download_url, dynmap_url):
    command = 'docker build ./modserver -t "%s" --build-arg DOWNLOAD_URL=%s --build-arg DYNMAP_URL=%s' % (
        docker_tag, download_url, dynmap_url
    )

    if not args.silent:
        print(command)

    if not args.dryrun:
        buildProcess = subprocess.Popen(command, shell=True)
        os.waitpid(buildProcess.pid, 0)

    if not args.dryrun:
        pushProcess = subprocess.Popen('docker push ' + docker_tag, shell=True)
        os.waitpid(pushProcess.pid, 0)


def docker_tag(name, pack_version="", mc_version="", latest=False):
    tag = "feedthebeast/" + name
    if latest:
        return (tag, "latest")
    return (tag, pack_version + "_" + mc_version)


def build_modpack(modpack):
    if modpack.server_pack == "":
        return False

    versions = []
    if modpack.old_versions != "":
        versions = modpack.old_versions.split(';')

    versions.append(modpack.version)

    builds = {}

    for v in versions:
        download_url = "http://ftb.cursecdn.com/FTB2/modpacks/"+modpack.dir+"/"+v.replace('.','_')+"/"+modpack.server_pack
        dynmap_url = DYNMAP_URLS[modpack.mc_version]

        if v == modpack.version:
            builds['latest'] = (docker_tag(modpack.dir.lower(), latest=True), download_url, dynmap_url)

        if not args.latest:
            builds[v] = (docker_tag(modpack.dir.lower(), v, modpack.mc_version), download_url, dynmap_url)

    for key, bt in builds.items():
        tag = args.prefix + bt[0][0] + ":" + bt[0][1]
        if not args.prefix:
            r = requests.get("https://index.docker.io/v1/repositories/"+bt[0][0]+"/tags/"+bt[0][1])
            if r.status_code != 404:
                continue
        if not args.silent:
            print("Building " + tag)
        do_build(tag, bt[1], bt[2])


def main():
    global args

    parser = argparse.ArgumentParser(allow_abbrev=True)
    parser.add_argument('-m', '--modpack', dest='modpack', action='store', help='Limit to single modpack')
    parser.add_argument('-l', '--latest', dest='latest', action='store_true', help='Limit to the latest tag for a modpack')
    parser.add_argument('-s', '--silent', dest='silent', action='store_true', help='Silent the output')
    parser.add_argument('-d', '--dryrun', dest='dryrun', action='store_true', help='Dont actually build or push, useful for testing')
    parser.add_argument('-p', '--prefix', dest='prefix', action='store', default='', help='Override docker prefix from empty (docker hub)')
    args = parser.parse_args()

    r = requests.get("https://ftb.cursecdn.com/FTB2/static/modpacks.xml")
    tree = bs4.BeautifulSoup(r.text, "html.parser")

    modpacks = {}
    for packelm in tree.find_all('modpack'):
        modpack = Modpack(
            name=packelm.get('name'),
            description=packelm.get('description'),
            dir=packelm.get('dir'),
            version=packelm.get('version'),
            old_versions=packelm.get('oldversions'),
            mc_version=packelm.get('mcversion'),
            min_jre=packelm.get('minjre'),
            image=packelm.get('image'),
            logo=packelm.get('logo'),
            server_pack=packelm.get('serverpack'),
            repo_version=packelm.get('repoversion')
        )
        if args.modpack and modpack.dir.lower() != args.modpack.lower():
            continue
        modpacks[modpack.dir] = modpack

    for key, modpack in modpacks.items():
        build_modpack(modpack)


if __name__ == '__main__':
    main()
