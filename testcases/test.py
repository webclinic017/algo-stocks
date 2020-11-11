import os

from method.algofuncs import getHOSETickers

vnx_file = os.path.abspath('../vn-stock-data/VNX.csv')
data = getHOSETickers(vnx_file)
print(data)