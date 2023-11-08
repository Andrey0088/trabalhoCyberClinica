class Clinica():

    def __init__(self, nome, endereco, lista_pacientes, lista_medicos):
        self._nome = nome
        self._endereco = endereco
        self._lista_pacientes = lista_pacientes
        self._lista_medicos = lista_medicos

    def adicionaPaciente(self, cpf, paciente):
        self._lista_pacientes[cpf] = paciente


    def obterMedico(self, ID):
        if ID in self._lista_medicos.keys():
            return self._lista_medicos[ID]
        else:
            return "Erro"


    def obterPaciente(self, CPF):
        if len(self._lista_pacientes) != 0 and CPF in self._lista_pacientes.keys():
            return self._lista_pacientes[CPF]
        else:
            return "Erro"
        

    def excluirPaciente(self, CPF):
        if CPF in self._lista_pacientes.keys():
            del self._lista_pacientes[CPF]
            return True
        else:
            return False
        

    def encaminharPaciente(self, ID):
        if ID in self._lista_medicos.keys():
            return 1
        else:
            return 0
        
    def listaPacientesDoMedico(self, ID):
        if ID in self._lista_medicos.keys():
            pacientes_do_medico = []
            for key, paciente in self._lista_pacientes.items():
                if paciente.getID() == ID:
                    pacientes_do_medico.append(paciente)
            if pacientes_do_medico:
                return pacientes_do_medico
            else:
                return "Médico sem pacientes"
        else:
            return "ID de médico inválido ou Medico nao possui pacientes"

        

    def getLista_Medicos(self):
        return self._lista_medicos

    def getLista_Pacientes(self):
        return self._lista_pacientes

    



class Pessoa():

    def __init__(self, nome, cpf, idade, endereco):
        self._nome = nome
        self._cpf = cpf
        self._idade = idade
        self._endereco = endereco


class Paciente(Clinica, Pessoa):

    def __init__(self, nome, cpf, idade, data, ID):
        self._nome = nome
        self._cpf = cpf
        self._idade = idade
        self._data = data
        self._ID = ID
        self._lista_pacientes = {}

    def getNome(self):
        return self._nome

    def getCPF(self):
        return self._cpf

    def getIdade(self):
        return self._idade

    def getID(self):
        return self._ID
    
    def getData(self):
        return self._data


class Medico(Clinica, Pessoa):

    def __init__(self, ID, nome, cpf, idade, especializacao):
        self._ID = ID
        self._nome = nome
        self._cpf = cpf
        self._idade = idade
        self._especializacao = especializacao

    def getID(self):
        return self._ID

    def getNome(self):
        return self._nome

    def getCPF(self):
        return self._cpf

    def getIdade(self):
        return self._idade

    def getEspecializacao(self):
        return self._especializacao