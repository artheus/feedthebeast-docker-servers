import os
import bs4
import requests
import subprocess


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


def do_build(docker_tag, download_url):
    command = 'docker build ./modserver -t "'+docker_tag+'" --build-arg DOWNLOAD_URL='+download_url
    with open('/dev/stdout', 'w') as stdout:
        p = subprocess.Popen(command, shell=True, stdout=stdout)
        os.waitpid(p.pid, 0)

        p = subprocess.Popen('docker push '+docker_tag, shell=True, stdout=stdout)
        os.waitpid(p.pid, 0)


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

    builds = []

    for v in versions:
        download_url = "http://ftb.cursecdn.com/FTB2/modpacks/"+modpack.dir+"/"+v.replace('.','_')+"/"+modpack.server_pack

        builds.append((docker_tag(modpack.dir.lower(), v, modpack.mc_version), download_url))
        if v == modpack.version:
            builds.append((docker_tag(modpack.dir.lower(), latest=True), download_url))

    for bt in builds:
        r = requests.get("https://index.docker.io/v1/repositories/"+bt[0][0]+"/tags/"+bt[0][1])
        if r.status_code == 404:
            do_build(':'.join(bt[0]), bt[1])


def main():
    r = requests.get("https://ftb.cursecdn.com/FTB2/static/modpacks.xml")
    tree = bs4.BeautifulSoup(r.text, "html.parser")

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
        build_modpack(modpack)


if __name__ == '__main__':
    main()
