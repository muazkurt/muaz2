#!/usr/bin/env python
# -*- coding: utf-8 -*
f=open("muaz.txt","r")
q=f.read()
y=q.split(' \n')
a=list(y)
b=raw_input("Aranacak Deger: ")
def Search(a,b):
	if(len(a)==0):
		print "failed"
	else:
		Test_Entry=a[1/2]
		if(b==Test_Entry):
			print "Search succeeded"
		if(b<Test_Entry):
			Sublist=a(0, 1/2)
			print Sublist
Search(a,b)
