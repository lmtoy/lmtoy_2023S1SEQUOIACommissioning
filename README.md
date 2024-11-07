# 2023S1SEQUOIACommissioning

Various SEQ commission tasks:

1.  birdies
2.  coordinate systems (Az-El, Ra-Dec, L-B)
3.  efficiency difference small maps between Map(Ra/C) and Map(Ra/D)
4.  Bs/Ps testing - narrow, intermediate and wide mode

Science projects in 2023-S1:

1. 2023-S1-UM-8  - NGC4388 -  1 bank 800 MHz
2. 2023-S1-MX-28 - TYC_2597_735_1 -  1 bank 800 MHz
3. 2023-S1-MX-49 - L1157-B1 - 2 banks 400MHz - many birdies 
4. 2023-S1-UM-15 - HB114_13CO - 1 bank mistake -  200MHz - w/ birdies
5. 2023-S1-UM-16 - G1.7+3.7-234  [MarkH] 400MHz? 

# Observations

     2023-02-15T03:05:28 - 12:43:44  105480     Ori-KL (Bs,Map) and many sources (all sky pointing?)
     2023-02-16T02:56:34 - 03:49:23  105693     -
     2023-02-17T02:36:18 - 09:09:12  105836     only few pointings
     2023-04-01T08:50:59 - 10:19:54  107570     -
     2023-04-02T08:28:59 - 11:52:54  107638     only few pointings
     2023-04-14T20:05:32 - 21:21:38  107796     -
     2023-04-15T08:00:13 - 12:53:44  107899     only few pointings
     2023-04-20T08:34:40 - 11:55:01  108726     DAY1: VX-Sgr (Ps/Bs)  M17 (1x) CHI-Cyg (pointing)
     2023-05-04T08:13:26 - 10:07:10  109420     DAY2: VX-Sgr (4x), Bs/Ps different modes
     2023-05-08T03:12:20 - 08:03:53  109905     DAY3: RLeo (4x)
     2023-05-26T05:10:36 - 11:05:22  110002     U-Her,RR-Aql 

# chi-Cyg strong continuum

107662 is not part of the combination, it's a slightly smaller map.

# M17SW

first example of dual IF system

# VX-Sgr

comparing different mapping strategies


# birdies

birdies generally have side-lobes.  In medium resolution mod 3 channels below and above:

##  109941:  2-IF  4096 channels


Here one can clearly side birdie has side-lobe structures

       # quick peek
      SLpipeline.sh obsnum=109941 restart=1 dv=50 dw=50 maskmoment=0 
       # RESTFREQ 86.2434 88.6318 GHz   - 560.919  -829.189 km/s and 545.776  -806.872 km/s  
       # fake center vlsr=-250 to get the wide band
      SLpipeline.sh obsnum=109941 restart=1 vlsr=-250 dv=50 dw=500 maskmoment=0 extent=240
       # clear birdies=1024,2048,3072 in both bank's
      SLpipeline.sh obsnum=109941 oid=0 bank=0 birdies=1024,2048,3072
      SLpipeline.sh obsnum=109941 oid=1 bank=1 birdies=1024,2048,3072 pix_list=-0
      SLpipeline.sh obsnum=109941 oid=1 bank=1 birdies=1021,1024,1027,2045,2048,2051,3069,3072,3075      
      SLpipeline.sh obsnum=109941 oid=1 bank=1 birdies=1021,1024,1027,2045,2048,2051,3069,3072,3075      
      mv 109941 109941__wide

       # bank 0 beam 13 has slope, bit noisier
       # bank 0 beam 0  partially 0 again


      SLpipeline.sh obsnum=109941 restart=1 dv=50 dw=50 maskmoment=0 extent=240
       # clear birdies=1024,2048,3072 in both bank's
      SLpipeline.sh obsnum=109941 oid=0 bank=0 birdies=1021,1024,1027,2045,2048,2051,3069,3072,3075
      SLpipeline.sh obsnum=109941 oid=1 bank=1 birdies=1024,2048,3072 pix_list=-0
      mv 109941/ 109941__narrow

      SLpipeline.sh obsnum=109941 restart=1 dv=100 dw=400 maskmoment=0 pix_list=-0 birdies=$birdies

      SLpipeline.sh obsnum=109941 restart=1 dv=50 dw=50 maskmoment=0 pix_list=-13 bank=0


## 108768 :  M17, 2-IF example of intermediate channels (400MHz, 4096 channels)

       # M17SW 115.271204  110.201353 	
      SLpipeline.sh obsnum=108768 pix_list=-0,14,15 restart=1 dv=50 dw=400 extent=240  maskmoment=0
       # bank=0 115.27120  birdies=1024,2048,3072
       # bank=1 110.20135  birdies=1024,2048,3072

