//
//  main.cpp
//  CTCI5_2
//
//  Created by Gautam on 11/1/16.
//  Copyright © 2016 Gautam. All rights reserved.
//

#include <iostream>
#include <string>

using namespace std;

string printBinaryVersion(double number)
{
    if (number < 0 || number >=1)
    {
        return "ERROR!";
    }
    string result = "";
    result = result + ".";
    while(number > 0)
    {
        if(result.length() >= 64)
        {
            return "ERROR";
        }
        double r = number * 2;
        if(r >= 1)
        {
            result = result + "1";
            number = r - 1.0;
        }
        else
        {
            result = result + "0";
            number = r;
        }
    }
    return result;
}

int main(int argc, const char * argv[])
{
    double a = 0.625;
    cout<<printBinaryVersion(a)<<"\n";
    return 0;
}
