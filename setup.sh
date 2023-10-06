docker build . -t dghl_docker

docker run -it --gpus all --network host dghl_docker
