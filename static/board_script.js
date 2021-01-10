// const { default: axios } = require("axios");

$("#guess_form").submit(async function(e){
    
    // console.log("testing js code");
    // alert("testing js code")
    e.preventDefault();
    input_val = $('#word_input').val();
    console.log(input_val);
    this.reset();
    // response = axios.get();
});