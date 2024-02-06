# MITM Interceptor 🛡️

MITM Interceptor is a Python script designed for conducting Man-In-The-Middle (MITM) attacks on a network. It uses ARP poisoning to intercept network traffic between a target machine and the gateway, allowing for packet manipulation and monitoring.

## Features 🚀

- Conduct MITM attacks to intercept network traffic.
- Redirect packets between a target machine and the gateway.
- Spoof ARP packets to manipulate network traffic.
- Monitor and analyze intercepted packets.
- Easy-to-use command-line interface.

## Prerequisites 🛠️

Before using MITM Interceptor, ensure you have the following prerequisites installed:

- Python 3.x
- scapy
- optparse

## Installation 💻

1. Clone the repository:

```bash
git clone https://github.com/LeatherFire/MITMInterceptor.git
```

2. Navigate to the MITMInterceptor directory:

```bash
cd MITMInterceptor
```

3. Run the script with Python:

```bash
python mitm_interceptor.py -t [TARGET_IP] -g [GATEWAY_IP]
```

Replace `[TARGET_IP]` with the IP address of the target machine and `[GATEWAY_IP]` with the IP address of the gateway.

## Usage 📋

To use MITM Interceptor, follow these steps:

1. Run the script with Python, providing the target and gateway IP addresses as command-line arguments.
2. Wait for the script to set up the MITM attack.
3. Once the attack is running, monitor the intercepted packets for analysis.

## Configuration 🛠️

Before running MITM Interceptor, make sure to configure the following settings in the script:

- `target_ip`: Replace with the IP address of the target machine.
- `gateway_ip`: Replace with the IP address of the gateway.

## Disclaimer ⚠️

MITM Interceptor is designed for educational and testing purposes only. Unauthorized use of this script on networks without permission is illegal and unethical. Use it responsibly and only on networks you own or have explicit permission to test.

## Support 🤝

For any questions, issues, or feedback, please open an issue on GitHub or reach out to the project maintainer.

## License 📜

MITM Interceptor is licensed under the [MIT License](LICENSE).
```
