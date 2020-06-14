#!/usr/bin/env bash

if [[ "$1" == "update" ]]; then
    docker-compose -f tests/docker-compose.yml build --no-cache
fi
docker-compose -f tests/docker-compose.yml up --force-recreate --abort-on-container-exit