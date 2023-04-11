#include <stdio.h>
#include <stdlib.h>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char** argv) {
	
	float salario_bruto, inss, salario_liquido;
		
	printf("Qual eh o seu salario? ");
	
	scanf("%f", &salario_bruto);
	
	
	if (salario_bruto < 5646.80){
		
		if (salario_bruto <= 1693.72) {
		inss = 0.08;
		}
		else
		if (salario_bruto > 1693.72 && salario_bruto <= 2822.90){
			inss = 0.09;
		}
		else {
			inss = 0.11;
		}
		
		salario_liquido = salario_bruto * inss;
		
	} else {
		inss = 621.04;
		salario_liquido = salario_bruto - inss;
	}
	
	printf("\n Seu salario bruto eh %.2f", salario_bruto); 
	printf("\n Seu INSS fica em %.2f", inss);
	printf("\n O resultado eh um salario liquido de %.2f \n", salario_liquido);
	
	system("pause");
	
	return 0;
}
