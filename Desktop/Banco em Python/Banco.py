from datetime import datetime

# Menu
def menu():
    print('MENU:')
    print('1 - Novo Cliente')
    print('2 - Apaga Cliente')
    print('3 - Listar Cliente')
    print('4 - Débito Cliente')
    print('5 - Depósito Cliente')
    print('6 - Extrato')
    print('7 - Transferência Entre Contas')
    print('8 - Cadastro de Cartões')
    print('9 - Sair')

# Listas que utilizei
clientesTotal = []
extratos = []
extratoCliente = []
cartoes = []

# Data e Hora no extrato
dataEhoraAtual = datetime.now()
modeloBomHoraEData = dataEhoraAtual.strftime("%A %d %B %y %I:%M")

# Função para cadastrar novo cliente
def novo_cliente():
    nome = str(input('Digite seu nome: '))
    cpf = int(input('Digite seu CPF: '))

    # Procurar se o cliente já está cadastrado          
    for clienteProcurado in clientesTotal:
        if cpf in clienteProcurado:
            print('Esse CPF já está cadastrado')
            return 0

    conta = str(input('Digite o tipo da sua conta (comum ou plus): '))
    valorInicial = float(input('Digite o valor inicial da sua conta: '))
    senha = int(input('Digite a sua senha: '))
    
    # Cadastrando o novo cliente
    clienteNovo = [nome, cpf, conta, valorInicial, senha]
    clientesTotal.append(clienteNovo)
    print('Cliente cadastrado com sucesso\n')

    # Salvando o novo cliente no arquivo    
    arquivo = open('clientes.txt', 'a')
    arquivo.write(str(clienteNovo))
    arquivo.write('\n')
    arquivo.close()
    
    #Extrato
    extratoCliente = [nome, cpf, senha, modeloBomHoraEData, valorInicial]
    extratos.append(extratoCliente)
    
    #Cartão
    cartaoCliente = [nome, cpf, senha]
    cartoes.append(cartaoCliente)

# Função para apagar um cliente
def apaga_cliente():
    cpf = int(input('Digite seu CPF: '))
    senha = int(input('Digite a sua senha: '))
    
    # Procurar se o cliente existe
    for clienteProcurado in clientesTotal:
        if cpf in clienteProcurado:
            if senha in clienteProcurado:
                #Indíce de Remoção
                posicaoLista = clientesTotal.index(clienteProcurado)
                
                #Achando a linha
                arquivo = open('clientes.txt', 'r')
                achandoLinha = arquivo.readlines()
                arquivo.close()
                
                pulandoLinha = 0            
                
                arquivo = open('clientes.txt', 'w')
                
                # Reescrevendo os clientes 
                for linha in achandoLinha:
                    if pulandoLinha != posicaoLista:
                        arquivo.write(linha)
                    pulandoLinha += 1       
                    
                # Apagando o cliente da lista    
                clienteProcurado.clear()
                arquivo.close() 
                print('Cliente apagado com sucesso')
                return 0
            
            else:
                print('Senha Incorreta')
                return 0
        
    print('Cliente não está no sistema')

# Função para listar os clientes do banco        
def listar_cliente():
    clientesAtualizados = list(filter(None, clientesTotal))
    for clientesMostrar in clientesAtualizados:
        print('----------')
        print('Nome: ', clientesMostrar[0])
        print('CPF: ', clientesMostrar[1])
        print('Tipo de Conta: ', clientesMostrar[2])
        print('Valor da Conta: ', clientesMostrar[3])
        print('Senha: ', clientesMostrar[4])
        print('----------')
        
# Função para Débito    
def debito_cliente():
    cpf = int(input('Digite seu CPF: '))
    senha = int(input('Digite a sua senha: '))
    valor = float(input('Digite o quanto deseja debitar: '))
    
    # Função para procurar o cliente
    for clienteProcurado in clientesTotal:
        if cpf in clienteProcurado:
            if senha in clienteProcurado:
                break
            else:
                print('Senha incorrreta')
                return 0
    else:
        print('Cliente não está no sistema')
        return 0
    
    # Entra no valor de juros do cliente        
    if clienteProcurado[2] == 'comum':
        valorAtual = (clienteProcurado[3] - valor) * 0.03
        valorAtual = round(valorAtual, 2)
        if (valorAtual < clienteProcurado[3]) == False:
            print('Saldo insuficiente')
            return 0
        else:
            clienteProcurado[3] = clienteProcurado[3] - valorAtual
            
    elif clienteProcurado[2] == 'plus':
        valorAtual = (clienteProcurado[3] - valor) * 0.05
        valorAtual = round(valorAtual, 2)
        if (valorAtual < clienteProcurado[3]) == False:
            print('Saldo insuficiente')
            return 0
        else:
            clienteProcurado[3] = clienteProcurado[3] - valorAtual

    #Extrato
    for extratoProcurado in extratos:
        if cpf in extratoProcurado:
            if senha in extratoProcurado:
                break
                
    extratoProcurado.append(modeloBomHoraEData)
    extratoProcurado.append(valorAtual) 

    #Arquivos
    arquivo = open('clientes.txt', 'w')
    for linha in clientesTotal:
        arquivo.write(str(linha))
        arquivo.write('\n')
    arquivo.close()     

    print('Debito realizado')
    
