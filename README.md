# LLM Recipe Generator App

## Description
This application uses an LLM to generate a recipe based on the ingredients listed by the user. 
The response includes the list of ingredients, instructions, estimated cooking time and difficulty level.
The goal of the app is to demonstrate a simple single-turn LLM interaction where one prompt produces one complete response.

## Architecture overview
React (Frontend) → FastAPI (Backend) → Gemini API (LLM)

## Technical choices

### Frontend
#### React 
Chosen for simplicity and familiarity. Handles user input and displays the response.
### Backend
#### FastAPI
Lightweight and easy to set up. Good for building simple APIs quickly.
### LLM
#### Gemini API
Suitable free tier for single-turn applications.
### Other libraries
#### requests
Used to send HTTP requests to the LLM API
#### python-dotenv
Used for managing environment variables securely.
#### uvicorn
ASGI server for running FastAPI

## Setup
### Clone the repository
#### git clone <repo-url>
#### cd capstone
### Backend
#### cd server
#### pip install -r requirements.txt
#### Create a `.env` file:
#### GEMINI_API_KEY=your_api_key

### Run:
#### uvicorn main:app --reload

### Frontend
#### cd client
#### npm install
#### npm start

## Usage
1. Open http://localhost:3000
2. Enter your ingredients
3. Click "Generate"
4. View the generated recipe

## Known limitations
The app relies entirely on the LLM, so the generated ingredients/instructions might be unrealistic or even dangerous.
No error handling for malformed API responses besides basic try/catch.
No rate limiting or security measures, CORS is fully open (These would need to change for production use).
No persistence.
No unit tests. 
Simple UI.

## AI Tools Used
- ChatGPT
Helped with boilerplate code for backend and frontend.
Helped in coming up with known limitations.

