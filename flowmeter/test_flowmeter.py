from flowmeter.flowmeter import Flowmeter
import pandas as pd
import time

t0 = time.time()


feature_gen = Flowmeter("/Users/kyletopasna/Documents/hunter/fm/1548216696.814641.pcap")
df = feature_gen.build_feature_dataframe()

df.to_csv("/Users/kyletopasna/Documents/hunter/system_input/1548216696.814641.csv")

t1 = time.time()

print(t1-t0)