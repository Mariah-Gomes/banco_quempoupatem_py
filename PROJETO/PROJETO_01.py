from shutil import copyfile
from datetime import datetime
def menu(): # Função menu com todas as opções que o usuário pode acessar no banco
    # Abaixo estão os prints para aparecer na tela do usuário escolher a opção que deseja
    print('Menu:')
    print('1 - Novo Cliente')
    print('2 - Apaga Cliente')
    print('3 - Débito')
    print('4 - Depósito')
    print('5 - Extrato')
    print('6 - Transferência Entre Contas')
    print('7 - Cartão')
    print('0 - Sair')
    x = str(input('Digite a opção que deseja acessar do menu: ')) # Variável para o usuário colocar a opção que deseja acessar no banco
    # A seguir está as condições para encaminhar o cliente para as funções da funcionalidade que deseja 
    if x == '1 - Novo Cliente':
        novo_cliente()
    elif x == '2 - Apaga Cliente':
        apaga_cliente()
    elif x == '3 - Débito':
        debito()
    elif x == '4 - Depósito':
        deposito()
    elif x == '5 - Extrato':
        extrato()
    elif x == '6 - Transferência Entre Contas':
        transferencia_entre_contas()
    elif x == '7 - Cartão':
        cartao()
    elif x == '0 - Sair':
        sair() 
    else:
        print('Operação Inválida')

    while x != "0 - Sair":
        if x != "0 - Sair":
            menu()
        else:
            break

# Logo abaixo está a primeira funcionalidade do menu para cadastrar um novo cliente.
def novo_cliente():
    # Abre um arquivo para salvar as informações do cliente:
    arquivo = open("Projeto.txt", "w")
    # Abaixo está todos os dados solicitados para criar um novo cliente
    nome = str(input('Digite seu nome: '))
    cpf = str(input('Digite seu CPF: '))
    tipo_de_conta = str(input('Digite o tipo da sua conta: '))
    valor_inicial_da_conta = str(input('Digite o valor inicial de sua conta: '))
    senha = str(input('Digite sua senha: '))
    # Import de biblioteca para colocar hora nas operações
    data_atual = datetime.now()
    data = data_atual.strftime('%d/%m/%Y %H:%M')
    # Escrevendo os dados do usuário no arquivo
    arquivo.write("Nome: %s; CPF: %s; Tipo de conta: %s; Valor: %s; Senha: %s;\n" % (nome, cpf, tipo_de_conta, valor_inicial_da_conta, senha))
    # Fechando o arquivo
    arquivo.close()    
    # Abre o arquivo
    arquivo = open('Extrato.txt', 'w')
    # Fecha o arquivo
    arquivo.close()
    # Abre o arquivo
    arquivo = open('Extrato.txt', 'a')
    # Escreve as informações no arquivo
    arquivo.write("Data: %s, %s\n" % (data, valor_inicial_da_conta))
    # Fecha o arquivo
    arquivo.close()
    # Fazendo o loop para acrescentar informações de outros clientes
    while nome != "":
        # Usando a condição do nome do cliente para fazer o loop ou parar
        nome = str(input('Digite seu nome: '))
        if nome == "":
            break
        else:
            # Abre o arquivo já existente e lê as informações
            arquivo = open("Projeto.txt", "r")
            # Condição para ler todas as linhas do arquivo
            linha = arquivo.readlines()
            # Acrescentando informações do novo cliente
            cpf = str(input('Digite seu CPF: '))
            tipo_de_conta = input('Digite o tipo da sua conta: ')
            valor_inicial_da_conta = input('Digite o valor inicial de sua conta: ')
            senha = input('Digite sua senha: ')
            # Acrescentando uma linha com informações novas
            linha.append("Nome: %s; CPF: %s; Tipo de conta: %s; Valor: %s; Senha: %s;\n" % (nome, cpf, tipo_de_conta, valor_inicial_da_conta, senha))
            # Abrindo o arquivo para escrever as informações novas
            arquivo = open('Projeto.txt', 'w') 
            # Escrevendo uma linha no arquivo com informações novas de outro cliente
            arquivo.writelines(linha)
            # Fechando o arquivo    
            arquivo.close()

