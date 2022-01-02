I2C1.setup({ 'scl': 5,
             'sda': 4,
             bitrate: 100000 });
var g = require("SSD1306").connect(I2C1);
var y=0;


function start() {
  y++;
  if (y>50){
    y=0;
  }
  g.clear();
  g.drawString("Hello NSI",15,y);
  // write to the screen
  g.flip();  
}


function onInit() {
      g.setFontVector(20);
      setInterval(start,1);
}
