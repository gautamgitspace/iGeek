//
//  main.cpp
//  Next Power of Two
//
//  Created by Gautam on 11/2/16.
//  Copyright © 2016 Gautam. All rights reserved.
//

#include <iostream>

unsigned int nextPowerOf2(unsigned int n)
{
    unsigned int p = 1;
    if (n && (n & (n - 1))==0)
        return n;
    while (p < n)
    {
        p <<= 1;
        printf("after shift: %d\n",p);
    }
    return p;
}

/* Driver program to test above function */
int main()
{
    unsigned int n = 9;
    printf("%d", nextPowerOf2(n));
    
    getchar();
    return 0;
}

