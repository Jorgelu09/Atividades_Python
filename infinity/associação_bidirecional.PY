from typing import Type

class Pedido:
    
    def __init__(self,nome):
        
        self.nome=nome
        

class Cliente:
    
    def __init__(self,nome):
        
        self.nome=nome
        self.pedido=[]
        
    def cadastrar_pedido(self, pedido: Type[Pedido]):
        
        self.pedido.append(pedido)
        
        
    def listar_pedido(self):
        
        if self.nome==self.nome:
        
        
            for pedido in self.pedido:
            
                print(f'Cliente:{self.nome}  Pedido:{pedido}') 
            
            


cliente1=Cliente("Jorge")
pedido1=cliente1.cadastrar_pedido("Camisa da nike")
pedid2=cliente1.cadastrar_pedido("Camisa da adidas")
pedid2=cliente1.cadastrar_pedido("Camisa da puma")
pedid2=cliente1.cadastrar_pedido("Camisa da wilson")


cliente2=Cliente("Tailane")
pedido2=cliente2.cadastrar_pedido("Camisa vermelha")
pedido2=cliente2.cadastrar_pedido("Camisa azul")
pedido2=cliente2.cadastrar_pedido("Camisa PRETA")

cliente1.listar_pedido()
cliente2.listar_pedido()
        
        
        