# Abaixo está a função apaga cliente que serve para apagar clientes.
def apaga_cliente():
    # Criando uma lista vazia para adicionar itens mais tarde nela
    clientes = []
    # Colocando uma variável para receber o CPF do cliente que deseja apagar
    cpf = str(input('Digite seu CPF: '))
    # Convertendo a variável para ficar igual a linha do arquivo que está salvo os clientes
    cpf = 'CPF: %s' % (cpf)
    # Abrindo o arquivo que está salvo com as informações dos clientes
    arquivo = open("Projeto.txt", "r")
    # Lendo linha por linha do arquivo
    l = arquivo.readlines()
    # Salvando as linhas em uma variável
    for linha in l:
        # Fechando o arquivo
        arquivo.close()
        copyfile('Projeto.txt', 'Projeto1.txt')
        # Fazendo o split e separando as informações que uma linha do arquivo tem por ";"
        separacao = linha.split(";")
        # Se a segunda informação da linha for diferente do CPF digitado entra na condição
        if separacao[1] != cpf:
            # Salva todas as informações do arquivo com excessão da linha que possui o mesmo CPF digitado
            clientes.append(linha)
    # Para escrever as informações no arquivo precisamos transformar os elementos da lista em strings
    for c in clientes:
        # Abre o arquivo para escrever
        arquivo = open("Projeto.txt", "w")
        # Escreve as informações no arquivo
        arquivo.write(c)
        # Fecha o arquivo
        arquivo.close()
    