## 107996 : KZ-Peg 2-IF wide channel (800MHz, 2048 channels) with birdies in bank 0

       # KZ-Peg 86.243442  88.631847 - Map/A/C
       # first test which beams are bad
      SLpipeline.sh obsnum=107996 restart=1 dv=50 dw=50
       # bank=0 14,15 are very bad
       # bank=1 all good, though beam 0 has oddly low Tsys (RMS higher too)
      SLpipeline.sh obsnum=107996 pix_list=-14,15

       # now  remove the bad beams over the full range of the band - we ignore the bad edge channels
      SLpipeline.sh obsnum=107996 pix_list=-14,15 restart=1 dv=100 dw=1200 extent=120 maskmoment=0
       # 86.243442   birdies=512,1024,1536    beam 1 large RMS mostly due to extreme channels
       # 88.631847   no obvious birdies       beam 0,4 have missing data , tsys low in low channels
      SLpipeline.sh obsnum=107996 oid=0 bank=0 birdies=512,1024,1536 
      SLpipeline.sh obsnum=107996 oid=1 bank=1 pix_list=-0,4 
      mv 107996 107996__wide

       # now focus on the maser line
      SLpipeline.sh obsnum=107996 pix_list=-14,15 restart=1 dv=10 dw=20 extent=120 maskmoment=0
       # bank 0, beams 2,6 looks negative, due to the birdies
       # we skip birdies for bank 1
      SLpipeline.sh obsnum=107996 oid=0 bank=0 birdies=512,1024,1536 
      SLpipeline.sh obsnum=107996 oid=1 bank=1 pix_list=-0,4 birdies=0
      mv 107996 107996__narrow

## 107666: wide band 1-IF (800 MHz 2048 channels)

       # chi-Cyg 115.271204,0  Map/Az-D
       # first a quick run with all beams to see which are bad
      SLpipeline.sh obsnum=107666 restart=1 dv=50 dw=50
       # actually crashed, look at Tsys logs: 3 and 13 are bad
      SLpipeline.sh obsnum=107666 restart=1 pix_list=-3,13 dv=50 dw=50 extent=120 maskmoment=0

       # wide view
      SLpipeline.sh obsnum=107666 pix_list=-3,13 restart=1 dv=100 dw=900 extent=120 maskmoment=0
       # clearly shows increasing Tsys towards 115
       # no birdies!

Could it be that birdies only show up if the 2nd IF is present?


# coordinate systems

     109933 MAP  Az/EL
     109935 MAP  RA/DEC
     109937 MAP  RA/DEC rot
     109941 MAP  L/B

      # pix_list=-1,8 to easily identify the orientation of the array on the sky
      # run2
     SLpipeline.sh obsnum=109933 restart=1 dv=50 dw=50 maskmoment=0 extent=240 pix_list=-1,8
     SLpipeline.sh obsnum=109935 restart=1 dv=50 dw=50 maskmoment=0 extent=240 pix_list=-1,8
     SLpipeline.sh obsnum=109937 restart=1 dv=50 dw=50 maskmoment=0 extent=240 pix_list=-1,8
     SLpipeline.sh obsnum=109941 restart=1 dv=50 dw=50 maskmoment=0 extent=240 pix_list=-1,8

      # and checking if ds9 sees the same thing
     SLpipeline.sh obsnum=109935 restart=1 dv=50 dw=50 maskmoment=0 extent=240
     SLpipeline.sh obsnum=109935 oid=0 bank=0
     SLpipeline.sh obsnum=109935 oid=1 bank=1

     SLpipeline.sh obsnum=109941 restart=1 dv=50 dw=50 maskmoment=0 extent=240
     mv 109941 109941__lb
     SLpipeline.sh obsnum=109941 restart=1 dv=50 dw=50 maskmoment=0 extent=240 map_coord_use=1     
     mv 109941 109941__rd

# Mapping Efficiencies

     # RT-Vir
     SLpipeline.sh obsnum=109963 restart=1 extent=150 pix_list=-13,14,15  # Az/D   1-IF
     SLpipeline.sh obsnum=109958 restart=1 extent=150 pix_list=-13,14,15  # Az/C   2-IF
     # CHI-Cyg
     SLpipeline.sh obsnum=108783 restart=1 extent=150 pix_list=-13,14,15  # Ra/D   2-IF
     SLpipeline.sh obsnum=108787 restart=1 extent=150 pix_list=-13,14,15  # Ra/C   2-IF

