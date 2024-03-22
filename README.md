# Image syncer
### Aim: 
To check and sync the deployment of images with one selected cluster with the production cluster 
## Image syncer v_1:
### Aim: 
To compare the production deployment image with the the image in pp in the same namespace.
### How it works: 
Input the image id of the deployment along with the of the namespace. Then it returns if it is in synced or asynced.
#### Input variables:
- Namespace
- JSON file path containing all the namespace and corresponding image
#### Output:
The list of deployments with non-synced images
