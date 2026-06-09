#include <WiFi.h>

const char* ssid = "C7-5F-TR";
const char* password = "robot20212021robot";

WiFiServer server(5000);

// ===== モータ設定 =====
const int motorPin = 12;
const int motorChannel = 0;
const int pwmFreq = 2000;
const int pwmResolution = 8;

// ===== データ保存 =====
#define MAX_DATA 800

int times[MAX_DATA];
int speeds[MAX_DATA];
int dataCount = 0;

String buffer = "";

// ===== 再生制御 =====
bool playMode = false;
unsigned long startTime = 0;
int playIndex = 0;

// =========================
// 1行パース処理
// =========================
void parseLine(String line) {

  line.trim();
  if (line.length() == 0) return;

  int comma = line.indexOf(',');

  if (comma < 0) return;

  int t = line.substring(0, comma).toInt();
  int s = line.substring(comma + 1).toInt();

  if (dataCount < MAX_DATA) {
    times[dataCount] = t;
    speeds[dataCount] = constrain(s, 0, 255);
    dataCount++;
  }
}

void setup() {
  Serial.begin(115200);

  // PWM初期化
  ledcSetup(motorChannel, pwmFreq, pwmResolution);
  ledcAttachPin(motorPin, motorChannel);

  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
  }

  server.begin();
  Serial.println("Server started");
}

void loop() {

  WiFiClient client = server.available();

  // =========================
  // ① 受信処理
  // =========================
  if (client) {
    Serial.println("Client connected");

    buffer = "";
    dataCount = 0;
    playMode = false;

    while (client.connected()) {
      while (client.available()) {
        char c = client.read();

        if (c == '\n' || c == '\r') {
		  if (buffer.length() > 0) {
			Serial.println("LINE:");
    		Serial.println(buffer);
		  }
          parseLine(buffer);
          buffer = "";
        } else {
          buffer += c;
        }
      }
    }

    client.stop();
    Serial.println("Client disconnected");

    // 受信完了 → 再生開始準備
    if (dataCount > 0) {
      playMode = true;
      startTime = millis();
      playIndex = 0;
    }
  }

  // =========================
  // ② 再生処理
  // =========================
  if (playMode) {

    unsigned long now = millis() - startTime;

    if (playIndex < dataCount) {

      if (now >= times[playIndex]) {

        int speed = speeds[playIndex];

        ledcWrite(motorChannel, speed);

        Serial.print("t=");
        Serial.print(times[playIndex]);
        Serial.print(" speed=");
        Serial.println(speed);

        playIndex++;
      }

    } else {
      // 再生終了
      ledcWrite(motorChannel, 0);
      playMode = false;
    }
  }
}

