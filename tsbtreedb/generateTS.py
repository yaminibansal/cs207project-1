import os, sys
curr_dir = os.getcwd().split('/')
sys.path.append('/'.join(curr_dir[:-1]))
ts_dir = curr_dir[:-1]
ts_dir.append('timeseries')
sys.path.append('/'.join(ts_dir))
import timeseries.Timeseries as ts
import SimilaritySearch as ss
import numpy as np

'''
SCRIPT 1, Milestone 2 Part 7

This file is a script to generate
1000 different timeseries

How to run:
python generateTS.py

Requires folder:
tsdata

'''


if __name__ == "__main__":

	time = np.linspace(.01,.99,1024)
	#Generate 1000 timeseries
	#using SimilaritySearch tsmaker function
	for i in range(1000):
		file_path = 'tsdata/ts'+str(i)+'.dat'
		fp = open(file_path,'w+')
		t1 = ss.tsmaker(0.5, 0.1, 0.01)
		regT1 = t1.interpolate(time)
		np.savetxt(file_path,np.transpose(np.array([list(regT1.itertimes()),list(regT1)])), delimiter=' ')