# Função para Depósito    
def deposito_cliente():
    cpf = int(input('Digite seu CPF: '))
    senha = int(input('Digite a sua senha: '))
    
    # Função para procurar o cliente
    for clienteProcurado in clientesTotal:
        if cpf in clienteProcurado:
            if senha in clienteProcurado:
                break
            else:
                print('Senha incorreta')
                return 0
    else:
        print('Cliente não está no sistema')
        return 0
    
    valor = float(input('Digite o quanto deseja depositar: '))
    valor = round(valor, 2)
    
    clienteProcurado[3] = clienteProcurado[3] + valor
    
    #Extrato
    for extratoProcurado in extratos:
        if cpf in extratoProcurado:
            if senha in extratoProcurado:
                break
        
    extratoProcurado.append(modeloBomHoraEData)
    extratoProcurado.append(valor)

    #Arquivos
    arquivo = open('clientes.txt', 'w')
    for linha in clientesTotal:
        arquivo.write(str(linha))
        arquivo.write('\n')
    arquivo.close()    
    
    print('Deposito realizado')

# Função para Extrato    
def extrato():
    cpf = int(input('Digite seu CPF: '))
    senha = int(input('Digite a sua senha: '))
    
    # Função para procurar o cliente
    for clienteProcurado in clientesTotal:
        if cpf in clienteProcurado:
            if senha in clienteProcurado:
                break
            else:
                print('Senha Incorreta')
                return 0
    else:
        print('Esse cliente não está cadastrado')
        return 0
    
    # Printa os dados do cliente
    print('----------')
    print('Nome: ', clienteProcurado[0])
    print('CPF: ', clienteProcurado[1])
    print('----------')
    
    # Arquivos
    arquivo = open('extrato.txt', 'w')
    arquivo.write('----------')
    arquivo.write('\n')
    arquivo.write('Nome: ')
    arquivo.write(str(clienteProcurado[0]))
    arquivo.write('\n')
    arquivo.write('CPF: ')
    arquivo.write(str(clienteProcurado[1]))
    arquivo.write('\n')
    arquivo.write('----------')
    arquivo.write('\n')

    contPar = 3
    contImpar = 4
    cont = 3  
    
    # Função para procurar o extrato
    for extratoProcurado in extratos:
        if cpf in extratoProcurado:
            if senha in extratoProcurado: 
                break
          
    while cont < len(extratoProcurado):
        print('----------')
        print(extratoProcurado[contPar])
        print(extratoProcurado[contImpar])
        print('----------')
        
        # Arquivos
        arquivo.write('----------')
        arquivo.write('\n')
        arquivo.write(str(extratoProcurado[contPar]))
        arquivo.write('\n')
        arquivo.write(str(extratoProcurado[contImpar]))
        arquivo.write('\n')
        arquivo.write('----------')
        arquivo.write('\n')

        contPar = contPar + 2
        contImpar = contImpar + 2
        cont = 2 + cont
        
    print('----------')    
    print('Saldo Atual: ', clienteProcurado[3])
    print('----------')
        
    # Arquivos
    arquivo.write('----------')
    arquivo.write('\n')
    arquivo.write('Saldo Atual: ')
    arquivo.write(str(clienteProcurado[3]))
    arquivo.write('\n')
    arquivo.write('----------')
     
    arquivo.close() 
    
