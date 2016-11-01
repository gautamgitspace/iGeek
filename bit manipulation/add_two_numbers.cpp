//
//  main.c
//  Bitwise Number Addition
//
//  Created by Gautam on 10/31/16.
//  Copyright © 2016 Gautam. All rights reserved.
//

#include <stdio.h>
int add(int, int);
int main(int argc, const char * argv[])
{
    int num1, num2;
    printf("Enter two numbers\n");
    scanf("%d %d", &num1, &num2);
    printf("%d\n",add(num1, num2));
    return 0;
}

int add(int a, int b)
{
    if (!a)
        return b;
    return add((a & b) << 1, a ^ b);
}


