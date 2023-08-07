let menu = document.querySelector('#menu-icon');
let navbar = document.querySelector('.nav-list');

menu.onclick = () => {
    navbar.classList.toggle('open');
};


function insert(expression) {
    let input = document.getElementById('user_input');
    if (expression.includes('()') && !input.value.includes(',')) {
        // it works for all functions with ()
        input.value = expression.substring(0, expression.length - 1) + input.value + ')';
    } else if (expression === 'x!') {
        input.value = input.value + '!';
    } else if (expression === '||') {
        input.value = `|${input.value}|`;
    } else if (input.value.includes(',') && !expression.includes('()')) {
        let parts = input.value.split(',');
        input.value = expression.substring(0, expression.length - 4) + parts[0] + ',' + parts[1] + ')';
    } else if (expression.includes('e^')) {
        input.value = expression + input.value;
    } else {
        input.value = expression;
    }

}

function show_content() {
    const tool = document.getElementById('myTooltip');
    const res = document.getElementById('user_input').value;
    tool.innerHTML = 'submitted: ' + res;
}

function clear_content() {
    const inputField = document.getElementById('user_input');
    const clearLabel = document.getElementById('clear');
    let res = inputField.value;
    inputField.value = '';
    clearLabel.innerHTML = 'cleared: ' + res;
}