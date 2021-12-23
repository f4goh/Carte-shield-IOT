"""
ds18s20 onewire
        esp8266   esp32
broche   12(9)     19(9)
"""
 
from onewire import OneWire
from ds18x20 import DS18X20
from machine import Pin

#bus = OneWire(Pin(12))
bus = OneWire(Pin(19))
ds = DS18X20(bus)
capteur_temperature = ds.scan()
ds.convert_temp()
temp_celsius = ds.read_temp(capteur_temperature[0])
print(temp_celsius)

