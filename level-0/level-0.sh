for ((i = 0; i < 1024; i++)); do curl 'http://54.221.6.249/level0.php' -H 'Host: 54.221.6.249' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:51.0) Gecko/20100101 Firefox/51.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.5' --compressed -H 'Referer: http://54.221.6.249/level0.php' -H 'Cookie: PHPSESSID=s4l8it10ip9tv9dcb0qcl3iu82' -H 'Connection: keep-alive' -H 'Upgrade-Insecure-Requests: 1' --data 'id=28&holdthedoor=Submit+Query' > /dev/null 2> /dev/null; sleep `./random_sleep`; done