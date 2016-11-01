//
//  main.cpp
//  Min and Max
//
//  Created by Gautam on 11/1/16.
//  Copyright © 2016 Gautam. All rights reserved.
//

#include <iostream>

int getMax(int a, int b)
{
    int c = a - b;
    int k = (c >> 31) &1;
    int max = a - k * c;
    return max;
}

int main(int argc, const char * argv[])
{
    int a = 7, b = 9;
    if(getMax(a, b) == 7)
    {
        printf("max is: %d\n", a);
        printf("min is: %d\n", b);
    }
    else
    {
        printf("max is: %d\n", b);
        printf("min is: %d\n", a);
    }
    return 0;
}
