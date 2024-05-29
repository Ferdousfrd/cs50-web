document.addEventListener("DOMContentLoaded", function(){

    document.querySelector('h1').innerHTML = localStorage.getItem('counter') 
    
    
    if (!localStorage.getItem('counter')){
        localStorage.setItem('counter', 0)
    }


    //to use it in interval
    function count(){
        let counter = localStorage.getItem('counter')
        counter++
        document.querySelector('h1').innerHTML = counter
        localStorage.setItem('counter', counter)                   
    }



    document.querySelector('button').onclick = function(){
        count()

    }


})