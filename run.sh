gnome-terminal -x sh -c "docker run -it --rm -v ${PWD}/ui/ui/:/app -p 3001:3000 -e CHOKIDAT_USEPOLLING=true three_tier-ui:latest; bash"
#gnome-terminal -x sh -c "docker run -it --rm -p 3001:3000 -e CHOKIDAT_USEPOLLING=true three_tier-ui:latest; bash"
gnome-terminal -x sh -c "docker run -it --rm -p 5001:5000 three_tier-bl:latest; bash"

#gnome-terminal -x sh -c "docker run -it --rm -p 0.0.0.0:3307:3306 -e MYSQL_ROOT_PASSWORD=password -e MYSQL_DATABASE=mysql -d mysql:latest"]


