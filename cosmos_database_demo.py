# Our required import statements
from azure.cosmos import exceptions, CosmosClient, PartitionKey

# Your endpoint is specific to your database, allowing you to access
# its contents over the internet!
ENDPOINT = '<ENDPOINT>'

# Your private key is your unique "password" that grabts you
# permission to modify your database, DO NOT SHARE THIS KEY!
KEY = '<PRIVATE KEY>'

# Initialize your CosmosDB Client, allowing you to use CosmosDB APIs
cosmos_client = CosmosClient(ENDPOINT, KEY)

# Initialize your database if it doesn't exist
# Pick out a database name, I'm calling my database 'demo_database'
database_name = 'demo_database'

# Create the database by this name if it doesn't already exist
# id = name of the database
cosmos_database = cosmos_client.create_database_if_not_exists(id = database_name)

# Initialize your container inside of the database if it doesn't exist
# Pick out a container name, I'm calling my container 'demo_container'
container_name = 'demo_container'

# Create the container by this name if it doesn't already exist
# id = name of the container
# partition key = how the data in this container will be partitioned (sorted)
# offer_throughput = You can ignore this and keep it as '400', but it represents the capacity of the database
# (lower numbers means less reads and writes per second)
cosmos_container = cosmos_database.create_container_if_not_exists(id = container_name, 
    partition_key = PartitionKey(path = '/type'),
    offer_throughput = 400)

while True:
    print('--- COMMANDS: ---')
    print('[1] Create Data')
    print('[2] Read Data')
    print('[3] Update Data')
    print('[4] Delete Data')
    
    # Get user input (enter a number in the console)
    input_value = input('Please enter a command: ')

    if input_value == '1':
        # .create_item(object) creates an object in the database based on what we passed in
        # Note that the 'id' and your chosen partition key MUST exist inside the object for
        # this line of code to work!
        # An object we want to create in our database

        create_data_object = {
            'id': '123', # Our object ID
            'type': 'smoothie', # Our object partition key value
            'name': 'fruit smoothie', # Data types can be simple strings...
            'ingredients': ['blueberry', 'strawberry'], # or arrays...
            'properties': { # or even a whole nested object!
                'texture': 'smooth',
                'flavor': 'berry',
                'color': 'purple'
            }
        }

        cosmos_container.create_item(body = create_data_object)
        print('Successfully created the object!')

    elif input_value == '2':
        try:
            response = cosmos_container.read_item(item = '123', partition_key = 'smoothie')
            print(response)
        except:
            print('Item not found!')

    elif input_value == '3':
        # An object containing the key / value pairs we want to update in our database
        # Since we want to update the 'name' field, we include that in our body
        update_data_object = {
            'name': 'berry fruit smoothie'
        }

        read_item = cosmos_container.read_item(item = '123', partition_key = 'smoothie')
        
        # For each key in the update_data_object, replace that corresponding key's value
        # in the read item from the database

        # Example:
        # In the originally uploaded data object, the 'name' key had value 'fruit smoothie'
        # Now, we replace the original 'name' key's value with 'berry fruit smoothie'
        for key in update_data_object:
            read_item[key] = update_data_object[key]

        cosmos_container.upsert_item(body = read_item)
        print('Successfully updated the object! (The "name" key should be different now!)')

    elif input_value == '4':
        cosmos_container.delete_item(item = '123', partition_key = 'smoothie')
        print('Successfully deleted the object!')

    # Whitespace printing
    print()