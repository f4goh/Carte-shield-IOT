I2C1.setup({ 'scl': 5,
             'sda': 4,
             bitrate: 100000 });
var g = require("SSD1306").connect(I2C1);
var y=0;
var sens=0;


function start() {
  if (sens==0){
      y+=2;
      if (y>50){
        sens=1;
      }
  }
  else{
      y-=2;
      if (y<0){
        sens=0;
      }    
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
