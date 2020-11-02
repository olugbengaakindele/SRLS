/*   
    1- Declare empty list 
    2- Declare empty object
    3- populate object and append to list 
    4- JSON.stringfy the list then you have JSOn
    6- Send the JSON data to API
    7- from API route send to data base 

*/

//declare all variables 
const slider = document.querySelector('.slider');
M.Slider.init(slider,{

    indicators: false,
    height:500,
    transition:700,
    interval:6000
}
);
