# from transformers import AutoTokenizer, pipeline
from flask import render_template, jsonify, request
from app import app
from config import GOOGLE_API_KEY
from app.models import songs
import random
import requests
import google.generativeai as genai

# from transformers import AutoTokenizer, AutoModelForCausalLM, AutoModelForMaskedLM
# import torch

genai.configure(api_key=GOOGLE_API_KEY)

from flask import render_template, jsonify, request
from app import app
from app.models import songs
import random
import google.generativeai as genai

# Configure Gemini API
GOOGLE_API_KEY = "AIzaSyDNJxHXySaFYDHDG8uQBZ9nHqnUZlwBjrk"
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-1.5-pro-latest')

@app.route('/api/generate-lyrics', methods=['GET'])
def generate_lyrics():
    try:
        # Select a random song from our list
        selected_song = random.choice(songs)
        song_title = selected_song['title']
        artist = selected_song['artist']

        # Prompt for the LLM
        prompt = f"""Generate a short, recognizable lyric snippet (2-4 lines) from the song "{song_title}" by {artist}."""
        print (prompt)

        # Generate the lyrics using Gemini
        response = model.generate_content(prompt)
        print(response)
        # Extract the lyric snippet from the response
        lyric_snippet = response.text.strip()
        print(lyric_snippet)

        return jsonify({
            'status': 'success',
            'lyric_snippet': lyric_snippet,
            'song_title': song_title,
            'artist': artist
        })

    except Exception as e:
        app.logger.error(f"Error in generate_lyrics: {str(e)}")
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/check-answer', methods=['POST'])
def check_answer():
    data = request.json
    user_guess = data.get('user_guess', '').strip().lower()
    correct_title = data.get('correct_title', '').lower()
    artist = data.get('artist', '')
    
    # Simple string matching (could be improved with fuzzy matching)
    is_correct = user_guess == correct_title
    
    return jsonify({
        'status': 'success',
        'is_correct': is_correct,
        'correct_title': correct_title,
        'artist': artist
    })
