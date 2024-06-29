from typing import Type

class Tarefa:
    
    def __init__(self, nome):
        
        self.nome=nome
        
class Projeto: 
            
    def __init__(self,nome):
        
        self.nome=nome
        self.tarefas=[]

    
    def adicionar_tarefa(self, tarefa:Type[Tarefa]):
        
        self.tarefas.append(tarefa)
        
        
    def listar_tarefa(self):
        
        for tarefa in self.tarefas:
            
            print(f'O projeto:{self.nome}e a tarefa é:{tarefa}')
        
        

projeto1=Projeto("Limpeza geral")

tarefa1=projeto1.adicionar_tarefa("Lavar banheiros")
tarefa1=projeto1.adicionar_tarefa("Lavar vasos")

tarefa1=projeto1.listar_tarefa()
