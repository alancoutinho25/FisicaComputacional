### Atividade 1
Gradiente Descendente

---

#### Exercício 1

No exercício 1 ao ajustar a taxa de aprendizado $\alpha=0,9$ nota-se que a convergência até o mínimo é representada por uma trajetória dos pontos $x_n$ oscilando entre os dois lados da parábola. Com esse valor de $\alpha$ é possível uma melhor visualização do método do Gradiente Divergente, no sentido de que se percebe a oscilação dos valores de $f(x_n)$ até se obter o mínimo. Se $0,6\leq\alpha\leq 0,9$ a trajetória de convergência começa a oscilar na parábola.

![download](https://github.com/user-attachments/assets/8b7075a9-d412-4a2b-84ad-260164bee502)

Quando a taxa de aprendizado é muito pequena, $\alpha=0,03$, a convergência ocorre lentamente somente por um dos lados da parábola até o mínimo, dependendo do sinal de $x_0$. Se $x_0$ for positivo, apenas pelo lado direito. Por outro lado, se $x_0<0$ a convergência ocorre pelo lado esquerdo.

![download](https://github.com/user-attachments/assets/08f62b1c-8f80-4b07-8806-f0797d89b790)



#### Exercícios 2 e 3 

Nos exercícios seguintes, as funções a serem minimizadas são $v(x)=x^4-x^2$ e $w(x)=x^4-x^2+\frac{x}{4}$. A função $w(x)$ faz com que um dos mínimos locais, do lado positivo do gráfico, se desloque para cima (na direção $\hat{y}$, tornando-o mínimo local enquanto o outro mínimo é global. Com relação à convergência, para $\alpha=0,9$ verifica-se a oscilação entre os mínimos locais na trajetória de $x$ em ambas as funções. Dependendo do valor inicial $x_0$ os valores de $v(x)$ e $w(x)$ divergem rapidamente dado a potência de 4ª ordem das funções. Por isso o valor inicial de $x_0$ foi ajustado para $x_0=0,9$.
![download](https://github.com/user-attachments/assets/f46786ff-5e2e-4fb7-bb0e-160b133e88af)

![download](https://github.com/user-attachments/assets/7ca1e2b2-c234-4405-bff7-ae479381ac44)

Para os valores de taxa de aprendizado até $\alpha=0,7$ as trajetórias ficam limitadas a um lado dos gráficos, isto é, em apenas um mínimo local, dependendo do sinal de $x_0$. A função $w(x)$, a partir de $\alpha=0,7$ começa a oscilar entre os dois minimos.

![download](https://github.com/user-attachments/assets/b478f669-2d9c-4702-bee1-0d27d4d609a4)

![download](https://github.com/user-attachments/assets/efd44bc2-1023-4cd8-a2a7-d35887e98a51)



#### Exercício 4

No exercício 4 ao variar a posição inicial definida pelo ponto $(x_0,y_0)$ verifica-se que antes de alcançar o mínimo, a trajetória dos pontos é modificada, indicada pela linha vermelha traçada no gráfico de contorno. A velocidade de convergência parece não sofrer alteração com a modificação apenas dos pontos iniciais. Percebe-se também que a trajetória dos pontos traça um caminho até mínimos locais diferentes para parâmetros $(x_0,y_0)$ diferentes.

Quando variamos a taxa de aprendizado $\alpha$ verifica-se que a curva de convergência representada pelo gráfico de iterações, sofre alteração, isto é, se aumentarmos a taxa de aprendizado, a convergência se torna mais "abrupta". A medida que diminuímos a taxa de aprendizado, a convergência é mais lenta e representada por uma curva menos "suave".
![download](https://github.com/user-attachments/assets/337ba302-0fe4-4ea3-9ab0-a29d25c0341e)
