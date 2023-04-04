window.onload = () => {
    const audio = document.getElementById('audio');
    const playButton = document.getElementById('play-button');
    const pauseButton = document.getElementById('pause-button');
    const prevButton = document.getElementById('prev-button');
    const nextButton = document.getElementById('next-button');
    const time = document.getElementById('time');

    const popup = document.querySelector('.full-screen');

    function updateTime() {
        var totalSeconds = Math.floor(audio.duration - audio.currentTime);
        var minutes = Math.floor(totalSeconds / 60);
        var seconds = totalSeconds % 60;
        time.innerHTML = minutes.toString().padStart(2, "0") + ":" + seconds.toString().padStart(2, "0");
      }
    
      
    setInterval(updateTime, 1000);

  
    playButton.addEventListener('click', () => {
      audio.play();
      playButton.style.display = 'none';
      pauseButton.style.display = 'inline-block';
    });
  
    pauseButton.addEventListener('click', () => {
      audio.pause();
      playButton.style.display = 'inline-block';
      pauseButton.style.display = 'none';
    });
  
    audio.addEventListener('play', () => {
      playButton.style.display = 'none';
      pauseButton.style.display = 'inline-block';
    });
  
    audio.addEventListener('pause', () => {
      playButton.style.display = 'inline-block';
      pauseButton.style.display = 'none';
    });
  
    audio.addEventListener('ended', () => {
      playButton.style.display = 'inline-block';
      pauseButton.style.display = 'none';
    });

        // Add click event listeners to the prev/next buttons
    prevButton.addEventListener('click', () => {
        // TODO: Load the previous song and update the song title
    });
    nextButton.addEventListener('click', () => {
        // TODO: Load the next song and update the song title
    });


    
};






