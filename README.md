# 2023S1SEQUOIACommissioning

this project ....


# chi-Cyg strong continuum

107662 is not part of the combination, it's a slightly smaller map.

# M17SW

first example of dual IF system

# VX-Sgr

comparing different mapping strategies


# birdies


# birdies testing

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

