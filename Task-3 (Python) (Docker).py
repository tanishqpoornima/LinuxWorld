import docker

class DockerAPI:
    def __init__(self):
        self.client = docker.from_env()
        
    def list_containers(self):
        containers = self.client.containers.list()
        return containers
    
    def create_container(self, image, command, detach=True):
        container = self.client.containers.run(image, command, detach=detach)
        return container
    
    def stop_container(self, container_id):
        container = self.client.containers.get(container_id)
        container.stop()
    
    def remove_container(self, container_id):
        container = self.client.containers.get(container_id)
        container.remove()
    
    def list_images(self):
        images = self.client.images.list()
        return images
    
    def build_image(self, path, tag):
        image = self.client.images.build(path=path, tag=tag)
        return image
        
docker_api = DockerAPI()

containers = docker_api.list_containers()
for container in containers:
    print(container.id)

new_container = docker_api.create_container('ubuntu', 'echo "Hello, World!"')
print(new_container.id)

docker_api.stop_container(new_container.id)
docker_api.remove_container(new_container.id)

images = docker_api.list_images()
for image in images:
    print(image.tags)

docker_api.build_image('/path/to/dockerfile', 'my-custom-image:latest')
