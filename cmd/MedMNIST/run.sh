# # If you use run.sh to launch many peer nodes, you should comment below line
# #client.lib.Input() in peer.py
# #Input() in peer.go

# NUM_NODES=6
# START_ADDR=127.0.0.1
# START_PORT=8001
# BOOTSTRAP_ADDR=127.0.0.1
# BOOTSTRAP_PORT=9999


# for i in `seq 1 $NUM_NODES`
# do
#     python3 peer.py $START_ADDR $(($i + $START_PORT)) $BOOTSTRAP_ADDR:$BOOTSTRAP_PORT | tee node$(($i + $START_PORT)).log 2>&1 &
#     sleep 1
# done

#!/bin/bash

#!/bin/bash

#!/bin/bash

#!/bin/bash

NUM_NODES=15
START_ADDR=127.0.0.1
START_PORT=7999
BOOTSTRAP_ADDR=127.0.0.1
BOOTSTRAP_PORT=9999
OUTPUT_FILE="output/edgeClientList.json"

# Create the initial JSON structure
echo '{ "node_list": [' > $OUTPUT_FILE

for i in $(seq 1 $NUM_NODES)
do
    PORT=$(($i + $START_PORT))
    python3 peer.py $START_ADDR $PORT $BOOTSTRAP_ADDR:$BOOTSTRAP_PORT | tee node$PORT.log 2>&1 &
    sleep 1

    # Add node information to the JSON file
    echo -n "    {" >> $OUTPUT_FILE
    echo -n "\"node_id\": $((i-1))," >> $OUTPUT_FILE
    echo "\"node_info\": {" >> $OUTPUT_FILE
    echo -n "\"ip\": \"$START_ADDR\"," >> $OUTPUT_FILE
    echo "\"port\": $PORT" >> $OUTPUT_FILE
    echo -n "}}," >> $OUTPUT_FILE

done

# Remove the trailing comma from the last entry
sed -i '$s/,$//' $OUTPUT_FILE

# Close the JSON structure with the rounds array
echo '],' >> $OUTPUT_FILE
echo '"rounds":[]}' >> $OUTPUT_FILE



