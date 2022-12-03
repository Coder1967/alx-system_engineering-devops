The outage occured between 1pm-3pm WAT.
The static webpage 0-index/hbnb was unable to be acessed. The root cause was an error in the nginx configuration.
The location parameter was directing users to the file 0-index/bnb instead of 0-index/hbnb. As a result, a 404 error was raised.
The issue was detected 5:20pm WAT, when the acessing the webpage was attempted. It was odd as other webpages functioned properly.
My first move was to ensure nginx was listening on the right port by running 'sudo lsof -i -P -n | grep LISTEN' on the commandline which showed
nginx was indeed listening on the right port. My next thought was to acess the nginx server configuration where the location parameter was defined for
acess to 0-index/hbnb content which was when I spotted the problem. A simple typo mistake. Fixed it and behold, the webpage was properly displayed
on the browser. This would have been easily detected before deployment if better tests were carried out.
