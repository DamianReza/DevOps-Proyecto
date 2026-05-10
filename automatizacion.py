import boto3
from datetime import datetime, timedelta

# Inicializar clientes
ec2 = boto3.client('ec2', region_name='us-east-1')
s3 = boto3.client('s3', region_name='us-east-1')
cloudwatch = boto3.client('cloudwatch', region_name='us-east-1')
autoscaling = boto3.client('autoscaling', region_name='us-east-1')

def listar_instancias():
    print("\n--- 🖥️ Instancias EC2 ---")
    response = ec2.describe_instances()
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            print(f"ID: {instance['InstanceId']} | Tipo: {instance['InstanceType']} | Estado: {instance['State']['Name']}")

def reporte_cpu():
    print("\n---  Reporte de CPU (Últimas 24h) ---")
    # Obtener IDs de instancias en ejecución
    instances = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
    
    for res in instances['Reservations']:
        for inst in res['Instances']:
            instance_id = inst['InstanceId']
            stats = cloudwatch.get_metric_statistics(
                Namespace='AWS/EC2',
                MetricName='CPUUtilization',
                Dimensions=[{'Name': 'InstanceId', 'Value': instance_id}],
                StartTime=datetime.utcnow() - timedelta(days=1),
                EndTime=datetime.utcnow(),
                Period=3600,
                Statistics=['Average']
            )
            
            puntos = stats.get('Datapoints', [])
            if puntos:
                avg_cpu = puntos[0]['Average']
                print(f"Instancia {instance_id}: {avg_cpu:.2f}% promedio")
            else:
                print(f"Instancia {instance_id}: Sin datos suficientes")

def listar_s3():
    print("\n--- Buckets S3 y Objetos ---")
    buckets = s3.list_buckets()
    for bucket in buckets['Buckets']:
        name = bucket['Name']
        print(f"Bucket: {name}")
        # Listar objetos del bucket
        objects = s3.list_objects_v2(Bucket=name)
        if 'Contents' in objects:
            for obj in objects['Contents']:
                print(f"  └─ Objeto: {obj['Key']} ({obj['Size']} bytes)")
        else:
            print("  └─ (Vacío)")

def consultar_asg():
    print("\n---  Grupos de Auto Scaling ---")
    response = autoscaling.describe_auto_scaling_groups()
    for asg in response['AutoScalingGroups']:
        print(f"Nombre: {asg['AutoScalingGroupName']}")
        print(f"  Capacidad -> Min: {asg['MinSize']} | Max: {asg['MaxSize']} | Deseada: {asg['DesiredCapacity']}")

if __name__ == "__main__":
    try:
        listar_instancias()
        reporte_cpu()
        listar_s3()
        consultar_asg()
    except Exception as e:
        print(f"Error detectado: {e}")