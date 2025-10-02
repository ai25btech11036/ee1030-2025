#include <stdio.h>

int main() {
    // Coefficient matrix A
    float a11 = 7, a12 = 2;
    float a21 = 4, a22 = -1;

    // Constants vector b
    float b1 = 11, b2 = 2;

    // Determinant of A
    float det = a11 * a22 - a12 * a21;

    if (det == 0) {
        printf("No unique solution exists.\n");
    } else {
        // Inverse method (Cramer's rule could also be used)
        float u = ( (b1 * a22) - (a12 * b2) ) / det;
        float v = ( (a11 * b2) - (b1 * a21) ) / det;

        printf("Solution:\n");
        printf("u = %.2f\n", u);
        printf("v = %.2f\n", v);
    }

    return 0;
}