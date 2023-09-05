document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('correctionForm');
    const correctedSentenceSpan = document.getElementById('correctedSentence');
  
    form.addEventListener('submit', async (event) => {
      event.preventDefault();
  
      const inputSentence = document.getElementById('sentence').value;
  
      try {
        const response = await fetch('/correct', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ sentence: inputSentence }),
        });
  
        const data = await response.json();
        correctedSentenceSpan.textContent = data.correctedSentence;
      } catch (error) {
        console.error('Error:', error);
      }
    });
  });
  