#!/usr/bin/env bash
# Como setar sua versão do bot
# usando heroku docker containers

heroku container:login
heroku create
heroku container:push worker
heroku container:release worker
heroku ps:scale worker=1
