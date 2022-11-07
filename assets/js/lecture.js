const slides = document.querySelectorAll("section.slide");
let currentSlide = 0;

showSlide();

function showSlide(direction='right') {
    console.log("showing slide", currentSlide, direction);
    const previous = document.querySelector("section.slide.previous");
    if(previous) {
        previous.classList.remove('previous');
        previous.classList.remove('left');
        previous.classList.remove('right');
    }
    const current = document.querySelector("section.slide.current");
    if(current) {
        current.classList.replace('current', 'previous');
        current.classList.remove('left');
        current.classList.remove('right');
        current.classList.add(direction);
    }
    slides[currentSlide].classList.add('current');
    slides[currentSlide].classList.remove('previous');
    slides[currentSlide].classList.add(direction);
}

function nextSlide(direction) {
    currentSlide++;
    currentSlide %= slides.length;
    showSlide(direction);
}
function previousSlide(direction) {
    currentSlide--;
    currentSlide += slides.length;
    currentSlide %= slides.length;
    showSlide(direction);
}

document.addEventListener('keydown', ev => {
    switch(ev.key) {
        case "ArrowLeft":
            previousSlide('left');
            break;
        case "ArrowRight":
            nextSlide('right');
            break;
        }
})