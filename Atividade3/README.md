### Rede neural simples para treinamento de funções trigonométricas e derivadas
#### Função Seno.
---

Nessa atividade nos propomos a construir uma rede neural para treinar funções trigonométricas e derivadas. O objetivo é implementar uma rede neural simples usando PyTorch, SKLearn
e TensorFlow.

Nessa pasta adiciono o código que criei usando o PyTorch em .ipynb. Esse texto é uma explicação breve acerca dos principais resultados.

---

Começamos importando os módulos do PyTorch, como $torch.nn$ e $torch.optim$. Esses módulos serão usados para criar nossa rede neural, pois utilizando orientação a objetos,
criamos uma classe que herdará os recursos da biblioteca do PyTorch. Além disso, as bibliotecas importadas possuem os módulos de treinamento $model.train()$ e previsão $model.eval()$.
Também serão usadas as funções de perda (**MSE**) e otimização (**Adam**) do $torch.optim$.

A rede neural utiliza funções de ativação para treinar (ReLU, Tanh, Linear, etc.). Essas funções inicializam pesos e bias aleatórios.
Se não usarmos uma semente, toda vez que rodarmos o script, os valores dos pesos e bias serão diferentes e isso pode gerar resultados não reproduzíveis.
Por isso iniciamos uma semente para o numpy e para o torch (tensores do torch). Assim, toda vez que a função de ativação for usada, iniciará sempre os mesmos valores aleatórios de w e b.

Em $num_samples=100$ criamos o número de ângulos que vamos utilizar para o treinamento da rede. Os dados de treino são criados como dois arrays contendo 100 amostras. O primeiro array
angles_train contém 100 ângulos no intervalo de $0$ a $4\pi$ e sin_values_train contém o $sen(x)$ de cada ângulo acrescido de um ruído criado usando o np.random.normal(). É um valor pequeno
adicionado ao seno para tornar o treinamento mais realista. Finalmente usa-se um método reshape para tornar o array linha em uma matriz coluna. Isso será necessário porque na camada
de entrada, teremos um único neurônio.

Depois transformamos os arrays em tensores usando o torch.tensor, pois os módulos do PyTorch trabalham com esse tipo de variável.

Em seguida vamos definir o nosso modelo de rede neural. Em PyTorch, isso significa criar uma classe que depois será instanciada em um objeto que será o nosso modelo de rede neural.
No TensorFlow e no SkLearn alguns modelos estão prontos, não precisamos criar a classe, apenas instanciar uma classe já criada passando parâmetros. No loop $for$ que vamos criar para
construir camadas da rede, a função de ativação nn.Linear(a,b) cria uma camada conectada em que existem $a$ camadas com $b$ neurônios em cada uma.
Normalmente $a=1$ então teremos $a$ dados (ângulos) de entrada ($\phi_i$) e esses ângulos são atualizados ($\theta_i$) com o cálculo dos pesos ($w_{ij}$) e bias ($b_i$):

$$\theta_i = \sum_{j=1}^aw_{ij}\cdot \phi_i+b_i$$

Mas essa função de ativação linear fornece valores aleatórios. Por isso usamos uma outra função não linear cujas saídas estão no intervalo $[-1,1]$, a nn.Tanh(). Então,
aplicando na nossa rede neural, temos nn.Linear(1,10) $\Rightarrow$ uma única camada, recebe um único ângulo, libera 10 valores de saída. Depois nn.Tanh() $\Rightarrow$ pega 10 valores e aplica a função não linear e passa para a próxima camada.

Lembrando que

$$tanh(x)=\dfrac{e^x-e^{-x}}{e^x+e^{-x}}$$

Depois implementamos uma função de perda (loss funtion). A função de perda é fundamental para redes neurais enquanto ocorrem as etapas do treinamento da rede, pois somente com elas é que a rede vai aprender e ajustar
os pesos e bias para previsão de valores mais próximos da realdiade. Por exemplo, podemos usar o desvio quadrático médio (MSE) ou outras funções que verificam a diferença entre o valor real do seno e o valor
calculado pela rede.

Se a diferença foi maior que o valor da função de perda, então o otimizador (Adam) (definido a frente) vai ajustar os pesos e bias das camadas ocultas para ajustar melhor o valor.
Isso ocorre durante a iteração das chamadas épocas que veremos quando implementarmos o loop para cálculo do seno.

Na etapa do treinamento do nosso modelo criamos um loop for de iterações, em que em cada época, o modelo recebe um valor de entrada, passa por todas as camadas, obtém um output,
calcula a função de perda, verifica o otimizador e armazena em um array de dados previstos.

No model.train() colocamos a rede em "estado" de treinamento, os valores aqui são calculados para se obter uma espécie de padrão da rede em reconhecer a função seno. Os gradientes dos
erros calculados pela função de perda são usados para atualização dos pesos e bias e a cada $500$ iterações (épocas) acompanhamos esses cálculos para verificar o progresso.

Finalmente usamos o model.eval() que faz predições dos valores para um intervalo escolhido. Verificamos que a rede foi treinada no intervalo de $0$ a $4\pi$, mas as predições foram
feitas no intervalo de $0$ a $6\pi$ e o gráfico mostra que após $4\pi$ a previsão da rede começa a estrapolar (desviar significativamente).

---

#### Derivadas

---
