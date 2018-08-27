```bash

# first you'll need a username on dreamhost to access with ssh
# and to know which server you use - see https://panel.dreamhost.com/index.cgi?tree=users.users& and if you don't
# note that in these commands i've masked the username and server i use on dreamhost (displayed here as 'my-bot' and 'my-dreamhost-server' respectively)

# this file was very useful - https://gist.github.com/moonmilk/8d78032debd16f31a8a9

# command history
ssh my-bot@my-dreamhost-server.dreamhost.com
# password

# install python3 - [instructions](https://help.dreamhost.com/hc/en-us/articles/115000702772-Installing-a-custom-version-of-Python-3)
cd ~
mkdir tmp
cd tmp
wget https://www.python.org/ftp/python/3.6.2/Python-3.6.2.tgz
tar zxvf Python-3.6.2.tgz 
cd Python-3.6.2 
./configure --prefix=$HOME/opt/python-3.6.2
make
make install

cd ~
nano .bash_profile
# add the following line
export PATH=$HOME/opt/python-3.6.2/bin:$PATH
# ctrl-O to save; enter to confirm; ctrl-x to close; now we're back to bash

# check we have the right python
which python3 
python3 --version
pip3 install --upgrade pip # just to be sure we're up to date
pip3 install virtualenv # not actually necessary, comes pre-installed


# now to make the bot
virtualenv movielinesbot
cd movielinesbot
pip install tweepy

# in a separate shell window
# create a test file named ```test.py``` (just contains ```print("Hello World")```) on local machine
# cd to folder
cd /Users/o/Documents/github-root/bots/movielinesbot/
# scp upload file
scp test.py my-bot@my-dreamhost-server.dreamhost.com:/home/my-bot/movielinesbot
# password

# back to the ssh shell
python test.py
# it prints "Hello World" - success!

# now scrabble to write python code
# made several files:
# - "movie_lines-alphabetised.txt" - a clean "movie lines" document - all duplicates removed
# - "lines_read.csv" - a log file (to log time, number of tweets posted, and tweet content)
# - bot.py - a script to post tweets
# - movielinebot.sh a bash script to activate the virtualenv, run the python script with authentication, and then deactivate the virtualenv. this isn't included in GitHub as it has my bot credentials in it.

# change the demo-script.sh.txt to be named script.sh
# and put your access keys, secrets and tokens into the bits marked ```YOUR_TOKEN_HERE``` etc
# and change the filepaths to point to the ones you set up earlier
# scp entire folder to dreamhost (from non-ssh window)
scp * my-bot@my-dreamhost-server.dreamhost.com:/home/my-bot/movielinesbot

# back to the ssh window
# we need to make the script executable
chmod +x script.sh

# then test it
./script.sh

# if it works you'll see a tweet
# if not, something messed up and you need to google around and see what went wrong

# setting a cron job on dreamhost
# see here for help with this https://help.dreamhost.com/hc/en-us/articles/215088668-How-do-I-create-a-cron-job-
# this is my cron command - it just fires up the cron 
# as set in https://panel.dreamhost.com/index.cgi?tree=advanced.cron&
sh /home/my-bot/movielinesbot/script.sh > /dev/null

# mine runs every five minutes

# enjoy :)
```