from os import system #Essa função serve para dar um comando de limpar o terminal
from time import sleep #essa função serve para fazer o programa aguardar um tempo

#fila normal
filaNormal = []
#fila preferencial
filaPreferencial = []
#Encaminhamento para outro hospital
filaEncaminhamento = [] 

#tipos de atendimentos
#essa função checa se o atendimento é grave e retorna True ou False
def atendimentoGrave():
    system('cls')
    resultado = respostaValida("Seu atendimento é grave?[s/n]: ", "s", "n")
    if resultado.lower() == "s":
        return True
    else:
        return False

#checando se ha leitos disponiveis
#essa função vai dizer se o pacience sera encaminhado, retornando True or False
def encaminhamento(leitosDisponiveis):
    if leitosDisponiveis == 0:
        return True
    else:
        return False

#validar resposta
#Essa função valida resposta e possui tres parametros,
#o primeiro é um string que sera mostrado no terminal,
#o segundo e terceiro são os parametros para indicar quais
#as duas opções validas para entrada
def respostaValida(pergunta, opcaoUm, opcaoDois):
    repetir = True
    while repetir:
        system('cls')
        opcao = input(pergunta)
        if opcao.lower() == opcaoUm or opcao.lower() == opcaoDois:
            repetir = False
            return opcao
        else:
            print("Resposta inválida!")
            sleep(0.5)


#menor de idade?
#essa função checa se o paciente é adulto
def adulto(idade):
    if idade >= 18:
        return True
    else:
        return False

 
#Fazendo agendamento agendamento
#função para fazer o agendamento tem como parametro True or False
def agendamento(atendimentoGrave):
    system('cls')
    nome = input("nome: ")
    idade = int(input("Idade: "))
    senhaAtendimento = (len(filaNormal) + 1) 
    sexo = respostaValida("Sexo biológico[M/F]: ", "m", "f")

    if adulto(idade):
        #salvando as variavies de dados do paciente dentro da lista paciente
        paciente = [nome, idade, sexo]
    else:
        nomeMae = input("Nome da mae: ")
        paciente = [nome, idade, sexo, nomeMae]
    
    if atendimentoGrave:
        if encaminhamento(2 - len(filaPreferencial)):
            paciente.append("urgente")
            filaEncaminhamento.append(paciente)
            print("Não possuimos leitos disponiveis, você será encaminhado para outro posto de saúde.")
            sleep(1)
        else:
            paciente.append("atendido")
            filaPreferencial.append(paciente)
            print("Você será atendido agora")
            sleep(1)
    else:
        paciente.append(senhaAtendimento)
        filaNormal.append(paciente)
        print(f'Aguarde na fila, sua senha é: {len(filaNormal)}')
        sleep(1)


#checar a fila de atendimento
def checarFila(fila, tipo):
    print(f'\n{tipo.upper()}')
    for paciente in fila:
        if paciente[1] >= 18:
            print(f'Nome: {paciente[0]}\nIdade: {paciente[1]}')
            if paciente[2] == 'm':
                print(f'Sexo: masculino')
            else:
                print(f'Sexo: femenino')
            print(f'Senha: {paciente[3]}')
        else:
            print(f'Nome: {paciente[0]}\nIdade: {paciente[1]}')
            if paciente[2] == 'm':
                print(f'Sexo: masculino')
            else:
                print(f'Sexo: femenino')
            print(f'Nome da mãe: {paciente[3]}\nSenha: {paciente[4]}')
        print("===" * 20)

#iniciar
def bemVindo():
    print("===> Bem vindo ao hospital SUS_SÓ_QUE_BOM <===")
    print("+=" * 25)

    while True:
        print("Olá, como posso ajudar?\n1 - Atendimento\n2 - Consultar fila\n3 - Checar leitos\n4 - Encaminhados")
        resp = input(": ")
        if resp == "1" or resp.lower() == "atendimento":
            agendamento(atendimentoGrave())
        elif resp == "2" or resp.lower() == "consultar fila":
            checarFila(filaNormal, "fila de atendimento")
        elif resp == "3" or resp.lower() == "checar leitos":
            checarFila(filaPreferencial, "leitos ocupados")
        elif resp == "4" or resp.lower() == "encaminhados":
            checarFila(filaEncaminhamento, "lista de encaminhados")


bemVindo()
