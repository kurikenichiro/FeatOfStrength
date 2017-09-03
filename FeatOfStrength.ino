/*
Library examples for TM1638.

Copyright (C) 2011 Ricardo Batista <rjbatista at gmail dot com>

This program is free software: you can redistribute it and/or modify
it under the terms of the version 3 GNU General Public License as
published by the Free Software Foundation.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
*/

#include <TM1638.h>

const byte dioPin = 8;
const byte clkPin = 9;
const byte stb0Pin = 7;
const bool isDisplayActive = true;
const byte intensity = 1;

TM1638 module(dioPin, clkPin, stb0Pin, isDisplayActive, intensity);

void setup()
{
  Serial.begin(9600);

  // display a hexadecimal number and set the left 4 dots
  module.setDisplayToHexNumber(0x1234ABCD, 0xF0);
}

void loop()
{
  serialCommandHandler();
}

void serialCommandHandler()
{
  static String inString = "";

  while (Serial.available() > 0)
  {
    char inChar = Serial.read();

    if (inChar != '\n')
    {
      inString += inChar;
    }
    else
    {
      char firstChar = inString.charAt(0);

      // Handle LED Command
      if (firstChar == 'l')
      {
        char secondChar = inString.charAt(1);

        if (secondChar == 'a')
        {
          word ledWord = stringToInt(inString.substring(2));
          module.setLEDs(ledWord);
        }
        else
        {
          byte ledColor = TM1638_COLOR_NONE;

          if (secondChar == 'r')
          {
            ledColor = TM1638_COLOR_RED;
          }
          else if (secondChar == 'g')
          {
            ledColor = TM1638_COLOR_GREEN;
          }

          byte ledPosition = stringToInt(inString.substring(2));

          if (ledPosition < 8)
          {
            module.setLED(ledColor, ledPosition);
          }
          else
          {
            Serial.println("led position must be 0~7");
          }
        }
      }
      else if (firstChar == 'b')
      {
        byte buttons = module.getButtons();
        Serial.println(buttons, DEC);
      }

      // clear the string for new input:
      inString = "";
    }
  }
}

int stringToInt(String parseString)
{
  parseString.trim();
  return parseString.toInt();
}
