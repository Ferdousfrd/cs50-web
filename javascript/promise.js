let p = new Promise((resolve, reject) => {
  let sum = 2 + 3

  if(sum == 5){
    resolve("Success")
  }
  else{
    reject("Failed")
  }
})

p.then((message) => {
  console.log("This is then, " + message) 
}).catch((message) => {
  console.log(message)
})


