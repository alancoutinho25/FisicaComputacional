### Classe Partícula e método Newton
---
Nesta atividade, criamos uma classe chamada Particula que inicializa variáveis de posição $(x,y)$ e velocidades $(v_x,v_y)$ e a massa $m$ da partícula. A classe possui um método denominado
newton que recebe os valores das compoenentes da força $F_x$ e $F_y$ e o incremento (ou tamanho do intervalo) de tempo $dt$. Assim, o método newton atualiza a posição $(x,y)$ e a velocidade
$(v_x,v_y)$ da partícula usando a segunda lei de Newton: $$\vec{F}=m\vec{a}$$.

Da segunda lei retiramos as seguintes equações:

* $a_x=\dfrac{F_x}{m}$
* $a_y=\dfrac{F_y}{m}$
* $v_x=v_0+a_x\cdot dt$
* $v_y=v_0+a_y\cdot dt$
* $x=x_0+v_x\cdot dt$
* $y=y_0+v_y\cdot dt$

O código implementa tais equações na classe Particula para que toda vez que uma instância da classe for criada com parâmetros de inicialização adequados (posição e velocidade iniciais) o
método newton funcione como atualização das variáveis que descrevem a trajetória da partícula.

No código exemplo01.py criamos uma trajetória balística, isto é, uma partícula que se move em 2D com uma velocidade inicial em ambas as direções, $v_x=v_y=10m/s$. Saindo da origem $(x_0=0,y_0=0)$
aplicamos uma força constante na direção vertical $F_y=-9.8$ e usamos a classe partícula e o método newton para atualizar a trajetória parabólica. O tempo total do percurso da partícula é
$t=5s$, subdividido em intervalos de $dt=0.1s$.

A figura abaixo ilustra o resultado obtido.

![download](https://github.com/user-attachments/assets/a7bf9fda-ecd3-42de-9f50-53eef75cc529)
