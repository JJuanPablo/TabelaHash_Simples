import hashlib

class TabelaHash():

    # Inicaliza a tabela com o tamanho 10 por padrão
    def __init__(self, tamanho: int = 10) -> int:
        self.tabela = [None] * tamanho
        self.tamanho = tamanho
        print(f'Tabela com {tamanho} posições criada com sucesso!')

    # Cria a função que define o valor hash para usa chave
    def funcao_hash(self, chave):
        # Calcula o Hash da sua chave usando o Algoritmo sha-256
        # Transforma sua entrada em binario, e depois em hexadecimal 
        hash_sha256 = hashlib.sha256(chave.encode('utf-8')).hexdigest()
        # precisa converter para inteiro, nao tem como fazer operações matematicas usando string
        hash_inteiro = int(hash_sha256, 16)
        # retorna o valor do seu Hash e o resto da divisão é o índice onde sera armazenado
        return hash_inteiro % self.tamanho
    
    # Cria uma função onde voce irá passar um par(chave/valor)
    def inserir(self, chave, valor):
        #Calcula o índice
        indice = self.funcao_hash(chave)
        # Se a tabela não tiver nada
        if self.tabela[indice] is None:
            # Usando encadeamento
            self.tabela[indice] = []
        
        # Adiciona o par para a tabela
        self.tabela[indice].append((chave, valor))
        print(f'{chave} -> {valor} foi inserido no índice {indice}')

    # Faz uma busca da sua chave para obter os dados
    def buscar(self, chave):
        indice = self.funcao_hash(chave)
        if self.tabela[indice] is not None:
            # 'enumerate' serve para voce buscar o índice e o valor ao mesmo tempo
            for k, v in enumerate(self.tabela[indice]):
                if k == chave:
                    return v
        return None
    
    # Exibe a tabela
    def exibir_tabela(self):
        print('\nTabela Hash')
        # Lista o índice junto com os dados armazenados
        for i, v in enumerate(self.tabela):
            print(f'ìndice: {i} -> {v}')
        
    # Remove a chave 
    def remover(self, chave):
        indice = self.funcao_hash(chave)
        if self.tabela[indice] is not None:
            for k, v in enumerate(self.tabela[indice]):
                if k == chave:
                    del self.tabela[indice][v]
                    return print(f'Chave {chave} removida com sucesso!')
        return None
    


def menu():
    while True:
            # Usa try para tratamentos de erros
            try:
                # Solicita a entrada do usuário
                posicao = input('Quantas posições deseja ter? (1/50): ')
                # Converte para inteiro
                posicao = int(posicao)

                # Verifica se a entrada está dentro do intervalo permitido
                if 1 <= posicao <= 50:
                    tabela = TabelaHash(posicao)
                else:
                    print('Erro: O número deve estar entre 1 e 50. Tente novamente.')
            except ValueError:
                # Trata o caso em que o usuário insere algo que não é um número inteiro
                print('Erro: Entrada inválida. Certifique-se de inserir um número inteiro.')
                posicao = int(input('Quantas posições deseja ter? (1/50): '))
                tabela = TabelaHash(posicao)


            while True:

                print('\n1. Adicionar cliente')
                print('2. Buscar cliente')
                print('3. Excluir cliente')
                print('4. Exibir tabela')
                print('5. Sair')
                try:
                    acao = input('Escolha uma das alternativas acima: ')
                    acao = int(acao)
                except ValueError:
                    print('Error: Por favor insira um número inteiro.')
                    print('\n1. Adicionar cliente')
                    print('2. Buscar cliente')
                    print('3. Excluir cliente')
                    print('4. Exibir tabela')
                    print('5. Sair')    
                    acao = int(input('Escolha uma das alternativas acima: '))

                if acao == 1:
                    nome = input('Insira a chave (nome do usuário): ')
                    dados = input(f'Insira os dados do usuário {nome}: ')
                    tabela.inserir(nome, dados)
                elif acao == 2:
                    nome_id = input('Insira o nome do usuário que deseja buscar: ')
                    resultado = tabela.buscar(nome_id)
                    if resultado:
                        print(f'Dados encontrados: {resultado}')
                    else:
                        print('Usuário não encontrado.')
                elif acao == 3:
                    remover = input('Nome do usuário que deseja excluir: ')
                    tabela.remover(remover)
                elif acao == 4:
                    tabela.exibir_tabela()
                    
                elif acao == 5:
                    print('Você saiu com sucesso!')
                    break
                else:
                    print('Finalizando o programa...')
                    break

menu()
