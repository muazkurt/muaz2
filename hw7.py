#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
def cRNF(max,min,count,OutputFileName):
	outputFile = open(OutputFileName,"a+")
	for item in range (0,count):
		randomNumber = random.randint(min,max)
		outputFile.write(str(randomNumber)+" \n")
	outputFile.close()
cRNF(99,1,40,"muaz.txt")
