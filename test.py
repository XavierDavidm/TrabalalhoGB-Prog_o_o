#entrgar diagrama de classes
class Processo:
    def __init__(self,pid):
        self.pid=int(pid) #pid é passado no main por um contador que sempre começa do ultimo número da fila
                    #ex na fila de processos parou no 3 ele deve gerar ids apartir do 4 para cima
    def execute(self):
        pass

class ProcessoCalculo(Processo):
    def __init__(self, pid, expressao): # expressao é uma string que será recebida e depois dividida usando split
        super().__init__(pid)
        expressao=str(expressao)#validação só para garantir que é string
        i=expressao.split(' ',3) #"i" split dividirá a string em operandoA,operandoB e operador
        self.operandoA=int(i[0]) 
        self.operandoB=int(i[2])
        self.operador=i[1]

    def execute(self):
        #seletor de operação e calculadora
        if self.operador=='+':
            resultado=(self.operandoA+self.operandoB)
            print(self.operandoA,'+',self.operandoB,'é igual a',resultado)
        elif self.operador=='-':
            resultado=(self.operandoA-self.operandoB)
            print(self.operandoA,'-',self.operandoB,'é igual a',resultado)
        elif self.operador=='*':
            resultado=(self.operandoA*self.operandoB)
            print(self.operandoA,'*',self.operandoB,'é igual a',resultado)
        elif self.operador=='/':
            resultado=(self.operandoA/self.operandoB)
            print(self.operandoA,'/',self.operandoB,'é igual a',resultado)
        else:
            print('operação inválida')

class ProcessoGravacao(Processo):
    def __init__(self, pid):
        super().__init__(pid)
    def execute(self):
        pass

class ProcessoLeitura(Processo):
    def __init__(self, pid):
        super().__init__(pid)
    def execute(self):
        pass

class ProcessoImpressao(Processo):
    def __init__(self, pid):
        super().__init__(pid)
    def execute(self):
        pass

class Sistema:
    def __init__(self):
        self.fila=[] #fila de operações inicia vazia dentro de sistema
        self.start=False #variavel de validação do metodo geradorDeIds

    def menu(self):
        encerrar=False
        while encerrar!=True:
            print('______________')
            print('-----MENU-----')
            print('1 -> Criar Processo')
            print('2 -> Executar Próximo')
            print('3 -> Executar Processo específico')
            print('4 -> Salvar a fila de processos')
            print('5 -> Carregar do arquvio a fila processos')
            print('0 -> Salvar e Sair')
            r=str(input('digite a ação que deseja realizar:'))
            if r=='0':
                encerrar=True
                #chamar save aq
                print('encerrando sistema...')
            elif r=='1':
                print('Tipos de processo')
                print('1 -> Processo de Cálculo')
                print('2 -> Processo de Gravação')
                print('3 -> Processo de Leitura')
                print('4 -> Processo de Impressão')
                r=str(input('Qual Processo deseja Criar: '))
                if r=='1':
                    expressao=str(input('Digite a expressão do processo de calculo (usar espaço)ex :1 + 1 : '))
                    newProcesso=ProcessoCalculo(self.geradorDeIds(),expressao)
                    self.fila.append(newProcesso)
                elif r=='2':
                    pass
                elif r=='3':
                    pass
                elif r=='4':
                    pass
                else:
                    print('seleção inválida!')

            elif r=='2':
                pass
            elif r=='3':
                pass
            elif r=='4':
                pass
            elif r=='5':
                pass
            else:
                print('comando não reconhecido!')
    def geradorDeIds(self): #irá gerar ids e contem verificação de qual id parou considerando o arquivo
        #start verifica se o computation já foi lido para continuar a geração de ids
        if self.start==False:
            with open('computation.txt','r') as ARQcomputation:
                nLinhas=int(sum(1 for _ in ARQcomputation))
                ARQcomputation.seek(0)
                self.newId=nLinhas+1
                self.start=True
                return(self.newId)
        else: 
            self.newId=self.newId+1
            return(self.newId)

#anotações para fazer o trabalho: (apagar depois)
#dar split na expressão usando o espaço 3 + 2 -> 3 , + , 4

#main
#chamando sistema e menu
#sistema=Sistema()
#sistema.menu()
ex=[(1),(2),(3)]
print(ex[0])
ex.remove(ex[0])
print(ex[0])
