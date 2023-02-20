import socket
import json

host = socket.gethostname()
port = 5000
# Erstelle einen Socket für den Server
server_socket = socket.socket()

# Binde den Socket an eine Adresse und einen Port
server_socket.bind((host, port))

# Beginne das Abhören von Verbindungen
server_socket.listen()

# Akzeptiere eine Verbindung von einem Client
client_socket, client_address = server_socket.accept()

print('connection from: ' + str(client_address))
# Empfange Daten vom Client

while True:
    data = client_socket.recv(1024)
    print('Daten empfangen: ', data)
    
    
        
    
    if(data != b''):
        jsonFormat = json.loads(data)
        name = jsonFormat['name']
        print('name ist' , name)
        
        
        if(name != 'unknown'):
            
            print('name != unknown')
            client_socket.send(b'OK')
        
        if(name == 'unknown'):
          
            val = input("Enter Name: ")
            persons_name = str.encode(val)
            
            client_socket.send(persons_name)
            
    
    
    
    
    
    

            

# Sende eine Antwort zurück an den Client


# Schließe die Verbindung mit dem Client
client_socket.close()

# Schließe den Server-Socket
server_socket.close()


#sudo kill -9 $(ps -A | grep python | awk '{print $1}')`wenn sich server aufhängt