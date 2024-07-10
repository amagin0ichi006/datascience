#series are like rows
import pandas as pd
a = [10, 40, 60]
s_eries = pd.Series(a)
print(s_eries)

#.loc to locate it
print(s_eries.loc[0])

#change d same
ser = pd.Series(a, index=["monday", "tuesday", "wenesday"])
print(ser)

#index is what wew use to change its namoing