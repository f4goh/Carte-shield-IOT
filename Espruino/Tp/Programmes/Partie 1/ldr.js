var ldr;

function start() {
    ldr=analogRead(A0);
    console.log(ldr);
}

function onInit() {
      setInterval(start,1000);
}



