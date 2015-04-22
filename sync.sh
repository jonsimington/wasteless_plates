#!/bin/bash

# script to fetch new recipes every hour

# sync $NUM_SYNCSth page 3 times
# 100 API requests per hour, 30 items per page -> 100 / 30 = 3.33 -> run sync 3 times every hour 
for i in `seq 1 3`; do
    python3 wasteless_plates/recipes/sync.py
    NUM_SYNCS=$((NUM_SYNCS+1));
done
