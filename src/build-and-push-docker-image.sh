#!/bin/bash

docker build -t tchaudhry/rainbow-hasher:SHA256 .

docker push tchaudhry/rainbow-hasher:SHA256
