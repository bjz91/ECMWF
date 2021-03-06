#!/usr/bin/env python
from ecmwfapi import ECMWFDataServer

server = ECMWFDataServer()
server.retrieve({
   	 "class": "ei",
   	 "dataset": "interim",
   	 "date": "2015-09-11",
   	 "expver": "1",
   	 "levelist": "46/to/60",
   	 "levtype": "ml",
   	 "param": "130.128/131.128/132.128/138.128",
   	 "step": "0",
   	 "stream": "oper",
   	 "target": "20150911_ml.nc",
	 "format": "netcdf",
   	 "time": "00/06/12/18",
   	 "type": "an",
	 "area": "75/-20/30/70",
	 "grid": "0.36/0.36",
})
