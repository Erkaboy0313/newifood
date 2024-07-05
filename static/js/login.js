document.addEventListener('mousemove', (e) => {
    const background = document.getElementById('background');
    const formContainer = document.getElementById('form-container');

    const moveFactor = 20;
    const xOffset = (window.innerWidth / 2 - e.pageX) / moveFactor;
    const yOffset = (window.innerHeight / 2 - e.pageY) / moveFactor;

    background.style.transform = `translate(${xOffset}px, ${yOffset}px)`;
    formContainer.style.transform = `translate(${xOffset / 2}px, ${yOffset / 2}px)`;
});
