#include<stdio.h>

int main(){
    int p ,r ,t, si;
    //int si;
   printf("Enter the prcinpal ,rate of interest and time to calculate simple interest rate ");
   scanf("%d,%d,%d ",&p,&r,&t);
   printf("The simple interest is %d ", p*r*t/100);
    return 0;
}