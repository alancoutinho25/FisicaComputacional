# 📁 Análise de Bandas de Energia em um Cristal 1D

Este repositório contém códigos em Python para calcular **bandas de energia eletrônica** em um cristal unidimensional periódico, usando a **equação de ondas planas** em unidades atômicas reduzidas (ℯ = 2m = 1). O objetivo é estudar como diferentes potenciais periódicos afetam a estrutura de bandas.

---

## ⚙️ Parte 1: Modelo com Acoplamento Simples entre Ondas Planas

Na primeira parte, consideramos um modelo simplificado em que o potencial periódico é incluído apenas por meio de **acoplamentos entre ondas planas vizinhas**. O Hamiltoniano é dado por:

$$
H_{ij} = |k - G_i|^2 \delta_{ij} + \alpha (\delta_{i,j+1} + \delta_{i,j-1})
$$

- Os vetores de onda seguem \(G_n = 2\pi n\), com periodicidade \(R = 1\).
- O termo cinético \(|k - G_i|^2\) representa a energia livre do elétron.
- O termo \(\alpha\) modela o efeito do potencial periódico de forma simples.

### 📊 Resultados

- As bandas de energia são simétricas em torno de \(k = 0\).
- Lacunas de energia aparecem nas bordas da zona de Brillouin.
- O valor de \(\alpha\) controla a largura das lacunas.

---

Na segunda parte, substituímos o modelo simplificado por potenciais reais definidos no espaço real. Exemplos utilizados:

- \(V(x) = A \cos(2\pi q x)\)
- Potenciais gaussianos:
  - \(V(x) = -A e^{-x^2 / 2\gamma^2}\)
  - \(V(x) = -A e^{-(x - \tfrac{1}{4})^2 / 2\gamma^2} - B e^{-(x + \tfrac{1}{4})^2 / 2\gamma^2}\)

Calculamos a matriz de potencial \(V_{mn}\) diretamente por:

$$
V_{mn} = \int_0^1 V(x) e^{-i 2\pi (m - n)x} dx
$$

Assim, o Hamiltoniano total é dado por:

$$
H_{mn}(k) = |k - G_m|^2 \delta_{mn} + V_{mn}
$$

### 📊 Resultados

- O perfil das bandas muda conforme a forma de \(V(x)\).
- Potenciais localizados resultam em acoplamentos fracos entre modos distantes.
- Potenciais assimétricos podem abrir ou fechar lacunas em diferentes pontos da zona de Brillouin.

---

## 🧪 Comparativo entre os Modelos

| Aspecto           | Modelo Simplificado              | Potencial Real                       |
| ----------------- | -------------------------------- | ------------------------------------ |
| Forma de \(V\)    | \(\alpha \delta_{i,j\pm1}\)      | Função \(V(x)\) periódica            |
| Matriz \(V_{mn}\) | Tridiagonal (diagonais vizinhas) | Matriz densa com decaimento          |
| Grau de controle  | Parâmetro \(\alpha\)             | Forma, largura, posição do potencial |
| Precisão          | Aproximação qualitativa          | Representação física realista        |

---

## 📊 Visualizações Disponíveis

- Gráfico do potencial \(V(x)\) no intervalo \([0, 1]\) para inspeção visual da periodicidade e forma.
- Gráficos das **bandas de energia** \(E_n(k)\) para \(k \in [-\pi, \pi]\).
- Impressão da matriz \(V_{mn}\) para análise da estrutura de acoplamento.

---

## 🚀 Como Executar

Instale as dependências com:

```bash
pip install numpy matplotlib scipy
```

Execute os scripts Python desejados. Parâmetros como o tipo de potencial, o número de ondas planas (\(G\)), e a intensidade dos poços podem ser modificados diretamente nos scripts para explorar diferentes configurações.

---

## 💡 Sugestões de Exploração

- Experimente variar \(\gamma\) para observar como o alargamento da gaussiana afeta os acoplamentos.
- Use diferentes funções \(V(x)\) periódicas, como serrotes, quadradas, ou combinações harmônicas.
- Calcule e plote os autovetores para observar a localização dos estados.

---

Para dúvidas ou melhorias, sinta-se à vontade para abrir uma *issue* ou *pull request*!

