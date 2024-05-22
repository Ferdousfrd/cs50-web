document.addEventListener("DOMContentLoaded", ()=>{
    document.querySelector('select').onchange = ()=>{
        document.querySelector('#hello').style.color = this.value;
    }
})