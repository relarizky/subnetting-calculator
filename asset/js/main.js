// Javascript Files
// For fetching subnetting information from API

function showResult(result) {
  var tables = document.getElementById("subnetting-table");
  var result = JSON.parse(result);

  if (result.status == false){
    tables.innerHTML = "";
    tables.innerHTML += "<tr> <th colspan=2>" + result.message + " </th> </tr>";
  }else{
    tables.innerHTML = "";
    Object.keys(result.output).forEach(key => {
      if (key == "range"){
        table = "<tr><th>" + key.toUpperCase() + "</th>";
        table += "<td>" + result.output[key]["min"] + " - ";
        table += result.output[key]["max"] + "</td>";
      }else if (key == "class"){
        table = "<tr><th>" + key.toUpperCase() + "</th>";
        table += "<td>Class <b>" + result.output[key]["class"] + "</b></td>";
      }else{
        table = "<tr><th>" + key.toUpperCase() + "</th>";
        table += "<td>" + result.output[key] + "</td></tr>";
      }
      tables.innerHTML += table;
    });
  }
}

function subnetting() {
  var ip = document.querySelector('[name="ip"]').value;
  var netmask = document.querySelector('[name="netmask"]').value;
  var endpoint = window.location.origin + "/api/";

  var xhr_object = new XMLHttpRequest();
  var xhr_params = JSON.stringify(
      {
          ip: ip,
          netmask: netmask
      }
  );

  xhr_object.onreadystatechange = function () {
    if (xhr_object.readyState == 4 &&
       (xhr_object.status == 200 || xhr_object.status == 400)) {
      showResult(xhr_object.responseText);
    }
  }

  xhr_object.open("POST", endpoint, true);
  xhr_object.setRequestHeader("Content-Type", "application/json");
  xhr_object.send(xhr_params);
}
