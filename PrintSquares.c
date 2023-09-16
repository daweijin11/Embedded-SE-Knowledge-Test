#include <stdio.h>
#include <stdlib.h>
int main() {
   int N,M;
   printf("Please Enter N: ");
   scanf("%d",&N);
   printf("The Value of N is %d\n", N);
   printf("Please Enter M: ");
   scanf("%d",&M);
   printf("The Value of M is %d\n", M);
   void Square(int N, int M){
        if (N <= 0 || M <= 0) {
            printf("invalid value for N and M. N and M must be positive integers");
            return 0;
        }
        while (N > 0 && M > 0) {
            if(N > M) {
                printf("%dx%d ",M,M);
                N -= M;
            }
            if(N <= M) {
                printf("%dx%d ",N,N);
                M -= N;
            }
    }
   }
   Square(N,M);
   return;
}
