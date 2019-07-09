#!/bin/sh

docker build -t viber-bot .
docker images | grep viber-bot

echo "What's The Next Version"
read NUM

docker tag viber-bot codeandrew/viber-bot:v$NUM
docker push codeandrew/viber-bot:v$NUM
