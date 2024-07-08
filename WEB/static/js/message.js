document.addEventListener('DOMContentLoaded',function(){
    var flashMessage = document.querySelectorAll('.flash-message')
    flashMessage.forEach(function(message){
        message.style.display = 'block';
        setTimeout(function(){
            message.style.display = 'none';
        },3000);
    });
});