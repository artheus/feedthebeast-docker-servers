# Dockerized FTB Minecraft servers [![Build Status](https://travis-ci.org/artheus/feedthebeast-docker-servers.svg?branch=master)](https://travis-ci.org/artheus/feedthebeast-docker-servers)

So, you want to run your own FTB Minecraft Server? Use these Docker images to do so!

To use this, you will need some knowledge on how to use Docker.
Please read about docker here: https://docs.docker.com/learn/

Pull the docker images from
https://hub.docker.com/u/feedthebeast/

# Milestones
- Add McMyAdmin to increase control over the server
- Add an app for rendering world maps
- Include all servers from the FTB ModPack list
- Automatic builds of the docker images, pushing directly to Docker hub

# Usage

TL;DR; `docker run -it feedthebeast/direwolf20`

The images are all hosted on Docker hub under the organization feedthebeast and the repositories
all have names naturally mapping to their real mod pack name.

## Versioning
The `latest` tag might not always be correct, just so that is said.

Version tags in the docker repo should always be MCV-MPV where MCV is the Minecraft version, and MPV is
the mod pack version. So say you want direwolf20's pack version 1.5.1 for minecraft 1.10 you should then
run the command `docker run -it feedthebeast/direwolf20:1.10-1.5.1`

## Configuration

You can config the server.properties file using these environment variables:

| Variable | default value |
| --- | --- |
| MAX_TICK_TIME | 60000 |
| GENERATOR_SETTINGS |  |
| FORCE_GAMEMODE | false |
| ALLOW_NETHER | true |
| GAMEMODE | 0 |
| ENABLE_QUERY | false |
| PLAYER_IDLE_TIMEOUT | 0 |
| DIFFICULTY | 1 |
| SPAWN_MONSTERS | true |
| OP_PERMISSION_LEVEL | 4 |
| ANNOUNCE_PLAYER_ACHIEVEMENT | true |
| PVP | true |
| SNOOPER_ENABLED | true |
| LEVEL_TYPE | DEFAULT |
| HARDCORE | false |
| ENABLE_COMMAND_BLOCK | false |
| MAX_PLAYERS | 20 |
| NETWORK_COMPRESSION_THRESHOLD | 256 |
| RESOURCE_PACK_SHA1 |  |
| MAX_WORLD_SIZE | 29999984 |
| SERVER_PORT | 25565 |
| SERVER_IP |  |
| SPAWN_NPCS | true |
| ALLOW_FLIGHT | false |
| LEVEL_NAME | world |
| VIEW_DISTANCE | 10 |
| RESOURCE_PACK |  |
| SPAWN_ANIMALS | true |
| WHITE_LIST_ENABLED | false |
| GENERATE_STRUCTURES | true |
| ONLINE_MODE | true |
| MAX_BUILD_HEIGHT | 256 |
| LEVEL_SEED |  |
| USE_NATIVE_TRANSPORT | true |
| ENABLE_RCON | false |

Say you want to create a server with the level seed "mylevelseed", then you use this command:
`docker run -it -e LEVEL_SEED="mylevelseed" feedthebeast/direwolf20`

Read more about environment variables in docker here:
https://docs.docker.com/engine/reference/commandline/run/#/set-environment-variables--e---env---env-file

# Pull requests and Issues are welcome!

Please feel free to create pull requests and write about your issues here on GitHub.
Though, if you are having trouble using docker or something is wrong with the modpack,
please either read the docker documentation or refer to the mod pack author(s).

# The credit goes to!

Whoever works on building the mod packs!

I, artheus, only make them more available for the users who wants to host their own servers.
