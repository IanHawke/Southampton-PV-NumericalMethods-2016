# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 14:22:25 2016

@author: ih3

First get some data from HelioClim. I used

http://www.soda-is.com/eng/services/service_invoke/gui.php?xml_descript=hc3v5_invoke_15_demo.xml#parameters

Get a file. Save the data. Change the start of the name from "request" to "<place>" and add the <place> to the list of places below.

By fixing the skiprows to 25 it's likely that the first couple of entries gets missed, but the request doesn't give a consistent number of header rows. As the first couple of entries are at night, the data isn't interesting anyway.
"""
from glob import glob
import numpy

years=[2004,2005]
places=["southampton", "loughborough", "liverpool", "bath", "oxford", "cambridge", "sheffield"]

for place in places:
    f=glob(place+"*csv")[0]
    print(f)
    data=numpy.loadtxt(f,skiprows=25,delimiter=";",usecols=(0,5))
    for year in years:
        d=data[data[:,0]==year,-1]
        d=numpy.fmax(d, 0)
        t=numpy.linspace(0,(len(d)-1)/4.0,len(d))
        dt = numpy.vstack((t,d)).T
        header = """HelioClim data for {}.
        Columns: Hours after midnight, Jan 1 {}. Diffuse Solar Irradiation (Wh/m2).""".format(place, year)
        numpy.savetxt(place+"_{}.txt".format(year), dt, header=header)
