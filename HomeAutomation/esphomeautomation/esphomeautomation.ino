#include <WiFi.h>
#include <WiFiClientSecure.h>
#include <UniversalTelegramBot.h>


#define WIFI_SSID         "Airtel_Arankalle"    
#define WIFI_PASS         "air90299"

#define BOT_TOKEN "6657941764:AAH4hdWx6kN2TVbZdTrwXyGrxPUmqjfhBGw"

const unsigned long BOT_MT = 1000; // mean time 

WiFiClientSecure secured_client;

UniversalTelegramBot bot(BOT_TOKEN, secured_client);
unsigned long bot_lasttime; // last time messages

const int fanPin = 15; // D23
const int bulbPin = 4; // D22

int fanStatus = 0;
int bulbStatus = 0;

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
      from_name = "User";

    if (text == "Switch on the fan")
    {
      bot.sendChatAction(chat_id, "typing");
      delay(100);
      bot.sendMessage(chat_id, "Turning on the fan", "");
      digitalWrite(fanPin, HIGH);
      fanStatus = 1;
    }

    if (text == "Turn off the fan")
    {
      bot.sendChatAction(chat_id, "typing");
      delay(100);
      bot.sendMessage(chat_id, "Turning off the fan", "");
      digitalWrite(fanPin, LOW);
      fanStatus = 0;
    }

    if (text == "Switch on the bulb")
    {
      bot.sendChatAction(chat_id, "typing");
      delay(100);
      bot.sendMessage(chat_id, "Turning on the bulb", "");
      digitalWrite(bulbPin, HIGH);
      bulbStatus = 1;
    }

    if (text == "Turn off the bulb")
    {
      bot.sendChatAction(chat_id, "typing");
      delay(100);
      bot.sendMessage(chat_id, "Turning off the bulb", "");
      digitalWrite(bulbPin, LOW);
      bulbStatus = 0;
    }

    if (text == "Status")
    {
      bot.sendChatAction(chat_id, "typing");
      delay(100);
      bot.sendMessage(chat_id, "The fan is " + String(fanStatus == 1 ? "on" : "off") + "\nThe bulb is " + String(bulbStatus == 1 ? "on" : "off"), "");
    }


  }
}
void setup()
{
  Serial.begin(115200);
  Serial.println();

  // Customized welcome message
  Serial.println("Initializing Smart Home Bot...");

  pinMode(fanPin, OUTPUT);
  pinMode(bulbPin, OUTPUT);

  delay(10);

  digitalWrite(fanPin, LOW);
  digitalWrite(bulbPin, LOW);

  Serial.print("Connecting to WiFi SSID ");
  Serial.print(WIFI_SSID);

  // Connect to WiFi
  WiFi.begin(WIFI_SSID, WIFI_PASS);
  secured_client.setCACert(TELEGRAM_CERTIFICATE_ROOT);

  // Customized connection animation
  while (WiFi.status() != WL_CONNECTED)
  {
    Serial.print(".");
    delay(500);
  }
  Serial.print("\nWiFi connected. IP address: ");
  Serial.println(WiFi.localIP());

  // Customized time retrieval message
  Serial.print("Fetching current time...");

  // Fetch current time from NTP server
  configTime(0, 0, "pool.ntp.org");
  time_t now = time(nullptr);
  while (now < 24 * 3600)
  {
    Serial.print(".");
    delay(100);
    now = time(nullptr);
  }
  Serial.println(now);

  // Customized setup complete message
  Serial.println("Setup complete. Smart Home Bot is ready.");
}

void loop()
{
  // Customized bot update check message
  Serial.println("Checking for new messages...");

  if (millis() - bot_lasttime > BOT_MT)
  {
    int numNewMessages = bot.getUpdates(bot.last_message_received + 1);

    while (numNewMessages)
    {
      Serial.println("New messages received. Processing...");

      // Handle new messages
      handleNewMessages(numNewMessages);
      numNewMessages = bot.getUpdates(bot.last_message_received + 1);
    }

    bot_lasttime = millis();
  }
}
