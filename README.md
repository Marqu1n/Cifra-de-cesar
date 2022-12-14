# Cifra-de-cesar

## Explicação geral

O propósito do código é criptografar mensagens utilizando a [Cifra de César](https://pt.wikipedia.org/wiki/Cifra_de_C%C3%A9sar). A cifra de césar é um metodo de criptografia utilizado por Julio César e consiste em alterar cada letra de uma palavra um número x de casas.
O código codifica, decodifica com uma chave e decodifica por força bruta.
Durante a codificação, o código percorre todas as letras da palavra e as que estiverem na lista "alphabet" são alteradas "shift" casas para a frente.
A decodificação faz o contrário, pois muda "shift" casas para trás.

## Explicação das [Funções](https://docs.python.org/pt-br/3.10/tutorial/controlflow.html#defining-functions)
As funções são blocos de códigos que são definidos pela palavra reservada "def", o nome da função e os parâmetros, com os parâmetros sendo opcionais. Ademais, o motivo das funções existirem é bem simples, sempre que for necessário usar várias linhas de código para executar uma tarefa é usado uma função. Ela funciona como uma variável para linhas de código, sendo que é possivel armazenar diversas linhas de código dentro delas, simplificando o seu código.

As funções existentes no código são: encrypt(msg,num), decrypt(msg,num) e main().

As primeiras 2 são descritas acima, tendo como proposito codificar e decodificar com a chave.

A função "main()" é basicamente o esqueleto do código, pois ela verifica se o usuário quer codificar ou decodificar com chave. Além disso, a função alerta se o usuário tiver digitado sua escolha errada e coleta a mensagem do usuário e a chave, caso seja necessário.

## Documentação do Python

### [Documentação](https://docs.python.org/pt-br/3.10/tutorial)
