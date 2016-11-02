//
//  main.cpp
//  Power of Four
//
//  Created by Gautam on 11/1/16.
//  Copyright © 2016 Gautam. All rights reserved.
//

#include <iostream>

bool checkPowerOfFour(int n)
{
    int count = 0;
    /*CHECK IF ONLY ONE BIT IS SET*/
    if(n && (n&(n-1))==0)
    {
        /*COUNT ZERO BITS BEFORE THE ONE SET BIT*/
        while(n > 1)
        {
            n >>= 1;
            count +=1;
        }
        /*CHECK IF COUNT IS EVEN*/
        return (count%2)==0?1:0;
    }
    return 0;
}

int main(int argc, const char * argv[])
{
    int result = checkPowerOfFour(16384);
    if (result == 1)
        printf("\n[YES] power of four\n");
    else
        printf("[NO] power of four\n");
    return 0;
}
