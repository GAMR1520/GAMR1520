let queryParams = new URLSearchParams(window.location.search);
let currentSlide = queryParams.has('slide') ? parseInt(queryParams.get('slide')) - 1 : 0;

async function convertSlides() {
    while(document.querySelector('hr:last-of-type')) {
        const rule = document.querySelector('hr:last-of-type');
        const slide = document.createElement('section');
        const wrapper = document.createElement('div');
        slide.classList.add('slide');
        const content = document.querySelectorAll('hr:last-of-type ~ *:not(section.slide)');
        rule.after(slide);
        wrapper.append(...content);
        slide.append(wrapper);
        rule.remove();
    }
    document.querySelector('#slideCount').textContent = document.querySelectorAll('.slide').length;
}

function showSlide(direction='right') {
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
    document.querySelector('#slideNumber').textContent = (currentSlide + 1).toString().padStart(2, '0');
	queryParams.set('slide', currentSlide + 1);
	window.history.replaceState({}, "", `${window.location.origin}${window.location.pathname}?${queryParams.toString()}`);
}

function nextSlide() {
    currentSlide++;
    currentSlide %= slides.length;
    showSlide('right');
}
function previousSlide() {
    currentSlide--;
    currentSlide += slides.length;
    currentSlide %= slides.length;
    showSlide('left');
}

document.addEventListener('keydown', ev => {
    switch(ev.key) {
        case "ArrowLeft":
            previousSlide();
            break;
        case "ArrowRight":
            nextSlide();
            break;
        }
});

document.querySelector("#previousSlide").addEventListener('click', ev => {
    previousSlide();
});
document.querySelector("#nextSlide").addEventListener('click', ev => {
    nextSlide();
});

let touchX;
document.addEventListener('touchstart', ev => {
	touchX = ev.touches[0].clientX;
});
document.addEventListener('touchmove', ev => {
	if(touchX) {
		let moveX = touchX - ev.touches[0].clientX;
		if (moveX < -50) {
			previousSlide();
			touchX = null;
		}	else if (moveX > 50) {
			nextSlide();
			touchX = null;
		}
	}
});

convertSlides();
let slides = document.querySelectorAll('section.slide');
showSlide();
