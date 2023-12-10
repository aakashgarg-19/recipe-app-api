#!/bin/sh

set -e

envsubst < /etc/ngnix/default.conf.tpl > /etc/ngnix/conf.d/default.conf
ngnix -g 'daemon off;'