//
//  main.cpp
//  Multiply Integer with 3.5
//
//  Created by Gautam on 10/31/16.
//  Copyright © 2016 Gautam. All rights reserved.
//

#include <iostream>

int multiplyWithThreePointFive(int x)
{
    return (x << 1) + x + (x >> 1);
}

int multiplyWithSeven(int x)
{
    return ((x << 1) + x + (x >> 1))*2;
}

int multiplyTwoNumbers(int x, int y)
{
    int result = 0;
    while(y!=0)
    {
        if(y & 01) //if b is odd add a to the result
        {
            result = result + x;
        }
        x<<=1; //double a
        y>>=1; //half b
    }
    return result;
}

int main(int argc, const char * argv[])
{
    printf("%d\n",multiplyWithThreePointFive(2));
    printf("%d\n",multiplyWithSeven(2));
    printf("%d\n",multiplyTwoNumbers(4, 3));
    
    return 0;
}
