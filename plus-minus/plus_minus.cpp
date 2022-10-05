#include<stdio.h>
#include<iostream>
#include<math.h>
#include<locale.h>
#include<stdlib.h>

// 2010840 - Gabriele Cardoso das Virgens

/*  Aula X - DD/MM/AAAA
	ESTRUTURA DE DADOS

    ****** CONTE�DO ******
*/

void plusMinus(int n, int* arr) {
    
    int pos=0, neg=0, zer=0;
    float p_ratio = 0;
    float n_ratio = 0;
    float z_ratio = 0;
    
    //printf("%i", n);
    
    for(int i=0; i<n; i++){
    	
        if (arr[i] == 0){
            zer++;
        }else if(arr[i] < 0){
            neg++;
        }else{
            pos++;
        }	
    }
    
    p_ratio = float(pos)/n;
    n_ratio = float(neg)/n;
    z_ratio = float(zer)/n;
      
	printf("%f\n", p_ratio);
	printf("%f\n", n_ratio);
	printf("%f\n", z_ratio);
}

int main(){

	setlocale(LC_ALL, "Portuguese");
	
	const int n = 6;
	int arr[n]= {-4, 3, -9, 0, 4, 1};
	
	plusMinus(n, arr);
	
	return 0;
}

