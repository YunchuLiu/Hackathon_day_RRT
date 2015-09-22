import numpy as np
import matplotlib.pyplot as mp
from matplotlib.path import Path
import matplotlib.patches as patches
import random 
import math 


q_init=(50,50)
K=input('input number of vertices: ')
delta_q=1
G_vertex=[]
G_edge=[]

def G_INIT():
    a=[q_init,]
    return a 
    
def RAND_CONF():
    q_rand=(random.uniform(0,100),random.uniform(0,100))
    return q_rand     

def NEAREST_VERTEX(q_rand,G):
    a=100
    for item in G:
        dist=math.sqrt((item[0]-q_rand[0])**2+(item[1]-q_rand[1])**2)
        if dist<a:
           a=dist
           b=item
    return b
    
def NEW_CONF(q_near,q_rand):
    q_new=()
    q_new=q_near[0]+(q_rand[0]-q_near[0])/a,q_near[1]+(q_rand[1]-q_near[1])/a
    return q_new 
    

G_vertex=G_INIT() 
       
for k in range(K):
    q_rand= RAND_CONF()
    q_near=NEAREST_VERTEX(q_rand,G_vertex)
    a=math.sqrt((q_rand[0]-q_near[0])**2+(q_rand[1]-q_near[1])**2)
    q_new=NEW_CONF(q_near,q_rand)
    G_vertex.append(q_new)
    G_edge.append((q_near,q_new))

# let's plot:
verts = []
codes = []
for i,t in enumerate(G_edge[0:len(G_edge)-1]):
    verts.append(t[0])
    verts.append(G_edge[i][1])
    codes.append(Path.MOVETO)
    codes.append(Path.LINETO)
fig = mp.figure()
path = Path(verts, codes)
patch = patches.PathPatch(path)
ax = fig.add_subplot(111)
ax.add_patch(patch)
ax.set_xlim([0,100])
ax.set_ylim([0,100])
mp.show()





   
