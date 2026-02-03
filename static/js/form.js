let inputs = document.querySelectorAll('input');
console.log(inputs)
window.onload = () =>{
    for(let i=1; i<inputs.length; i++){
        let label = inputs[i].nextElementSibling;
        console.log(label)
        if(inputs[i].value.trim().length > 0){
            label.classList.add('label-ativo');
        }

        inputs[i].addEventListener('focus', () => {
            label.classList.add('label-ativo');
        })

        inputs[i].addEventListener('blur', () => {
            if(inputs[i].value.trim().length === 0){
                let label = inputs[i].nextElementSibling;
                label.classList.remove('label-ativo');
            }
        })
    }
}
