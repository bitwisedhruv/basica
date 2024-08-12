
function updateLineNumbers() {
    const codeInput = document.getElementById('input');
    const lineNumbers = document.getElementById('lineNumbers');
    const lines = codeInput.value.split('\n').length;
    lineNumbers.innerHTML = '';
    for (let i = 1; i <= lines; i++) {
        const div = document.createElement('div');
        div.textContent = i;
        div.style.backgroundColor="rgb(83, 83, 83)";
        lineNumbers.appendChild(div);
    }
}

function syncScroll() {
    const codeInput = document.getElementById('input');
    const lineNumbers = document.getElementById('lineNumbers');
    lineNumbers.scrollTop = codeInput.scrollTop;
}


document.addEventListener('DOMContentLoaded', () => {
    const codeInput = document.getElementById('input');
    codeInput.addEventListener('input', updateLineNumbers); 
    codeInput.addEventListener('scroll', syncScroll); 
});


const runButton = document.querySelector('.run-button');
const outputScreen = document.querySelector('.output');
runButton.addEventListener('click', () => {
  outputScreen.style.display = 'block';
});


const clearButton = document.querySelector('.clear-button');
const textarea=document.querySelector("#input");
clearButton.addEventListener('click', () => {
  outputScreen.style.display = 'none';
  textarea.value='';
  updateLineNumbers();
});