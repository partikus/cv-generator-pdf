#!/usr/bin/env bash

TASK_NAME=$1;

case $TASK_NAME in
  'build')
    docker build -t cvgenerator/generator docker/python3
    ;;
  'run')
    docker-compose -f docker-compose.yml -f docker-compose.local.yml up
    ;;
  'run-server')
    docker-compose -f docker-compose.yml -f docker-compose.local.yml up python3-server
    ;;
esac
