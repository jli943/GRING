sudo pkill -9 bootstrap
sudo pkill -9 publisher
sudo pkill -9 peer
sudo pkill -9 bench
sudo pkill -9 go
sudo pkill -9 tee
sudo pkill -9 sleep
sudo pkill -9 python3

# Define the range of port numbers you want to consider
start_port=8000
end_port=8100

# Loop through the port numbers and delete the files
for ((port = start_port; port <= end_port; port++)); do
  peer_file="peer${port}.json"
  node_log="node${port}.log"

  # Check if the peer file exists before attempting to delete it
  if [ -e "$peer_file" ]; then
    rm "$peer_file"
    echo "Deleted $peer_file"
  fi

  # Check if the node log file exists before attempting to delete it
  if [ -e "$node_log" ]; then
    rm "$node_log"
    echo "Deleted $node_log"
  fi
done

echo "Cleanup complete."
