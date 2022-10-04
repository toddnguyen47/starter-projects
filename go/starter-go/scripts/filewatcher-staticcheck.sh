#!/bin/bash

# To be used with Goland's file watcher

#echo $1
#staticcheck $1
staticcheck "${1}/..."
