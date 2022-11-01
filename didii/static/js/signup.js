const loginText = document.querySelector(".title-text .login");
const loginForm = document.querySelector("form.login");
const loginBtn = document.querySelector("label.login");
const signupBtn = document.querySelector("label.signup");
const signupLink = document.querySelector("form .signup-link a");
signupBtn.onclick = (()=>{
  loginForm.style.marginLeft = "-50%";
  loginText.style.marginLeft = "-50%";
});
loginBtn.onclick = (()=>{
  loginForm.style.marginLeft = "0%";
  loginText.style.marginLeft = "0%";
});

const add = document.getElementById("add_branch")

function get_amount_branch(){
  const el = document.getElementsByClassName('branch_counter')
  // console.log(el)
  return el.length
}

add.addEventListener('click', function(){
  document.getElementById('first_branch').hidden = false
  const branch = document.getElementById("branch")

  const div_row = document.createElement('div')
  div_row.classList.add('row')

  const form_gr_1 = document.createElement('div')
  form_gr_1.classList.add('col-4')
  const label_1 = document.createElement('label')
  label_1.classList.add('form-label')
  label_1.innerText = "tỉnh/thành phố"
  const input_1 = document.createElement('input')
  input_1.classList.add('form-control')
  form_gr_1.appendChild(label_1)
  form_gr_1.appendChild(input_1)
  div_row.appendChild(form_gr_1)

  const form_gr_2 = document.createElement('div')
  form_gr_2.classList.add('col-4')
  const label_2 = document.createElement('label')
  label_2.classList.add('form-label')
  label_2.innerText = "quận/huyện"
  const input_2 = document.createElement('input')
  input_2.classList.add('form-control')
  form_gr_2.appendChild(label_2)
  form_gr_2.appendChild(input_2)
  div_row.appendChild(form_gr_2)

  const form_gr3 = document.createElement('div')
  form_gr3.classList.add('col-4')
  const label3 = document.createElement('label')
  label3.classList.add('form-label')
  label3.innerText = "phường/xã/thị trấn"
  const input3 = document.createElement('input')
  input3.classList.add('form-control')
  form_gr3.appendChild(label3)
  form_gr3.appendChild(input3)
  div_row.appendChild(form_gr3)

  // console.log(div_row)

  const address_branch = document.createElement('div')
  address_branch.className += "py-2 border-top border-bottom"

  const counter_branch = document.createElement('div')
  counter_branch.className = "text-center mb-2"
  counter_branch.innerText = "chi nhánh "
  const counter_item = document.createElement('span')
  counter_item.classList.add('branch_counter')
  counter_item.innerText = get_amount_branch() + 1
  counter_branch.appendChild(counter_item)
  address_branch.appendChild(counter_branch)

  const div_detail = document.createElement('div')
  div_detail.classList.add('mb-2')
  const label_detail = document.createElement('label')
  label_detail.classList.add('form-label')
  label_detail.innerText = 'số nhà đường'
  const input_detail = document.createElement('input')
  input_detail.classList.add('form-control')
  div_detail.appendChild(label_detail)
  div_detail.appendChild(input_detail)
  
  address_branch.appendChild(div_row)
  address_branch.appendChild(div_detail)
  branch.appendChild(address_branch)  


  num = document.getElementById('num_branch')
  num.value() = get_amount_branch() + 1
})