def debito():
    # Criando uma lista vazia para adicionar itens mais tarde nela
    clientes = []
    cli = []
    cl = []
    # Colocando uma variável para receber o CPF do cliente que deseja realizar o débito
    cpf = str(input('Digite seu CPF: '))
    # Colocando uma variável para receber o valor que o cliente deseja débitar de sua conta
    valor  = float(input('Digite o valor que deseja: '))
    # Colocando uma variável para receber a senha do cliente que deseja realizar o depósito
    senha = str(input('Digite sua senha: '))
    # Convertendo a variável para ficar igual a linha do arquivo que está salvo os clientes
    cpf = ' CPF: %s' % (cpf)
    # Convertendo a variável para ficar igual a linha do arquivo que está salvo os clientes
    senha = ' Senha: %s' % (senha)
    # Import de biblioteca para colocar hora nas operações
    data_atual = datetime.now()
    data = data_atual.strftime('%d/%m/%Y %H:%M')
    # Abre o arquivo para ler
    arquivo = open("Projeto.txt", "r")
    # Lê linha por linha do arquivo
    l = arquivo.readlines()
    # Salvando as linhas em uma variável
    for linha in l:
        # Fecha o arquivo
        arquivo.close()
        # Fazendo o split e separando as informações que uma linha do arquivo tem por ";"
        separacao = linha.split(";")
        # Se a segunda informação da linha for igual do CPF e a quinta informação da linha for igual a senha digitado entra na condição
        if (separacao[1] == cpf) and (separacao[4] == senha):
            # Se para verificar o tipo de conta
            if (separacao[2] == ' Tipo de conta: plus'):
                # Faz um split e separa a parte escrita a do valor da conta
                dados = separacao[3].split(":")
                # Faz a diferença do valor antigo da conta com o valor que deseja fazer o débito
                valor_final = float(dados[1]) - float(0.3 * valor)
                # O novo valor da separação será com o escrito anterior mais o valor final
                separacao[3] = dados[0] + ":" + " " + str(valor_final)
                # Reescrevendo a linha do cliente que depósitou um valor em sua conta
                clientes.append(separacao[0] + ';' + separacao[1] + ';' + separacao[2] + ';' + separacao[3] + ';' + separacao[4] + ';' + "\n")
                cli.append(separacao[3])
            # Se para verificar o tipo de conta
            elif (separacao[2] == ' Tipo de conta: comum'):
                # Faz um split e separa a parte escrita a do valor da conta
                dados = separacao[3].split(":")
                # Faz a diferença do valor antigo da conta com o valor que deseja fazer o débito
                valor_final = float(dados[1]) - float(0.5 * valor)
                # O novo valor da separação será com o escrito anterior mais o valor final
                separacao[3] = dados[0] + ":" + " " + str(valor_final)
                # Reescrevendo a linha do cliente que depósitou um valor em sua conta
                clientes.append(separacao[0] + ';' + separacao[1] + ';' + separacao[2] + ';' + separacao[3] + ';' + separacao[4] + ';' + "\n")
                cl.append(separacao[2])
                cli.append(separacao[3])
        else:
            # Adiciona a linha igualzinha sem fazer alterações
            clientes.append(linha)
    # Abre o arquivo
    arquivo = open('Projeto.txt', 'w')
    # Fecha o arquivo
    arquivo.close()
    # Abre o arquivo
    arquivo = open('Extrato.txt', 'w')
    # Fecha o arquivo
    arquivo.close()
    for c in clientes:
        # Abre o arquivo
        arquivo = open('Projeto.txt', 'a')
        # Escreve as informações no arquivo
        arquivo.write(c)
        # Fecha o arquivo
        arquivo.close()
    for cll in cl:
        # Se para verificar o tipo de conta
        if cll == " Tipo de conta: plus":
            for ci in cli:
                tarifa = 0.3
                # Abre o arquivo
                arquivo = open('Extrato.txt', 'a')
                # Escreve as informações no arquivo
                arquivo.write("Data: %s  - %s  Tarifa: %s  Saldo: %s\n" % (data, valor, tarifa, ci))
                # Fecha o arquivo
                arquivo.close()
        # Se para verificar o tipo de conta
        elif cll == " Tipo de conta: comum":
            for ci in cli:
                tarifa = 0.5
                # Abre o arquivo
                arquivo = open('Extrato.txt', 'a')
                # Escreve as informações no arquivo
                arquivo.write("Data: %s  - %s  Tarifa: %s  Saldo: %s\n" % (data, valor, tarifa, ci))
                # Fecha o arquivo
                arquivo.close()       

def deposito():
    # Criando uma lista vazia para adicionar itens mais tarde nela
    clientes = []
    cli = []
    # Colocando uma variável para receber o CPF do cliente que deseja realizar o depósito
    cpf = str(input('Digite seu CPF: '))
    # Convertendo a variável para ficar igual a linha do arquivo que está salvo os clientes
    cpf = ' CPF: %s' % (cpf)
    # Variável para digitar o valor que deseja inserir na conta
    valor  = float(input('Digite o valor que deseja: '))
    # Import de biblioteca para colocar hora nas operações
    data_atual = datetime.now()
    data = data_atual.strftime('%d/%m/%Y %H:%M')
    # Abre o arquivo para ler
    arquivo = open("Projeto.txt", "r")
    # Lê linha por linha do arquivo
    l = arquivo.readlines()
    # Fecha o arquivo
    arquivo.close()
    # Salvando as linhas em uma variável
    for linha in l:
        # Fazendo o split e separando as informações que uma linha do arquivo tem por ";"
        separacao = linha.split(";")
        # Se a segunda informação da linha for igual do CPF digitado entra na condição
        if separacao[1] == cpf:
            # Faz um split e separa a parte escrita a do valor da conta
            dados = separacao[3].split(":")
            # Junta o valor antigo da conta com o valor que deseja fazer o depósito
            valor_final = float(dados[1]) + float(valor)
            # O novo valor da separação será com o escrito anterior mais o valor final
            separacao[3] = dados[0] + ":" + " " + str(valor_final)
            # Reescrevendo a linha do cliente que depósitou um valor em sua conta
            clientes.append(separacao[0] + ';' + separacao[1] + ';' + separacao[2] + ';' + separacao[3] + ';' + separacao[4] + ';' + "\n")
            cli.append(separacao[3])
        # Se a segunda informação da linha for diferente do CPF digitado entra na condição
        else:
            # Adiciona a linha igualzinha sem fazer alterações
            clientes.append(linha)
    # Abre o arquivo
    arquivo = open('Projeto.txt', 'w')
    # Fecha o arquivo
    arquivo.close()
    # Abre outro arquivo
    arquivo = open('Extrato.txt', 'w')
    # Fecha outro arquivo
    arquivo.close()
    # Para escrever as informações no arquivo precisamos transformar os elementos da lista em strings
    for c in clientes:
        # Abre o arquivo para adicionar informações
        arquivo = open('Projeto.txt', 'a')
        # Escreve as informações no arquivo
        arquivo.write(c)
        # Fecha o arquivo
        arquivo.close()
    # Para escrever as informações no arquivo precisamos transformar os elementos da lista em strings
    for ci in cli:
        tarifa = 0.00
        # Abre o arquivo para adicionar informações
        arquivo = open('Extrato.txt', 'a')
        # Escreve as informações no arquivo
        arquivo.write("Data: %s  + %s  Tarifa: %s  Saldo: %s\n" % (data, valor, tarifa, ci))
        # Fecha o arquivo
        arquivo.close()
        
