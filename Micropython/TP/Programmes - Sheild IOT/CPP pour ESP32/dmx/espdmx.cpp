/**
    @file       espdmx.cpp
    @brief      Implémentation de la classe espdmx
                Gestion d'un trame DMX en émission
    @version    1.0
    @author     Anthony Le Cren
    @date       14 juin 2020
*/

/* ----- LIBRARIES ----- */
#include <Arduino.h>
#include "espdmx.h"



Espdmx::Espdmx(uint16_t _nbChannels, uint8_t uart) {
  serialDmx = new HardwareSerial(uart);
  nbChannels = _nbChannels + 1;
  dmxData = (uint8_t*)malloc(nbChannels * sizeof(uint8_t));
  int n;
  for (n = 0; n < nbChannels; n++) {    //clear buffer
    dmxData[n] = 0;
  }
}

// Function to send DMX data
void Espdmx::write(int Channel, uint8_t value) {
  if ((Channel >= 1) && (Channel <= nbChannels) && (value >= 0) && (value <= 255)) {
    dmxData[Channel] = value;
  }
}


void Espdmx::update() {
  //Send break
  serialDmx->begin(BREAKSPEED, BREAKFORMAT);
  serialDmx->write(0);
  serialDmx->flush();
  serialDmx->end();
  //send data
  serialDmx->begin(DMXSPEED, DMXFORMAT);
  serialDmx->write(dmxData, nbChannels);
  serialDmx->flush();
  delay(1);
  serialDmx->end();
}
