#include <stdio.h>
#include <math.h>

int main() {
    // Semi-ellipse parameters
    double a = 4.0;   // semi-major axis (half width = 8/2)
    double b = 2.0;   // semi-minor axis (height at centre)

    // Distance from the end
    double d = 1.5;

    // x-coordinate at this position
    double alpha = a - d;

    // Equation of ellipse: (x^2 / a^2) + (y^2 / b^2) = 1
    // Solve for y
    double lhs = 1.0 - (alpha * alpha) / (a * a);

    if (lhs < 0) {
        printf("No real solution (point outside ellipse).\n");
        return 0;
    }

    double beta = b * sqrt(lhs);

    printf("Height of the arch at %.2f m from the end = %.3f m\n", d, beta);

    return 0;
}