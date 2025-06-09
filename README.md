Essa parte é responsável por explicar o que está acontecendo no código

O código main.py, tem como função executar um Quiz, onde o usuário pode interagir usando o terminal e sistema de 'input'.

O quiz conta com 20 perguntas diversificadas sobre um único tema que é DC, cada pergunta possui 4 alternativas (de A a D). Também conta com sistema de pontuação, que aparece a cada pergunta que você responde e também no final.

O sistema do quiz conta com função, if...else e input. A função principal é a 'checarResposta' que checa se a resposta apresentada no input é igual a resposta da pergunta. Caso for adiciona um ponto para o usuário e diz que ele acertou a pergunta, caso erre, ainda mostra a pontuação, mas diz que ele errou. Após a verificação de acerto, é retornado o valor do score para definir a pontuação geral na varíavel 'globalScore'.

No mais, cada pergunta é diversificada como havia dito antes, e no final de cada pergunta a função 'checarResposta' é chamada definindo a varíavel 'globalScore' para que a pontuação esteja sempre sendo atualizada.