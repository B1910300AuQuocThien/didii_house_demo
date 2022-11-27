function click_and_cancel(el_1, el_2, el_3) {
  // const btn_edit = document.getElementById(el_1)

  window.addEventListener("load", function () {
    document.getElementsByClassName(el_3)[0].hidden = false;
    document.getElementsByClassName(el_2).addEventListener("click", function(){
        document.getElementsByClassName(el_3)[0].hidden = true;
        console.log('thien')
    });
    
  });
  
}

click_and_cancel("btn_edit_info", "btn_cancel_info", "edit_info");
click_and_cancel("btn_create_post", "btn_cancel_create", "create_post");
