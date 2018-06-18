import sys
import json
import os
import boto3
from boto3.dynamodb.conditions import Key, Attr

def funcion(event, context):  
    nombre = ''
    
    try:
        nombre = event['query']['nombre']
    except:
        nombre = 'Ponyo'
    
    mensaje = 'Hola {}!!!'.format(nombre)
    
    return { 
        'message' : mensaje,
        'jsonEvent': json.dumps(event)
    }