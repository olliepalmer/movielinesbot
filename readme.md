# Movie lines bot


What does it do? It tweets one line from an alphabetised list of movie dialogue every five minutes. It was a quick exercise to get my rusty head aroung Twitter bots in 2018 (as opposed to the last time I made them about 5 years ago...).

This bot can be found at [@al_film_betical](https://twitter.com/al_film_betical)

The setup is fairly simple: I have a Dreamhost account, a Python script, and a file I want to read from. The bot runs as a cron job from my Dreamhost account once every 5 minutes.

Below are the bash instructions to set up this bot on Dreamhost. Most of the files have annotations.

You will need:

- A username on Dreamhost with access to SSH (or another web provider who'll let you use cron). Note that my username and password have been masked here as 'my-bot' and 'my-dreamhost-server' respectively
- A Twitter account set up with Developer credentials, and API keys (see [here](https://www.slickremix.com/docs/how-to-get-api-keys-and-tokens-for-twitter/) for a nice tutorial)

Note that [this file](https://gist.github.com/moonmilk/8d78032debd16f31a8a9) was very useful in setting up my bot! 

## So, let's begin!

Log into your server via SSH
```ssh my-bot@my-dreamhost-server.dreamhost.com```
```# enter password```

Install Python3  
([detailed instructions here](https://help.dreamhost.com/hc/en-us/articles/115000702772-Installing-a-custom-version-of-Python-3))

```bash
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
```

### Now to make the bot!
```
virtualenv movielinesbot
cd movielinesbot
pip install tweepy
```

in a separate shell window
create a test file named ```test.py``` (just contains ```print("Hello World")```) on local machine
```
# cd to folder
cd /Users/o/Documents/github-root/bots/movielinesbot/
# scp upload file
scp test.py my-bot@my-dreamhost-server.dreamhost.com:/home/my-bot/movielinesbot
# enter password
```

back to the ssh shell:

```
python test.py
```

if it prints "Hello World" - success!


### now scrabble to write python code

I made several files:

- [movie_lines-alphabetised.txt](movie_lines-alphabetised.txt) - a clean "movie lines" document - all duplicates removed
- [lines_read.csv](lines_read.csv) - a log file (to log time, number of tweets posted, and tweet content)
- [bot.py](bot.py) - a script to post tweets
-  ```script.sh``` - a bash script to activate the virtualenv, run the python script with authentication, and then deactivate the virtualenv. this isn't included in GitHub as it has my bot credentials in it - you'll have to look through the [demo-script.sh.txt](demo-script.sh.txt) file here and make some changes to it with your credentials!


- Change the demo-script.sh.txt to be named ```script.sh```
- Put your access keys, secrets and tokens into the bits marked ```YOUR_TOKEN_HERE``` etc
- Change the filepaths to point to the ones you set up earlier
- then ```scp``` entire folder to dreamhost (from non-ssh window):
```
scp * my-bot@my-dreamhost-server.dreamhost.com:/home/my-bot/movielinesbot
```

back to the ssh window! We need to make the script executable:
```
chmod +x script.sh
```
then test it:
```
./script.sh
```

If it works you'll see a tweet on your account. If not, something messed up and you need to google around and see what went wrong...

### Setting a Cron job on Dreamhost

See [here](https://help.dreamhost.com/hc/en-us/articles/215088668-How-do-I-create-a-cron-job-) for help with this 

This is my Cron command - it just fires up the cron in my [Dreamhost panel](https://panel.dreamhost.com/index.cgi?tree=advanced.cron&)
```
sh /home/my-bot/movielinesbot/script.sh > /dev/null
```
Mine runs every five minutes. You can fire yours up whenever you like.

I hope this helps! Enjoy. :)