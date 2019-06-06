#include <stdio.h>

int main(){
   for(int i = 1; i <= 50;i++){
        if(i%2==0){
            printf("%i par\n", i);
        }else{
            printf("%i impar\n", i);
        }
    }
   return 0;
}
