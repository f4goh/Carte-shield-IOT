/*
  Envoie une trame DMX sur l'uart 2 pour l'esp32 ou l'uart 1 pour l'esp8266
*/

#include "espdmx.h"

#define CHANNELS 16
#define UART 2


Espdmx dmx(CHANNELS, UART);

void setup() {
  //Serial.begin(9600);

  dmx.write(1, 128);
  dmx.write(2, 0);
  dmx.write(3, 0);
  dmx.write(4, 255);
}

void loop() {
  int n;
  for (n = 0; n <= 255; n++) {
    dmx.write(1, n);
    dmx.write(2, 255-n);
    dmx.update();
    delay(10);
  }

}
