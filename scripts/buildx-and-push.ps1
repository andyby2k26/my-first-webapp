# Build and push the multi-architecture image for 'app1'
# The --platform flag specifies the architectures.
# The --push flag sends the resulting image to Docker Hub.
docker buildx build --platform linux/amd64,linux/arm64,linux/arm/v8 --push -t andyby2k26/andyby2k26:app1 ./app1

# Build and push the multi-architecture image for 'app2'
docker buildx build --platform linux/amd64,linux/arm64,linux/arm/v8 --push -t andyby2k26/andyby2k26:app2 ./app2