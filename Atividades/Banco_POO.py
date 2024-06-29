#Classe base onde os atributos e  metodos principais estão sendo definidos
class Conta:
    def __init__(self,n_conta,t_conta,titular):
        self.n_conta=n_conta
        self.t_conta=t_conta
        self.titular=titular
        self.saldo_conta=0

#Metodo para realizar o deposito de valores nas contas

    def deposito(self):

        self.valor=float(input("Digite o valor:"))
        self.saldo_conta+=self.valor
        print(f"Deposito de:{self.valor}")
        
#Metodo para realizar saque 

    def saque(self):

        if self.saldo_conta>0:

            self.valor=float(input("Digite o valor:"))
            self.saldo_conta-=self.valor
        else:

            print("Você está sem saldo")

#Metodo para resumo de informações de cada conta, utilizando um dicionário e um for para percorrer o mesmo. 
    def resumo(self):

        resumo_contabancaria={

            "Número da conta":self.n_conta,
            "Conta corrrente/poupança":self.t_conta,
            "Titular da cotna":self.titular,
            "Saldo em conta":self.saldo_conta

        }
        for chave,valor in resumo_contabancaria.items():

            print(f"{chave}:{valor}")

#Classe filha, herdando as informações da classe pai e inserindo seu atributo proprio "cheque especial" e com o metodo saque sendo sobrescrito com a particularidade da condição do cheque especial.

class Conta_Corrente(Conta):
        def __init__(self,n_conta,titular):
            self.cheque_especial=1.000
            super().__init__(n_conta,"Corrente",titular)    

        def saque(self):
            
            valor=float(input("Digite o valor: "))
            
            if self.saldo_conta<=0:
                print("Saldo insuficiente parar sacar! ")
                
            if valor<=self.saldo_conta+self.cheque_especial:
                self.saldo_conta-=valor
                print(f"Saque realizado!!")
                print(f"Saldo:{self.saldo_conta}|!")
                
#Classe filha herdando atributos e metodos da classe pai, porém inserindo o metodo de taxa de juros e acrescentando o atributo também. 
              
class Conta_Poupanca(Conta):
    
    def __init__(self, n_conta, titular,taxa_juros):
        self.taxa_juros=taxa_juros
                
        super().__init__(n_conta, "Poupança", titular)
                
    def calcular_juros(self):
        
        juros=self.saldo_conta*(self.taxa_juros/100)
        self.saldo_conta+=juros
        print(F"A taxa do juros é de{juros}")
        print(F"Saldo:{self.saldo_conta}")
        
        
        
cc=Conta_Corrente(55368,'Jorge Luis')
cc.deposito()
cc.resumo()

cp=Conta_Poupanca(55364,'Tailane Sidral')
cc.deposito()
cc.resumo()     
                
                
            
                
                
                            
        
            
            
  

            






