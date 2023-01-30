#!/usr/bin/python3
""" this module takes in a number and returns the pascal triangle for that number """

def factorial(n):
    if (n == 0 ):
        return 1;
    else:
        return n * factorial(n-1);

def nCr(num, re):
    """ method to create the combination """
    factN = factorial(num);
    factRe = factorial(re);
    factN_re = factorial(num - re);
    deno = factN_re * factRe;
    result = (factN)/(deno);
    return result;

def pascal_triangle(num):
    """ method to create the pascal triangle """
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
