const button1 = document.querySelector('#btn')
console.log(button1)

const div1 = document.createElement('div')

//first we give our function a name and add async word. like async () instead of ()
const clickHandler = async() => {      
    try{
    //instead of fetch().then or promise.then
    //we use await.fetch or await.promise which returns a response
    //so use have to store that response
    const res = await fetch('https://reqres.in/api/users')


    //the resoponse is another promise which we brings us some string weird data
    //that we have to use.json() to make useable
    //so we sstore that in data variable 
    const data = await res.json()

    if(!res.ok){
        console.log(data.description)
        return
    }

    const userData1 = data.data
    div1.innerHTML = `ID : ${userData1[1].id}`
    }          

    catch(error){
        console.log(error)
    }  

}

document.body.appendChild(div1)

button1.addEventListener('click', clickHandler)


//.then method
// fetch('https://reqres.in/api/users')
//     .then(res => {
//         if(!res.ok){
//             console.log("Error")
//             return
//         }
//         return res.json()})
//     .then(data => {
        
//         const userData1 = data.data
//         div1.innerHTML = `ID : ${userData1[1].id}`
//     })
//     .catch(error => console.log("error"))