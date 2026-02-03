let inputs = document.querySelectorAll('input');
window.onload = () =>{
    let inputDate;
    for(let i=1; i<inputs.length; i++){
        let label = inputs[i].nextElementSibling;
        if(inputs[i].type != 'date'){
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
        }else{
            label.classList.add('label-ativo');
        }
    }
}
