# Discover Balochistan
### AI-Powered Smart Tourism Platform

Discover Balochistan is a smart tourism platform designed to help people explore the natural beauty, cultural heritage and tourist destinations of Balochistan, Pakistan.

The platform provides tourism information, AI-assisted conversations, personalized destination recommendations and travel itinerary planning through a responsive web interface.

## Project Features

- **Tourism Destinations:** Explore popular destinations across Balochistan, including Hingol National Park, Kund Malir Beach, Ziarat, Hanna Lake, Gwadar and Moola Chotok.
- **Bilingual Interface:** Switch between English and Roman Urdu.
- **AI Tourism Assistant:** Ask tourism-related questions. English responses use a local Ollama model, while Roman Urdu responses use a tourism knowledge base.
- **Personalized Recommendations:** Discover destinations based on selected interests such as nature, history, beaches, mountains and adventure.
- **Smart Trip Planner:** Generate sample travel itineraries based on destination, duration and interests.
- **Progressive Web App (PWA):** Includes a web app manifest, service worker and caching for supported offline resources.
- **Android Application:** An Android WebView application provides access to the responsive website.

## Technologies Used

| Component | Technology |
|---|---|
| Backend | Python, Flask |
| Frontend | HTML, CSS, JavaScript |
| AI Model | Ollama, Qwen 2.5 (1.5B) |
| Tourism Data | Python |
| PWA | Web App Manifest, Service Worker |
| Android | Kotlin, Android WebView |
| Development Tools | VS Code, Android Studio |

## Project Structure

```text
discover_balochistan/
│
├── app.py
├── data.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── templates/
│   └── index.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── app.js
│   ├── images/
│   ├── icons/
│   ├── data/
│   ├── manifest.json
│   └── sw.js
│
└── Other supporting files
```

## Requirements

- Python 3.10 or later
- pip
- VS Code (recommended)
- Ollama for the local English AI chatbot
- Qwen 2.5 (1.5B) model installed in Ollama

## Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd discover_balochistan
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Install and run Ollama

Install Ollama and download the required model:

```bash
ollama pull qwen2.5:1.5b
```

Make sure Ollama is running before using the English AI chatbot.

### 6. Run the Flask application

```bash
python app.py
```

Open the application in your browser:

http://127.0.0.1:5000

## API Endpoints

| Endpoint | Method | Purpose |
|---|---|---|
| `/` | GET | Main tourism homepage |
| `/api/destinations` | GET | Retrieve destination information |
| `/api/chat` | POST | Tourism chatbot |
| `/api/recommend` | POST | Personalized recommendations |
| `/api/itinerary` | POST | Generate travel itinerary |
| `/sw.js` | GET | Service worker |

## Offline Support

The PWA includes caching for selected website resources, including the homepage, stylesheets, JavaScript, icons and destination images.

**Note:** Dynamic features such as chatbot responses, recommendations and itinerary generation require the Flask backend. The English chatbot also requires the Ollama service.

## Important Limitations

- Destination information and travel itineraries should be verified before making actual travel decisions.
- Images and destination descriptions should be checked for accuracy and usage rights.
- The local Ollama chatbot requires a running local model.
- The current Android application uses a WebView connected to the development server.
- Public deployment requires a cloud-hosted backend and an accessible AI service.
- Live hotel availability, bookings and verified travel services are not currently provided.

## Future Improvements

- Public cloud deployment and custom domain.
- Cloud-based AI integration.
- Verified tourism information and destination database.
- Interactive maps and destination coordinates.
- Hotel and local guide information.
- Administrative dashboard and database integration.
- Improved offline functionality.
- Public Android application release.

## Project Purpose

Discover Balochistan aims to promote tourism, improve access to regional tourism information and demonstrate how artificial intelligence and modern web technologies can support digital tourism development in Balochistan.

---

**Discover Balochistan — Explore More. Discover Balochistan.**