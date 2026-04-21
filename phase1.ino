#include <Wire.h> #include<FaBo3Axis_ADXL345.h> FaBo3Axis;
int x; int y; int z;
#include<SoftwareSerial.h> SoftwareSerialmySerial(8,9); const int FLX1=A0;
const int FLX2=A1; const int FLX3=A2; const int FLX4=A3; float tempc=0;
float tempc1=1; float tempc2=0; float tempc3=0; void setup()
{
Serial.begin(9600); mySerial.begin(9600); Serial.println("WELCOME"); pinMode(FLX1,INPUT);
pinMode(FLX2,INPUT); pinMode(FLX3,INPUT); pinMode(FLX4,INPUT); if(fabo3axis.searchDevice())
{
 
Serial.println("I am ADXL345");
}
Serial.println("Init..."); fabo3axis.configuration(); fabo3axis.powerOn(); delay(500);
}
void loop()
{
home:
fabo3axis.readXYZ(&x, &y, &z);
// Serial.print("x:");
// Serial.println(x);
// Serial.print("y:");
//Serial.println(y); if(x>20)
{
flex(); if((tempc<0.9)&&(tempc1>1.0)&&(tempc2>1.0)&&(tempc3<1.0))
{
Serial.println("THANKYOU"); mySerial.print("THANKYOU"); delay(1000);
goto home;
}
if((tempc<0.9)&&(tempc1<1.0)&&(tempc2<1.0)&&(tempc3<1.0))
{
Serial.println("HELLO"); mySerial.print("HELLO”); delay(1000);
goto home;
}
if((tempc>0.9)&&(tempc1>1.0)&&(tempc2>1.0)&&(tempc3>1.0))
{
Serial.println("SORRY"); mySerial.print("SORRY"); delay(1000);
goto home;
}
if((tempc>0.9)&&(tempc1>1.0)&&(tempc2>1.0)&&(tempc3<1.0))
{
Serial.println("I NEED HELP"); mySerial.print("I NEED HELP"); delay(1000);
goto home;
}
}
if(y>20)
{
flex(); if((tempc>1.0)&&(tempc1>1.0)&&(tempc2>1.0)&&(tempc3>1.0))
{
Serial.println("MEDICINE"); mySerial.print("MEDICINE"); delay(1000);
goto home;
}
if((tempc>1.0)&&(tempc1<1.0)&&(tempc2<1.0)&&(tempc3<1.0))
{
Serial.println("WATER"); mySerial.print("WATER"); delay(1000);
 
goto home;
}
if((tempc<1.0)&&(tempc1>1.0)&&(tempc2>1.0)&&(tempc3<1.0))
{
Serial.println("I LOVEYOU"); mySerial.print("I LOVEYOU"); delay(1000);
goto home;
}
}
if((tempc>1.0)&&(tempc1>1.0)&&(tempc2<1.0)&&(tempc3<1.0))
{
Serial.println("I AM IN EMERGENCY"); 
mySerial.print("I AM IN EMERGENCY");
if((tempc<1.0)&&(tempc1<1.0)&&(tempc2<1.0)&&(tempc3>1.0))
{
Serial.println("FOOD"); mySerial.print("FOOD"); delay(1000);
goto home;
}
}
}
void flex()
{
vout=analogRead(FLX1); tempc=vout*(5.0/1024.0);
//Serial.print("FLX1:");
//Serial.println(tempc); delay(200); vout=analogRead(FLX2);
 
tempc1 = vout * (5./1024.0);
//Serial.print("FLX2:");
//Serial.println(tempc1); delay(200);
vout =analogRead(FLX3); tempc2 = vout *(5.0/1024.0);
//Serial.print("FLX3:");
//Serial.println(tempc2); delay(200);
vout = analogRead(FLX4); tempc3 = vout * (5.0/1024.0);
//Serial.print("FLX4:");
//Serial.println(tempc3); delay(200);
}

