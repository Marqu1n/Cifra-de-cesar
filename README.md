<h1>Cifra-de-cesar</h1>


<h2>Explicação Geral</h2>

O propósito do código é codificar uma mensagem utilizando a <a href = 'https://pt.wikipedia.org/wiki/Cifra_de_C%C3%A9sar'>Cifra de César</a>.<br> O código funciona alterando letra por ela pelo valor de shift.

<h2>Explicação das palavras reservadas</h2>
<h3><a href=https://docs.python.org/pt-br/3.10/tutorial/controlflow.html#defining-functions>Funções</a></h3>

def Função(<i>parametro<i>)<br>
    Defini uma função, que é basicamente um bloco de código que pode ser chamado em qualquer linha de código. A função pode receber quantos parametros o programador quiser, os quais, tem como função de uma variavel local, ou seja, ela só existe dentro da função.
    Ex.:
    x=1
    y=1
    #As variáveis acima são variáveis globais, ou seja, podem ser acessadas durante todo o código
    def soma():
        x=2
        y=2
        #As variáveis acima são variáveis locais
        print("A soma de x e y é:", x+y)
    print("a multiplicação de x e y é:",x*y )
    soma()
 
