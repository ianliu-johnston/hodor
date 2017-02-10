# Holberton School - Hodor (Hold the Door)
Execises to connect to websites.

## Process:
0. Open up Firefox 45.0 and Firefox Developer toolbar, select the ``Network Monitor`` tab
1. Go to the website and try to post a vote.
2. Observe post request. Right click and select ``Copy as cURL``
3. Paste the curl request in a terminal session, and hit <enter>. Refresh the page to see if it worked.
4. If it did, put it in a for loop in bash. ``for ((i=0;i < 1025; i++)); do curl blahblahblah; done``
<br>
<p>This works for the first three tasks, then captcha and time restraints come into play. For the next three tasks, google it. Results are below.</p>

## Repository Conetents:
### Directory Root:
<h6>random_sleep.c</h6>
A simple program written in C to output random floating values for the sleep function, to simulate human interaction, instead of the rhythmic POST-ing of a bot
<h6>random_sleep</h6>
The program random_sleep.c compiled with ``gcc -Wall -Werror -Wextra -pedantic random_sleep.c -o random_sleep``

### Level 0:
<h6>level-0.sh</h6>
Simple shell script to curl a POST request 1024 times as a windows user and a cookie. After, it sleeps for a random amount of time between 0.0 and 10.0 seconds.
<h6>random_sleep</h6>
Compiled randomizer function.

### Level 1:
<h6>level-1.sh</h6>
Simple shell script to curl a POST request 1024 times as a windows user and a cookie. After, it sleeps for a random amount of time between 0.0 and 10.0 seconds.
<h6>random_sleep</h6>
Compiled randomizer function.

### Level 2:
<h6>level-2.sh</h6>
Simple shell script to curl a POST request 1024 times as a windows user and a cookie. After, it sleeps for a random amount of time between 0.0 and 10.0 seconds.
<h6>random_sleep</h6>
Compiled randomizer function.

### Level 3:
<h6>bypass_capcha.py</h6>

<h6>random_sleep</h6>
Compiled randomizer function.

### Level 4:
<h6>ip_renew.py</h6>
A simple Python script to tunnel through the TOR network, using random IP addresses, and POST-ing.

* [Primary Tutorial](http://sacharya.com/crawling-anonymously-with-tor-in-python/) - from sacharya.com

* Prerequisites:
  * Install Tor
  * Install Privoxy
  * Install PyTorCtl

* Brief Summary of the steps in the tutorial:
  1. Install TOR: ``sudo apt-get update; sudo apt-get install tor; sudo /etc/init.d/tor restart``
  2. Configure TOR: ``tor --hash-password password; sed -i 's/#ControlPort 9051/ControlPort 9051/;s/#HashedControlPassword/HashedControlPassword/ /etc/tor/torrc``
  3. Install PyTorCtl: ``git clone git://github.com/aaronsw/pytorctl.git; sudo pip install pytorctl/``
  4. Install Privoxy: ``sudo apt-get install privoxy``
  5. Configure Privoxy: ``sudo sed -i '1338s/^#/forward-socks5 \/localhost:9050 ./' /etc/privoxy/config``
  6. Restart privoxy and tor: ``sudo /etc/init.d/privoxy restart; sudo /etc/init.d/tor restart``
* Usage:
  * Run with ``sudo ip_renew.py | grep "" | grep -A3 "28 "``