def extrato():
    # Criando uma lista vazia para adicionar itens mais tarde nela
    clientes = []
    cli = []
    # Colocando uma variável para receber o CPF do cliente que deseja ver seu extrato
    cpf = int(input('Digite seu CPF: '))
    # Colocando uma variável para receber a senha do cliente que deseja ver seu extrato
    senha = int(input('Digite sua senha: '))
    # Convertendo a variável para ficar igual a linha do arquivo que está salvo os clientes
    cpf = ' CPF: %s' % cpf
    # Convertendo a variável para ficar igual a linha do arquivo que está salvo os clientes
    senha = ' Senha: %s' % senha
    # Import de biblioteca para colocar hora nas operações
    data_atual = datetime.now()
    data = data_atual.strftime('%d/%m/%Y %H:%M')
    # Abre o arquivo para ler
    arquivo = open("Projeto.txt", "r")
    # Lê linha por linha do arquivo
    l = arquivo.readlines()
    # Fecha o arquivo
    arquivo.close()
    arquivo = open("Extrato.txt", "r")
    li = arquivo.readlines()
    arquivo.close()
    # Salvando as linhas em uma variável
    for linha in l:
        # Fazendo o split e separando as informações que uma linha do arquivo tem por ";"
        separacao = linha.split(";")
        # Se a segunda informação da linha for igual do CPF digitado e a quinta informação da linha for igual a senha digitada entra na condição
        if (separacao[1] == cpf) and (separacao[4] == senha):
            # Reescrevendo a linha do cliente que está querendo ver o extrato de sua conta
            clientes.append(separacao[0] + '\n' + separacao[1] + '\n' + separacao[2] + '\n')
            cli.append(li)
    # Abre o arquivo
    arquivo = open('Extrato.txt', 'w')
    # Fecha o arquivo
    arquivo.close()
    for c in clientes:
        # Abre o arquivo
        arquivo = open('Extrato.txt', 'a')
        # Escreve as informações no arquivo
        arquivo.write(c)
        # Fecha o arquivo
        arquivo.close()
    for ci in cli:
        # Abre o arquivo
        arquivo = open('Extrato.txt', 'a')
        # Escreve as informações no arquivo
        arquivo.writelines(ci)
        # Fecha o arquivo
        arquivo.close()

