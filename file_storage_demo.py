from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

# This is your connection string, a single string that allows you to connect
# to you Azure Storage account
# Note this is slightly different than CosmosDB, which required a URL and Key to work!
# In Storage, we ONLY need the connection string!
CONNECTION_STRING = '<CONNECTION STRING>'

# Create the BlobServiceClient object which will be used to create a container client
blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)

# Create a unique name for the container,
# I'm going call call my container 'demo-container'
container_name = 'demo-container'

# Try to create the container
try:
    container_client = blob_service_client.create_container(container_name)
    print(f'Created container {container_name}!')
# If you get an exception, it's caught here
# and it means that a container with this name already exists
except:
    print('Container already exists!')

# We will be uploading a file called puppy.png, located with the path ./puppy.png
# the './' refers to how the image is in the same location as this Python script
local_file_name = 'puppy.jpg'
local_file_path = './puppy.jpg'

# 'blob_client' refers to the object that will allow us to read / write data at this specific location
# in Azure Storage
blob_client = blob_service_client.get_blob_client(container = container_name, blob = local_file_name)

# Upload the image by opening a 'read' connection to the image on our computer and call
# the .upload_blob API that uploads the file into Azure Storage

try:
    with open(local_file_path, 'rb') as data:
        blob_client.upload_blob(data)
    print('Successfully uploaded our file!')
except:
    print('A file with this name already exists at this location!')