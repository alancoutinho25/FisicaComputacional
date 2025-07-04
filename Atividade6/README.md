### Análise de Bandas de Energia em um Cristal 1D

---
### Bandas de Energia em um Cristal 1D (Modelo de Ondas Planas) - PARTE 1
---
Este projeto calcula e plota as bandas de energia de um cristal unidimensional com potencial periódico, utilizando o método das ondas planas para resolver a equação de Schrödinger no espaço recíproco.

### Hamiltoniano

Assumindo unidades atômicas (ℏ = 2m = 1) e potencial periódico com período R = 1, o vetor de recíproco é Gₙ = 2πn e a primeira zona de Brillouin é −π < k ≤ π.

A matriz Hamiltoniana no espaço de ondas planas é tridiagonal e dada por:

$$H(k) =
⎡ λ(k−G₋ₙ)−Eₖ α 0 ⋯ ⎤
⎢ α λ(k−G₋ₙ₊₁)−Eₖ α ⋯ ⎥
⎢ 0 α λ(k−G₋ₙ₊₂)−Eₖ ⋯ ⎥
⎢ ⋮ ⋮ ⋮ ⋱ ⎥$$

onde:
- λ(k−G) = |k − G|²
- α é a constante que representa a intensidade do potencial periódico (acoplamento entre ondas vizinhas)
- V₀ = 0 e Vᵢⱼ = α δᵢ,ⱼ±₁

Passos adotados para construção das bandas de energia:
- Construimos o Hamiltoniano H(k) tridiagonal para diferentes valores de k na 1ª zona de Brillouin;
- Diagonalizamos H(k) para obter os autovalores (bandas de energia);
- Plotamos as bandas de energia para diferentes valores de k;

### Resultados

As bandas obtidas mostram a formação de gaps de energia que crescem com o aumento de α. Quanto maior o número de ondas planas consideradas, mais precisa é a descrição das bandas. O modelo reproduz qualitativamente as Figuras 5.14 e 5.17 das notas de aula do prof. Rodrigo Capaz e a Figura 9.4 do livro de Ashcroft & Mermin.

---
### Cálculo de Bandas de Energia com Potencial Periódico $V(x)$ - PARTE 2
---
Estendemos o cálculo das bandas de energia de um cristal unidimensional utilizando a equação de ondas planas. Aqui, o potencial periódico $V(x)$ é escolhido como uma função explícita no espaço real, e a matriz $V_{mn}$ é calculada por meio de integração numérica.

### Potencial Periódico

Assumimos que o potencial satisfaz a condição de periodicidade:

$$
V(x) = V(x + R)
$$

com $R = 1$. Um exemplo usado neste projeto é:

$$
V(x) = A \cos(2\pi q x)
$$

onde $A$ e $q$ são parâmetros que definem a forma e periodicidade do potencial.

### Construção da Matriz $V_{mn}$

A matriz de acoplamento no espaço recíproco é dada por:

$$
V_{mn} = \\int_0^1 V(x) e^{-i 2\pi (m - n) x} dx
$$

## Hamiltoniano

A matriz Hamiltoniana no espaço de ondas planas é construída como:

$$
H_{mn}(k) = \delta_{mn} |k - G_n|^2 + V_{mn}
$$

onde $G_n = 2\pi n$, com $n \in [-N, N]$, e o termo $|k - G_n|^2$ representa a energia cinética.

Com isso, realizamos o seguinte procedimento:
- Definimos o potencial periódico $V(x)$ no espaço real
- Plotamos $V(x)$ para verificar sua forma
- Calculamos numericamente a matriz $V_{mn}$
- Construimos o Hamiltoniano $H(k)$ para cada valor de $k$ na 1ª zona de Brillouin ($-\\pi < k \\leq \\pi$)
- Diagonalizamos $H(k)$ para obter as bandas de energia
- Plotamos as primeiras bandas obtidas

### Resultados

Comparado ao modelo anterior (com matriz tridiagonal e acoplamento constante $\alpha$), este método permite simular potenciais mais realistas e estudar como diferentes formas de $V(x)$ afetam a abertura de gaps e o formato das bandas. A simetria e localização dos potenciais influencia diretamente a estrutura eletrônica do cristal.


