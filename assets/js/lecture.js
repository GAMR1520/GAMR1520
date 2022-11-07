let queryParams = new URLSearchParams(window.location.search);
let currentSlide = queryParams.has('slide') ? queryParams.get('slide') : 0;

async function convertSlides() {
    while(document.querySelector('hr:last-of-type')) {
        const rule = document.querySelector('hr:last-of-type');
        const slide = document.createElement('section');
        slide.classList.add('slide');
        const content = document.querySelectorAll('hr:last-of-type ~ *:not(section.slide)');
        console.log(content[0]);
        rule.after(slide);
        slide.append(...content);
        rule.remove();
    }
}


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
	queryParams.set('slide', currentSlide);
	window.history.replaceState({}, "", `${window.location.origin}${window.location.pathname}?${queryParams.toString()}`);
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

convertSlides();
let slides = document.querySelectorAll('section.slide');
showSlide();
