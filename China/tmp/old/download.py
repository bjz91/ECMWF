#!/usr/bin/env python
from ecmwfapi import ECMWFDataServer

import sys

str=sys.argv[1]

server = ECMWFDataServer()
server.retrieve({
   	 "class": "ei",
   	 "dataset": "interim",
   	 "date": str,
   	 "expver": "1",
   	 "levelist": "46/to/60",
   	 "levtype": "ml",
   	 "param": "131.128/132.128",
   	 "step": "0",
   	 "stream": "oper",
   	 "target": "2010/"+str.replace('-','')+"_U_V_ml.nc",
	 "format": "netcdf",
   	 "time": "00/06/12/18",
   	 "type": "an",
	 "area": "60/70/10/150",
	 "grid": "0.36/0.36",
})
