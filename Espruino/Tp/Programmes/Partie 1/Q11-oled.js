I2C1.setup({ 'scl': 5,
             'sda': 4,
             bitrate: 100000 });
var g = require("SSD1306").connect(I2C1);

function start() {
  g.setFontVector(20);
  g.drawString("Hello NSI",0,0);
  // write to the screen
  g.flip();  
}


