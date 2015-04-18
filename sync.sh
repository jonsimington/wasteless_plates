# script to sync the db every hour

# sync first page 6 times
# 200 API requests per hour, 30 items per page -> 200 / 30 = 6.67 -> run sync 6 times every hour 
for i in `seq 1 6`; do
    python3 wasteless_plates/recipes/sync.py
done
