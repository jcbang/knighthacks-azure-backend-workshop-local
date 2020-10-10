# knighthacks-azure-backend-workshop-local

## Setting up this Python Code
- Inside cosmos_database_demo.py, replace the placeholder values for ```ENDPOINT``` and ```KEY``` at the top of the script with your own values
- Inside file_storage_demo.py, replace the placeholder value for ```CONNECTION_STRING``` at the top of the script with your own values
- Instructions on how to get these values can be found on my slides https://docs.google.com/presentation/d/10Of0NQ-5KmFdixxoxN-K04-LyT8vbQJfrXZ96AH0d8U/edit?usp=sharing

## Running this Python Code
Packages Required:
- azure-storage-blob
- azure-cosmos

In order to install a package, run ```pip install azure-storage-blob``` and ```pip install azure-cosmos```

In order to run a script, download this repository, navigate to it via command line, and type ```python cosmos_database_demo.py``` or ```python file_storage_demo.py```

## Interacting with this Python Code
### cosmos_database_demo
A command line prompt will appear after you run the script, asking you if you want to create data, read data, update data, or delete data on the Database. If you get this far without errors, it should mean you have correctly configured ENDPOINT and KEY values outlined in the first step.

### file_storage_demo
There's no command line prompt for this script, this script will automatically upload the puppy.jpg image to your Azure Storage account assuming you submitted the right CONNECTION_STRING variable outlined in the first step.
