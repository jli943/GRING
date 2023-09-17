# If you use run.sh to launch many peer nodes, you should comment below line
#client.lib.Input() in peer.py
#Input() in peer.go

NUM_NODES=6
START_ADDR=127.0.0.1
START_PORT=8001
BOOTSTRAP_ADDR=127.0.0.1
BOOTSTRAP_PORT=9999


for i in `seq 1 $NUM_NODES`
do
    python3 peer.py $START_ADDR $(($i + $START_PORT)) $BOOTSTRAP_ADDR:$BOOTSTRAP_PORT | tee node$(($i + $START_PORT)).log 2>&1 &
    sleep 1
done
