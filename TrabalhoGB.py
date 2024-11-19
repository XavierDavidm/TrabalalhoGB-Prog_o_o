#entrgar diagrama de classes
class Processo:
    def __init__(self,pid,tipo):
        self.pid=int(pid) #pid é passado no main por um contador que sempre começa do ultimo número da fila
                    #ex na fila de processos parou no 3 ele deve gerar ids apartir do 4 para cima
        self.tipo=str(tipo) #tipo identifica qual processo é('c','g','l','i')
    def execute(self):
        pass
    def getId(self):
        return self.pid
    
class ProcessoCalculo(Processo):
    def __init__(self, pid, tipo, expressao): # expressao é uma string que será recebida e depois dividida usando split
        super().__init__(pid,tipo)
        self.expressao=str(expressao)#validação só para garantir que é string
        i=self.expressao.split(' ',3) #"i" split dividirá a string em operandoA,operandoB e operador
        self.operandoA=int(i[0]) 
        self.operandoB=int(i[2])
        self.operador=i[1]

    def execute(self):
        #seletor de operação e calculadora
        print('executando Cálculo...')
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
    def __init__(self, pid, tipo, expressao):
        super().__init__(pid,tipo)
        self.expressao=str(expressao)
    def execute(self): #escreve expressão no fim do arquivo sem sobrescrever
        print('executando Gravação...')
        with open('computation.txt','a') as ARQcomputation:
            linha=str(self.expressao+'\n')
            ARQcomputation.write(linha)

class ProcessoLeitura(Processo):
    def __init__(self, pid, tipo):
        super().__init__(pid,tipo)
    def execute(self):
        print('executando Leitura...')
        #le o arquivo computation e retorna a fila com os processo lidos
        with open('computation.txt','r') as ARQcomputation:
            nLinhas=int(sum(1 for _ in ARQcomputation))
            ARQcomputation.seek(0)
            filaTemp=[] #fila temporaria que será adicionada a fila oficial dentro do sistema
            for i in range(nLinhas):
                linha = ARQcomputation.readline().strip()
                processo=ProcessoCalculo(sistema.geradorDeIds(),'c',linha)
                filaTemp.append(processo)
            print(len(filaTemp))
        #limpa o arquivo computation
        with open('computation.txt','w') as ARQcomputation:
            pass
        return sistema.fila.extend(filaTemp)
    
class ProcessoImpressao(Processo):
    def __init__(self, pid, tipo):
        super().__init__(pid, tipo)
    def execute(self):
        print('executando Impressão...')
        for i in range(len(sistema.fila)):
            processo=sistema.fila[i]
            if processo.tipo=='c':
                print('pID:',processo.getId(),'- tipo: Cálculo','expressão:',processo.expressao)

