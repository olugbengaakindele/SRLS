const pstcod = document.querySelector("#postcode");
const cmbCountry= document.querySelector("#country");

/*http://api.postcodes.io/postcodes/OX495NU*/


/* this loads all event listeners */
loadEventListeners();
function loadEventListeners() {
    pstcod.addEventListener("change", getcity);
    cmbCountry.addEventListener("change", runAjax);

}



function  getcity(){
pst_val = pstcod.value;

xhr = new XMLHttpRequest();
xhr.open('GET', `https://api.postcodes.io/postcodes/${pst_val}`, true);
xhr.onload = function(){
    console.log(pst_val);
    if (xhr.status === 200){
        data= JSON.parse(this.responseText);
        console.log(data.result[5]);
        }

    }
 xhr.send();
}
