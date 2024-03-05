
/*
#include <stdio.h>
#include <omp.h>

int main(int argc, char const *argv[])
{
    int N = 10000;
    int myArray[10000];
    
    #pragma omp parallel for
    for(int i=0; i<N; i++){
        myArray[i] = i * 2;
    
    }
    return 0;
}



/*

#include <stdio.h>
#include <omp.h>
#include <stdbool.h>

int main(int argc, char const *argv[]){
    int start = 1, end = 100;
    int moves_counter = 0;
    int binaryNum = 0;
    int minNum, maxNum;
    int numForSearch;

    bool flag = false;
    #pragma omp parallel

     while(flag == false){
         moves_counter += 1;
            binaryNum = (minNum + maxNum) / 2;
     }
    if(numForSearch < binaryNum){
        maxNum = binaryNum - 1;
    }
    else if(numForSearch > binaryNum){
        minNum = binaryNum + 1;
    }
    else if(numForSearch == binaryNum){
        printf("The number was %d and was found in  place %d tries" ,numForSearch, moves_counter);
        printf("The range was between " , start , "to ", end);
        flag = true;
    }

    return 0;
}
*/
#include <stdio.h>
#include <omp.h>

int main(int argc, char const *argv[]){

        #pragma omp parallel sections 
{
    printf("\nSection 1");
        #pragma omp section
{
            for(int i=0; i<100; i++){
            printf("\nMy Id is %d", omp_get_thread_num());
   }
}
                printf("\nSection 2!");
        #pragma omp section
        {
            for(int i=0; i<100; i++){
            printf("\nMy Id is %d", omp_get_thread_num());
        }
    }
                printf("\nSection 3!");
        #pragma omp section
        {
         for(int i=0; i<100; i++){
         printf("\nMy Id is %d", omp_get_thread_num());
  }
 }
}
printf("\n\n");
    return 0;
}