class Sistema:
    def __init__(self):
        self.fila=[] #fila de operações inicia vazia dentro de sistema
        self.newId=0 #variavel do metodo geradorDeIds

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
            elif r=='1': #criador de processos
                print('Tipos de processo')
                print('1 -> Processo de Cálculo')
                print('2 -> Processo de Gravação')
                print('3 -> Processo de Leitura')
                print('4 -> Processo de Impressão')
                r=str(input('Qual Processo deseja Criar: '))
                if r=='1': #Processo de Cálculo
                    expressao=str(input('Digite a expressão do processo de calculo (usar espaço)ex :1 + 1 :'))
                    #validação
                    i=expressao.split(' ',3) #"i" split dividirá a string em operandoA,operandoB e operador
                    operandoA=int(i[0]) 
                    operandoB=int(i[2])
                    operador=i[1]
                    if operador=='/' and operandoB == 0:
                        print('Erro! é impossivel dividir por zero')
                    else:
                        Processo=ProcessoCalculo(self.geradorDeIds(),'c',expressao)
                        print('Id:',Processo.getId())
                        self.fila.append(Processo)
                        print('Processo de Cálculo criado com sucesso!')
                    
                elif r=='2': #Processo de Gravação
                    expressao=str(input('Digite a expressão que será gravada (usar espaço)ex :1 + 1 :'))
                    Processo=ProcessoGravacao(self.geradorDeIds(),'g',expressao)
                    print('Id:',Processo.getId())
                    self.fila.append(Processo)
                    print('Processo de Gravação criado com sucesso!')

                elif r=='3': #Processo de Leitura
                    Processo=ProcessoLeitura(self.geradorDeIds(),'l')
                    print('Id:',Processo.getId())
                    self.fila.append(Processo)
                    print('Processo de Leitura criado com sucesso!')

                elif r=='4': #Processo de Impressão
                    Processo=ProcessoImpressao(self.geradorDeIds(),'i')
                    print('Id:',Processo.getId())
                    self.fila.append(Processo)
                    print('Processo de Impressão criado com sucesso!')

                else:
                    print('seleção inválida!')

            #executar proximo da fila
            elif r=='2':
                #validação se a fila está vazia
                if len(self.fila)==0:
                    print('A Fila de processos está vazia! crie um processo para executa-lo')
                else:
                    #executa o primeiro processo da fila[0]
                    Processo = self.fila[0]
                    Processo.execute()
                    self.fila = self.fila[1:] #remove o primeiro processo após sua execução
            #executar processo especifico
            elif r=='3':
                #validação se a fila está vazia
                if len(self.fila)==0:
                    print('A Fila de processos está vazia! crie um processo para executa-lo')
                else:
                    #executa o processo selecionado pelo user usando pid
                    status=False #validação se o processo existe ou não
                    id = int(input('digite o pid do precesso que deseja executar: '))
                    for Processo in self.fila: #busca o processo com pid informado o pelo user e o executa
                        if Processo.pid == id:
                            Processo.execute()
                            self.fila.remove(Processo)
                            status=True
                            break
                    if status==False:
                        print('Processo não encontrado na lista')
            #Salvar a fila de processos                 
            elif r=='4':
                with open('fila.txt','r') as ArqFila:
                    for i in range(len(self.fila)):
                        processo=self.fila[i]
                        #salvando tipos c e g
                        if processo.tipo=='c' or processo.tipo=='g':
                            tipo=str(processo.tipo)
                            id=str(processo.getId)
                            expressao=(processo.expressao)
                            linha=str(tipo+id+expressao+'\n')
                            ArqFila.write(linha)
                        else: 
                            tipo=str(processo.tipo)
                            id=str(processo.getId)
                            linha=str(tipo+id+'\n')
                            ArqFila.write(linha)
                    print('salvando fila atual em arquivo...')

            #Carregar do arquivo a fila de processos #mudar para acomodar o arquivo da fila
            elif r=='5':
                print('Carregando Fila de Processos salva...')
                with open('fila.txt','r') as ArqFila:
                    nLinhas=int(sum(1 for _ in ArqFila))
                    ArqFila.seek(0)
                    for i in range(nLinhas):
                        linha = ArqFila.readline().strip()
                        a = linha.split(',',3) #a[0]=tipo a[1]=pid a[2]=expressao(se tiver)
                        if a[0]=='c':
                            Processo=ProcessoCalculo(a[1],'c',a[2])
                            self.fila.append(Processo)
                        elif a[0]=='g':
                            Processo=ProcessoGravacao(a[1],'g',a[2])
                            self.fila.append(Processo)
                        elif a[0]=='l':
                            Processo=ProcessoLeitura(a[1],'l')
                            self.fila.append(Processo)
                        elif a[0]=='i':
                            Processo=ProcessoImpressao(a[1],'i')
                            self.fila.append(Processo)
            else:   
                print('comando não reconhecido!')
    #este metodo gera os ids, é usado pelos criadores de processo e pelo carregador       
    def geradorDeIds(self): 
        if len(self.fila)==0:
            self.newId=1
        else:
            processo=self.fila[-1]
            self.newId=(processo.getId()) + 1 #mudar para o ultimo da fila
        return(self.newId)

#anotações para fazer o trabalho: (apagar depois)
#check list
#processo de calculo + execute ->FEITO
#processo de GRAVAÇÃO + execute -> feito
#processo de leitura + execute -> feito
#processo de impressao + execute -> feito

#menu
#1.1-> FEITO
#1.2-> feito
#1.3-> feito
#1.4-> feito

#2-> FEITO
#3-> feito
#4-> 
#5-> feito

#implementar save
#implementar validações adicionais no 1(criação dos processos)

#main
#chamando sistema e menu

sistema=Sistema()
sistema.menu()