from classes import Paciente, Medico, Clinica
import json
import datetime


# bloco para salvar cadastro, salva apenas os dados do paciente.


def salva_cadastros(clinica):
    Lista_Pacientes2 = dict()
    # pega as posiçoes do da lista de pacientes e coloca em i, i é uma instancia da classe clinica
    # que esta sendo usando para armazenar todos os atributos de paciente
    # separamos as variaveis e colocamos em um dic.
    for i in (clinica.getLista_Pacientes()).values():
        Nome = i.getNome()
        cpf = i.getCPF()
        idade = i.getIdade()
        dataEhora = i.getData()
        if i.getDoencas() == '':
            pass
        else:
            doencas = i.getDoencas()
        ID = i.getID()

        Lista_Pacientes2[cpf] = [Nome, cpf, idade, dataEhora, doencas, ID]
    # se nao existir cria e salva a lista ja formatada em dic, se existir, apenas salva a lista em formato dic
    with open('Pacientes_clinica.json', 'w') as arquivo:
        arquivo.write(json.dumps(Lista_Pacientes2))


def ler_cadastros():
    with open('Medicos_clinica.json', 'r') as arquivo:
        listaM = json.loads(arquivo.read())

    with open('Pacientes_clinica.json', 'r') as arquivo:
        listaP = json.loads(arquivo.read())

    return [listaM, listaP]


lista_medicos, lista_pacientes = ler_cadastros()

lista_medicos2 = dict()

for i in lista_medicos.values():
    ID, nome, cpf, idade, especialidade = i
    _Medico = Medico(ID, nome, cpf, idade, especialidade)
    lista_medicos2[ID] = _Medico


lista_pacientes2 = dict()

for i in lista_pacientes.values():
    nome, cpf, idade, data, doenca, ID = i
    _paciente = Paciente(nome, cpf, idade, data, doenca,  ID)
    lista_pacientes2[cpf] = _paciente

_clinica = Clinica("AVA", "Rua 900", lista_pacientes2, lista_medicos2)

while True:

    Escolha = input("-"*15 + "MENU CLÍNICA" + "-"*15 +
                    "\n1 - Adicionar paciente\n2 - Obter Paciente\n3 - Obter Medico\n4 - Obter pacientes do Medico(a)\n5 - Alta de pacientes\n 0 - Sair\nEscolha: ")
    if Escolha == '1':

        Nome = input("Insira o nome do paciente: ")
        CPF = input("Insira o CPF do paciente: ")
        Idade = input("Insira a idade do paciente: ")
        data = str(datetime.datetime.now())
        doenca = ''
        for i in (_clinica.getLista_Medicos()).values():
            print(
                f'Nome: {i.getNome()}\nEspecialidade: {i.getEspecializacao()}\nID: {i.getID()}\n')

        while True:
            ID = int(input("Com qual médico deseja se consultar, insira o ID: "))
            if _clinica.encaminharPaciente(ID):
                print(
                    f'Você será encaminhado para o médico {_clinica._lista_medicos[ID].getNome()}\nque possui especialidade {_clinica._lista_medicos[ID].getEspecializacao()}')
                _paciente = Paciente(Nome, CPF, Idade, data, doenca, ID)
                _clinica.adicionaPaciente(CPF, _paciente)

                break
            else:
                print(
                    "\nErro ao encaminhar paciente, o ID foi inserido incorretamente.\n")

    elif Escolha == '2':
        CPF = input("Insira o CPF do paciente: ")
        _paciente = _clinica.obterPaciente(CPF)

        if _paciente != 'Erro':
            print(
                f'\nInformações:\nNome: {_paciente.getNome()}\nCPF: {_paciente.getCPF()}\nIdade: {_paciente.getIdade()}\nNome do médico: {_clinica._lista_medicos[_paciente.getID()].getNome()}\n')
            

            fazer_diagnostico = input("Deseja fazer um diagnóstico? (S/N): ")
            if fazer_diagnostico.lower() == 's':
                id = _paciente.getID()
                Especialidade = _clinica.obterMedico(id).getEspecializacao()
                doenca = _clinica.escolheDoenca(Especialidade)
                _paciente.adicionaDoenca(doenca)
                _clinica.adicionaPaciente(CPF, _paciente)
            
        else:
            print(f'\nErro ao acessar paciente com CPF "{CPF}"\n')

    elif Escolha == '3':
        ID = int(input("Insira o ID do médico: "))
        _medico = _clinica.obterMedico(ID)
        if _medico != 'Erro':
            print(
                f'\nInformações:\nID: {_medico.getID()}\nNome: {_medico.getNome()}\nCPF: {_medico.getCPF()}\nIdade: {_medico.getIdade()}\nEspecialidade: {_medico.getEspecializacao()}\n')
        else:
            print(f'\n Erro ao acessar médico com ID "{ID}"\n')

    elif Escolha == '4':
        # Dentro deste bloco, pegamos do usuario um ID, que faz referencia ao medico
        # E logo apos imprime todos os pacientes que possui esse mesmo ID
        # Pois ID em paciente faz referencia ao ID do medico.
        # Esssa estrutura se repete, ate que o ID seja valido.
        continua = True
        ID = ''
        while continua:
            ID = input("Insira o ID do médico para listar seus pacientes: ")
            if ID.isdigit():
                ID = int(ID)
            else:
                print("\nErro! Por favor, digite um ID de 1 a 6.\n")
            if ID < 1 or ID > 6:
                print('!ERRO! - Digite um ID dentro do intervalo de 1 a 6\n')
            else:
                _medico = _clinica.obterMedico(ID)

                PacientesDoMedico = _clinica.listaPacientesDoMedico(ID)
                if PacientesDoMedico != "Médico sem pacientes" and PacientesDoMedico != "ID de médico inválido":
                    print(
                        f"Lista de pacientes do medico {_medico.getNome()}\n")
                    for pos, p in enumerate(PacientesDoMedico):
                        print(f'{pos} - {p.getNome()}')
                        continua = False
                elif PacientesDoMedico == "Médico sem pacientes":
                    print('Medico sem pacientes')
                    continua = False
                elif PacientesDoMedico == "ID de médico inválido":
                    print('ID do medico é invalido')

    elif Escolha == '5':
        cpf_paciente = input(
            'Digite o CPF do paciente que ira receber alta:\n')

        if cpf_paciente.isdigit():
            sucesso = _clinica.excluirPaciente(cpf_paciente)
            if sucesso:
                print('\nAlta realizada com sucesso!\n')
            else:
                print('\nPaciente nao existe ou ja recebeu alta.')
        else:
            print('!ERROR! - CPF invalido')

    elif Escolha == '0':
        print("\nSistema encerrado com sucesso, os dados foram armazenados!\n")
        salva_cadastros(_clinica)
        break
