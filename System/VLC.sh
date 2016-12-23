sudo raspivid -o - -t 0 -w 640 -h 360 -fps 20 | cvlc -vvv stream:///dev/stdin --sout '#standard{access=http,mux=ts,dst=:8090}' :demux=h264
