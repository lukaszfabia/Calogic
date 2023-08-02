let menu = document.querySelector('#menu-icon');
let navbar = document.querySelector('.nav-list');

menu.onclick = () => {
    navbar.classList.toggle('open');
};

