import json
import boto3

def lambda_handler(event, context):
    
    ### vars
    caminho_do_arquivo_local="/tmp/arquivo.txt"
    nome_do_arquivo_local="arq_dentro_do_s3.txt"
    nome_do_s3="bucket_name"
    
    ### Cria arquivo
    arquivo = open(caminho_do_arquivo_local, 'w')
    arquivo.write('linha 1 \n')
    arquivo.write('linha 2 \n')
    arquivo.write('linha 3 \n')
    arquivo.close()
    
    ### Realiza Upload do arquivo
    s3 = boto3.client('s3')
    with open(caminho_do_arquivo_local, "rb") as f:
        s3.upload_fileobj(f, nome_do_s3, nome_do_arquivo_local) 
    
    print('Mensagem recebida')
    print(event)
    
    for record in event.get('Records'):
        print('Mensagem recebida - Records')
        print(record)
        
        body = json.loads(record.get('body'))
        id_person = body.get('id')
        name = body.get('Name')
        
        print(f'Name: {name}, ID: {id_person}')

        
        
        
