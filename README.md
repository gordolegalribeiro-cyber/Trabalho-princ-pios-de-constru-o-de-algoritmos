Trabalho prático AV2.

Matéria Princípios de Construção de Algoritmos (PCA) 

Alunos: José Flavio de moraes RIbeiro matrícula:06013830
        Renan Caçador Dos Santos      matrícula:06013843

Sistema de Cadastro de Alunos

   Descrição
   
Sistema de gestão de registro de estudantes criado em Python com o uso da biblioteca Pandas. O sistema possibilita o registro, consulta, modificação e exclusão de dados dos alunos, guardando essas informações em um arquivo CSV.


  Finalidade
O sistema elimina a necessidade de gerenciar manualmente os registros dos alunos, proporcionando:
.Registro automatizado com criação de matrícula em sequência
.Armazenamento duradouro em arquivo CSV
.Busca eficaz por nome ou matrícula
.Interface fácil e intuitiva por meio do terminal
.Edição seletiva de campos específicos
.Remoção segura com verificação

  Dados Armazenados
O sistema guarda os seguintes dados por estudante:
.Inscrição (criada de forma automática)
.Nome completo:
.Endereço completo (rua, número, bairro, cidade e estado)
.Telefone móvel
.E-mail

 Pré-requisitos
 
Python 3.x instalado
Biblioteca Pandas

   Instalação das Dependências
bash

 Instalar a biblioteca Pandas
  pip install pandas

Ou se estiver usando requirements.txt
 pip install -r requirements.txt
 Como Executar
 Clone o repositório ou baixe o arquivo sistema_alunos.py

Execute o script Python:

 bash
python sistema_alunos.py
O sistema criará automaticamente o arquivo alunos.csv na primeira execução

Estrutura do Projeto
text
sistema-alunos/
│
├── sistema_alunos.py    # Código principal do sistema
├── alunos.csv           # Arquivo de dados (gerado automaticamente)
├── README.md            # Este arquivo
└── requirements.txt     # Dependências (opcional)
Fluxo de Uso
Menu Principal
text
==================================================
SISTEMA DE CADASTRO DE ALUNOS
==================================================
1 - Inserir novo aluno
2 - Pesquisar/Editar/Remover aluno
3 - Sair
1. Cadastrar Novo Aluno
O sistema gera automaticamente uma matrícula sequencial

Solicita dados pessoais e de endereço

Salva automaticamente no arquivo CSV

2. Pesquisar/Alterar/Remover
Pesquisar por: Matrícula ou Nome

Após encontrar: Opções para Editar ou Remover

Edição: Permite alterar campos específicos

Remoção: Confirmação necessária antes de excluir

3. Sair do Sistema
Encerra o programa

Dados são automaticamente salvos

Exemplos de Uso
Cadastro de Aluno
text
CADASTRO DE NOVO ALUNO
--------------------------------------------------
Número de matrícula gerado: 1
Nome: João Silva
Rua: Rua das Flores
Número: 123
Bairro: Centro
Cidade: São Paulo
UF: SP
Telefone: (11) 99999-9999
E-mail: joao@email.com

Aluno 'João Silva' cadastrado com sucesso!
Matrícula: 1
Pesquisa por Nome
text
PESQUISAR ALUNO
__________________________________________________
Opções de pesquisa:
1 - Por número de matrícula
2 - Por nome

Digite a opção (1 ou 2): 2
Digite o nome (ou parte do nome): joao

DADOS DO ALUNO
--------------------------------------------------
Matrícula: 1
Nome: João Silva
Endereço: Rua das Flores, 123
Bairro: Centro
Cidade: São Paulo - SP
Telefone: (11) 99999-9999
E-mail: joao@email.com
Edição de Dados
text
EDITAR DADOS DO ALUNO
__________________________________________________
Selecione o campo que deseja editar:
1 - Nome
2 - Rua
3 - Número
4 - Bairro
5 - Cidade
6 - UF
7 - Telefone
8 - E-mail
9 - Cancelar

Digite a opção (1-9): 7
Digite o novo valor para Telefone: (11) 98888-8888

Campo 'Telefone' atualizado com sucesso!

   
  Estrutura do Arquivo CSV
O arquivo alunos.csv contém as seguintes colunas:
.Matricula (inteiro, único)
.Nome (string)
.Rua (string)
.Numero (string)
.Bairro (string)
.Cidade (string)
.UF (string, 2 caracteres)
.Telefone (string)
.Email (string)

   Características Técnicas
.Persistência: Dados salvos em CSV com codificação UTF-8
.Busca: Case-insensitive para nomes
.Validação: UF convertida para maiúsculas automaticamente
.Segurança: Confirmação para operações de remoção
.Robustez: Tratamento de erros na leitura do arquivo
.Interface: Menu intuitivo com feedback claro

   Observações
   Na primeira execução, o arquivo alunos.csv é gerado automaticamente.
.As matrículas são criadas de forma sequencial, começando pelo maior número já existente
.O sistema preserva as informações entre as execuções por meio do arquivo CSV
.Para fazer o backup, é suficiente copiar o arquivo alunos.csv

 Contribuição
Este projeto foi criado como parte de um trabalho acadêmico sobre Princípios de Construção de Algoritmos, ilustrando a aplicação de:
.Estruturas de dados (DataFrames)
.Persistência em documentos
.Interface de comando de texto
.Confirmação de entrada
.Gestão de estado

 Desenvolvido como um projeto prático de algoritmos
Utilizando Python e Pandas para gerenciamento de dados educacionais no Github
