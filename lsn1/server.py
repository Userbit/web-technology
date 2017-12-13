import socket                                                                   
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                           
s.bind(('0.0.0.0', 2222))                                                       
s.listen(10)                                                                    
while True:                                                                     
    conn, addr = s.accept()                                                     
    while True:                                                                 
        data = conn.recv(1024)                                                  
        print(str(data).strip())                                                
        if not data or str(data).strip() == "close":                              
            break
        conn.send(data)                                                         
    conn.close()
