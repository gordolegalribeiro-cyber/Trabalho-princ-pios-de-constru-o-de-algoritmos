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
    
   
    df.to_csv(ARQUIVO_ALUNOS, index=False, encoding='utf-8') #Salvar no arquivo CSV
    
    print(f"\nAluno '{nome}' cadastrado com sucesso!")
    print(f"Matrícula: {matricula}")
    
    return df

def pesquisar_aluno(df):
    print("\n" + "_"*50)       #Função para pesquisar aluno por matrícula ou nome
    print("Pesquisar aluno")
    print("_"*50)
    
    if df.empty:
        print("Nenhum aluno cadastrado")
        return df, None
    
    print("Opções de pesquisa:")
    print("1 - Por número de matrícula")
    print("2 - Por nome")
    
    opcao = input("\nDigite a opção (1 ou 2): ").strip()
    
    if opcao == '1':
        try:
            matricula = int(input("Digite o número de matrícula: "))
            resultado = df[df['Matricula'] == matricula]
        except ValueError:
            print("Matrícula inválida! Deve ser um número.")
            return df, None
    
    elif opcao == '2':
        nome = input("Digite o nome (ou parte do nome): ").strip().lower()
        
        resultado = df[df['Nome'].str.lower().str.contains(nome, na=False)] #Pesquisa case-insensitive
    
    else:
        print("Opção inválida!")
        return df, None
    
    if resultado.empty:
        print("\nAluno não encontrado.")
        return df, None
    elif len(resultado) > 1:
        print("\nForam encontrados vários alunos:")
        for idx, aluno in resultado.iterrows():
            print(f"{aluno['Matricula']} - {aluno['Nome']}")
        
        try:
            matricula = int(input("\nDigite a matrícula do aluno desejado: "))
            resultado = df[df['Matricula'] == matricula]
            if resultado.empty:
                print("Matrícula não encontrada.")
                return df, None
        except ValueError:
            print("Matrícula inválida!")
            return df, None
    
    
    aluno = resultado.iloc[0] #Mostrar dados do aluno encontrado
    mostrar_dados_aluno(aluno)
    
    return df, aluno['Matricula']

def mostrar_dados_aluno(aluno): #Mostra os dados de um aluno formatados
    print("\n" + "-"*50)
    print("DADOS DO ALUNO")
    print("-"*50)
    print(f"Matrícula: {aluno['Matricula']}")
    print(f"Nome: {aluno['Nome']}")
    print(f"Endereço: {aluno['Rua']}, {aluno['Numero']}")
    print(f"Bairro: {aluno['Bairro']}")
    print(f"Cidade: {aluno['Cidade']} - {aluno['UF']}")
    print(f"Telefone: {aluno['Telefone']}")
    print(f"E-mail: {aluno['Email']}")
    print("_"*50)

def editar_aluno(df, matricula):   #Função para editar dados de um aluno
    print("\n" + "_"*50)
    print("Editar dados do aluno")
    print("_"*50)
    
    
    idx = df.index[df['Matricula'] == matricula].tolist()[0] #Encontrar o indice do aluno
    
    
    print("\nSelecione o campo que deseja editar:") #Mostrar menu de edição
    print("1 - Nome")
    print("2 - Rua")
    print("3 - Número")
    print("4 - Bairro")
    print("5 - Cidade")
    print("6 - UF")
    print("7 - Telefone")
    print("8 - E-mail")
    print("9 - Cancelar")
    
    opcao = input("\nDigite a opção (1-9): ").strip()
    
    campos = {
        '1': 'Nome',
        '2': 'Rua',
        '3': 'Numero',
        '4': 'Bairro',
        '5': 'Cidade',
        '6': 'UF',
        '7': 'Telefone',
        '8': 'Email'
    }
    
    if opcao in campos:
        campo = campos[opcao]
        novo_valor = input(f"Digite o novo valor para {campo}: ").strip()
        
        if campo == 'UF':
            novo_valor = novo_valor.upper()
        
        
        df.at[idx, campo] = novo_valor #Atualizar o campo no DataFrame
        
        
        df.to_csv(ARQUIVO_ALUNOS, index=False, encoding='utf-8') #Salvar no arquivo CSV
        
        print(f"\nCampo '{campo}' atualizado com sucesso!")
        
        
        aluno_atualizado = df.iloc[idx]   #Mostrar dados atualizados
        mostrar_dados_aluno(aluno_atualizado)
    
    elif opcao == '9':
        print("Edição cancelada.!")
    else:
        print("Opção inválida!")
    
    return df

def remover_aluno(df, matricula):   #Função para remover um aluno
    print("\n" + "*"*50)
    print("Remover aluno")
    print("*"*50)
    
    
    aluno = df[df['Matricula'] == matricula].iloc[0] #Encontrar o aluno
    nome = aluno['Nome']
    
    print(f"\nVocê está prestes a remover o aluno:")
    print(f"Matrícula: {matricula}")
    print(f"Nome: {nome}")
    
    
    confirmacao = input("\nTem certeza que deseja remover este aluno? (Sim/Não): ").strip().upper() #Confirmação
    
    if confirmacao == 'Sim':
        
        df = df[df['Matricula'] != matricula] #Remover o aluno do DataFrame
        
        
        df.to_csv(ARQUIVO_ALUNOS, index=False, encoding='utf-8') #Salvar no arquivo CSV
        
        print(f"\nAluno '{nome}' removido com sucesso!")
    else:
        print("Operação cancelada.")
    
    return df

def menu(): #Função principal do menu 
    print("\n" + "^"*50)
    print("Sistema de cadastro de alunos")
    print("-"*50)
    print("1 - Inserir novo aluno")
    print("2 - Pesquisar/Editar/Remover aluno")
    print("3 - Sair")
    print("~"*50)
    
    opcao = input("Digite a opção desejada (1-3): ").strip()
    return opcao

def main():
    
    print("Inicializando sistema de cadastro de alunos") #Função principal do programa
    
    
    df = inicializar_arquivo() #Inicializar DataFrame
    
    while True:
        opcao = menu()
        
        if opcao == '1':
            df = inserir_aluno(df)
        
        elif opcao == '2':
            df, matricula = pesquisar_aluno(df)
            
            if matricula is not None:
                print("\nOpções:")
                print("1 - Editar dados")
                print("2 - Remover aluno")
                print("3 - Voltar ao menu")
                
                acao = input("\nDigite a opção (1-3): ").strip()
                
                if acao == '1':
                    df = editar_aluno(df, matricula)
                elif acao == '2':
                    df = remover_aluno(df, matricula)
                elif acao == '3':
                    continue
                else:
                    print("Opção inválida!")
        
        elif opcao == '3':
            print("\nEncerrando o sistema")
            print("Programa Finalizado!")
            break
        
        else:
            print("\nOpção inválida! Digite 1, 2 ou 3.")
        
        input("\nPressione Enter para continuar")

if __name__ == "__main__":
    main()