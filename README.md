
# Algoritmo de Prim – Árvore Geradora Mínima (MST)

Este projeto implementa o **Algoritmo de Prim** em Python para encontrar a Árvore Geradora Mínima (MST) de um grafo. O algoritmo de Prim é utilizado para construir uma árvore que conecta todos os vértices de um grafo com o menor custo total, garantindo que não haja ciclos. Essa abordagem é amplamente usada em problemas de redes, planejamento de infraestrutura e otimização de conexões.

---

## Sobre o Algoritmo de Prim

O algoritmo de Prim inicia por um vértice arbitrário e, a cada iteração, adiciona a aresta de menor peso que conecta um vértice já incluído na MST a um vértice que ainda não faz parte dela. O processo continua até que todos os vértices estejam conectados. Essa técnica garante que o custo total da árvore geradora seja minimizado.

---

## Explicação do Código

### 1. Classe **Grafo**

- **Construtor (`__init__`):**  
  Inicializa o grafo com uma lista de adjacências (dicionário) e define se ele é orientado ou não.

- **Método `vertices()`:**  
  Retorna o conjunto de vértices do grafo.

- **Método `arestas(v_origem)`:**  
  Se um vértice de origem é fornecido, retorna as arestas desse vértice. Caso contrário, retorna as arestas de todo o grafo.

- **Método `v_arestas(v_origem)`:**  
  Itera sobre os vizinhos de um vértice e retorna as arestas com seus respectivos custos.

- **Método `inserir_arestas(u, v, custo)`:**  
  Insere uma aresta entre os vértices `u` e `v` com o custo especificado. Se o grafo não for orientado, a aresta é inserida em ambas as direções.

- **Método `inserir_aresta(arestas)`:**  
  Insere múltiplas arestas utilizando o método acima.

- **Método `imprimir()`:**  
  Exibe todas as arestas da MST e o custo total, ajustando para duplicidade caso o grafo seja não orientado.

### 2. Função **prim(grafo, inicio)**

Esta função implementa o algoritmo de Prim:
- **Inicialização:**  
  Cria uma MST vazia (grafo orientado) e insere uma aresta fictícia que conecta o vértice inicial a si mesmo com custo zero.

- **Loop Principal:**  
  Enquanto o conjunto de vértices da MST não for igual ao conjunto de vértices do grafo original:
  - Exibe o estado atual da MST e os vértices ainda não incluídos.
  - Adiciona as arestas do vértice atual à lista ordenada de arestas.
  - Ordena as arestas por custo.
  - Seleciona a aresta de menor custo que conecta um vértice já na MST a um vértice ainda não incluído e adiciona essa aresta à MST.
  - Atualiza o vértice atual e repete o processo.

- **Retorno:**  
  A função retorna o grafo MST, que é então impresso.

### 3. Uso do Algoritmo

O código define um conjunto de arestas e cria um grafo, insere as arestas e executa o algoritmo de Prim com o vértice inicial 'A'. Ao final, a MST é impressa com todas as arestas e o custo total.

---

## Como Executar

1. Certifique-se de ter o Python instalado.
2. Salve o código em um arquivo, por exemplo, `prim.py`.
3. Execute o script:
   ```bash
   python prim.py
   ```

---

## Considerações

- O algoritmo de Prim é eficiente para grafos conectados e encontra a MST com custo total mínimo.
- O código implementa uma abordagem simples utilizando listas e conjuntos para gerenciamento dos vértices e arestas.
- Para melhorar a eficiência e evitar loops infinitos, é importante chamar corretamente os métodos (por exemplo, `mst.vertices()`).

---

## Contato

- **GitHub:** [IsaqueAlmeida](https://github.com/IsaqueAlmeida)
- **LinkedIn:** [Isaque F. S. Almeida](https://www.linkedin.com/in/isaque-f-s-almeida/)

---

Este projeto demonstra conhecimentos em algoritmos de grafos e estruturas de dados, sendo uma aplicação prática do algoritmo de Prim para obtenção da árvore geradora mínima.

---
