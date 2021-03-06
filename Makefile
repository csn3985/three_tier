

default: UI BL

UI:
	docker build -t three_tier-ui:latest ./ui/ui

BL:
	docker build -t three_tier-bl:latest ./bl
