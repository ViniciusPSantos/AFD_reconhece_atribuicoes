import pandas as pd

class AfdReconheceAtribuicoes():

    def __init__(self):
        self.__estadosDeAceitacao = ["q7"]
        self.__estadoAtual = "q0" #O Automato inicializa no estado inicial, no caso seria o q0
        self.__conjuntoDeEstados = ["q0", "q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8"]
        self.__alfabeto = {
            "letras" : ["a", "q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "s", "d", "f", "g", "h", "j", "k", "l", "ç", "x", "c", "v", "b", "n", "m", "z"],
            "numeros" :  ["0", "1", "2", "3", "4","5", "6", "7", "8", "9"],
            "especiais" : ["_", "=", ";", "."]
        }

        self.__tabelaDeTransiscao = self.__criaTabelaDeTransicao()
        
        
    def verificaAtribuicao(self, palavra):
        
        if(self.verificaSimbolos(palavra)):
            if (palavra[-1] == ";"):
                for letra in palavra:
                    self.__transicao(letra)
                if (self.__estadoAtual == self.__estadosDeAceitacao[0]):
                    self.__estadoAtual = "q0" #Quando a verificação da atribuição é terminado, o estado atual do automato é resetado para o estado inicial
                    return "Palavra Aceita!"
                else:
                    self.__estadoAtual = "q0"
                    return "Palavra não aceita!"
            else:
                return "Palavra não aceita! Você esqueceu de adicionar o ';'"
        else:
            return "Palvra não aceita! Esta palavra contém símbolos que não fazem parte da lingaugem"
 
    
    def __transicao(self, letra):
        self.__estadoAtual = self.__tabelaDeTransiscao.loc[self.__estadoAtual, letra]
        
    def __criaTabelaDeTransicao(self):
        
        #Atribuindo os valores do Alfabeto a uma variável que será utilizada como o valor das colunas do DataFrame
        letras = [letra for letra in self.__alfabeto["letras"]]
        numeros = [numero for numero in self.__alfabeto["numeros"]]
        especiais = [especial for especial in self.__alfabeto["especiais"]]
        
        colunas = letras + numeros + especiais
        
        umaTabelaDeTransicao = pd.DataFrame(columns=colunas, index=self.__conjuntoDeEstados)
        
        #Atribuindo os valores a tabela de transição
        umaTabelaDeTransicao.loc["q0", "a":"z"]= "q1"
        umaTabelaDeTransicao.loc["q0", "0":"."]= "q8"
        
        umaTabelaDeTransicao.loc["q1", "a":"_"]= "q1"
        umaTabelaDeTransicao.loc["q1", "="]= "q2"
        umaTabelaDeTransicao.loc["q1", ";":"."]= "q8"
        
        umaTabelaDeTransicao.loc["q2", "_":"."]= "q8"
        umaTabelaDeTransicao.loc["q2", "a":"z"]= "q4"
        umaTabelaDeTransicao.loc["q2", "0":"9"]= "q3"
        
        umaTabelaDeTransicao.loc["q4", "a":"_"]= "q4"
        umaTabelaDeTransicao.loc["q4", ";"]= "q7"
        umaTabelaDeTransicao.loc["q4", ["=", "."]]= "q8"
        
        umaTabelaDeTransicao.loc["q7", "a":"."]= "q8"
        
        umaTabelaDeTransicao.loc["q3", "0":"9"]= "q3"
        umaTabelaDeTransicao.loc["q3", "."]= "q5"
        umaTabelaDeTransicao.loc["q3", ";"]= "q7"
        umaTabelaDeTransicao.loc["q3", "a":"z"]= "q8"
        umaTabelaDeTransicao.loc["q3", "_":"="]= "q8"

        umaTabelaDeTransicao.loc["q5", "0":"9"]= "q6"
        umaTabelaDeTransicao.loc["q5", "a":"z"]= "q8"
        umaTabelaDeTransicao.loc["q5", "_":]= "q8"
      
        umaTabelaDeTransicao.loc["q6", "0":"9"]= "q6"
        umaTabelaDeTransicao.loc["q6", ";"]= "q7"
        umaTabelaDeTransicao.loc["q6", "a":"z"]= "q8"
        umaTabelaDeTransicao.loc["q6", ["_","=","."]]= "q8"
        
        umaTabelaDeTransicao.loc["q7", "a":"."]= "q8"
                
        umaTabelaDeTransicao.loc["q8"] = "q8" #Q8 é o estado de "lixo", no entanto, sempre que o automato entrar nele, ele permanecerá no mesmo estado
        
        return umaTabelaDeTransicao
        
    def verificaSimbolos(self, palavra): #Verifica se todos os símbolos da palvra fazem parte do alfabeto
        quantidadeDeSimbolosQueFazemPartedoAlfabeto = 0
        
        for letra in palavra:
            if((letra in self.__alfabeto["numeros"]) |(letra in self.__alfabeto["letras"]) | (letra in self.__alfabeto["especiais"])):
                quantidadeDeSimbolosQueFazemPartedoAlfabeto+=1
        
        if (quantidadeDeSimbolosQueFazemPartedoAlfabeto == len(palavra)):
           return True
        else:
            return False