# What's the Weather?

A simple weather web application built with **Python** and **Flask**. It uses the **OpenWeatherMap API** to retrieve the current weather for a city and renders the result in an HTML page.

## Features

- Look up the current weather by city name.
- Retrieve weather information from OpenWeatherMap.
- Render pages with Flask and Jinja templates.
- Display a dedicated page when a city cannot be found.
- Keep page styling in a separate CSS file.

## Tech stack

- **Python** — application logic
- **Flask** — web framework and routing
- **Jinja2** — HTML templating (included with Flask)
- **Requests** — HTTP requests to the OpenWeatherMap API
- **python-dotenv** — loading environment variables from a `.env` file
- **OpenWeatherMap API** — current weather data
- **Waitress** — production-ready WSGI server

## Project structure

```text
.
├── main.py                 # Creates the Flask application and defines routes
├── weather.py              # Fetches current weather from OpenWeatherMap
├── requirements.txt        # Python dependencies
├── .env                    # Local API-key configuration (create this file)
├── static/
│   └── style.css           # Application styles
└── templates/
    ├── index.html          # Main page / city search form
    ├── weather.html        # Weather results page
    └── city-not-found.html # Page shown when a city is not found
```

## Getting started

### 1. Clone the repository

```bash
git clone https://github.com/cindercrest/what-s-Waether-.git
cd what-s-Waether-
```

### 2. Create and activate a virtual environment

**Linux / macOS**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows (PowerShell)**

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure the OpenWeatherMap API key

The application needs an API key to request weather data. Create an account at [OpenWeatherMap](https://openweathermap.org/) and obtain an API key.

Create a `.env` file in the project root:

```env
OPENWEATHER_API_KEY=your_api_key_here
```

Make sure the variable name matches the one read by `weather.py`. If the code uses a different name, use that name in `.env` instead. Keep the key private and do not commit `.env` to Git.

### 5. Run the application

```bash
python main.py
```

Open the local address printed by Flask in your browser (commonly `http://127.0.0.1:5000/`). The exact host and port depend on the configuration in `main.py`.

## How it works

1. The browser loads the main page rendered from `templates/index.html`.
2. The user submits a city name through the page's search form.
3. A Flask route in `main.py` handles the request and uses the weather functionality in `weather.py`.
4. `weather.py` sends a request to OpenWeatherMap and obtains the current weather data.
5. Flask renders `templates/weather.html` with the returned data. When the city cannot be found, the application can render `templates/city-not-found.html`.
6. The pages use `static/style.css` for styling.

## Dependencies

The project dependencies are pinned in `requirements.txt`:

```text
blinker==1.9.0
certifi==2026.10.23
charset-normalizer==3.5.2
click==8.5.1
Flask==3.1.3
idna==3.20
itsdangerous==2.2.0
Jinja2==3.1.6
MarkupSafe==3.0.4
python-dotenv==1.2.4
requests==2.34.2
urllib3==2.8.0
waitress==3.0.2
Werkzeug==3.1.9
```

## Running with Waitress

For a deployment environment, use a production WSGI server rather than Flask's built-in development server. If the Flask application object in `main.py` is named `app`, you can start it with:

```bash
waitress-serve --host 0.0.0.0 --port 8000 main:app
```

Then access the application on port `8000` of the machine running it. Adjust `main:app` if your module name or Flask application variable is different. Configure your hosting environment's API-key variable securely; do not expose the key in source code or commit it to version control.

## Troubleshooting

- **API key error:** Check that the key is valid, that it is available to the running process, and that the variable name matches the one used in `weather.py`.
- **City not found:** Check the spelling of the city name. The application may show its city-not-found page when the API cannot resolve the requested city.
- **Request or network error:** Check your internet connection and verify that the OpenWeatherMap service is reachable.
- **Module not found:** Activate the virtual environment and run `python -m pip install -r requirements.txt` again.

## API reference

Weather data is provided by [OpenWeatherMap](https://openweathermap.org/api). Refer to its documentation for API usage, available fields, and request limits.

## License

No license information was provided for this repository. Unless a `LICENSE` file is added, permission to reuse, modify, or distribute this project should not be assumed.
