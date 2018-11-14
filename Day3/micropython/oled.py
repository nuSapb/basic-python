#hardware platform: FireBeetle-ESP8266
from machine import Pin,I2C
import ssd1306
from time import sleep
i2c = I2C(scl=Pin(2), sda=Pin(0), freq=100000)  #Init i2c

lcd=ssd1306.SSD1306_I2C(128,64,i2c)
lcd.fill(0)#create LCD object,Specify col and row
 
a = 0
while True:
  lcd.fill(0)
  lcd.text("Hello",0,0)                         #set "DFRobot" at (0,0)
  lcd.text("Test",24+a,16)
  lcd.text(str(a),64,24)
  lcd.show()
  a += 1 
  print(a)
  sleep(1) 
