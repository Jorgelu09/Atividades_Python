class Aluno:
    
    def __init__(self,nome,idade,matricula):
        
        self.__nome=nome
        self.__idade=idade
        self.__matricula=matricula
        
        
    def get_nome(self):
        
        return self.__nome
    
    
    def set_nome(self,novo_nome):
        
        self.__nome=novo_nome
        
    
    def get_idade(self):
        
        return self.__idade
    
    
    def set_idade(self,nova_idade):
        
        self.__idade=nova_idade
                
    
    def dados_aluno(self):
        aluno={
            
            "Nome":self.__nome,
            "idade":self.__idade,
            "matricula":self.__matricula
            
        }
        
        print(f"{aluno['Nome']} adicionado")
        
        print("Carregando dados...")
        
        for key,value in aluno.items():
            print(f"{key}:{value}")
        

aluno1=Aluno('Jorge',"23","123456")

aluno1.dados_aluno()
aluno1.set_nome("Tailane")
aluno1.dados_aluno()

    
