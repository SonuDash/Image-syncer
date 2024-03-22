import json
from kubernetes import client, config

def get_current_image(namespace, deployment_name):
    config.load_kube_config()

    api_instance = client.AppsV1Api()

    try:

        deployment = api_instance.read_namespaced_deployment(deployment_name, namespace)


        container_image = deployment.spec.template.spec.containers[0].image

        return container_image

    except Exception as e:
        print(f"Error: {e}")
        return None

def check_images_from_json(namespace, json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)

    non_matching = []

    for deployment_name, desired_image in data.items():
        current_image = get_current_image(namespace, deployment_name)

        if current_image and current_image != desired_image:
            non_matching.append(deployment_name)

    return non_matching


namespace = input("Enter the namespace: ")
json_file = input("Enter the path to the JSON file: ")

result = check_images_from_json(namespace, json_file)

print("\nDeployments with non-matching images:")
for deployment_name in result:
    print(f"- {deployment_name}")
