import json
import re
#import urllib2
#import urllib.request
from urllib.request import urlopen

#text = urllib2.urlopen('http://dcsd.nutrislice.com/menu/meadow-view/lunch/').read()
text = urlopen("http://dcsd.nutrislice.com/menu/meadow-view/launch/").read()
menu = json.loads(re.search(r"bootstrapData\['menuMonthWeeks'\]\s*=\s*(.*);", text).group(1))

print(menu)
