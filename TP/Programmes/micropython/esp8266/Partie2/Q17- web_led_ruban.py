from machine import Pin
import usocket as socket
from neopixel import NeoPixel
from machine import Pin,ADC

NBPIXELS=4
np = NeoPixel(Pin(14), NBPIXELS)

def setColorLed(color):
    for n in range(0,4):
        np[n] = color
    np.write()
    

def web_page():
  html = """<html>
            <head>
            <title>ESP neopixels Web Server</title>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            </head>
            <body>
            <h1>ESP neopixels Web Server</h1> 
            <form>
                Choisir une couleur pour le ruban de leds:
                <input type="color" name="couleur" id="couleur"/>
                <br>
                Envoi de la couleur sélectionnée
                <input type="submit" value="envoyer" />
            </form>
            </body>
            </html>"""

  return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)


while True:
  conn, addr = s.accept()
  print('Got a connection from %s' % str(addr))
  request = conn.recv(1024)
  request = str(request)
  print('Content = %s' % request)

  position_couleur = request.find('%')
  print(position_couleur)
  if position_couleur==16:
      rouge = int(request[19:21],16)
      vert = int(request[21:23],16)
      bleu = int(request[23:25],16)
      print(rouge,vert,bleu)
      couleur=(rouge,vert,bleu)
      for n in range(0,NBPIXELS):
          np[n] = couleur
      np.write()
  response = web_page()
  conn.send('HTTP/1.1 200 OK\n')
  conn.send('Content-Type: text/html\n')
  conn.send('Connection: close\n\n')
  conn.sendall(response)
  conn.close()
  
  
  
  







 