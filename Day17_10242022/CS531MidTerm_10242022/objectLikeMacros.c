#include <stdio.h>
// Below is the object like macros
#define PI 3.1415
// Below is the function like macros
#define circleArea(r) (PI*r*r)
int main() {
    float radius = 2.0, area;
    area = circleArea(radius);
    printf("Area = %.2f", area);
    return 0;
}
