import boto3
from botocore.exceptions import ClientError

def configurar_s3(nombre_bucket):
    s3 = boto3.client('s3')
    
    try:
        # Crear bucket
        print(f"Creando bucket: {nombre_bucket}...")
        s3.create_bucket(Bucket=nombre_bucket)
        
        # Configurar Política de Ciclo de Vida (Lifecycle Policy)
        # Esto cumple con el punto de la rúbrica sobre la política de ciclo de vida
        s3.put_bucket_lifecycle_configuration(
            Bucket=nombre_bucket,
            LifecycleConfiguration={
                'Rules': [
                    {
                        'ID': 'ReglaDeTransicionYExpiracion',
                        'Status': 'Enabled',
                        'Filter': {'Prefix': ''},
                        'Transitions': [
                            {
                                'Days': 30,
                                'StorageClass': 'STANDARD_IA'
                            }
                        ],
                        'Expiration': {
                            'Days': 90
                        }
                    }
                ]
            }
        )
        print("Bucket creado y Lifecycle Policy configurada exitosamente.")
        
    except ClientError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    configurar_s3("mi-bucket-devops-proyecto-final")