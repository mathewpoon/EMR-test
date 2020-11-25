import boto3
import datetime

def lambda_handler(event, context):
    client = boto3.client('emr')
    age = 13
    timestamp = datetime.datetime.today() - datetime.timedelta(age)
    print(timestamp)
    response = client.list_clusters(
        CreatedAfter=timestamp,
        #CreatedBefore=timestamp,
        ClusterStates=['STARTING','BOOTSTRAPPING','RUNNING','WAITING','TERMINATING','TERMINATED','TERMINATED_WITH_ERRORS']
    )
    
    for cluster in response['Clusters']:
      print(cluster['Id'])
