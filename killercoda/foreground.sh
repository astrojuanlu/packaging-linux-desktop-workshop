echo "Installing scenario..."
while [ ! -f /tmp/finished ]; do sleep 1; done
echo DONE

tmux new -s workshop "su - ubuntu"
