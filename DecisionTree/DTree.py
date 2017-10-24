#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This is the algorithm used to create a rudimentary decision tree
differentiating only between French and Spanish.
This can be generalized further if necessary- we chose to focus on KNN as our nonlinear method
but this is included in the report as a proof of concept.
"""

import math
import collections
#calculates the entropy of the dataset before any operations
def Entropy(pos, neg):
    Sum = float(pos + neg)
    output = -pos/(Sum)*math.log(pos/Sum,2)-(neg/Sum)*math.log(neg/Sum,2)
    return output

def ConditionalEntropy(posT, negT, posN, negN):
    SumT = float(posT + negT)
    SumN = float(posN + negN)
    SumAll = float(SumT + SumN)
    #how do we deal with 0 here
    #we know that the input is gonna be >=0
    #so we use approximate results 
    if(posT == 0):
        posT = 0.000000000000001
    if(negT == 0):
        negT = 0.000000000000001
    if(posN == 0):
        posN = 0.000000000000001
    if(negN == 0):
        negN = 0.000000000000001
    output = (SumT/SumAll)*(-1*(posT/SumT)*math.log(posT/SumT,2)-(negT/SumT)*math.log(negT/SumT,2))+(SumN/SumAll)*(-1*(posN/SumN)*math.log(posN/SumN,2)-(negN/SumN)*math.log(negN/SumN,2))
    return output

#Calculates the information gain
def IG(posT, negT, posN, negN):
    entropy = Entropy(posT+posN, negT+negN)
    conditionalEntropy = ConditionalEntropy(posT,negT,posN,negN)
    return (entropy-conditionalEntropy)

#Extracts the Spanish and French entries from a dataset
def SplitLanguage(dataset):
    
    French=[]
    Spanish=[]
    for lineY in dataset:
    
        lang = lineY[0]
    #    text = (lineY.split(",")[1])
        text = lineY
        
        chars = text.split()
    

                        
        if lang == '1':
            French.append(text)
        if lang == '2':
            Spanish.append(text)
    return [French,Spanish]


#Takes French and Spanish datasets as entries, as well as the past keys used
#Uses Information Gain to choose the best feature for separation
#Then separates the set with the best separation feature.
def MakeDictionary(French,Spanish,pastkeys):

            
        
    Fcount=0
    Fren={}
    for line in French:
        line=line.lower()
        chars = line.split()
        for char in chars:
            charnew=list(char)
            for carps in charnew:
                Fcount=Fcount+1
                if carps in Fren:
                    Fren[carps][0] += 1
                else:
                    Fren[carps] = [1,0,0,0]
    Spcount=0           
    for line in Spanish:
        line=line.lower()
        chars = line.split()
        for char in chars:
            charnew=list(char)
            for carps in charnew:
                Spcount=Spcount+1
                if carps in Fren:
                    Fren[carps][1] += 1
                else:
                    Fren[carps] = [0,1,0,0]
    chartot=Spcount+Fcount
    
    numberline=[',','0','1','2','3','4','5','6','7','8','9']
    for k in Fren.keys():
        if k in numberline:
            del Fren[k]
        if k in pastkeys:
            del Fren[k]
    
    for key in Fren:
        posT=Fren[key][0]*1.00
        negT=Fren[key][1]*1.00
        
        posF=chartot-posT
        negF=chartot-negT
        
        if posT==0:
            posT = 0.000000000000001
        if negT==0:
            negT = 0.000000000000001
        if posF==0:
            posF = 0.000000000000001
        if negF==0:
            negF = 0.000000000000001        
        entrop=Entropy(posT,negT)
        Fren[key][2]=entrop
        
        infgain=IG(posT, negT, posF, negF)
        Fren[key][3]=infgain
        
        
    listy={}
    for key in Fren:
        listy[key]=Fren[key][3]
    
    maxvalue=0
    comparevalue=0
    maxkey=''
    for key in listy:
        comparevalue=listy[key]
        if comparevalue>maxvalue:
            maxvalue=comparevalue
            maxkey=key

    Frenmax=Fren[maxkey][0]
    Spanmax=Fren[maxkey][1]
    if Frenmax > Spanmax:
        langchoice = '1'
    if Spanmax > Frenmax:
        langchoice = '2'

    SetTr=[]
    SetFa=[]
    
    for line in French:
        langprob=0
        line=line.lower()
        chars = line.split()
        for char in chars:
            charnew=list(char)
            for carps in charnew:
                if carps == maxkey:
                    langprob = langprob+1
        if langprob > 0:
            if langchoice == '1':
                SetTr.append(line)
            else:
                SetFa.append(line)
        else:
            if langchoice == '1':
                SetFa.append(line)
            else:
                SetTr.append(line)
    
    for line in Spanish:
        langprob=0
        line=line.lower()
        chars = line.split()
        for char in chars:
            charnew=list(char)
            for carps in charnew:
                if carps == maxkey:
                    langprob = langprob+1
                    
        if langprob > 0:
            if langchoice == '1':
                SetFa.append(line)
            else:
                SetTr.append(line)
        else:
            if langchoice == '1':
                SetTr.append(line)
            else:
                SetFa.append(line)
    



    return [maxkey,langchoice,SetTr,SetFa]


    

    

import numpy as np
import math as m
import random as ran
NEW_TRAIN_X = open("train08.csv","r")

#X = NEW_TRAIN_X.readlines()
#Y = NEW_TRAIN_Y.readlines()
#NEW_TRAIN_X.close()
#NEW_TRAIN_Y.close()
#NEW_TRAIN_X = open("train_set_x.csv","r")
#NEW_TRAIN_Y = open("train_set_y.csv","r")
#alphabet for all languages

French = []
Spanish = []

Alphabet = []
for lineY in NEW_TRAIN_X:

    lang = lineY[0]
#    text = (lineY.split(",")[1])
    text = lineY
    
    chars = text.split()

    for char in chars:
        char=char.lower()
        for candy in char:
            for stars in candy: 
                if stars not in Alphabet:
                    Alphabet.append(stars)
                    
    if lang == '1':
        French.append(text)
    if lang == '2':
        Spanish.append(text)
        
Fcount=0
Fren={}
for line in French:
    line=line.lower()
    chars = line.split()
    for char in chars:
        charnew=list(char)
        for carps in charnew:
            Fcount=Fcount+1
            if carps in Fren:
                Fren[carps][0] += 1
            else:
                Fren[carps] = [1,0,0,0]
#total = 1.00*sum(Fren.values())
#for key, value in Fren.items():
#    Fren[key] = value*1.00 / total
        
        
Spcount=0           
for line in Spanish:
    line=line.lower()
    chars = line.split()
    for char in chars:
        charnew=list(char)
        for carps in charnew:
            Spcount=Spcount+1
            if carps in Fren:
                Fren[carps][1] += 1
            else:
                Fren[carps] = [0,1,0,0]
#total = 1.00*sum(Span.values())
#for key, value in Span.items():
#    Span[key] = value*1.00 / total    

chartot=Spcount+Fcount

numberline=[',','0','1','2','3','4','5','6','7','8','9']
for k in Fren.keys():
    if k in numberline:
        del Fren[k]

for key in Fren:
    posT=Fren[key][0]*1.00
    negT=Fren[key][1]*1.00
    
    posF=chartot-posT
    negF=chartot-negT
    
    if posT==0:
        posT = 0.000000000000001
    if negT==0:
        negT = 0.000000000000001
    if posF==0:
        posF = 0.000000000000001
    if negF==0:
        negF = 0.000000000000001        
    entrop=Entropy(posT,negT)
    Fren[key][2]=entrop
    
    infgain=IG(posT, negT, posF, negF)
    Fren[key][3]=infgain
    
listy={}
for key in Fren:
    listy[key]=Fren[key][3]

pastkeys=''

inputset=NEW_TRAIN_X
[maxvaluekey,langcode,SetTr,SetFa]=MakeDictionary(French,Spanish,pastkeys)

pastkeys1='e'
[Fr,Sp]=SplitLanguage(SetTr)
[mv,lc,st,sf]=MakeDictionary(Fr,Sp,pastkeys1)

pastkeys2=['e','s']
[Fr11,Sp11]=SplitLanguage(st)
[mv11,lc11,st11,sf11]=MakeDictionary(Fr11,Sp11,pastkeys2)
#st11 is French
#sf11 is Spanish
[Fr12,Sp12]=SplitLanguage(sf)
[mv12,lc12,st12,sf12]=MakeDictionary(Fr12,Sp12,pastkeys2)
#st12 is French
#sf12 is Spanish

[Fr2,Sp2]=SplitLanguage(SetFa)
[mv2,lc2,st2,sf2]=MakeDictionary(Fr2,Sp2,pastkeys1)

pastkeys3=['e','a']
[Fr21,Sp21]=SplitLanguage(st)
[mv21,lc21,st21,sf21]=MakeDictionary(Fr21,Sp21,pastkeys3)
#st21 is French
#sf21 is Spanish
[Fr22,Sp22]=SplitLanguage(sf)
[mv22,lc22,st22,sf22]=MakeDictionary(Fr22,Sp22,pastkeys3)
#st22 is French
#sf22 is Spanish

FrenchGuess=[]
for lines in st11:
    FrenchGuess.append(lines)
for lines in st12:
    FrenchGuess.append(lines)
for lines in st21:
    FrenchGuess.append(lines)
for lines in st22:
    FrenchGuess.append(lines)


FrenRight=0
FrenWrong=0
for lines in FrenchGuess:
    lang = lines[0]
    if lang == '1':
        FrenRight=FrenRight+1
    if lang =='2':
        FrenWrong=FrenWrong+1
        
SpanishGuess=[]
for lines in sf11:
    SpanishGuess.append(lines)
for lines in sf12:
    SpanishGuess.append(lines)
for lines in sf21:
    SpanishGuess.append(lines)
for lines in sf22:
    SpanishGuess.append(lines)

SpanRight=0
SpanWrong=0
for lines in SpanishGuess:
    lang = lines[0]
    if lang == '2':
        SpanRight=SpanRight+1
    if lang =='1':
        SpanWrong=SpanWrong+1

AccuracyFren=(FrenRight*1.00)/(FrenWrong*1.00+FrenRight*1.00)
AccuracySpan=(SpanRight*1.00)/(SpanWrong*1.00+SpanRight*1.00)
AccuracyTotal=(FrenRight*1.00+SpanRight*1.00)/(FrenWrong*1.00+SpanWrong*1.00+SpanRight*1.00+FrenRight*1.00)


VALIDATION = open("test02.csv","r")

numberlines=0
valcorrect=0
FC=0
FN=0
SC=0
SN=0
for lineY in VALIDATION:
    numberlines=numberlines+1
    lv=[0,0,0,0]
    lc=''
    
    lang=lineY[0]
    text=lineY

    
    chars = text.split()
    
    for char in chars:
        if char == 'e':
            lv[0]+=1
        if char == 's':
            lv[1]+=1
        if char == 'a':
            lv[2]+=1
        if char == 'n':
            lv[3]+=1
    
    if lv[0]>0:
        if lv[1]>0:
            if lv[2]>0:
                lc='1'
            else:
                lc='2'
        else:
            if lv[3]>0:
                lc='1'
            else:
                lc='2'
    else:
        if lv[2]>0:
            if lv[1]>0:
                lc='1'
            else:
                lc='2'
        else:
            if lv[3]>0:
                lc='1'
            else:
                lc='2'
                
                
    if lang=='1':
        if lc=='1':
            FC+=1
        if lc=='2':
            FN+=1
    if lang=='2':
        if lc=='2':
            SC+=1
        if lc=='1':
            SN+=1
            

FC=FC*1.00
FN=FN*1.00
SC=SC*1.00
SN=SN*1.00
FA=0
TA=0
FA=FC/(FC+FN)
SA=SC/(SC+SN)
TA=(FC+SC)/(FC+SC+FN+SN)
        

    
