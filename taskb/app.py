from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

app = Flask(__name__)

# Read Gemini API key from .env
API_KEY = os.getenv("GEMINI_API_KEY")

# Gemini API endpoint
URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"


# Home route
# This is useful so browser does not show 404 at '/'
@app.route('/')
def home():
    return jsonify({
        "message": "Gemini API Flask App is running"
    })


# Generate route
@app.route('/generate', methods=['POST'])
def generate():

    # Get JSON data from request body
    data = request.get_json()

    # Check if request body is valid JSON
    if data is None:
        return jsonify({
            "error": "Request body must be valid JSON"
        }), 400

    # Read prompt from request JSON
    prompt = data.get("prompt")

    # Optional debug flag
    # If true, raw Gemini response will also be returned
    debug = data.get("debug", False)

    # Check if prompt is missing or empty
    if prompt is None or prompt.strip() == "":
        return jsonify({
            "error": "Prompt is required"
        }), 400

    # Check if API key is available
    if API_KEY is None or API_KEY.strip() == "":
        return jsonify({
            "error": "GEMINI_API_KEY not found in .env file"
        }), 500

    # Prepare Gemini request payload
    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "text": prompt
                    }
                ]
            }
        ]
    }

    try:
        # Send POST request to Gemini API
        response = requests.post(
            URL,
            params={"key": API_KEY},
            json=payload,
            timeout=30
        )

        # Convert Gemini response to JSON
        result = response.json()

    except requests.exceptions.Timeout:
        return jsonify({
            "error": "Request to Gemini API timed out"
        }), 500

    except requests.exceptions.ConnectionError:
        return jsonify({
            "error": "Could not connect to Gemini API"
        }), 500

    except Exception as e:
        return jsonify({
            "error": "Unexpected error while calling Gemini API",
            "details": str(e)
        }), 500

    # If Gemini API returns error response
    if response.status_code != 200:
        return jsonify({
            "error": "Failed to get response from Gemini API",
            "status_code": response.status_code,
            "details": result
        }), response.status_code

    # Variable to store extracted Gemini response text
    generated_text = ""

    # Extract generated response safely
    if "candidates" in result:

        candidates = result["candidates"]

        if len(candidates) > 0:

            content = candidates[0].get("content", {})

            parts = content.get("parts", [])

            if len(parts) > 0:
                generated_text = parts[0].get("text", "")

    # If Gemini returns no text
    if generated_text.strip() == "":
        return jsonify({
            "error": "Gemini returned an empty response"
        }), 500

    # Final response object
    output = {
        "prompt": prompt,
        "response": generated_text
    }

    # Include raw Gemini payload only if debug=True
    if debug:
        output["raw_response"] = result

    return jsonify(output)


# Run Flask app
if __name__ == '__main__':
    app.run(debug=True)