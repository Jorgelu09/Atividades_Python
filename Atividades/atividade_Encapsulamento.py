class Produto:
    
    def __init__(self,nome,preco,quantidade):
        
        self.__nome=str (nome)
        self.__preco=float(preco)
        self.__quantidade=int(quantidade)
        
    def get_nome(self):
        
        return print(self.__nome)
    
    def set_nome(self,novo_nome):
        
        self.__nome=novo_nome
        
    def get_preco(self):
        
        return print( self.__preco)
    
    def set_preco(self,novo_preco):
        
        if novo_preco<0:
            
            print("Valor negativo não é permitido")
            
        else:
            
            self.__preco=novo_preco        

    def get_quantidade(self):
        
        return print(self.__quantidade)
    
    def set_quantidade(self,nova_quantidade):
        
        if nova_quantidade<0:
            
            print("Valor negativo não é permitido")
            
        else:
            
            self.__quantidade=nova_quantidade
            
            
    def adicionar_produto(self):
        
        produto={
            
            'Nome':self.__nome,
            'Preço':self.__preco,
            'Quantidade':self.__quantidade
            
        }
        
        for chave,valor in produto.items():
            
            print(f'{chave}:{valor}')
            
    
produto1=Produto("Feijão",6.80,150)

produto1.adicionar_produto()
    
produto1.set_nome("Feijão carioca")

produto1.adicionar_produto()   

produto1.set_preco(-2)     
        
        
        
        
        