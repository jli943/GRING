sudo pkill -9 bootstrap
sudo pkill -9 publisher
sudo pkill -9 peer
sudo pkill -9 bench
sudo pkill -9 go
sudo pkill -9 tee
sudo pkill -9 sleep
sudo pkill -9 python3

# Specify the path to the "output/" folder
output_path="output"

# Delete the relationship.json file if it exists
grouplog_file="${output_path}/grouplog.json"
if [ -e "$grouplog_file" ]; then
  rm "$grouplog_file"
  echo "Deleted $grouplog_file"
fi

globalModel_file="${output_path}/globalModel.json"
if [ -e "$globalModel_file" ]; then
  rm "$globalModel_file"
  echo "Deleted $globalModel_file"
fi

relationship_file="${output_path}/relationship.json"
if [ -e "$relationship_file" ]; then
  rm "$relationship_file"
  echo "Deleted $relationship_file"
fi

# Define the range of port numbers you want to consider
start_port=8000
end_port=8100

# Loop through the port numbers and delete the files
for ((port = start_port; port <= end_port; port++)); do
  peer_file="output/peer${port}.json"
  node_log="node${port}.log"
  relationship_file="output/relationship${port}.json"

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

  if [ -e "$relationship_file" ]; then
    rm "$relationship_file"
    echo "Deleted $relationship_file"
  fi
done

echo "Cleanup complete."
