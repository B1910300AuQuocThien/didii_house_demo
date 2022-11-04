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
  input_1.name = "CT_add_city"
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
  input_2.name = "CT_add_district"
  form_gr_2.appendChild(label_2)
  form_gr_2.appendChild(input_2)
  div_row.appendChild(form_gr_2)

  const form_gr_3 = document.createElement('div')
  form_gr_3.classList.add('col-4')
  const label_3 = document.createElement('label')
  label_3.classList.add('form-label')
  label_3.innerText = "phường/xã/thị trấn"
  const input_3 = document.createElement('input')
  input_3.classList.add('form-control')
  input_3.name = "CT_add_ward"
  form_gr_3.appendChild(label_3)
  form_gr_3.appendChild(input_3)
  div_row.appendChild(form_gr_3)

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
  input_detail.name = "CT_add_street"
  div_detail.appendChild(label_detail)
  div_detail.appendChild(input_detail)
  
  address_branch.appendChild(div_row)
  address_branch.appendChild(div_detail)
  branch.appendChild(address_branch)  

  num = document.getElementById('num_branch')
  num.value = get_amount_branch()
  console.log(num.value)
})


function checkPass(el1, el2){
  const pass = document.getElementsByName(el1)[0]
  const retype = document.getElementsByName(el2)[0]
  retype.addEventListener('blur', function(){
    if(pass.value != retype.value && pass !== "" && retype   !== ""){
      pass.style.cssText = "border: 1px solid red;"
      retype.style.cssText = "border: 1px solid red;"
    }
    else{
      pass.style.cssText = "border: 1px solid green;"
      retype.style.cssText = "border: 1px solid green;"
    }
  })
}

checkPass("CT_pass", "CT_retype_pass")
checkPass("KH_pass", "KH_retype_pass")


var CT_date = document.getElementsByName('CT_age')[0];
var KH_date = document.getElementsByName('KH_age')[0];
function checkValue(str, max) {
  if (str.charAt(0) !== '0' || str == '00') {
    var num = parseInt(str);
    if (isNaN(num) || num <= 0 || num > max) num = 1;
    str = num > parseInt(max.toString().charAt(0)) && num.toString().length == 1 ? '0' + num : num.toString();
  };
  return str;
};

function func_1(){
  this.type = 'text';
  var input = this.value;
  if (/\D\/$/.test(input)) input = input.substr(0, input.length - 3);
  // console.log(input)
  var values = input.split('/').map(function(v) {
    return v.replace(/\D/g, '')
  });
  if (values[0]) values[0] = checkValue(values[0], 31);
  if (values[1]) values[1] = checkValue(values[1], 12);
  var output = values.map(function(v, i) {
    return v.length == 2 && i < 2 ? v + ' / ' : v;
  });
  this.value = output.join('').substr(0, 14);
}

function func_2(){
  this.type = 'text';
  var input = this.value;
  var values = input.split('/').map(function(v, i) {
    return v.replace(/\D/g, '')
  });
  var output = '';
  
  if (values.length == 3) {
    var year = values[2].length !== 4 ? parseInt(values[2]) + 2000 : parseInt(values[2]);
    var month = parseInt(values[0]) - 1;
    var day = parseInt(values[1]);
    var d = new Date(year, month, day);
    if (!isNaN(d)) {
      document.getElementById('result').innerText = d.toString();
      var dates = [d.getMonth() + 1, d.getDate(), d.getFullYear()];
      output = dates.map(function(v) {
        v = v.toString();
        return v.length == 1 ? '0' + v : v;
      }).join(' / ');
    };
  };
  this.value = output;
}


CT_date.addEventListener('input', func_1)
CT_date.addEventListener('blur', func_2)

KH_date.addEventListener('input', func_1)
KH_date.addEventListener('blur', func_2)

function ValidateEmail() {
  var validRegex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
  if (this.value.match(validRegex)) {
    this.style.cssText = "border: 1px solid green"
    return true;
  } 
  else {
    this.style.cssText = "border: 1px solid red"
    return false;
  }
}

CT_email = document.getElementsByName('CT_email')[0]
CT_email.addEventListener('blur', ValidateEmail)

KH_mail = document.getElementsByName('KH_email')[0]
KH_mail.addEventListener('blur', ValidateEmail)