## Projeto Restaurant Orders

> Quinto projeto do módulo de Ciência da Computação do curso de desenvolvimento web da [Trybe](https://www.betrybe.com/)

**Contexto**

Os dois últimos blocos do curso são focados no estudo mais aprofundado das estruturas de dados que temos utilizado desde o início de nossa jornada na Trybe. Neste projeto, praticamos com dois desses tipos de dados: os Hash maps e os Sets.

**Objetivo do projeto**

Uma lanchonete possui um sistema de faturamento dos pedidos dos clientes, que salva o nome da pessoa, o pedido realizado, e dia do atendimento (dia da semana). O projeto consiste em ajudar a lanchonete a melhorar esse sistema para que ele possibilite extração de relatórios e, num segundo momento, a controlar seu estoque. 

**Principais habilidades desenvolvidas nesse trabalho**

  - Trabalhar com as estruturas de dados Hash map (Dict) e Set
  - Trabalhar com classes e manipulação de arquivos

**Tecnologia utilizada**

- <a href="https://www.python.org"><img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" title="Python" height="35" align="center"/> - Python</a> 

---

### Lista de requisitos propostos pela Trybe:

#### Obrigatórios

#### 1 - Campanha de publicidade, implemente um método chamado `analyze_log` no módulo `src/analyze_log.py` que gere informações de uma lanchonete.

A lanchonete quer promover ações de marketing e, para isso, a agência de publicidade precisa exatamente das informações abaixo:

- Qual o prato mais pedido por 'maria'?

- Quantas vezes 'arnaldo' pediu 'hamburguer'?

- Quais pratos 'joao' nunca pediu?

- Quais dias 'joao' nunca foi na lanchonete?

#### Dados

O atual sistema guarda os `logs` de todos os pedidos feitos em um arquivo _csv_, contendo o formato `cliente, pedido, dia`, um por linha e sem nome das colunas (a primeira linha já é um pedido).

O `log` a ser utilizado é o arquivo `data/orders_1.csv`. Todas as informações são _strings_ com letras minúsculas. O histórico contém pedidos feitos em todos os dias da semana que a lanchonete abre, e de todos os pratos que a lanchonete oferece. Ou seja, é possível saber o cardápio e agenda completos. Os dias da semana estão no formato `"...-feira", "sabado" ou "domingo"`, e **não nos interessa informações sobre os dias que a lanchonete não abre**.

#### Implementação

No arquivo `analyze_log.py`, escreva uma função que responda às seguintes perguntas abaixo:

- Qual o prato mais pedido por 'maria'?

- Quantas vezes 'arnaldo' pediu 'hamburguer'?

- Quais pratos 'joao' nunca pediu?

- Quais dias 'joao' nunca foi na lanchonete?

A função não retornará nada! A função deve apenas salvar as respostas no arquivo `data/mkt_campaign.txt`, na mesma ordem que acima.

**Assinatura da função:**

```python
def analyze_log(path_to_file):
    # Código vem aqui
```

**Saída correta:**

```
hamburguer
1
{'pizza', 'coxinha', 'misto-quente'}
{'sabado', 'segunda-feira'}
```

> A ordem dos pedidos, bem como dos dias não precisa ser exatamente a apresentada no exemplo

- No arquivo analyze_log.py deve estar implementada a função `def analyze_log(path_to_file)`;

- A função deve realizar a leitura do `log` e salvar em um arquivo `txt` as informações solicitadas;

- Utilização correta de `Dict/Set`, vistos no módulo;

- Faça um código legível e modularizado, quando for o caso.

#### 2 - Análises contínuas, implemente a classe `TrackOrders` que gere informações contínuas de uma lanchonete.

A campanha de marketing foi um sucesso! A gerência agora deseja um sistema que mantenha um registro contínuo dessas informações. Mais especificamente, desejam que o sistema permita a extração das seguintes informações a qualquer momento:

- Prato favorito por cliente;

- Pratos nunca pedidos por cada cliente;

- Dias nunca visitados por cada cliente;

- Dia mais movimentado;

- Dia menos movimentado.

Para isso, você deverá implementar uma classe que entregue as informações acima.

#### Implementação

**Arquivos**

- O arquivo `track_orders.py` é onde você implementará a classe `TrackOrders`.

- O arquivo `src/main.py` é apenas auxiliar e faz a leitura do arquivo `csv` especificado e envia a informação de cada pedido para as classes `TrackOrders` e para a classe `InventoryControl`, ao mesmo tempo. Não se preocupe ainda com o arquivo `inventory_control.py` (classe InventoryControl), pois ele é necessário apenas para a realização dos requisitos bônus.

- Ainda no arquivo `src/main.py`, após a leitura completa do arquivo `csv`, algumas informações são impressas na tela para que você observe o comportamento das classes.

**Teste o comportamento do arquivo `main.py`**

Abra o arquivo `main.py` e complete a variável _path_ com `data/orders_1.csv`. Rode o arquivo `main.py`. Quatro linhas de `None` devem ser impressas. Isso acontece, porque as funções não estão devidamente implementadas ainda.

**Implemente a solução**

No arquivo `track_orders.py`, implemente a classe `TrackOrders`, contendo, **no mínimo**, os métodos abaixo:

```python
class TrackOrders:
    # aqui deve expor a quantidade de estoque
    def __len__(self):
        pass

    def add_new_order(self, customer, order, day):
        pass

    def get_most_ordered_dish_per_customer(self, customer):
        pass

    def get_never_ordered_per_customer(self, customer):
        pass

    def get_days_never_visited_per_customer(self, customer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
```

> Você é livre para criar os atributos e métodos necessários. Lembre-se de criar uma classe legível e bem modularizada. Lembre-se também de não incorrer em otimização prematura. Ou seja, não implemente funcionalidades que ainda não são necessárias, nem coloque atributos do tipo "vai que um dia precisa". Sempre rode o arquivo `main.py` para verificar o comportamento da sua classe.

- Classe `TrackOrders` implementada;

- A classe está devidamente modularizada;

- Os métodos fazem uso das técnicas de `Dict` e `Set` vistos no módulo;

- Os métodos atingem complexidade ótima (geralmente `O(1)` ou `O(n)`, em alguns métodos que usam `Set`).

#### Bônus:

#### 3 - Controle de estoque

Atualmente o controle de estoque de ingredientes é feito no caderninho. Ao final da semana, uma pessoa conta quantas unidades, de cada ingrediente, ainda restam no estoque e anota quantos precisam ser comprados, para completar o estoque mínimo de cada ingrediente.

A lanchonete deseja automatizar esse controle: no final da semana, a gerência irá imprimir uma lista de compras com as respectivas quantidades.

#### Dados

O `log` a ser utilizado ainda é o arquivo `data/orders_1.csv`. É garantido que os pedidos da semana não irão zerar nenhum dos estoques.

#### Implementação

No arquivo `inventory_control.py` você deve implementar a classe `InventoryControl` que retorna a lista de compras da semana, a partir da informação de cada. É importante que a lista seja atualizada a cada pedido, e não apenas ao final de semana, pois a gerência quer a liberdade de imprimir a lista de compras a qualquer momento.

A estrutura básica da classe está demonstrada abaixo e já contém as informações dos ingredientes, bem como o estoque mínimo de cada um. O método `get_quantities_to_buy` deve retornar um `Dict` que mapeia o ingrediente para a quantidade a ser comprada:

```python
class InventoryControl:
    INGREDIENTS = {
        'hamburguer': ['pao', 'carne', 'queijo'],
        'pizza': ['massa', 'queijo', 'molho', 'tomate'],
        'queijo-quente': ['pao', 'queijo', 'queijo'],
        'misto-quente': ['pao', 'queijo', 'presunto'],
        'bauru': ['pao', 'queijo', 'presunto', 'tomate'],
        'coxinha': ['massa', 'frango'],
    }
    MINIMUM_INVENTORY = {
        'pao': 50,
        'carne': 50,
        'queijo': 100,
        'molho': 50,
        'presunto': 50,
        'massa': 50,
        'frango': 50,
    }

    def __init__(self):
        pass

    def add_new_order(self, customer, order, day):
        pass

    def get_quantities_to_buy(self):
        pass
```

- Classe `InventoryControl` implementada;

- A classe está devidamente modularizada;

- Garanta que todos os ingredientes e pratos foram testados;

- Os métodos devem fazer uso das técnicas de `Dict` e `Set` vistos no módulo;

- Os métodos atingem complexidade ótima (geralmente `O(1)` ou `O(n)`, em alguns métodos que usam `Set`).

#### 4 - Estoque pode acabar

As campanhas de marketing tiveram sucesso novamente, e atraíram muitas novas pessoas clientes para a lanchonete. Se antes os estoques mínimos eram sempre suficientes para uma semana, agora não são mais...

Suponha os seguintes estoques:

```md
- Pao: 1;

- Queijo: 5;

- Presunto: 3.
```

Se uma pessoa pedir um misto-quente, será possível atendê-la. Porém o pão irá acabar. Se a próxima pessoa pedir hamburguer, não será possível atendê-la. Sua missão é implementar um código que, caso algum ingrediente acabe, todos os pratos que usam aquele ingrediente devem ser imediatamente removidos do cardápio eletrônico, evitando gerar frustração em clientes.

#### Dados

O `log` a ser utilizado agora é o arquivo `data/orders_2.csv`. Se quiser testar pelo arquivo `main.py`, não se esqueça de alterar a variável `path`.

#### Implementação

> Você fez commit do requisito `3 - Controle de estoque`? Se não, faça, pois agora você vai alterar o seu código!

Implemente um novo método na classe `InventoryControl` que retorne um conjunto com todos os pratos disponíveis, ou seja, que ainda tem ingredientes suficientes.

**Assinatura da função:**

```python
def get_available_dishes():
    # retorno: um conjunto de pratos que ainda têm ingredientes disponíveis
```

Altere o arquivo `main.py`:

- Caso o prato que a pessoa solicitou não esteja disponível, não registre o pedido na execução do método `add_new_order`.

- Novo método, `get_available_dishes`, implementado e funcionando corretamente.

- Alteração na `main.py` produzindo o efeito esperado.

- As classes/métodos estão devidamente modularizadas;

- Os métodos fazem uso das técnicas de `Dict` e `Set` vistos no módulo;

---

[Ir para a lista de projetos](https://github.com/willian-prado/trybe-records)
