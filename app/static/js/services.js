/*   
    1- Declare empty list 
    2- Declare empty object
    3- populate object and append to list 
    4- JSON.stringfy the list then you have JSOn
    6- Send the JSON data to API
    7- from API route send to data base 

*/

//declare all variables 
let form_sec = document.querySelector("#form-section");
const btn_add_service = document.querySelector("#add-service");



/* this loads all event listeners */
loadEventListeners();
function loadEventListeners() {
    btn_add_service.addEventListener("click", add_new_service_forms);
    

}



// Service will contain all the service of a user in a list of objects
let all_services =[];
// service contains description of each service
let services ={};