def transferencia_entre_contas():
    # Criando uma lista vazia para adicionar itens mais tarde nela
    clientes = []
    am = []
    cl = []
    lih = []
    # Colocando uma variável para receber o CPF do cliente que deseja realizar a transferência
    cpf = int(input('Digite seu CPF: '))
    # Convertendo a variável para ficar igual a linha do arquivo que está salvo os clientes
    cpf = ' CPF: %s' % (cpf)
    # Colocando uma variável para receber a senha do cliente que deseja realizar a transferência
    senha = int(input('Digite sua senha: '))
    # Convertendo a variável para ficar igual a linha do arquivo que está salvo os clientes
    senha = ' Senha: %s' % (senha)
    # Colocando uma variável para receber o CPF do cliente que deseja receber a transferência
    cpf_destino = int(input('Digite o CPF da pessoa que irá receber: '))
    # Convertendo a variável para ficar igual a linha do arquivo que está salvo os clientes
    cpf_destino = ' CPF: %s' % (cpf_destino)
    # Colocando uma variável para receber o valor do cliente que deseja fazer a transferência
    valor = float(input('Digite o valor para a transferência: '))
    # Import de biblioteca para colocar hora nas operações
    data_atual = datetime.now()
    data = data_atual.strftime('%d/%m/%Y %H:%M')
    # Abre o arquivo para ler
    arquivo = open("Projeto.txt", "r")
    # Lê linha por linha do arquivo
    l = arquivo.readlines()
    # Fecha o arquivo
    arquivo.close()
    # Salvando as linhas em uma variável
    for linha in l:
        # Fazendo o split e separando as informações que uma linha do arquivo tem por ";"
        separacao = linha.split(";")
        # Se a segunda informação da linha for igual do CPF digitado e a quinta informação for igual a senha digitada entra na condição
        if (separacao[1] == cpf) and (separacao[4] == senha):
            if (separacao[2] == ' Tipo de conta: plus'):
                # Faz um split e separa a parte escrita a do valor da conta
                dados = separacao[3].split(":")
                # Faz a diferença do valor antigo da conta com o valor que deseja fazer a transferência
                valor_final = float(dados[1]) - float(0.3 * valor)
                # O novo valor da separação será com o escrito anterior mais o valor final
                separacao[3] = dados[0] + ":" + " " + str(valor_final)
                # Reescrevendo a linha do cliente que realizou uma transferência em sua conta
                clientes.append(separacao[0] + ';' + separacao[1] + ';' + separacao[2] + ';' + separacao[3] + ';' + separacao[4] + ';' + "\n")
            elif (separacao[2] == ' Tipo de conta: comum'):
                # Faz um split e separa a parte escrita a do valor da conta
                dados = separacao[3].split(":")
                # Faz a diferença do valor antigo da conta com o valor que deseja fazer a transferência
                valor_final = float(dados[1]) - float(0.5 * valor)
                # O novo valor da separação será com o escrito anterior mais o valor final
                separacao[3] = dados[0] + ":" + " " + str(valor_final)
                # Reescrevendo a linha do cliente que realizou uma transferência em sua conta
                clientes.append(separacao[0] + ';' + separacao[1] + ';' + separacao[2] + ';' + separacao[3] + ';' + separacao[4] + ';' + "\n")
        # Se a segunda informação da linha for igual do CPF digitado entra na condição
        elif (separacao[1] == cpf_destino):
            # Faz um split e separa a parte escrita a do valor da conta
            dados = separacao[3].split(":")
            # Junta o valor antigo da conta com o valor que recebeu da transfeência
            valor_final = float(dados[1]) + float(valor)
            # O novo valor da separação será com o escrito anterior mais o valor final
            separacao[3] = dados[0] + ":" + " " + str(valor_final)
            # Reescrevendo a linha do cliente que recebeu uma transferência em sua conta
            clientes.append(separacao[0] + ';' + separacao[1] + ';' + separacao[2] + ';' + separacao[3] + ';' + separacao[4] + ';' + "\n")
            cl.append(valor_final)
            lih.append(separacao[1] + separacao[4])
        else:
            # Reescrevendo a linha do cliente que não realizou e nem recebeu transferência um valor em sua conta
            clientes.append(linha)
    # Abre o arquivo
    arquivo = open('Projeto.txt', 'w')
    # Fecha o arquivo
    arquivo.close()
    # Abre o arquivo
    arquivo = open('Extrato.txt', 'w')
    # Fecha o arquivo
    arquivo.close()
    for c in clientes:
        # Abre o arquivo
        arquivo = open('Projeto.txt', 'a')
        # Escreve as informações no arquivo
        arquivo.write(c)
        # Fecha o arquivo
        arquivo.close()
    for ha in lih:
        # Se a segunda informação da linha for igual do CPF digitado e a última informação for igual a senha digitada entra na condição
        if (ha == cpf) and (ha == senha):
            for ma in am:
                if (ma == ' Tipo de conta: comum'):
                    for cli in cl:
                        tarifa = 0.5
                        # Abre o arquivo
                        arquivo = open('Extrato.txt', 'a')
                        # Escreve as informações no arquivo
                        arquivo.write("Data: %s  - %s  Tarifa: %s  Saldo: %s\n" % (data, valor, tarifa, cli))
                        # Fecha o arquivo
                        arquivo.close()
                elif (ma == ' Tipo de conta: plus'):
                    for cli in cl:
                        tarifa = 0.3
                        # Abre o arquivo
                        arquivo = open('Extrato.txt', 'a')
                        # Escreve as informações no arquivo
                        arquivo.write("Data: %s  - %s  Tarifa: %s  Saldo: %s\n" % (data, valor, tarifa, cli))
                        # Fecha o arquivo
                        arquivo.close()
        # Se a segunda informação da linha for igual do CPF digitado entra na condição
        elif (ha == cpf_destino):
            for cli in cl:
                tarifa = 0.00
                # Abre o arquivo
                arquivo = open('Extrato.txt', 'a')
                # Escreve as informações no arquivo
                arquivo.write("Data: %s  + %s  Tarifa: %s  Saldo: %s\n" % (data, valor, tarifa, cli))
                # Fecha o arquivo
                arquivo.close()

