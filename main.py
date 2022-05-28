import requests as req
import re, html, time, os, random
from datetime import datetime

def generate():
    response = req.get("http://www.4geeks.de/cgi-bin/webgen.py")
    matcher = r"<pre>.*</pre>"
    programm = re.findall(matcher, response.text, flags=re.M | re.S)[0][5:-6]
    programm = html.unescape(programm)
    with open("generated.py", "w") as f:
        f.write(programm)

while True:
    generate()
    now = datetime.now()
    os.system("git add .")
    curr = now.strftime("%d/%m/%Y %H:%M:%S")
    os.system(f"git commit -m '{curr}'")
    os.system("git push")
    time.sleep(60*60 + random.randint(-600, 600))
