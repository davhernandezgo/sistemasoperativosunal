/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>

void so_strcpy(char str1[], char str2[]){
    int i=0;
    while (str1[i] != '\0') { 
        str2[i]=str1[i];
        i++;
    }
}
int main()
{
    char string1 []="cadena1";
    char string2 [30];
    so_strcpy(string1, string2);
    printf("La cadena dos es: %s", string2);

    return 0;
}
