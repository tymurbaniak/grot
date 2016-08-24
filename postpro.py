import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.cm as cm
from matplotlib.collections import PatchCollection
import math
import numpy

class prepare():
    def __init__(self, nodes, elements, results):
        self.nodes = nodes
        self.eles = elements
        self.res = results
        print(self.res[0])
    
    def nod_disp(self):
        colors = []
        xs = [self.nodes[i][0] for i in self.nodes]
        ys = [-self.nodes[i][1] for i in self.nodes]
        zs = []
        for i in range(0, len(self.res), 2):
            zs.append(math.sqrt((self.res[i] ** 2) + (self.res[i + 1] ** 2)))
        
        fig, ax = plt.subplots()
        patch_list = []
        print(self.eles)
        for i in self.eles:
            xlist, ylist = [], []
            xlist.append(self.eles[i][0][0])
            xlist.append(self.eles[i][1][0])
            xlist.append(self.eles[i][2][0])
            xlist.append(self.eles[i][3][0])
            ylist.append(self.eles[i][0][1])
            ylist.append(self.eles[i][1][1])
            ylist.append(self.eles[i][2][1])
            ylist.append(self.eles[i][3][1])
            patch_list.append(
                patches.Rectangle(
                    (min(xlist), -min(ylist)),   # (x,y)
                    1.0,          # width
                    1.0
                    )
                )
            
            dof1 = (self.eles[i][4] * 2) - 2
            dof2 = (self.eles[i][5] * 2) - 2
            dof3 = (self.eles[i][6] * 2) - 2
            dof4 = (self.eles[i][7] * 2) - 2
            dofs = [dof1, dof1 + 1, dof2, dof2 + 1, dof3, dof3 + 1, dof4, dof4 + 1]
            
            colors.append((self.res[dofs[0]] + self.res[dofs[2]] + self.res[dofs[4]] + self.res[dofs[6]]) / 4)
            
        #colors = 100*numpy.random.rand(len(patch_list))
        p = PatchCollection(patch_list, cmap=cm.jet, alpha=0.4)
        p.set_array(numpy.array(colors))
        ax.add_collection(p)
        plt.colorbar(p)
        plt.plot([0,10],[0,-10])
        plt.show()