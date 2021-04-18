#include <Wire.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd = LiquidCrystal_I2C(0x27, 16, 2);

void setup() {
  // Initiate the LCD:
  lcd.init();
  lcd.backlight();
}

void loop() {
  int delaylength = 10;
  for(int i=0; i<16; i++){
    lcd.setCursor(i, 0);
    lcd.print(random(9));
    delay(delaylength);
  }
  for(int i=0; i<16; i++){
    lcd.setCursor(i, 1);
    lcd.print(random(9));
    delay(delaylength);
  }
  delay(500);
}
