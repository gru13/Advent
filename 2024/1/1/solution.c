#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main(){
    FILE* fp = fopen("./input-full.txt", "r");
    
    while (fgetc(fp) != EOF)
    {
        int a, b;
        fscanf(fp, "%d\t%d", &a, &b);
        printf("%d %d\n", a, b);
    }
    fclose(fp);
    return 0;
}