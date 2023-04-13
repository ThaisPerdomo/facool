#include <stdio.h> 
// ^ Serve para trabalhar com funções e comandos de entrada e saída
#include <stdlib.h> 
// Ainda não sei o que faz

// Toda função em C deve ter um tipo de retorno, no caso, é inteiro.
// O método main é o método principal, onde o programa começa a ser executado, igual o App do React
int main (){
    // Declaração de variáveis
    
    char nome[30] = "";
    // ^ Declaração de variável, onde o tipo é caracter. 
    // O valor entre colchetes é o tamanho máximo da string. 
    // Deve-se declarar o tamanho máximo porque senão só vai pegar o primeiro caractere.

    int idade;
    // ^ Declaração de variável, onde o tipo é inteiro. Pode-se atribuir um valor a ela, mas não é obrigatório.

    float altura = 0.0;

    printf("\n Digite seu nome: ");
    // ^ Função que imprime na tela, sem quebra de linha.
    // Ao contrário de python etc, você precisa printar algo pra mandar uma mensagem junto com o input
    // Aqui é sem o & porque o nome é um vetor de caracteres, então não precisa do endereço de memória
    scanf("%29s", &nome);
    // ^ Função que recebe um valor do teclado. Neste caso, o valor é inteiro, então o %d e atribui-se a variável idade
    // ATENÇÃO: 
    // Aqui é sem o & porque o nome é um vetor de caracteres, então não precisa do endereço de memória

    printf("\n Digite sua idade: ");
    scanf("%d", &idade);
    // ^ Função que recebe um valor do teclado. Neste caso, o valor é inteiro, então o %d e atribui-se a variável idade com o &

    printf("\n Digite sua altura: ");
    scanf("%f", &altura);

    printf("\n Seu nome eh %s, vc tem %.2f de altura e %d anos", nome, altura, idade);
    // ^ Função que imprime na tela, com quebra de linha no inicio.
    
    return 0;
}
