var date = document.getElementsByName("age")[0];
function checkValue(str, max) {
  if (str.charAt(0) !== "0" || str == "00") {
    var num = parseInt(str);
    if (isNaN(num) || num <= 0 || num > max) num = 1;
    str =
      num > parseInt(max.toString().charAt(0)) && num.toString().length == 1
        ? "0" + num
        : num.toString();
  }
  return str;
}

function func_1() {
  this.type = "text";
  var input = this.value;
  if (/\D\/$/.test(input)) input = input.substr(0, input.length - 3);
  // console.log(input)
  var values = input.split("/").map(function (v) {
    return v.replace(/\D/g, "");
  });
  if (values[0]) values[0] = checkValue(values[0], 31);
  if (values[1]) values[1] = checkValue(values[1], 12);
  var output = values.map(function (v, i) {
    return v.length == 2 && i < 2 ? v + " / " : v;
  });
  this.value = output.join("").substr(0, 14);
}

function func_2() {
  this.type = "text";
  var input = this.value;
  var values = input.split("/").map(function (v, i) {
    return v.replace(/\D/g, "");
  });
  var output = "";

  if (values.length == 3) {
    var year =
      values[2].length !== 4 ? parseInt(values[2]) + 2000 : parseInt(values[2]);
    var month = parseInt(values[0]) - 1;
    var day = parseInt(values[1]);
    var d = new Date(year, month, day);
    if (!isNaN(d)) {
      document.getElementById("result").innerText = d.toString();
      var dates = [d.getMonth() + 1, d.getDate(), d.getFullYear()];
      output = dates
        .map(function (v) {
          v = v.toString();
          return v.length == 1 ? "0" + v : v;
        })
        .join(" / ");
    }
  }
  this.value = output;
}

date.addEventListener("input", func_1);
date.addEventListener("blur", func_2);

function ValidateEmail() {
  var validRegex =
    /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
  if (this.value.match(validRegex)) {
    this.style.cssText = "border: 1px solid green";
    return true;
  } else {
    this.style.cssText = "border: 1px solid red";
    return false;
  }
}

const gruopuser = document.getElementById("groupuser");
gruopuser.addEventListener("change", function () {
  // console.log(this.value)
  if (this.value == 'CT') {
    const add_branch = document.getElementById("add_branch");
    add_branch.disabled = false;
    function get_num_branch() {
      return parseInt(document.getElementById("num_branch").value);
    }

    add_branch.addEventListener("click", function () {
      const branch = document.createElement("div");
      branch.classList.add("py-2");

      const title = document.createElement("div");
      title.className = "text-center mb-2";
      title.innerText = "chi nhánh " + (get_num_branch() + 1);

      const row = document.createElement("div");
      row.classList.add("row");

      const cell_1 = document.createElement("div");
      cell_1.classList.add("col-4");
      const label_cell_1 = document.createElement("label");
      label_cell_1.classList.add("form-label");
      label_cell_1.innerText = "tỉnh/thành phố";
      const input_cell_1 = document.createElement("input");
      input_cell_1.classList.add("form-control");
      input_cell_1.name = "city";

      cell_1.appendChild(label_cell_1);
      cell_1.appendChild(input_cell_1);
      row.appendChild(cell_1);

      const cell_2 = document.createElement("div");
      cell_2.classList.add("col-4");
      const label_cell_2 = document.createElement("label");
      label_cell_2.classList.add("form-label");
      label_cell_2.innerText = "tỉnh/thành phố";
      const input_cell_2 = document.createElement("input");
      input_cell_2.classList.add("form-control");
      input_cell_2.name = "district";

      cell_2.appendChild(label_cell_2);
      cell_2.appendChild(input_cell_2);
      row.appendChild(cell_2);

      const cell_3 = document.createElement("div");
      cell_3.classList.add("col-4");
      const label_cell_3 = document.createElement("label");
      label_cell_3.classList.add("form-label");
      label_cell_3.innerText = "tỉnh/thành phố";
      const input_cell_3 = document.createElement("input");
      input_cell_3.classList.add("form-control");
      input_cell_3.name = "ward";

      cell_3.appendChild(label_cell_3);
      cell_3.appendChild(input_cell_3);
      row.appendChild(cell_3);

      const detail = document.createElement("div");
      detail.classList.add("mb-2");
      const detail_label = document.createElement("label");
      detail_label.classList.add("form-label");
      detail_label.innerText = "số nhà dường";
      const detail_input = document.createElement("input");
      detail_input.classList.add("form-control");
      detail_input.name = "street";

      detail.appendChild(detail_label);
      detail.appendChild(detail_input);

      branch.appendChild(title);
      branch.appendChild(row);
      branch.appendChild(detail);
      document.getElementById("branch").appendChild(branch);
      document
        .getElementById("branch")
        .appendChild(document.createElement("hr"));
      document.getElementById("num_branch").value = get_num_branch() + 1;
    });
  }
  else{
    const add_branch = document.getElementById("add_branch");
    add_branch.disabled = true;
  }
});
