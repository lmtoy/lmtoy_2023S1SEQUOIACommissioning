# 2023S1SEQUOIACommissioning

Various SEQ commission tasks:

1.  birdies
2.  coordinate systems (Az-El, Ra-Dec, L-B)
3.  efficiency difference small maps between Map(Ra/C) and Map(Ra/D)


# chi-Cyg strong continuum

107662 is not part of the combination, it's a slightly smaller map.

# M17SW

first example of dual IF system

# VX-Sgr

comparing different mapping strategies


# birdies

birdies generally have side-lobes.  In medium resolution mod 3 channels below and above:

      birdies=1021,1024,1027,2045,2048,2051,3069,3072,3075
      SLpipeline.sh obsnum=109941 restart=1 dv=100 dw=400 maskmoment=0 pix_list=-0 birdies=$birdies

      SLpipeline.sh obsnum=109941 restart=1 dv=50 dw=50 maskmoment=0 pix_list=-13 bank=0

      # M17SW 115.271204  110.201353 	
      SLpipeline.sh obsnum=108768 pix_list=-0,14,15 restart=1 dv=50 dw=400 extent=240  maskmoment=0
      115.27120  birdies at 1024, 2048, 3072
      110.20135  birdies at 1024, 2048, 3072


An example of a wide channel with birdies:

      # KZ-Peg 86.243442   88.631847 
      SLpipeline.sh obsnum=107996 pix_list=-0,4,14,15 restart=1 dv=100 dw=1200 extent=120 maskmoment=0
      86.243442   nchan=2048   birdies at 512, 1024, 1536
      88.631847                no obvious birdies

      # chi-Cyg 115.271204,0
      SLpipeline.sh obsnum=107666 pix_list=-3,13 restart=1 dv=100 dw=900 extent=120 maskmoment=0


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


# Mapping Efficiencies


     # RT-Vir
     SLpipeline.sh obsnum=109963 restart=1 extent=100 pix_list=-13,14,15  # Az/D
     SLpipeline.sh obsnum=109958 restart=1 extent=100 pix_list=-13,14,15  # Az/C
     # CHI-Cyg
     SLpipeline.sh obsnum=108783 restart=1 extent=120 pix_list=-13,14,15  # Ra/D
     SLpipeline.sh obsnum=108787 restart=1 extent=120 pix_list=-13,14,15  # Ra/C


## Bs examples

     108756 -- April 20  BS --  wrong freq -- shifted by 347 km/s
     108762 -- April 20  BS --  wrong freq -- shifted by 347 km/s
     108766 -- April 20  BS --  correct freq
     Where are 2nd IF spectra?

108766
process_bs.py --obs_list 108766 -o junk2.txt --pix_list 8,10 --use_cal --block -2 --stype 2


## Ps examples

     108754 -- April 20  PS -- wrong freq
     108760 -- April 20  PS -- not processed
     108764 -- April 20  PS -- not processed
