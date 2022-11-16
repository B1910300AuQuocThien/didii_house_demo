function click_and_cancel(el_1, el_2, el_3){
    const btn_edit = document.getElementById(el_1)
    const btn_cancel = document.getElementById(el_2)
    btn_edit.parentElement.addEventListener('click', function(){
        document.getElementsByClassName(el_3)[0].hidden = false
        console.log(btn_edit.parentElement)
    })
    
    btn_cancel.addEventListener('click', function(){
        document.getElementsByClassName(el_3)[0].hidden = true
    })
}

click_and_cancel('btn_edit_info', 'btn_cancel_info', 'edit_info')
click_and_cancel('btn_create_post', 'btn_cancel_create', 'create_post')