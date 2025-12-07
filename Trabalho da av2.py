import pandas as pd
import os

ARQUIVO_ALUNOS = 'alunos.csv' #Nome do arquivo CSV

def inicializar_arquivo():
    colunas = ['Matricula', 'Nome', 'Rua', 'Numero', 'Bairro', 'Cidade', 'UF', 'Telefone', 'Email'] #O arquivo CSV é inicializado com as colunas requeridas.
  
if not os.path.exists(ARQUIVO_ALUNOS):
        df = pd.DataFrame(columns=colunas)
        df.to_csv(ARQUIVO_ALUNOS, index=False, encoding='utf-8')
        return df
    else:
        try:
            df = pd.read_csv(ARQUIVO_ALUNOS, encoding='utf-8')
            return df
        except Exception as e:
            print(f"Erro ao ler arquivo: {e}")
            df = pd.DataFrame(columns=colunas) #Em caso de erro, cria um novo arquivo
            df.to_csv(ARQUIVO_ALUNOS, index=False, encoding='utf-8')
            return df

def gerar_matricula(df):
    if df.empty: #Gera o próximo número de matrícula sequência
        return 1
    else:
        return df['Matricula'].max() + 1

def inserir_aluno(df):
    
    print("\n" + "-"*50)  #Função para inserir um novo aluno
    print("CADASTRO DE NOVO ALUNO")
    print("-"*50)
    
    matricula = gerar_matricula(df) #Gerar matrícula automática
    print(f"Número de matrícula gerado: {matricula}")
    1
 nome = input("Nome: ").strip()  #Coletar dados do aluno
    rua = input("Rua: ").strip()
    numero = input("Número: ").strip()
    bairro = input("Bairro: ").strip()
    cidade = input("Cidade: ").strip()
    uf = input("UF: ").strip().upper()
    telefone = input("Telefone: ").strip()
    email = input("E-mail: ").strip()
    
    
    novo_aluno = { #Criar dicionário com os dados
        'Matricula': matricula,
        'Nome': nome,
        'Rua': rua,
        'Numero': numero,
        'Bairro': bairro,
        'Cidade': cidade,
        'UF': uf,
        'Telefone': telefone,
        'Email': email
    }
    
    
    df = pd.concat([df, pd.DataFrame([novo_aluno])], ignore_index=True)  #Adicionar ao DataFrame
    