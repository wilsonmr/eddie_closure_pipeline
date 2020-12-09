#!/bin/bash
# Grid Engine options (lines prefixed with #$)
# set name on cmd line
#$ -e ./output/$JOB_NAME.$TASK_ID.log
# set output to same file
#$ -o ./output/$JOB_NAME.$TASK_ID.log
# set cwd (~/<job_id>)
#$ -cwd
# resources (time and memory) per replica
#$ -l h_rt=08:00:00
# here we use 4 cores with 4G for n3fit global fit
#$ -pe sharedmem 4
#$ -l h_vmem=4G

#source bash_profile to ensure fitting tools are on the path
source /home/s1758208/.bash_profile
source use-conda
conda activate nnpdf

#run fit
n3fit <FITNAME>.yml $SGE_TASK_ID
