#!/usr/bin/env python
# -*- coding: utf-8 -*
import math
f=open("muaz.txt","r+")
q=f.read()
y=q.split(' \n')
a=list(y)
def Sort(list):
	N=2
	while(N<len(a)):
		PivotEnrtry=a[N]
		while(N>0 and a[N-1]>PivotEnrtry):
			a[N]=a[N-1]
			a[N-1]=PivotEnrtry
			N=N-1
		N=N+1
Sort(a)
print a, len(a)

