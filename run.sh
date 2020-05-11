#!/bin/bash

docker-compose up -d && docker exec -it achilleslite_src_1 bash && docker-compose down
