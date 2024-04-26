#include <WiFi.h>
#include <WiFiClientSecure.h>
#include <UniversalTelegramBot.h>


#define WIFI_SSID "Kubz"
#define WIFI_PASSWORD "Kubz1234"

#define BOT_TOKEN "7187037774:AAGujRBufY8Kmdz4RLXaV48npeZcbTpdVrg"

const unsigned long BOT_MTBS = 1000; // mean time between scan messages

WiFiClientSecure secured_client;
UniversalTelegramBot bot(BOT_TOKEN, secured_client);
unsigned long bot_lasttime; // last time messages' scan has been done

const int ledPin = 2;
const int fanpin = 4;
const int bulbpin = 5;
const int bulb2pin = 18;

int ledStatus = 0;
int fanStatus=0;
int bulbStatus=0;
int bulb2Status=0;
void handleNewMessages(int numNewMessages)
{
  Serial.print("handleNewMessages ");
  Serial.println(numNewMessages);

  for (int i = 0; i < numNewMessages; i++)
  {
    String chat_id = bot.messages[i].chat_id;
    String text = bot.messages[i].text;

    String from_name = bot.messages[i].from_name;
    if (from_name == "")
      from_name = "Guest";

      if (text == "Fan laga bhai")
    { bot.sendChatAction(chat_id, "typing");
    delay(100);
    bot.sendMessage(chat_id, "Abhi Karta hu Bhai", "");
    
      digitalWrite(fanpin, HIGH); 
      fanStatus = 1;
    }

      if (text == "Fan band kar")
    { bot.sendChatAction(chat_id, "typing");
    delay(100);
    bot.sendMessage(chat_id, "Abhi kar deta hu", "" );
    
      digitalWrite(fanpin, LOW); // turn the LED on (HIGH is the voltage level)
      fanStatus = 0;
    }

    if (text == "led laga bhai")
    { bot.sendChatAction(chat_id, "typing");
    delay(100);
    bot.sendMessage(chat_id, "Hogaya bhai", "");
    
      digitalWrite(ledPin, HIGH); // turn the LED on (HIGH is the voltage level)
      ledStatus = 1;
      
    }
    if (text == "led band karde")
    {bot.sendChatAction(chat_id, "typing");
    delay(100);
    bot.sendMessage(chat_id, "Ho gaya bhai", "");
      ledStatus = 0;
      digitalWrite(ledPin, LOW); // turn the LED off (LOW is the voltage level)
      
    }
    if (text == "Light laga")
    { bot.sendChatAction(chat_id, "typing");
    delay(100);
    bot.sendMessage(chat_id, "Ujala ho gaya sir", "");
    
      digitalWrite(bulbpin, HIGH); 
      bulbStatus = 1;
    }

      if (text == "Light band kar")
    { bot.sendChatAction(chat_id, "typing");
    delay(100);
    bot.sendMessage(chat_id, "Andhera kayam Rahe", "");
    
      digitalWrite(bulbpin, LOW); // turn the LED on (HIGH is the voltage level)
      bulbStatus = 0;
    }

      if (text == "Dusra Light Laga")
    { bot.sendChatAction(chat_id, "typing");
    delay(100);
    bot.sendMessage(chat_id, "Are Lavto ki", "");
    
      digitalWrite(bulb2pin, HIGH); // turn the LED on (HIGH is the voltage level)
      bulb2Status = 1;
    }

if (text == "Dusra light band kar")
    { bot.sendChatAction(chat_id, "typing");
    delay(100);
    bot.sendMessage(chat_id, "Hogaya bhai", "");
    
      digitalWrite(bulb2pin, LOW); // turn the LED on (HIGH is the voltage level)
      bulb2Status = 0;
    }
    if (text == "Led")
    
      {
    bot.sendChatAction(chat_id, "typing");
    delay(100);
      if (ledStatus)
      {
        bot.sendMessage(chat_id, "Shuru hai Bhai", "");
      }
      else
      {
        bot.sendMessage(chat_id, "Band hai Bhai ", "");
      }
    }
    if (text == "Fan")
    
      {
    bot.sendChatAction(chat_id, "typing");
    delay(100);
      if (fanStatus)
      {
        bot.sendMessage(chat_id, "Shuru hai Bhai", "");
      }
      else
      {
        bot.sendMessage(chat_id, "Band hai Bhai ", "");
      }
    }
    if (text == "Bulb")
    
      {
    bot.sendChatAction(chat_id, "typing");
    delay(100);
      if (bulbStatus)
      {
        bot.sendMessage(chat_id, "Shuru hai Bhai", "");
      }
      else
      {
        bot.sendMessage(chat_id, "Band hai Bhai ", "");
      }
    }
    if (text == "Bulb2")
    
      {
    bot.sendChatAction(chat_id, "typing");
    delay(100);
      if (bulb2Status)
      {
        bot.sendMessage(chat_id, "Shuru hai Bhai", "");
      }
      else
      {
        bot.sendMessage(chat_id, "Band hai Bhai ", "");
      }
    }

    if (text == "Hi")
    {
      {bot.sendChatAction(chat_id, "typing");
    delay(100);
      String welcome = "BOL BHAI " + from_name + ".\n";
     
      bot.sendMessage(chat_id, welcome, "Markdown");
    }
  }

  }

}
void setup()
{
  Serial.begin(115200);
  Serial.println();

  pinMode(ledPin, OUTPUT); 
  pinMode(fanpin,OUTPUT);
  pinMode(bulbpin,OUTPUT);
  pinMode(bulb2pin,OUTPUT);

  delay(10);
  digitalWrite(ledPin,LOW);
  digitalWrite(fanpin,LOW);
  digitalWrite(bulbpin,LOW);
  digitalWrite(bulb2pin,LOW);

  // attempt to connect to Wifi network:
  Serial.print("Connecting to Wifi SSID ");
  Serial.print(WIFI_SSID);
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  secured_client.setCACert(TELEGRAM_CERTIFICATE_ROOT); // Add root certificate for api.telegram.org
  while (WiFi.status() != WL_CONNECTED)
  {
    Serial.print(".");
    delay(500);
  }
  Serial.print("\nWiFi connected. IP address: ");
  Serial.println(WiFi.localIP());

  Serial.print("Retrieving time: ");
  configTime(0, 0, "pool.ntp.org"); // get UTC time via NTP
  time_t now = time(nullptr);
  while (now < 24 * 3600)
  {
    Serial.print(".");
    delay(100);
    now = time(nullptr);
  }
  Serial.println(now);
}

void loop()
{
  if (millis() - bot_lasttime > BOT_MTBS)
  {
    int numNewMessages = bot.getUpdates(bot.last_message_received + 1);

    while (numNewMessages)
    {
      Serial.println("got response");
      handleNewMessages(numNewMessages);
      numNewMessages = bot.getUpdates(bot.last_message_received + 1);
    }

    bot_lasttime = millis();
  }
}