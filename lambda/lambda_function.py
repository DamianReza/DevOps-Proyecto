import json
import random

def lambda_handler(event, context):
    mensajes = [
        "Despliegue exitoso", 
        "Pipeline completado", 
        "Infraestructura lista", 
        "Contenedores arriba", 
        "VPC configurada"
    ]
    return {
        'statusCode': 200,
        'body': json.dumps({
            'mensaje': random.choice(mensajes),
            'servicio': 'microservicio-devops'
        })
    }