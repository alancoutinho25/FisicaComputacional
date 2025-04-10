# Atividade 1

No exercício 1 ao ajustar a taxa de aprendizado $\alpha=0,9$ nota-se que a convergência até o mínimo é representada por uma trajetória dos pontos $x_n$ oscilando entre os dois lados da parábola. Com esse valor de $\alpha$ é possível uma melhor visualização do método do Gradiente Divergente, no sentido de que se percebe a oscilação dos valores de $f(x_n)$ até se obter o mínimo.

![download](https://github.com/user-attachments/assets/b7c15043-d472-4677-9fbd-5277067c7e35)

Se $0,6\leq\alpha\leq 0,9$ a trajetória de convergência começa a oscilar na parábola.

![download](https://github.com/user-attachments/assets/2c7d08eb-eaec-4357-886e-33b2493a898a)

Quando a taxa de aprendizado é muito pequena, $\alpha=0,03$, a convergência ocorre lentamente somente por um dos lados da parábola até o mínimo, dependendo do sinal de $x_0$. Se $x_0$ for positivo, apenas pelo lado direito. Por outro lado, se $x_0<0$ a convergência ocorre pelo lado esquerdo.

![download](https://github.com/user-attachments/assets/4f3fb2f0-e36f-4508-bd89-96b118b6a55c)   ![download](https://github.com/user-attachments/assets/6c5689c2-9a38-4e18-b4a7-b1f0d7beb017)

# Exercícios 2 e 3 




# Exercício 4

No exercício 4 ao variar a posição inicial definida pelo ponto $(x_0,y_0)$ verifica-se que antes de alcançar o mínimo, a trajetória dos pontos é modificada, indicada pela linha vermelha traçada no gráfico de contorno. A velocidade de convergência parece não sofrer alteração com a modificação apenas dos pontos iniciais. Percebe-se também que a trajetória dos pontos traça um caminho até mínimos locais diferentes para parâmetros $(x_0,y_0)$ diferentes.

Quando variamos a taxa de aprendizado $\alpha$ verifica-se que a curva de convergência representada pelo gráfico de iterações, sofre alteração, isto é, se aumentarmos a taxa de aprendizado, a convergência se torna mais "abrupta". A medida que diminuímos a taxa de aprendizado, a convergência é mais lenta e representada por uma curva menos "suave".
