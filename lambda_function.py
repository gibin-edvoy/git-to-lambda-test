import pandas as pd
import json
import sys



def lambda_handler(event, context):
    d = {'col1': [1, 2], 'col2': [3, 4]}
    df = pd.DataFrame(data=d)
    print("Python version: ", sys.version)
    print("Version info: ", sys.version_info)
    print(df)
    print('Done with api')
    response = {
        'statusCode': 200,
        'body': json.dumps(df)
    }

    return response