## Ps examples

SiO masers observed in dual-IF, setting to 86.2 (SiO) and 88.6 (HCN). The SiO line is about 25K, the HCN line about 0.1K.

     # VX-Sgr 86.243442,88.631847 
     108754 -- April 20  PS -- wrong freq
     108760 -- April 20  PS -- 
     108764 -- April 20  PS -- BENCH4

## Bs examples

     # VX-Sgr 86.243442,88.631847 
     108756 -- April 20  BS --  wrong freq -- shifted by 347 km/s
     108762 -- April 20  BS --  wrong freq -- shifted by 347 km/s
     108766 -- April 20  BS --  correct freq  BENCH4

      # 108766
     process_bs.py --obs_list 108766 -o junk2.txt --pix_list 8,10 --use_cal --block -2 --stype 2


# Testing multi-IF mapping

Here's the ongoing testing with the SLpipeline using bank= and oid= to test
the multi-IF data, as well as backwards compatility with the older single-IF
data.

Starting in Feburary 2023 we have new numbands=2 data, though one dataset
got messed up with numbands=2 and two restfreq's (the trigger for 2nd IF
data is present)

a. numbands=1  = old data - no __0 was used. we keep it that way - w
b. numbands=2  = new data, but with one band in bank 0; the normal way
c. numbands=2  = new data, but with one band in bank 1 (have no examples)
d. numbands=2  = new data, with data in both banks
e. numbands=2  = new data, with data in one bank, but restfreq shows 1 [bug]

Examples with small amounts of data for debugging
a.  94052  94048
b.  107666      also:  109963 
d.  109935 

##  old single IF

 # a: 1-IF  1-bank
SLpipeline.sh obsnum=94052 restart=1    #  bad
SLpipeline.sh obsnum=94048 restart=1    #  bad

 # old bench1 data
SLpipeline.sh obsnum=79448 restart=1 dv=20 dw=20     
  -> ok, but no __oid   (does say bank=)
SLpipeline.sh obsnum=79448
  -> now showing __oid
SLpipeline.sh obsnum=79448 dv=50 dw=50 vlsr=0
  -> something doesn't look quite right

 # and another way now
SLpipeline.sh obsnum=79448 restart=1 dv=20 dw=20 pix_list=-1
SLpipeline.sh obsnum=79448 dv=50 dw=50 vlsr=0                        # didn't catch the new vlsr
SLpipeline.sh obsnum=79448 pix_list=-2                               # ok
SLpipeline.sh obsnum=79448 dv=50 dw=50 vlsr=0 
 # alternative also works
SLpipeline.sh obsnum=79448 restart=1 dv=20 dw=20 bank=0

 # combine:
SLpipeline.sh obsnums=79448,79448 restart=1 bank=0
-> doesn't work now





## new dual IF

 # b: 2-IF  1-bank
SLpipeline.sh obsnum=107666 restart=1 pix_list=-3 dv=50 dw=50 extent=120 maskmoment=0
  -> need -3, something bad
SLpipeline.sh obsnum=107666 vlsr=10 dv=50 dw=100
  -> ok now (default vlsr=10 was a bit off for chi-Cyg)
  -> uses __0

 # then combine
SLpipeline.sh obsnums=107666,107666 restart=1
  -> works, but doesn't say __0 and some pars are off now
  

 # d: 2-IF 2-bank
debug=1

SLpipeline.sh obsnum=109935 restart=1 dv=20 dw=20 maskmoment=0 extent=240      debug=$debug
-> spectral coverage is for bank=1 for both
SLpipeline.sh obsnum=109935 oid=0 bank=0                                       debug=$debug
-> now good
SLpipeline.sh obsnum=109935 oid=1 bank=1 pix_list=-0                        debug=$debug
-> now good 
SLpipeline.sh obsnum=109935 oid=1 bank=1 dv=40 dw=40                           debug=$debug
-> not good, it's got beam 0 back!!!
SLpipeline.sh obsnum=109935 oid=1 bank=1 dv=40 dw=40 pix_list=-0               debug=$debug
-> would not work without the pix_list
SLpipeline.sh obsnum=109935 oid=0 bank=0   
-> ok

# combo of one bank
SLpipeline.sh obsnum=109935 restart=1 dv=20 dw=20 maskmoment=0 extent=240 oid=0 bank=0
SLpipeline.sh obsnums=109935,109935 oid=0 bank=0  

# NOW BAD
# e. 105907/105908 & 105527
SLpipeline.sh obsnum=105527 numbanks=-2 restart=1

