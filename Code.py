"""
MECH 305/6 DATA ANALYSIS
----------------------------------------
WRITTEN BY: THOMAS BEMENT
DATE: 3/07/2021

EXPERIMENT 4 NATURAL GAS ENGINE
"""
import csv
import os
import glob
import matplotlib.pyplot as plt
import numpy as np
import math
import time
from scipy.signal import savgol_filter

"""
DEFINE CONSTANTS
"""
# Start run time timer
start_time = time.time()
# [low load reg spark, high load reg spark, high load adv spark]
scaleWeight = [4.4482216153*6.5625,4.4482216153*10.625,4.4482216153*8.9375]

"""
READ IN DATA
"""
# Headers: X_Value	Intake Pressure	Cylinder Pressure	Encoder	TDC	Spark	Comment
def readDat(pathlist):
    ans = {}
    for path in pathlist:
        for filename in glob.glob(os.path.join(path, '*.txt')):
            key = filename.split('\\')[-1].replace('.txt', '')
            ans[key] = ([],[],[],[],[],[])
            with open(os.path.join(os.getcwd(), filename), 'r') as f: # open in readonly mode
                for row in csv.reader(f, delimiter='\t'):
                    if len(row) == 6:
                        for i in range(6):
                            ans[key][i].append(row[i])
    return ans
"""
    for key in ans:
        for i in range(6):
            ans[key][i] = np.array(ans[key][i])
"""
    

def get_cmap(n, name='magma'):
    return plt.cm.get_cmap(name, n)

def tsPlot(dat, key):
    cmap = get_cmap(5)
    legendLis = ['Intake Pressure',	'Cylinder Pressure','TDC',]
    plt.axis('off')
    #plt.tick_params(axis='both', which='both', bottom=False, top=False, right=False, left=False, labelbottom=False) 
    plt.title('Time Serries Plot:')
    #plt.autoscale(enable=True, axis='x')
    plt.xlabel('Time (s)')
    plt.ylabel('Magnitude')
    for i in range(1,6):
        if (i == 1)or(i == 2)or(i == 4):
            plt.plot(dat[key][0], savgol_filter(np.array(dat[key][i]), 11, 3), color=cmap(i-1))
    plt.legend(legendLis, bbox_to_anchor=(1.04, 0.5), loc="center left")
    #plt.savefig('PythonFigures/TimeSeries/%s.png' %key, format='png', bbox_inches='tight', orientation='landscape')    
    plt.show()
    return

def encoder(dat, key):
    cmap = get_cmap(5)
    legendLis = ['Intake Pressure',	'Cylinder Pressure', 'Encoder',	'TDC', 'Spark']
    plt.axis('off')
    #plt.tick_params(axis='both', which='both', bottom=False, top=False, right=False, left=False, labelbottom=False) 
    plt.title('Time Serries Plot:')
    #plt.autoscale(enable=True, axis='x')
    plt.xlabel('Time (s)')
    plt.ylabel('Magnitude')
    for i in range(1,6):
        if (i == 3)or(i == 5):
            plt.plot(dat[key][0], np.array(dat[key][i]), color=cmap(i-2))
    plt.legend(legendLis, bbox_to_anchor=(1.04, 0.5), loc="center left")
    #plt.savefig('PythonFigures/TimeSeries/%s.png' %key, format='png', bbox_inches='tight', orientation='landscape')    
    plt.show()
    return

"""
def plots(lis):
    fig, axs = plt.subplots(len(lis)-1)
    fig.suptitle('Plots:')
    fig.tight_layout(pad=3.0)
    for i in range(len(lis)-1):
        axs[i].plot(lis[0], lis[i]) 
        axs[i].set_title('Sub Plot %i' %i)
        axs[i].set(xlabel='X-Axis', ylabel='Y-Axis')
    # Save Plots
    plt.show()
    plt.close()
    return
"""
# Add when working,
# '.\Data\LowCR_HighLoad_AdvacnedSpark', '.\Data\LowCR_HighLoad_RegularSpark', '.\Data\LowCR_LowLoad_RegularSpark'
allDat = readDat(['.\Data\HighCR_HighLoad_AdvacnedSpark','.\Data\HighCR_HighLoad_RegularSpark','.\Data\HighCR_LowLoad_RegularSpark','.\Data\LowCR_HighLoad_AdvacnedSpark', '.\Data\LowCR_HighLoad_RegularSpark', '.\Data\LowCR_LowLoad_RegularSpark'])
"""
Key's:
HighCR_HighLoad_AdvacnedSpark_Set1
HighCR_HighLoad_AdvacnedSpark_Set2
HighCR_HighLoad_AdvacnedSpark_Set3
HighCR_HighLoad_AdvacnedSpark_Set4
HighCR_HighLoad_AdvacnedSpark_Set5
HighCR_HighLoad_RegularSpark_Set1
HighCR_HighLoad_RegularSpark_Set2
HighCR_HighLoad_RegularSpark_Set3
HighCR_HighLoad_RegularSpark_Set4
HighCR_HighLoad_RegularSpark_Set5
HighCR_LowLoad_RegularSpark_Set1
HighCR_LowLoad_RegularSpark_Set2
HighCR_LowLoad_RegularSpark_Set3
HighCR_LowLoad_RegularSpark_Set4
HighCR_LowLoad_RegularSpark_Set5
LowCR_HighLoad_AdvacnedSpark_Set1
LowCR_HighLoad_AdvacnedSpark_Set2
LowCR_HighLoad_AdvacnedSpark_Set3
LowCR_HighLoad_AdvacnedSpark_Set4
LowCR_HighLoad_AdvacnedSpark_Set5
LowCR_HighLoad_RegularSpark_Set1
LowCR_HighLoad_RegularSpark_Set2
LowCR_HighLoad_RegularSpark_Set3
LowCR_HighLoad_RegularSpark_Set4
LowCR_HighLoad_RegularSpark_Set5
LowCR_LowLoad_RegularSpark_Set1
LowCR_LowLoad_RegularSpark_Set2
LowCR_LowLoad_RegularSpark_Set3
LowCR_LowLoad_RegularSpark_Set4
LowCR_LowLoad_RegularSpark_Set5
#for key in allDat:
#    print(key)
"""
tsPlot(allDat, 'LowCR_HighLoad_RegularSpark_Set1')
encoder(allDat, 'LowCR_HighLoad_RegularSpark_Set1')

print("\nRun time: %s seconds" % (time.time() - start_time))