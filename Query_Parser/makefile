# Name of the Docker image
IMAGE_NAME=my_docker_image

# Dockerfile path (optional if in current directory)
DOCKERFILE_PATH=./Dockerfile

.PHONY: build run clean

# Target to build the Docker image
build:
	docker build -t $(IMAGE_NAME) -f $(DOCKERFILE_PATH) .

# Target to run the Docker container
run: build
	docker run -v $$(pwd)/externalfiles:/app/externalfiles -p 8888:8888 $(IMAGE_NAME)

# Target to clean up Docker images and containers (optional)
clean:
	docker rmi -f $(IMAGE_NAME)