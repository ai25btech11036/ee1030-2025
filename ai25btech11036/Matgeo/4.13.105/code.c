#include <stdio.h>

int main() {
    double alpha, beta, l;

    // Input alpha and beta
    printf("Enter value of alpha: ");
    scanf("%lf", &alpha);
    printf("Enter value of beta: ");
    scanf("%lf", &beta);

    // Check coplanarity condition:
    // (alpha + beta + 1) = 0
    if ((alpha + beta + 1) != 0) {
        printf("Vectors are not coplanar. No solution.\n");
        return 0;
    }

    // Plane: 3x + 3y - z + l = 0
    // Point (alpha, beta, 2) lies on plane
    l = -(3*alpha + 3*beta - 2);

    printf("The value of l is: %.2f\n", l);

    return 0;
}