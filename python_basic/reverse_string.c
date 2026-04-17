#include <stdio.h>
#include <string.h>
char* reverse_string(char s[]){
    int len=strlen(s);
    static char result[100];
    for(int i=0;i<len;i++){
        result[i]=s[len -1 -i];

    }
    result[len]='\0';
    return result;
}
int main() {
    char s[]="Rudransh";
    printf("%s\n",reverse_string(s));
    return 0;
}