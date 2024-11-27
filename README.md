# Tabela Hash em Python

Este repositório contém uma implementação de uma tabela hash em Python utilizando a função de hash `SHA-256`. O código oferece funcionalidades como inserção, busca, exclusão e exibição de elementos armazenados na tabela.

---

## 📋 Funcionalidades

- **Criar tabela hash**: O usuário pode definir o tamanho da tabela (entre 1 e 50 posições).
- **Inserir elementos**: Adicionar pares de chave-valor à tabela hash.
- **Buscar elementos**: Localizar dados associados a uma chave específica.
- **Excluir elementos**: Remover dados vinculados a uma chave.
- **Exibir tabela**: Mostrar o estado atual da tabela hash.

---

## 🛠️ Como executar o código

### Pré-requisitos

- Certifique-se de ter o Python 3.8 ou superior instalado em sua máquina.
- Um terminal ou IDE para executar o código.
*
### Passo a passo

1. **Clone este repositório**:
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd <NOME_DO_REPOSITORIO>
2. **Execute o script**:
    ````bash
    python tabela_hash.py

## 💻 Estrutura do Programa

### Classe TabelaHash

Métodos

- __init__(tamanho: int):
```
Inicializa a tabela hash com o número de posições especificado.
```

- funcao_hash(chave):
```
Gera um índice único para uma chave usando o algoritmo SHA-256.
```


- inserir(chave, valor):
```
Adiciona um par chave-valor à tabela.
```

- buscar(chave):
```
Retorna os dados associados a uma chave, se existirem.
```

- exibir_tabela():
```
Mostra todos os índices da tabela e seus respectivos valores.
```

- remover(chave):
```
Remove uma chave e seus dados da tabela.
```
- Função menu()
```
Controla a interação do usuário com o programa, exibindo as opções disponíveis e chamando os métodos da classe TabelaHash conforme necessário.
```

## 🖥️ Exemplo de Uso
### Criar uma tabela
Quantas posições deseja ter? (1/50): 10
Tabela com 10 posições criada com sucesso!

1. **Adicionar cliente**
```
Insira a chave (nome do usuário): João
Insira os dados do usuário João: Cliente VIP
João -> Cliente VIP foi inserido no índice 5
```

2. **Buscar cliente**
```
Insira o nome do usuário que deseja buscar: João
Dados encontrados: Cliente VIP
```

3. **Excluir cliente**
```
Nome do usuário que deseja excluir: João
Chave João removida com sucesso!
```

4. **Exibir tabela**
```

Tabela Hash:
Índice 0: None
Índice 1: None
Índice 2: None
Índice 3: None
Índice 4: None
Índice 5: None
Índice 6: None
Índice 7: None
Índice 8: None
Índice 9: None
Sair do programa
```

5. **Sair**
```
Você saiu com sucesso!
```


## 🙏 Agradecimentos

Muito obrigado por visitar este repositório! Espero que este projeto seja útil para você de alguma forma. Se tiver dúvidas ou sugestões, sinta-se à vontade para entrar em contato. 💻✨

**Boas práticas e bom aprendizado!**


