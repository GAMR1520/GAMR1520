menuToggler.addEventListener('click', ev => {
    menu.classList.toggle('open');
    ev.stopPropagation();
});

window.addEventListener('click', ev => {
    menu.classList.remove('open');
});