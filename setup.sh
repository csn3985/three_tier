export PUB_IP=$(curl http://169.254.169.254/latest/meta-data/public-ipv4)
echo REACT_APP_PUB_IP=$PUB_IP > ./ui/ui/.env
docker network create --driver bridge project-network

