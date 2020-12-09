#!/bin/bash
# Grid Engine options (lines prefixed with #$)
# Set Name on cmd line
#$ -e ./output/$JOB_NAME.log
#set output to same file
#$ -o ./output/$JOB_NAME.log
#set cwd (~/<job_id>)
#$ -cwd
#resources (time and memory) per replica
#$ -l h_rt=00:25:00
#$ -l h_vmem=4G
# email on abort (a) only, if you wish you can get email when it begins
# (change to ab)
#$ -m a

#source bash_profile to ensure fitting tools are on the path
source /home/s1758208/.bash_profile
source use-conda
conda activate nnpdf

# filter data, gen fakedata
vp-setupfit <FITNAME>.yml
# rebuild data for n3fit
vp-rebuild-data <FITNAME>
