import getpass
import os
import datetime
import time
import sys
from github import Github

#opening the github session
try:
    g = Github("your access token")
    user = g.get_user()
except (exception):
    sys.exit()

#timestamp
now = datetime.datetime.now()
timestamp = time.mktime(now.timetuple())

#creating the output directory
directory = "output/" + str("{:.0f}").format(timestamp)
if not os.path.exists(directory):
    os.makedirs(directory)

#creating and writing the HTML output
f = open(directory + "/" + "stars.html","w+")

f.write("<!DOCTYPE NETSCAPE-Bookmark-file-1>")
f.write("<HTML>")
f.write("<META HTTP-EQUIV=\"Content-Type\" CONTENT=\"text/html; charset=UTF-8\">")
f.write("<Title>Imported From Github</Title>")
f.write("<DT><H3 FOLDED>Github Stars</H3>")
f.write("<DL><p>")

for repo in user.get_starred():
    print("Exporting " + repo.name)
    link = "<DT><A HREF=\"" + repo.html_url + "\">" + repo.name + "</A>"
    f.write(link)

f.write("</DL><p>")
f.write("</HTML>")

f.close()
print("Export Completed!")
