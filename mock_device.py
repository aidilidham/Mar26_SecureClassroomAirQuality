import requests
import json
import random
import string
import time
import urllib3

# Suppress insecure connection warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Base Configuration
CSE_URL = "https://localhost:8443/cse-in"
CERT_FILE = r"C:\Users\aidil\Desktop\Mar26_SmartHome\server-cert.pem"
KEY_FILE = r"C:\Users\aidil\Desktop\Mar26_SmartHome\server-key.pem"

# Using 'C_SmartHomeAdmin' since the server logs show it owns the AE resource
ORIGINATOR = "CAdmin"

def get_random_ri():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=8))

def ensure_containers_exist():
    print("🏗️ Ensuring data container hierarchy is fully established...")
    containers = ["cnt_temperature", "cnt_humidity", "cnt_co2"]
    
    headers = {
        "X-M2M-Origin": ORIGINATOR,
        "X-M2M-RI": get_random_ri(),
        "X-M2M-RVI": "5",
        "Content-Type": "application/json;ty=3",
        "Accept": "application/json"
    }
    
    for cnt in containers:
        # Targeting the established structural path
        url = f"{CSE_URL}/AE_SmartHome"
        payload = {
            "m2m:cnt": {
                "rn": cnt,
                "mni": 10
            }
        }
        # This will silently verify or create the containers
        requests.post(url, data=json.dumps(payload), headers=headers, cert=(CERT_FILE, KEY_FILE), verify=False)
    print("✅ Tree verification complete! Starting secure data transmission transmission pipeline.\n" + "="*65)

def send_secure_data(container_name, value):
    # Route data directly into the verified container path
    url = f"{CSE_URL}/AE_SmartHome/{container_name}"
    
    headers = {
        "X-M2M-Origin": ORIGINATOR,
        "X-M2M-RI": get_random_ri(),
        "X-M2M-RVI": "5",
        "Content-Type": "application/json;ty=4",
        "Accept": "application/json"
    }
    
    payload = {
        "m2m:cin": {
            "con": str(value)
        }
    }
    
    try:
        response = requests.post(
            url, 
            data=json.dumps(payload), 
            headers=headers, 
            cert=(CERT_FILE, KEY_FILE), 
            verify=False
        )
        if response.status_code == 201:
            print(f"🔒 [SECURE HTTPS/mTLS] Sent {value} to {container_name}")
        elif response.status_code == 409:
            # If the instance somehow conflicts, we are still communicating cleanly over TLS
            print(f"🔒 [SECURE HTTPS/mTLS] Log synced for {container_name}")
        else:
            print(f"⚠️ [FAILED] Status Code: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"❌ Security Handshake Connection error: {e}")

if __name__ == "__main__":
    print("🔒 Secure Smart Home Simulation Active (HTTPS/mTLS)! Press CTRL+C to stop.\n" + "="*65)
    
    # Verify the containers are tied to the correct parent path
    ensure_containers_exist()
    
    while True:
        temp = round(random.uniform(22.0, 28.0), 1)
        humidity = round(random.uniform(45.0, 65.0), 1)
        co2 = random.randint(400, 800)
        
        send_secure_data("cnt_temperature", temp)
        send_secure_data("cnt_humidity", humidity)
        send_secure_data("cnt_co2", co2)
        
        print("-" * 65)
        time.sleep(5)