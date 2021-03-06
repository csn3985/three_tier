# three_tier

- Setup an AWS ec2 instance
- Make sure you have configured both ports 3001 and 5001 to have inbound TCP traffic enabled.
- Install all prereqs
- 
`sudo apt update && sudo apt upgrade`

`sudo apt install vim docker.io git python3 python3-pip mysql-client`

- Configure Docker to allow user to run

`sudo usermod -aG docker $USER`

`newgrp docker`


- Pull this repository

`git clone https://github.com/jarrettbranch/three_tier.git`

- Build the containers

`cd three-tier`

`make`

- Run it
Execute these steps:

`./setup.sh`

`docker run -it --rm --name db --network project-network -p 0.0.0.0:3307:3306 -e MYSQL_ROOT_PASSWORD=password -e MYSQL_DATABASE=mysql -d mysql:latest`

Wait about thirty seconds, then run:

`cd db`

`./load_data.sh`

`cd ..`

Now open two more putty session to your instance. In one, execute

`docker run -it --rm --name ui -v ${PWD}/ui/ui/:/app --network project-network -p 3001:3000 -e CHOKIDAR_USEPOLLING=true three_tier-ui:latest`

In the other,execute

`docker run -it --rm --name bl --network project-network -p 5001:5000 three_tier-bl:latest`

Navigate with a web browser to 
http://<Your public instance ip>:3001
