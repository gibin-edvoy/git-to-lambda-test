import pandas as pd
import json
import sys
import cv2
import pdf2image
import numpy as np
import pandas
import requests
import PIL
import passporteye


def lambda_handler(event, context):
    d = {'col1': [1, 2], 'col2': [3, 4]}
    df = pd.DataFrame(data=d)
    print("Python version: ", sys.version)
    print("Version info: ", sys.version_info)
    print(df)
    print('Done with api')
    print("cv2:", cv2.__version__)
    print("numpy: ", np.__version__)
    print("pandas: ", pandas.__version__)
    print("requests: ", requests.__version__)
    print("Pillow: ", PIL.__version__)
    print("passporteye: ", passporteye.__version__)
    response = {
        'statusCode': 200,
        'body': "success"
    }

    return response
