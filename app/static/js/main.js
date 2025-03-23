const { createApp, ref, computed } = Vue;

createApp({
  setup() {
    const loading = ref(false);
    const lyricSnippet = ref('');
    const correctTitle = ref('');
    const artist = ref('');
    const userGuess = ref('');
    const showAnswer = ref(false);
    const isCorrect = ref(false);

    const formattedLyrics = computed(() => {
      if (!lyricSnippet.value) return [];
      return lyricSnippet.value
        .split('\n')
        .filter(line => line.trim() !== '');
    });

    async function generateLyrics() {
      loading.value = true;
      resetGame();
      
      try {
        const response = await fetch('/api/generate-lyrics');
        const data = await response.json();
        
        if (data.status === 'success') {
          lyricSnippet.value = data.lyric_snippet;
          correctTitle.value = data.song_title;
          artist.value = data.artist;
        } else {
          alert('Error generating lyrics. Please try again.');
        }
      } catch (error) {
        console.error('Error:', error);
        alert('Error connecting to the server. Please try again later.');
      } finally {
        loading.value = false;
      }
    }
    
    async function checkAnswer() {
      if (!userGuess.value) return;
      
      try {
        const response = await fetch('/api/check-answer', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            user_guess: userGuess.value,
            correct_title: correctTitle.value,
            artist: artist.value
          }),
        });
        
        const data = await response.json();
        
        if (data.status === 'success') {
          isCorrect.value = data.is_correct;
          showAnswer.value = true;
        }
      } catch (error) {
        console.error('Error:', error);
        alert('Error checking answer. Please try again.');
      }
    }
    
    function resetGame() {
      userGuess.value = '';
      showAnswer.value = false;
      isCorrect.value = false;
    }

    return {
      loading,
      lyricSnippet,
      correctTitle,
      artist,
      userGuess,
      showAnswer,
      isCorrect,
      formattedLyrics,
      generateLyrics,
      checkAnswer,
      resetGame
    };
  }
}).mount('#app');
