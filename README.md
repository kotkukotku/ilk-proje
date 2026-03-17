# PyScanner: Multithreaded Network Port Scanner

A high-performance port scanner developed in Python to understand the fundamentals of socket programming, multithreading, and network reconnaissance.

## 🌟 Key Features
* **Fast Scanning:** Implements `ThreadPoolExecutor` for efficient multithreaded performance.
* **Service Identification:** Built-in dictionary to resolve common port services.
* **Banner Grabbing:** Captures service banners to identify software versions.
* **Thread-Safe Logging:** Uses `threading.Lock` to ensure clean console output and prevent race abandoned data.
* **Reporting:** Automatically exports scan results to a `.txt` file for further analysis.
* **Customizable:** User-defined timeouts and target IP ranges.

## 🛠️ Installation & Setup

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/kotkukotku/ilk-proje.git](https://github.com/kotkukotku/ilk-proje.git)
   cd ilk-proje

2. **Run the Scanner:**
   ```
   python hworld.py

## 📈 Roadmap / Version History

- **v1.0:** Basic socket connection and IP scanning.

- **v1.5:** Added manual threading and sequential listing.

- **v2.0 (Latest):** Transitioned to ThreadPoolExecutor for better resource management.

- Implemented Banner Grabbing & Service Detection.

- Added file logging and execution time measurement.

## ⚖️ Legal Disclaimer
This tool is strictly for educational purposes and authorized security testing. The developer is not responsible for any misuse or damage caused by this tool. Always obtain permission before scanning any network.

## 🤝 Contact & Contributions

Feel free to open an issue or submit a pull request if you have suggestions for improvement.