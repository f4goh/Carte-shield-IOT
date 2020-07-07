from machine import Pin
import usocket as socket

led = Pin(0,Pin.OUT)


def web_page():
  if led.value() == 1:
    gpio_state="ON"
  else:
    gpio_state="OFF"
  
  html = """<html>
            <head>
            <title>ESP LED Web Server</title>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            </head>
            <body>
            <h1>ESP Web Server</h1> 
            <p>GPIO state: """ + gpio_state + """</p>
            <p><a href="/?led=on"><button>ON</button></a></p>
            <p><a href="/?led=off"><button>OFF</button></a></p>
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
  led_on = request.find('/?led=on')
  led_off = request.find('/?led=off')
  if led_on == 6:
    print('LED ON')
    led.on()
  if led_off == 6:
    print('LED OFF')
    led.off()
  response = web_page()
  conn.send('HTTP/1.1 200 OK\n')
  conn.send('Content-Type: text/html\n')
  conn.send('Connection: close\n\n')
  conn.sendall(response)
  conn.close()