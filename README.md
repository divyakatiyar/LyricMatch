**Coding Challenge: "Lyric Match" \- AI-Powered Song Guessing Game**

**Problem Statement:**

Build a web application called "Lyric Match" that challenges users to guess the title of an English song based on a short snippet of its lyrics, provided by an AI.

**Functionality Requirements:**

1. **User Interface (VueJS):**  
   * A clean and user-friendly interface.  
   * A "Generate Lyric Snippet" button.  
   * A display area to show the AI-generated lyric snippet.  
   * An input field for the user to enter their song title guess.  
   * A "Check Answer" button.  
   * A display area to show whether the guess is correct or incorrect, and the actual song title if incorrect.  
2. **Backend (Python):**  
   * An API endpoint that triggers the AI to generate a short lyric snippet from a random English song.  
   * An API endpoint that receives the user's guess and the correct song title, and checks if they match.  
   * Integration with a chosen LLM (e.g., OpenAI's GPT models, Google's Gemini, or a suitable open-source alternative).  
   * The backend should store a list of song titles that the LLM will use to generate lyrics.  
   * Return the Lyric Snippet, and the answer result to the frontend in JSON format.  
3. **LLM Integration:**  
   * The LLM should be used to generate a short, recognizable lyric snippet (2-4 lines) from a randomly selected song title from the list.  
   * The LLM should be prompted to avoid giving away the song title directly and focus on generating evocative lyrics.  
   * The LLM should be prompted with a clear list of songs that it can use to generate the lyrics.

**Set up and running the app:**  
   * Run requirements.txt file to install all dependencies.  
   * In the command prompt, use the command, python run.py    

