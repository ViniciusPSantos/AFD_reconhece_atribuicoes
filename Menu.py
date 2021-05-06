from AfdReconheceAtribuicoes import AfdReconheceAtribuicoes

class Menu():

    @staticmethod
    def mostraMenu():
        
        reconheceAtribuicoes = AfdReconheceAtribuicoes()
        
        while True:
            
            print("\n=========================== Reconhece Atirbuicoes ==============================")
            print("1. Verificar se a atribuição é válida")
            print("2. Verificar se os símbolos da atribuição estão presentes no alfabeto")
            print("3. Sair")
            print("================================================================================")
            opcao = input("Selecione uma opção: ")
            
            if((opcao == "1") or (opcao == "2") or (opcao == "3")):
            
                if (opcao == "1"):
                    palavra = input("Digite a atribuição (lembre-se de não utilizar espaço): ")
                    print("\n" + reconheceAtribuicoes.verificaAtribuicao(palavra))
                
                if (opcao == "2"):
                    palavra = input("Digite a atribuição (lembre-se de não utilizar espaço): ")
                    
                    if(reconheceAtribuicoes.verificaSimbolos(palavra)):
                        print("\nOs símbolos da atribuição fazem parte do alfabeto!")
                    
                    else:
                        print("\nOs símbolos da atribuição não fazem parte do alfabeto!")
                    
                if (opcao == "3"):
                   break
            
            else:
                print("Opção inválida! Digite novamente")