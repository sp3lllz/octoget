# octoget
A simple webpage and python script to get the current rate from octopus energy.



##Prerequisites
A linux server with python and apache installed. (a rasberry pi is a great low cost way to host this)


#SETUP
Download the octoget.py file and index.html file 
Place in `/var/www/html/` 
SSH into or open the terminal to your machine and set up two crontab jobs as follows 
`*/31 * * * * python3 /var/www/html/octoget.py` and 
`*/1 * * * * python3 /var/www/html/octoget.py`
this will create two jobs to run the script 1 minute past and 31 minutes past the hour to grab the current rate since octopus tarrif works in 30 minute blocks
