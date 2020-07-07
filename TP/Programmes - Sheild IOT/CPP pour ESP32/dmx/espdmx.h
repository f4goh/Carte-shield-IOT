/**
    @file       espdmx.h
    @brief      Implémentation de la classe espdmx
                Gestion d'un trame DMX en émission
    @version    1.0
    @author     Anthony Le Cren
    @date       14 juin 2020
*/



#ifndef __ESPDMX__
#define __ESPDMX__


//#include <inttypes.h>
#include "Arduino.h"
#include <HardwareSerial.h>

#define DMXSPEED       250000
#define DMXFORMAT      SERIAL_8N2
#define BREAKSPEED     83333
#define BREAKFORMAT    SERIAL_8N1

class Espdmx
{
  public:
    Espdmx(uint16_t _nbChannels, uint8_t uart);
    
    void write(int channel, uint8_t value);
    void update();

  private:
    HardwareSerial *serialDmx;
    uint8_t *dmxData;
    int nbChannels;
};

#endif
