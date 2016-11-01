//
//  main.cpp
//  Power of Two and Set Bits
//
//  Created by Gautam on 10/31/16.
//  Copyright © 2016 Gautam. All rights reserved.
//

#include <iostream>

unsigned int countSetBits(unsigned int x)
{
    unsigned int count = 0;
    while(x)
    {
        count = count + (x&1);
        x>>=1;
    }
    return count;
}

void checkPowerOfTwo(unsigned int x)
{
    if(((x&(x-1)) == 0))
       printf("POWER OF 2\n");
    else
       printf("NOT A POWER OF 2\n");
}

int main(int argc, const char * argv[])
{
    unsigned int bitCount = countSetBits(256);
    if(bitCount == 1)
    {
        printf("\nNumber is a power of 2\n");
    }
    else
    {
        printf("Number is not a power of 2\n");
    }
    checkPowerOfTwo(256);
    return 0;
}
