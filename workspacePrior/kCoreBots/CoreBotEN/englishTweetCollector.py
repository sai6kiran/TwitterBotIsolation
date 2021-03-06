import csv
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import time
import goslate
import numpy as np
import cld3

fsn="/root/.encrypted/.pythonSai/kCoreBots/CoreBotEN/CoreBotsTweetsCombinedEN.csv"
for i in range(1,472):
	fpn="/root/.encrypted/.pythonSai/kCoreBots/CoreBotEN/CoreBot"+str(i)+"EN.csv"
	dfi = pd.read_csv(fpn, sep=",", header=0, skiprows=[1], chunksize=2000)
	for df_ in dfi:

		t0 = time.time()
		df_.insert(4, "language", "en")
		df_[["tweetid", "tweet_text", "hashtags", "urls", "language"]].to_csv(fsn, mode='a', header=False, index=False)
		t1 = time.time()
		print(t1-t0)	
