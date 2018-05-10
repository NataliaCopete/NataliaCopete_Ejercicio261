import numpy as np
import matplotlib.pyplot as plt

N=100000000
planosv=np.random.uniform(35,45,N)


def tet(K):
  planosang=np.random.uniform(0,(np.pi/2), K)
 
  return planosang


g=9.8


def vel(v,teta,d):
  d1=np.multiply(v**2,np.sin(2*teta)/g)
  vnuevas=v[(d-5<d1) & (d1<d+5)]
 
  return vnuevas




v1=vel(planosv,tet(len(planosv)),61)
v2=vel(v1,tet(len(v1)),115)
v3=vel(v2,tet(len(v2)),31)
v4=vel(v3,tet(len(v3)),177)

plt.hist(planosv)
plt.savefig("sindatos.png")
plt.clf()
plt.hist(v1,normed=True)
plt.savefig("primerdato.png")
plt.clf()
plt.hist(v2,normed=True)
plt.savefig("segundodato.png")
plt.clf()
plt.hist(v3,normed=True)
plt.savefig("tercerdato.png")
plt.clf()
plt.hist(v4,normed=True)
plt.savefig("cuartodato.png")



  


  
