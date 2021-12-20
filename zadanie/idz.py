#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Вариант 16


if __name__ == "__main__":
    U = set("abcdefghijklmnopqrstuvwxyz")
    A = {'b', 'd', 'f', 'g', 'l', 'u'}
    B = {'d', 'e', 'f', 'm', 'n', 'z'}
    C = {'h', 'i', 'r', 'x', 'y'}
    D = {'a', 'e', 'f', 'k', 'r', 's', 'x'}

    X = (A.difference(B)).intersection(C.union(D))
    print(f'X = {X}')

    AA = U.difference(A)

    Y = (AA.intersection(D)).union(C.difference(B))
    print(f'Y = {Y}')
