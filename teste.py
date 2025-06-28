import subprocess as app 

ip = '192.168.0.1'

for i in range(500):
    app.Popen(['ping', ip])

