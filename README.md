# IIB20804 IoT Application Security Mini Project (Semester Mar 2026)
## Project Name: Mar26_YourGroupNameHere

### 🏢 Course Details & Team Members
* **Course Code:** IIB20804 IoT Application Security
* **Institution:** UniKL MIIT
* **Lecturer Target Account:** `shahrul322` / shahrulniza@unikl.edu.my

### 🚀 Project Overview: Securing Smart Home Applications
This project demonstrates the complete implementation of a hardened, secure smart home telemetry system built using an open-source **oneM2M platform (ACME CSE)**. The architecture mitigates standard sniffing, tampering, and identity spoofing vulnerabilities by shifting away from insecure default parameters to a hardened perimeter defense.

### 🛡️ Security Features Implemented
1. **Transport Layer Security (TLSv1.3):** Closed default plaintext port `8080`. All communication is locked down to secure port `8443`.
2. **Mutual Authentication (mTLS):** The server actively validates the identity of the Application Entity (AE) using X.509 cryptographic certificates before allowing access to the data tree.
3. **Encrypted Payloads:** Telemetry streams (Temperature, Humidity, CO2) are fully obscured from network sniffers. 

### 🔧 Execution Instructions

#### 1. Start the Secure ACME CSE Server
Navigate to the root directory and initialize the server stack using the manual runtime security overrides:
```cmd
py -m acmecse --http-port 8443 --https