import boto3

dynamodb = boto3.client('dynamodb')
sns = boto3.client('sns')
sns_topic_arn = 'ARN_DO_TÓPICO_SNS'  # Substitua pelo ARN do tópico SNS adequado

def lambda_handler(event, context):
    # Extrair as informações do corpo da requisição
    body = event['body']
    name = body['name']
    numero = body['numero']
    cpf_cnpj = body['cpf_cnpj']
  
    # Armazenar as informações no DynamoDB
    dynamodb.put_item(
        TableName='vulpes-table',
        Item={
            'name': {'S': name},
            'numero': {'S': numero},
            'cpf_cnpj': {'S': cpf_cnpj}
        }
    )
  
    # Enviar SMS usando o serviço SNS
    message = f'Olá, {name}! Seus dados foram registrados com sucesso.'
    sns.publish(
        TopicArn=sns_topic_arn,
        Message=message,
        PhoneNumber=numero
    )
  
    return {
        'statusCode': 200,
        'body': 'Dados inseridos com sucesso no DynamoDB e SMS enviado.'