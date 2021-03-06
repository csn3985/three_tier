docker run -it --rm --name ui -v ${PWD}/ui/ui/:/app --network project-network -p 3001:3000 -e CHOKIDAR_USEPOLLING=true three_tier-ui:latest

docker run -it --rm --name bl --network project-network -p 5001:5000 three_tier-bl:latest

docker run -it --rm --name db --network project-network -p 0.0.0.0:3307:3306 -e MYSQL_ROOT_PASSWORD=password -e MYSQL_DATABASE=mysql -d mysql:latest

