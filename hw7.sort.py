#!/usr/bin/env python
# -*- coding: utf-8 -*
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

b=raw_input("Aranacak Deger: ")
def Search(a,b):
	if(len(a)==0):
		print "failed"
	else:
		Test_Entry=a[1/2]
		if(b==Test_Entry):
			print "Search succeeded"
		elif(b<Test_Entry):
			Sublist=list(str in range(a[0], a[str(len(a))/2]))
			Search(Sublist,b)
		elif(b>Test_Entry):
			Subblist= list(str in range (a[str(len(a))/2], a[str(len(a))])
			Search(Subblist,b)
Search(a,b)
