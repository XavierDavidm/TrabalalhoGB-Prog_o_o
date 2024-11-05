#entrgar diagrama de classes
class Processo:
    def __init__(self,pid):
        self.pid=pid #pid é passado no main por um contador que sempre começa do ultimo número da fila
                    #ex na fila de processos parou no 3 ele deve gerar ids apartir do 4 para cima
    def execute(self):
        pass

class ProcessoCalculo(Processo):
    def __init__(self, pid):
        super().__init__(pid)
    def execute(self):
        pass

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

#main e sistema/menu
fila=[]
arq=open('computation.txt','w')
#menu
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
            pass
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