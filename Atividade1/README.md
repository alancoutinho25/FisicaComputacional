# Atividade 1

No exercício 1 ao ajustar a taxa de aprendizado $\alpha=0,9$ nota-se que a convergência até o mínimo é lenta e a trajetória dos pontos $x_n$ oscila entre os dois lados da parábola. Com esse parâmetro é possível uma melhor visualização do método do Gradiente Divergente, no sentido de que se percebe a oscilação dos valores de $f(x_n)$ até se obter o mínimo.

![download](https://github.com/user-attachments/assets/ed655683-639b-447c-b59e-ed6256df29d8)

Observa-se que quando $\alpha= 0.5$ a convergência ocorre rapidamente para o mínimo.

![download](https://github.com/user-attachments/assets/d0807f7a-cece-4d0f-a9db-e04d6fae092a)

Se $0,6\leq\alpha\neq 0,9$ a trajetória de convergência começa a oscilar na parábola.

![download](https://github.com/user-attachments/assets/653c18aa-8685-453e-9b6f-8b18384b9519)

axa de aprendizado for $\alpha<0,9$ e $x_0>0$, a convergência ocorre lentamente somente do "lado positivo" ou do lado direito da parábola até o mínimo. Se a $\alpha<0.1$ a convergência não atinge o mínimo global. Por outro lado, se $x_0<0$ a convergência ocorre pelo lado esquerdo ou negativo.

![download](https://github.com/user-attachments/assets/4f3fb2f0-e36f-4508-bd89-96b118b6a55c)


![download](https://github.com/user-attachments/assets/cbba3f35-f3f5-4583-a89f-d4ac075323af)





![download](https://github.com/user-attachments/assets/2c7d08eb-eaec-4357-886e-33b2493a898a)


Para a taxa de aprenddizado $\alpha>0.9$ a convergência também ocorre de apenas um dos lados da parábola (dependendo do sinal de $x_0$) mas de forma muito mais rápida.

# Exercícios 2 e 3 




# Exercício 4

No exercício 4 ao variar a posição inicial definida pelo ponto $(x_0,y_0)$ verifica-se que antes de alcançar o mínimo, a trajetória dos pontos é modificada, indicada pela linha vermelha traçada no gráfico de contorno. A velocidade de convergência parece não sofrer alteração com a modificação apenas dos pontos iniciais. Percebe-se também que a trajetória dos pontos traça um caminho até mínimos locais diferentes para parâmetros $(x_0,y_0)$ diferentes.

Quando variamos a taxa de aprendizado $\alpha$ verifica-se que a curva de convergência representada pelo gráfico de iterações, sofre alteração, isto é, se aumentarmos a taxa de aprendizado, a convergência se torna mais "abrupta". A medida que diminuímos a taxa de aprendizado, a convergência é mais lenta e representada por uma curva menos "suave".
