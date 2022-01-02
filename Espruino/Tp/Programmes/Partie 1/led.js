var toggle = false;

function start() {
    toggle = !toggle;
    digitalWrite(D0, toggle);
}

function onInit() {
      setInterval(start,1000);
}



