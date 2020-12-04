#!/bin/bash
# Grid Engine options (lines prefixed with #$)
# Set Name on cmd line
#$ -e ./output/$JOB_NAME.log
#set output to same file
#$ -o ./output/$JOB_NAME.log
#set cwd (~/<job_id>)
#$ -cwd
#resources (time and memory) per replica
#$ -l h_rt=02:00:00
#$ -l h_vmem=8G
# email on abort (a) and end (e) so we know when to log back onto eddie
#$ -m ae

#source bash_profile to ensure fitting tools are on the path
source /home/s1758208/.bash_profile
source use-conda
conda activate nnpdf

source user_settings.ini

#run evolvefit
evolven3fit <FITNAME> $END_FIT_REP
# run postfit - bypass integrability for now.
postfit $TARGET_REPS <FITNAME> --integrability-threshold $INT_THRESH

# try uploading - only works if ssh key is on eddie
if [ $? -eq 0 ]; then
    echo "post fit successful: uploading"
    vp-upload <FITNAME>
else
    echo "postfit failed"
fi
