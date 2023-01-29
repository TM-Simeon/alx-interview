#!/usr/bin/env python3
import math

def nCr(num, re):
    factN = math.factorial(num);
    factRe = math.factorial(re);
    factN_re = math.factorial(num - re);
    deno = factN_re * factRe;
    result = (factN)/(deno);
    return result;

def pascal_triangle(num):
    triangle = [];
    if (num == 0):
        list = []
        list.append(1)
        triangle.append(list);
        return triangle;
    else:
        for x in range(num):
            num = x;
            r = 0;
            list = [];
            while(r <= num):
                R = int(nCr(num, r));
                list.append(R);
                r += 1;
            triangle.append(list);
        return triangle;