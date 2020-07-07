/*   NeoPixelTest
     clignote les 4 leds en rouge
     https://github.com/Makuna/NeoPixelBus/wiki/ESP32-NeoMethods
*/

#include <NeoPixelBus.h>
#define PIXEL_COUNT 4   // 4 rgb leds
#define PIXEL_PIN  18  // broche des neopixels

#define colorSaturation 8

NeoPixelBus<NeoGrbFeature, NeoEsp32Rmt0800KbpsMethod> strip(PIXEL_COUNT, PIXEL_PIN);

RgbColor rouge(colorSaturation, 0, 0);
RgbColor vert(0, colorSaturation, 0);
RgbColor bleu(0, 0, colorSaturation);
RgbColor blanc(colorSaturation);
RgbColor black(0);

int tempo=500;

void setup()
{
  Serial.begin(9600);
  while (!Serial); // wait for serial

  Serial.println();
  Serial.println("Initialisation...");
  Serial.flush();

  // this resets all the neopixels to an off state
  strip.Begin();
  strip.Show();

  Serial.println();
  Serial.println("Clignotement...");
}


void loop()
{
  allume(rouge);
  delay(200);
  eteint();
  delay(500);
}


void allume(RgbColor couleur) {
  int n;
  for (n = 0; n < PIXEL_COUNT; n++) {
    strip.SetPixelColor(n, couleur);
  }
  strip.Show();
}

void eteint() {
  int n;
  for (n = 0; n < PIXEL_COUNT; n++) {
    strip.SetPixelColor(n, black);
  }
  strip.Show();
}
