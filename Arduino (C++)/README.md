# Random numbers in I2C LCD Arduino
### Circuit
![image](https://user-images.githubusercontent.com/31751427/115131090-71e20400-a01f-11eb-9104-b86fa6aba1c7.png)
[Source Image](https://www.makerguides.com/character-i2c-lcd-arduino-tutorial/)

First of all, you need to download [This](https://github.com/johnrickman/LiquidCrystal_I2C) library and put it to your libraries folder.

After that, you need to scan the LCD Address first, using the code in this folder, I2C Scanner
If you are done, you can change the address to yours, (most common address is 0x27)

After getting the address, you need to change this line of code :
```cpp
LiquidCrystal_I2C lcd = LiquidCrystal_I2C(0x27, 16, 2);
```
Change the 0x27 to your I2C address, or if 0x27 is already your address, you're good to upload the code to your arduino board.

### How does the randomization work?
Well, using a for loop, it is pretty simple!
1. The program counts from 1 to 16
2. Each time they count, they will make a random integer and print it to the cursor with the position of the counted number.
