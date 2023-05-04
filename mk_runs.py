#! /usr/bin/env python
#
#   script generator for project="2021-S1-US-3"
#
#   lmtinfo.py grep US-3 Science Map | awk '{print $2}' | sort


import os
import sys

from lmtoy import runs

project="2023-S1-2023S1SEQUOIACommissioning"

#        obsnums per source (make it negative if not added to the final combination)
on = {}

on["M17SW"] = [ 108768,]

on["VX-Sgr"] = [ 108753, 108754, 108756, 108760, 108762, 108764, 108766,
                 109461, 109463, 109465, 109467,]                                # 4-may

on['chi-Cyg'] = [-107662, 107664, 107665, 107666, 107667 ]      # 2-apr


#        common parameters per source on the first dryrun (run1a, run2a)
pars1 = {}
pars1['chi-Cyg']   = "pix_list=-3,-13 extent=120"
pars1["M17SW"] = ""
pars1["VX-Sgr"] = ""


#        common parameters per source on subsequent runs (run1b, run2b)
pars2 = {}
pars2['chi-Cyg']   = "srdp=1 admit=0"
pars2["M17SW"] = ""
pars2["VX-Sgr"] = ""


if __name__ == '__main__':    
    runs.mk_runs(project, on, pars1, pars2)
