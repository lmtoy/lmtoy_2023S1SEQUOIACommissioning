#! /usr/bin/env python
#

import os
import sys

from lmtoy import runs

project="2023S1SEQUOIACommissioning"

#        obsnums per source (make it negative if not added to the final combination)
on = {}

on["M17SW"]  = [ 108768,]                                                       # 20 apr Map

on["R-Leo"]  = [ 109933, 109935, 109937, 109941,]                               # 8 may Map

on["VX-Sgr"] = [ 108753, 108754, 108756, 108760, 108762,                        # Ps/Bs
                 109461, 109463, 109465, 109467,]                               # 4-may Map

on["VX-Sgr_S"] = [ 108764, 108766 ]                                             # Ps and Bs

on['chi-Cyg'] = [-107662, 107664, 107665, 107666, 107667,                       # 2-apr Pointing
                 108772, 108774, 108775, 108776, 108777, 108780,
                 108781, 108782, 108783, 108787, ]
#RT-Vir  109958 109963

on['KZ-Peg']  = [ 107996 ]                                                      # only 1 obs

on['MonR2']  = [ 110405, 110407, 110411, ]

#        common parameters per source on the first dryrun (run1a, run2a)
pars1 = {}
pars1['chi-Cyg']   = "pix_list=-3,-13 extent=120"          # -3 is needed, or it will crash, 13 just high Tsys
pars1["M17SW"]     = "dv=50 dw=50"
pars1["VX-Sgr"]    = ""
pars1["VX-Sgr_S"]  = ""
#pars1["R-Leo"]     = "dv=50 dw=50 extent=240"
pars1["R-Leo"]     = "extent=240"
pars1["KZ-Peg"]    = "extent=120"

pars1['MonR2']  = "extent=500"


#        common parameters per source on subsequent runs (run1b, run2b)
pars2 = {}
pars2['chi-Cyg']   = "srdp=1 admit=0"
pars2["M17SW"]     = ""
pars2["VX-Sgr"]    = ""
pars2["R-Leo"]     = "bank=0 pix_list=-5,12,13"
pars2["KZ-Peg"]    = "bank=0 pix_list=-14,15"
pars2['MonR2']    = "bank=0 pix_list=-11,13"

#pars2['M17SW']  = ["bank=0 pix_list=-0,5,12,13,14,15",
#	  	    "bank=1 pix_list=-0,2,3,4,12,13"]

pars3 = {}
pars3['chi-Cyg']   = ""
pars3["M17SW"]     = ""
pars3["VX-Sgr"]    = ""
pars3["R-Leo"]     = "bank=1 pix_list=-0,4,8,9"   # no line
pars3["KZ-Peg"]    = "bank=1 pix_list=-0"
pars2['MonR2']    = "bank=1"

if __name__ == '__main__':    
    runs.mk_runs(project, on, pars1, pars2, pars3, sys.argv)
