#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # X = (A\B) /\ ( C u D)     Y = (A /\ not(B)) u (C\D)
    U = set("abcdefghijklmnopqrstuvwxyz")
    a = {'b', 'd', 'f', 'g', 'l', 'u'}
    b = {'d', 'e', 'f', 'm', 'n', 'z'}
    c = {'h', 'i', 'r', 'x'}
    d = {'a', 'e', 'f', 'k', 'r', 's', 'x'}
    print('X =', (a / b) & (c | d))
    print('Y =', (c | b) | (a & (c / d)))
