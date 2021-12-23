/*
  acquisition du convertisseur analogique numérique
  https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/peripherals/adc.html
*/
#include <driver/adc.h>

#define LDR ADC1_CHANNEL_7    //gpio 35


void setup() {
  Serial.begin(9600);
  while (!Serial); // wait for serial
  adc1_config_width(ADC_WIDTH_BIT_12);              /12 bits
  adc1_config_channel_atten(LDR,ADC_ATTEN_DB_11);   //full scale
}

void loop() {
  int val = adc1_get_raw(LDR);
  Serial.println(val);
  delay(200);
}
    
