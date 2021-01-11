// const { default: axios } = require("axios");

$("#guess_form").submit(async function(e){
    // console.log("testing js code");
    // alert("testing js code")
    e.preventDefault();
    let word = $('#word_input').val();
    console.log(word);
    
    const resp = await axios.get("/guess", { params: {word: word}});
    // console.log(resp);
    let result = resp.data.result;
    // console.log(result);
    // if(result == "not-a-word"){

    // }

    // this.reset();
});