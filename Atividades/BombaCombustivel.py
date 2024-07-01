class BombaCombustivel:
    
    def __init__(self,tipoCombustivel,valorLitro,quantidadeCombustivel):
        
        self.__tipoCombustivel=tipoCombustivel
        self.__valorLitro=float(valorLitro)
        self.__quantidadeCombustivel=float(quantidadeCombustivel)
        
        
    def abasterPorValor(self):
        
        valor=float (input(" Valor: "))
        
        litros=valor/self.__valorLitro

        if litros <= self.__quantidadeCombustivel:
                
                self.__quantidadeCombustivel-=litros
                
        print(f'Valor:{valor} Litros:{litros:.2f} de {self.__tipoCombustivel} abastecidos')
        print(f"Bomba atualizada:{self.__quantidadeCombustivel:.2f}")
        
        
    def abastecerPorLitro(self):
        
        l=float(input("Litros: "))
        
        vl=l*self.__valorLitro
        
        if l<=self.__quantidadeCombustivel:
            
            self.__quantidadeCombustivel-=l
            
        print(f'Litros:{l} de {self.__tipoCombustivel} | Valor a ser pago:{vl}')
        print(f'Bomba atualizado:{self.__quantidadeCombustivel}')
        
        
    
    def set_alterarValor(self,novoValor):
        
        self.__valorLitro=novoValor
        
        
    def set_alterarCombustivel(self,novoCombustivel):
        
        self.__tipoCombustivel=novoCombustivel
        
        
    def set_alterarQuantidade(self,novaQuantidade):
    
        self.__quantidadeCombustivel=novaQuantidade
        
            
carro1=BombaCombustivel("Gasolina", 6.45, 100.00)   
 

carro1.abasterPorValor()
carro1.abastecerPorLitro()
carro1.set_alterarCombustivel("Etanol")
carro1.abastecerPorLitro()
        
        