def transferencia():
    cpfOrigem = int(input('Digite o CPF de origem: '))
    senha = int(input('Digite a sua senha: '))
    valor = float(input('Digite o valor da transferência: '))
    cpfDestino = int(input('Digite o CPF da pessoa que irá receber: '))
    valor = round(valor, 2)
    
    # Função para procurar o cliente
    for clienteProcuradoUm in clientesTotal:
        if cpfOrigem in clienteProcuradoUm:
            if senha in clienteProcuradoUm:
                break
            else:
                print('Senha Incorreta')
    else:
        print('Cliente não encontrado que possui o CPF de origem')
        return 0
    
    # Função para procurar o cliente
    for clienteProcuradoDois in clientesTotal:
        if cpfDestino in clienteProcuradoDois:
            break
    else:
        print('Cliente não encontrado')
        return 0
    
    # Entra no valor de juros do cliente     
    if clienteProcuradoUm[2] == 'comum':
        valorAtual = (clienteProcuradoUm[3] - valor) * 0.03
        valorAtual = round(valorAtual, 2)
        if (valorAtual < clienteProcuradoUm[3]) == False:
            print('Saldo insuficiente')
            return 0
        else:
            clienteProcuradoUm[3] = clienteProcuradoUm[3] - valorAtual
            clienteProcuradoDois[3] = clienteProcuradoDois[3] + valor
            
    elif clienteProcuradoUm[2] == 'plus':
        valorAtual = (clienteProcuradoUm[3] - valor) * 0.05
        valorAtual = round(valorAtual, 2)
        if (valorAtual < clienteProcuradoUm[3]) == False:
            print('Saldo insuficiente')
            return 0
        else:
            clienteProcuradoUm[3] = clienteProcuradoUm[3] - valorAtual
            clienteProcuradoDois[3] = clienteProcuradoDois[3] + valor
            
    #Extrato
    for extratoProcuradoUm in extratos:
        if cpfOrigem in extratoProcuradoUm:
            if senha in extratoProcuradoUm:
                break
        
    extratoProcuradoUm.append(modeloBomHoraEData)
    extratoProcuradoUm.append(valor)

    for extratoProcuradoDois in extratos:
        if cpfDestino in extratoProcuradoDois:
            break
        
    extratoProcuradoDois.append(modeloBomHoraEData)
    extratoProcuradoDois.append(valor)
    
    #Arquivos
    arquivo = open('clientes.txt', 'w')
    for linha in clientesTotal:
        arquivo.write(str(linha))
        arquivo.write('\n')
    arquivo.close()    
    
    print('Transação Realizada')
    
# Função para cadastrar cartão                
def cartao():
    cpf = int(input('Digite seu CPF: '))
    senha = int(input('Digite a sua senha: '))
    tipoDeCartao = str(input('Digite se seu cartão é débito ou crédito: '))
    if tipoDeCartao == 'debito':
        vencimento = 'Esse cartao nao possui data de vencimento de fatura'
    elif tipoDeCartao == 'credito':
        vencimento = int(input('Digite o dia do vencimento do seu cartão: '))
    else:
        print('Esse cartao nao temos no banco')
        return 0
    
    # Função para procurar o cliente
    for cartaoProcurado in cartoes:
        if cpf in cartaoProcurado:
            if senha in cartaoProcurado:
                break
            else:
                print('Senha Incorreta')
                return 0
    else:
        print('Cliente não encontrado')

    cartaoProcurado.append(tipoDeCartao)
    cartaoProcurado.append(vencimento)
    
    #Arquivos
    arquivo = open('cartoes.txt', 'a')
    arquivo.write('Nome: ')
    arquivo.write(str(cartaoProcurado[0]))
    arquivo.write('\n')
    arquivo.write('CPF: ')
    arquivo.write(str(cartaoProcurado[1]))
    arquivo.write('\n')
    arquivo.write('Senha: ')
    arquivo.write(str(cartaoProcurado[2]))
    arquivo.write('\n')
    arquivo.write('Tipo de Cartao: ')
    arquivo.write(str(cartaoProcurado[3]))
    arquivo.write('\n')
    arquivo.write('Vencimento: ')
    arquivo.write(str(cartaoProcurado[4]))
    arquivo.write('\n')
    arquivo.write('----------')
    arquivo.write('\n')
    arquivo.write('----------')
    arquivo.write('\n')
    
    print('Cartão cadastrado com sucesso')

# Função para Sair    
def sair():
    print('Sistema Encerrado')

# Loop para o menu
while True:
    menu()
    variavel = int(input('Digite o que deseja acessar: ' ))
    if variavel == 1:
        novo_cliente()
    elif variavel == 2:
        apaga_cliente()
    elif variavel == 3:
        listar_cliente()
    elif variavel == 4:
        debito_cliente()
    elif variavel == 5:
        deposito_cliente()
    elif variavel == 6:
        extrato()
    elif variavel == 7:
        transferencia()
    elif variavel == 8:
        cartao()
    elif variavel == 9:
        sair()
        break
    else:
        print('Por favor, escolha um número que corresponde as opções a cima')