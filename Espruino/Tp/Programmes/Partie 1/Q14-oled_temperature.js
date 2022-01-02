I2C1.setup({ 'scl': 5,
             'sda': 4,
             bitrate: 100000 });
var g = require("SSD1306").connect(I2C1);
var ow = new OneWire(12);
var sensor = require("DS18B20").connect(ow);


function start() {
    var temp;
    temp=sensor.getTemp();
    console.log("Temp is "+temp+"°C");
    g.clear();
    g.drawString(temp.toString(),0,0);
    g.flip();
}

function onInit() {
      g.setFontVector(20);
      setInterval(start,1000);
}