def cartao():
    # Colocando uma variável para receber o tipo de cartão que o cliente que deseja cadastrar 
    tipo_de_cartao = str(input('Digite o tipo do cartão (débito ou crédito): '))
    # Colocando uma variável para receber o CPF do cliente que deseja cadastrar o cartão
    cpf = str(input('Digite seu CPF: '))
    # Convertendo a variável para ficar igual a linha do arquivo que está salvo os clientes
    cpf = ' CPF: %s' % (cpf)
    # Colocando uma variável para receber a data que o cliente que deseja pagar a fatura do cartão
    melhor_data_de_vencimento = str(input('Digite a melhor data de vencimento do cartão: '))
    # Abre o arquivo
    arquivo = open("Projeto.txt", "r")
    # Lê linha por linha do arquivo
    l = arquivo.readlines()
    # Fecha o arquivo
    arquivo.close()
    # Salvando as linhas em uma variável
    for linha in l:
        # Fazendo o split e separando as informações que uma linha do arquivo tem por ";"
        separacao = linha.split(";")
        # Se a segunda informação da linha for igual do CPF digitado entra na condição
        if (separacao[1] == cpf):
            # Abre o arquivo
            arquivo = open('Cartões.txt', 'w')
            # Fecha o arquivo
            arquivo.close()
            # Abre o arquivo
            arquivo = open("Cartões.txt", "a")
            # Escreve as informações no arquivo
            arquivo.write('%s; Tipo de cartão: %s; Data de vencimento da fatura: %s\n' % (cpf, tipo_de_cartao, melhor_data_de_vencimento))
            # Fecha o arquivo
            arquivo.close()

def sair():
# Abaixo está uma variável com a mensagem que o cliente vai ver quando sair
    mensagem = "OBRIGADA POR UTILIZAR OS SERVIÇOS"
    # Retorna a mensagem quando precionar a função sair
    return (mensagem)

# Logo abaixo está o menu que aparece para o cliente as opções para ele selecionar uma
menu()
# Print da função sair para sair do loop do menu
print(sair())