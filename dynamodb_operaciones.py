import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

def ejecutar_operaciones():
    tabla_nombre = 'devops-tabla'
    
    try:
        # 1. Crear Tabla
        print(f"Creando tabla {tabla_nombre}...")
        tabla = dynamodb.create_table(
            TableName=tabla_nombre,
            KeySchema=[{'AttributeName': 'id', 'KeyType': 'HASH'}],
            AttributeDefinitions=[{'AttributeName': 'id', 'AttributeType': 'S'}],
            BillingMode='PAY_PER_REQUEST'
        )
        tabla.wait_until_exists()
        
        # 2. Insertar Registro
        print("Insertando registro...")
        tabla.put_item(Item={'id': '001', 'nombre': 'AdminUser', 'status': 'active'})
        
        # 3. Actualizar Registro (usando ExpressionAttributeNames para evitar conflicto con 'status')
        print("Actualizando status...")
        tabla.update_item(
            Key={'id': '001'},
            UpdateExpression="SET #s = :nuevo_status",
            ExpressionAttributeNames={'#s': 'status'},
            ExpressionAttributeValueSets={':nuevo_status': 'inactive'}
        )
        
        # 4. Eliminar Registro
        print("Eliminando registro...")
        tabla.delete_item(Key={'id': '001'})
        
        print("✅ Operaciones en DynamoDB completadas.")
        
    except ClientError as e:
        print(f"Error: {e.response['Error']['Message']}")

if __name__ == "__main__":
    ejecutar_operaciones()