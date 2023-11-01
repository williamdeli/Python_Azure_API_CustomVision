import requests

# your project id and training key
project_id = "8c1537b1-86f5-4511-bf4d-8079ba8d231e"
training_key = "a49e6eb3607d4ef9af58f997e48aabba"

# url for the prediction endpoint
url = f"https://southeastasia.api.cognitive.microsoft.com/customvision/v3.4-preview/training/projects/{project_id}/predictions"

# Set the headers with the training key
headers = {
    "Training-Key": training_key
}

# Send the DELETE request
response = requests.delete(url, headers=headers)

# Check the response status code and handle accordingly
if response.status_code == 204:
    print("All predictions have been successfully deleted.")
else:
    print(f"Failed to delete predictions. Status code: {response.status_code}")
    print(response.text)
