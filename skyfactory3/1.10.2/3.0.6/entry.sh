#!/bin/bash


if [ ! -f server.properties ] ; then
	cat <<- EOF > server.properties
	# Minecraft server properties
	# ---
	max-tick-time=${MAX_TICK_TIME:-60000}
	generator-settings=${GENERATOR_SETTINGS}
	force-gamemode=${FORCE_GAMEMODE:-false}
	allow-nether=${ALLOW_NETHER:-true}
	gamemode=${GAMEMODE:-0}
	enable-query=${ENABLE_QUERY:-false}
	player-idle-timeout=${PLAYER_IDLE_TIMEOUT:-0}
	difficulty=${DIFFICULTY:-1}
	spawn-monsters=${SPAWN_MONSTERS:-true}
	op-permission-level=${OP_PERMISSION_LEVEL:-4}
	announce-player-achievements=${ANNOUNCE_PLAYER_ACHIEVEMENT:-true}
	pvp=${PVP:-true}
	snooper-enabled=${SNOOPER_ENABLED:-true}
	level-type=${LEVEL_TYPE:-DEFAULT}
	hardcore=${HARDCORE:-false}
	enable-command-block=${ENABLE_COMMAND_BLOCK:-false}
	max-players=${MAX_PLAYERS:-20}
	network-compression-threshold=${NETWORK_CONPRESSION_THRESHOLD:-256}
	resource-pack-sha1=${RESOURCE_PACK_SHA1}
	max-world-size=${MAX_WORLD_SIZE:-29999984}
	server-port=${SERVER_PORT:-25565}
	server-ip=${SERVER_IP}
	spawn-npcs=${SPAWN_NPCS:-true}
	allow-flight=${ALLOW_FLIGHT:-false}
	level-name=${LEVEL_NAME:-world}
	view-distance=${VIEW_DISTANCE:-10}
	resource-pack=${RESOURCE_PACK}
	spawn-animals=${SPAWN_ANIMALS:-true}
	white-list=${WHITE_LIST_ENABLED:-false}
	generate-structures=${GENERATE_STRUCTURES:-true}
	online-mode=${ONLINE_MODE:-true}
	max-build-height=${MAX_BUILD_HEIGHT:-265}
	level-seed=${LEVEL_SEED}
	use-native-transport=${USE_NATIVE_TRANSPORT:-true}
	enable-rcon=${ENABLE_RCON:-false}
	EOF
fi

./ServerStart.sh