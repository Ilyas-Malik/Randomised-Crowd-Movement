import numpy as np
import time
from random import *
n=15
m=15
k=0  # k et l sont ligne et ordonnée de la porte de sortie
l=0


def generatelist(k,long):
    l=[]
    for i in range(long):
        l.append(randint(0,k-1))
    return l

    
def generate(t,h,val):
    l1=generatelist(n,h)
    l2=generatelist(m,h)
    for x in range(h):
        t[l1[x],l2[x]]=val
    t[k,l]=0
    for x in possiblemoves(k,l):
        t[x[0],x[1]]=0
    return t


def eleves():
    l=[]
    for i in range(n):
        for j in range(m):
            if t[i,j]==1:
                l+=[(i,j)]
    return l

    
def switch(i,k,j,l):
    t[i,j],t[k,l]=t[k,l],t[i,j]


def move1():
    el=eleves()
    for x in el:
        (i,j)=x
        if i<k:
            if t[i+1,j]==0:
                switch(i,i+1,j,j)
                continue
        elif i>k:
            if t[i-1,j]==0:
                switch(i,i-1,j,j)
                continue
        if j<l:
            if t[i,j+1]==0:
                switch(i,i,j,j+1)
                continue
        elif j>l:
            if t[i,j-1]==0:
                switch(i,i,j,j-1)
                continue
        else:
            if i==k:
                t[i,j]=0


def d2(i,k,j,l):
    return (i-k)*(i-k)+(j-l)*(j-l)

    
def goto(i,j,x):
    switch(i,x[0],j,x[1])
    

def possiblemoves(i,j):
    l=[]
    l.append((i,j-1))
    l.append((i-1,j))
    l.append((i,j+1))
    l.append((i+1,j))
    if i==0:
        l[1]=0
    elif i==n-1:
        l[3]=0
    if j==0:
        l[0]=0
    elif j==m-1:
        l[2]=0
    l2=[]
    for i in range(4):
        if l[i]!=0:
            if t[l[i]]==0:
                l2.append(l[i])
    return l2

    
def indexmin(l):
    n=len(l)
    if n==0:
        return 4
    var=l[0]
    k=0
    for i in range(n):
        if var>l[i]:
            k=i
            var=l[i]
    return k
    
    
def aleamove(i,j):
    if (i,j)==(k,l):
        t[i,j]=0
        return
    a=possiblemoves(i,j)
    shuffle(a)
    switch(i,a[0][0],j,a[0][1])
    
    
def movealea():
    el=eleves()
    for x in el:
        (i,j)=x
        aleamove(i,j)
        
        
def pseudosmartmove(i,j):
    if (i,j)==(k,l):
        t[i,j]=0
        return
    a=possiblemoves(i,j)
    b=len(a)
    a2=[]
    for g in range(b):
        (x,y)=a[g]
        a2.append(d2(x,k,y,l))
    g=indexmin(a2)
    if g==4:
        return
    if random()<0.7:
        goto(i,j,a[g])
    else:
        aleamove(i,j)
    
    
def movepseudosmart():
    el=eleves()
    for x in el:
        pseudosmartmove(x[0],x[1])
    
        
t=np.zeros((n,m))
generate(t,n,2)
generate(t,n,1)


for i in range(1,300):
    time.sleep(0.3)
    movepseudosmart()
    print()
    print(t)
    if eleves()==[]:
        print("Succès : Temps =",i)
        break
if i==299:
    print("Echec : Il reste",len(eleves()),"élèves")


