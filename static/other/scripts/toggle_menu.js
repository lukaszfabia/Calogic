let menu = document.querySelector('#menu-icon');
let navbar = document.querySelector('.nav-list');

menu.onclick = () => {
    navbar.classList.toggle('open');
};

function copyToClipboard() {
    const copyText = document.getElementById("output_result");
    copyText.select();
    copyText.setSelectionRange(0, 99999);
    navigator.clipboard.writeText(copyText.value);

    const tooltip = document.getElementById("myTooltip");
    tooltip.innerHTML = "Copied: " + copyText.value;
}

function mouse_out_func_to_copy() {
    const tooltip = document.getElementById("myTooltip");
    tooltip.innerHTML = "Copy to clipboard";
}

function insert(expression) {
    let input = document.getElementById('user_input');
    input.value = expression;
}