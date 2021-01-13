// const { default: axios } = require("axios");
let score = 0;
let used_words = new Set();
let set_time = 61000;
$('#guess_form').hide();

function startTimer(duration, display) {
    var timer = duration, minutes, seconds;

    let interval = setInterval(function () {
        minutes = parseInt(timer / 60, 10);
        seconds = parseInt(timer % 60, 10);

        minutes = minutes < 10 ? "0" + minutes : minutes;
        seconds = seconds < 10 ? "0" + seconds : seconds;

        display.textContent = minutes + ":" + seconds;

        if (--timer < 0) {
            timer = duration;
        }
    }, 1000);

    setTimeout(function(){
        clearInterval(interval);
    },set_time);
}

$('#start_button').on('click',async function(){
    score = 0;

    $('#guess_form').show();
    display = document.querySelector('#time');
    startTimer(10,display);
    $('#start_button').hide();
    setTimeout(async function(){
        $('#guess_form').hide();

        //communicate score with backend
        const response = await axios.post("/finished", {score: score})
        console.log(response.data)

        $('#start_button').show();
        location.reload();
    },set_time);
    // changeback to 60000 instead of 1000
})


$("#guess_form").submit(async function(e){
    e.preventDefault();
    let word = $('#word_input').val();
    console.log(word);
    
    const resp = await axios.get("/guess", { params: {word: word}});
    // console.log(resp);
    let result = resp.data.result;
    // console.log(result);
    if (result == "ok"){
        
        if(!used_words.has(word)){
            used_words.add(word);
            console.log('it do be an ok word');
            $('#msg').html('That word was ok')
            score+= word.length
            $('#score').html(`${score}`)
        }
        else{
            $('#msg').html('That word has already been used!')
        }

    }
    else if (result == "not-on-board"){
        console.log('it do be not-on-board');
        $('#msg').html('That word was not on board')
    }
    else{
        console.log('it realy do be not a word');
        $('#msg').html('That word was not a word')
    }
    this.reset();
});