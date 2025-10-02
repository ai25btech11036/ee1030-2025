#include <stdio.h>

int main() {
    // Given circle: (u - (1,0))^T (u - (1,0)) = 1
    // Midpoint coordinates (m1, m2)
    double m1, m2;

    printf("The given circle is (x-1)^2 + y^2 = 1\n");
    printf("Equation in standard form: u^T u + 2c^T u + f = 0\n");
    printf("where c = (-1,0), f = 0\n\n");

    printf("Condition for midpoint (m1, m2) of chord through origin:\n");
    printf("   m^T c + m^T m = 0\n\n");

    printf("Substituting c = (-1,0):\n");
    printf("   -m1 + m1^2 + m2^2 = 0\n\n");

    printf("Hence, locus of midpoints is:\n");
    printf("   m1^2 + m2^2 = m1\n");

    return 0;
}