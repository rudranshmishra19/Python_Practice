#include <stdio.h>
#include <stdlib.h>

int main() {
    int arr[]={1,2,3,1,45,6,3};
    int count_frequency=0;
    int n =sizeof(arr)/sizeof(arr[0]);
    for(int i =0;i<n;i++){
      for (int j=i+1;j<n;j++){
             if (arr[j]==arr[i]){

              count_frequency++;
             }
      }
    }
printf("%d",count_frequency);    
    return 0;
}