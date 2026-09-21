# Métodos Numéricos

Projeto desenvolvido para a disciplina de Métodos Numéricos.

O projeto tem como objetivo aplicar métodos numéricos para determinar o tamanho de entrada `n` em que os algoritmos A e B apresentam o mesmo tempo de execução.

Os tempos de execução são modelados por:

* `TA(n) = 0,01 n log₂(n)`
* `TB(n) = 0,08n + 20/n`

A solução é formulada como uma equação não linear `f(n) = 0` e resolvida numericamente utilizando diferentes métodos.

## Métodos implementados

O pacote contém implementações próprias dos seguintes métodos numéricos:

* Método da Bisseção
* Método da Posição Falsa
* Método de Newton

Os métodos foram implementados sem a utilização de funções prontas para determinação de raízes.

## Estrutura do projeto

```text
Numerical-Methods/
├── notebook/
│   └── project.ipynb
├── src/
│   └── metodos/
│       ├── __init__.py
│       ├── bissecao.py
│       ├── posicao_falsa.py
│       └── newton_raphson.py
├── README.md
└── pyproject.toml
```

## Requisitos

* Python 3.10 ou superior
* pip
* Jupyter Notebook

## Instalação

Clone o repositório:

```bash
git clone https://github.com/Viniccius-Albuquerque/Numerical-Methods.git
```

Entre na pasta do projeto:

```bash
cd Numerical-Methods
```

Instale o pacote utilizando o `pip`:

```bash
pip install -e .
```

## Utilização

Após a instalação, os métodos podem ser importados normalmente pelo Python.

Exemplo:

```python
from metodos.bissecao import bissecao
from metodos.posicao_falsa import posicao_falsa
```

Os métodos recebem uma função `f(x)`, os limites do intervalo, as tolerâncias e o número máximo de iterações.

Exemplo de utilização da Bisseção:

```python
def f(x):
    return x**2 - 4

raiz, iteracoes = bissecao(
    f,
    0,
    3,
    1e-6,
    1e-6,
    100
)

print("Raiz:", raiz)
print("Iterações:", iteracoes)
```

## Notebook

O notebook presente no diretório `notebook/` utiliza as funções implementadas no pacote para resolver o problema proposto.

As implementações dos métodos numéricos permanecem no pacote `src/metodos`, enquanto o notebook é utilizado para aplicação, análise e comparação dos resultados.

## Critérios de parada

Os métodos utilizam critérios de parada baseados nas tolerâncias definidas para o problema e no número máximo de iterações (`kmax`).

As tolerâncias utilizadas podem ser ajustadas durante a execução dos métodos.

## Autores

Viniccius Albuquerque,
Kilber Alves,
Manuela Vilanova,
Eduardo Gomes,
Mirna Lustosa.
