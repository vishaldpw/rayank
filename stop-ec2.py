import boto3

 

# Prompt the user to enter the instance ID
instance_id = input("Enter the instance ID: ")

 

# Create a Boto3 EC2 client
ec2 = boto3.client('ec2')

 

# Stop the instance
response = ec2.stop_instances(InstanceIds=[instance_id])

 

# Check if the instance was successfully stopped
if len(response['StoppingInstances']) > 0:
    current_state = response['StoppingInstances'][0]['CurrentState']['Name']
    print(f"The instance {instance_id} is {current_state}.")
else:
    print("Failed to stop the instance.")