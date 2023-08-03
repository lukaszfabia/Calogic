let menu = document.querySelector('#menu-icon');
let navbar = document.querySelector('.nav-list');

menu.onclick = () => {
    navbar.classList.toggle('open');
};

function copyToClipboard() {
    const outputElement = document.getElementById("output_result");
    outputElement.select();
    document.execCommand("copy");
}