B=[0];a=[0,0]+[1]*6**8
for(i,p)in enumerate(a):
 if p:B+=[i];a[i*i::i]=[0]*len(a[i*i::i])
for i in[*open(0)][1:]:print(B[int(i)])
