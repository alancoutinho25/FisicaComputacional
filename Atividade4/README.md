### PINN (rede neural informada pela física)
---
Nesta atividade criamos uma PINN, uma rede neural informada pela física, que além de ser capaz de se adaptar e reproduzir os dados já possuídos, também é capaz de compreender e utilizar
os padrões físicos e as condições de contorno de um sistema físico real. Isso é possível quando se conhece, além de alguns dados (ainda que não suficientes para treinar uma NN de regressão
simples), mas também uma equação diferencial que exprima o padrão de tais dados.

No exemplo trabalhado nessa atividade, usamos o caso do resfriamento. A equação diferencial que descreve o resfriamento é dada por:

$$ \dfrac{dT(t)}{dt} = r\cdot (T_a - T(t)) $$

onde $r=0.005$ é uma taxa de resfriamento, $T_a=25°C$ é a temperatura ambiente e $T(t)$ é a temperatura em função do tempo.

#### Métodos
---

Iniciei gerando a solução analítica dessa equação diferencial, que é:

$$ T(t) = T_a - (T_0 - T(t))\cdot e^{-rt} $$

onde $T_0=100°C$ é a temperatura inicial.

Assim gerei um gráfico que descrevesse o comportamento dessa função analiticamente obtida num intervalo de tempo entre $0s$ a $1000s$. Depois gerei uma aproximação da solução da equação
diferencial por método de Runge-Kutta 4ª ordem, que implementei no código. Mas dessa solução, tomei 10 pontos no intervalo entre $0s$ a $200s$, o resultado ficou muito satisfatório, pois
o método RK4 é de ótima aproximação para o problema de valor incial. Entretanto, para gerar dados mais realistas, acrecentei um ruído aos dados obtidos por RK4 e os treinei em uma rede
neural de regressão simples, que chamei de testenn.

O modelo descreveu os dados de forma satisfatória, mas quando tentamos extrapolar os dados, o resultado é extremamente discrepante dos dados de treino ou do resultado analítico. Sendo assim
ficou comprovada a necessidade de adaptação da rede.

#### Implementação da PINN

----

Uma PINN (Physics-Informed Neural Network) é uma rede neural que, além de aprender com dados, é treinada para satisfazer a equação diferencial do sistema. No nosso caso, a equação de resfriamento de Newton:

$$ \dfrac{dT(t)}{dt} = r\cdot (T_a - T(t)) $$

A principal modificação introduzida por uma PINN é a adição de um termo de perda extra, chamado de perda física ou loss_physics, que mede o erro entre o lado esquerdo e o lado direito da equação diferencial.
O PyTorch permite calcular derivadas automaticamente com torch.autograd.grad. Isso é fundamental para PINNs, pois permite calcular: $\dfrac{dT}{dt}$, onde $T(t)$ é a predição da rede.

Para isso, usamos: 

dT_dt = torch.autograd.grad(T_pred, t_input, grad_outputs=torch.ones_like(T_pred), create_graph=True)[0]

Essa linha faz com que o PyTorch calcule a derivada de T_pred com relação a t_input, mantendo o grafo computacional (para futuras derivadas se necessário).

Com isso a rede foi capaz de extrapolar os dados, obedecendo às condições de contorno e ao comportamento da equação diferencial proposta.
