#include <stdio.h>

int main() {
    int A[2][2] = {{-3, 6}, {-2, 4}};
    int A2[2][2], A3[2][2];
    int i, j, k;

    // Compute A^2 = A * A
    for (i = 0; i < 2; i++) {
        for (j = 0; j < 2; j++) {
            A2[i][j] = 0;
            for (k = 0; k < 2; k++) {
                A2[i][j] += A[i][k] * A[k][j];
            }
        }
    }

    // Compute A^3 = A^2 * A
    for (i = 0; i < 2; i++) {
        for (j = 0; j < 2; j++) {
            A3[i][j] = 0;
            for (k = 0; k < 2; k++) {
                A3[i][j] += A2[i][k] * A[k][j];
            }
        }
    }

    // Print A
    printf("Matrix A:\n");
    for (i = 0; i < 2; i++) {
        for (j = 0; j < 2; j++) {
            printf("%3d ", A[i][j]);
        }
        printf("\n");
    }

    // Print A^2
    printf("\nMatrix A^2:\n");
    for (i = 0; i < 2; i++) {
        for (j = 0; j < 2; j++) {
            printf("%3d ", A2[i][j]);
        }
        printf("\n");
    }

    // Print A^3
    printf("\nMatrix A^3:\n");
    for (i = 0; i < 2; i++) {
        for (j = 0; j < 2; j++) {
            printf("%3d ", A3[i][j]);
        }
        printf("\n");
    }

    // Verify A^3 = A
    int flag = 1;
    for (i = 0; i < 2; i++) {
        for (j = 0; j < 2; j++) {
            if (A3[i][j] != A[i][j]) {
                flag = 0;
                break;
            }
        }
    }

    if (flag)
        printf("\nVerified: A^3 = A\n");
    else
        printf("\nVerification failed: A^3 != A\n");

    return 0;
}