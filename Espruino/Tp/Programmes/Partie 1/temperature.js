var ow = new OneWire(12);
var sensor = require("DS18B20").connect(ow);

function start() {
    var temp;
    temp=sensor.getTemp();
    console.log("Temp is "+temp+"°C");
}

function onInit() {
      setInterval(start,1000);
}


