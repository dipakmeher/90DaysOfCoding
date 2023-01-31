/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/
#include <vector>
#include <iostream>

void h(std::vector<double> & numbers)
{
    for (int i=0; i<numbers.size(); i++)
        numbers[i] /= 2;
}

void q(std::vector<double> numbers)
{
    for (int i=0; i<numbers.size(); i++)
        numbers[i] *= 4;
}

int main(void)
{
    std::vector<double> numbers = {0.0,0.5,1.0,1.5, 2.0};
    q(numbers);
    h(numbers);
    double sum = 0;
    for(int i = 0; i<numbers.size(); i++)
    {
        sum += numbers[i];
        
    }
    std::cout<<sum<<std::endl;
    
}

