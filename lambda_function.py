import json
import boto3
from datetime import date


def lambda_handler(event, context):
    
    s3 = boto3.client('s3')
    
    print('Mensagem recebida')
    print(event)
    
    ### Definindo nome do arquivo
    day = date.today().strftime('%d')
    month = date.today().strftime('%m')
    year = date.today().strftime('%Y')
    
    ### vars
    caminho_do_arquivo_local="/tmp/arquivo.txt"
    nome_do_arquivo_local=  year+ "/"+ month + "/" +day+".txt"
    nome_do_s3="nome_bucket"
    
    try:
    
        for record in event.get('Records'):
            print('#### Records ####')
            print(record)
            
            body = record.get('body')
            
            print('#### Body ####')
            print(body)
            
            ### Cria arquivo
            arquivo = open(caminho_do_arquivo_local, 'a')
            
            arquivo.write(body +'\n')
            
            ### Fecha arquivo
            arquivo.close()
            
            with open(caminho_do_arquivo_local, "rb") as f:
                s3.upload_fileobj(f, nome_do_s3, nome_do_arquivo_local)
            


    except Exception as e:  
        return e
        

        
