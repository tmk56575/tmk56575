import sys
import urllib.request
import urllib.parse

if(len(sys.argv) >= 2 ):
	title = sys.argv[1]
else:
	title = input("title>")

# dbg, json, none, php, txt, xml, yaml
data_format = "?format=txt"
# 
data_action = "&action=query"
data_prop = "&prop=revisions"
data_titles = "&titles="+urllib.parse.quote(title)
data_rvprop = "&rvprop=content"

baseurl = "http://ja.wikipedia.org/w/api.php"
apiurl = baseurl + data_format + data_action + data_prop + data_titles + data_rvprop
print(apiurl)

reply = urllib.request.urlopen(apiurl).read().decode("utf-8")
open("test.txt","w").write(reply)
