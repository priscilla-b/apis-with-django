const loginForm = document.getElementById('login-form')
const baseEndpoint = "http://localhost:8000/api"

if (loginForm) {
    // handle this login form

    loginForm.addEventListener('submit', handleLogin)
}

function handleLogin(event){
    console.log(event)
    event.preventDefault()
    const loginEndpoint = `${baseEndpoint}/token/`
    let loginFormData = new FormData(loginForm)
    let loginObjectData = Object.fromEntries(loginFormData)
    console.log(loginObjectData)
    const options = {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body:JSON.stringify(loginObjectData)
    }
    fetch(loginEndpoint, options)  // similar to request.post. A promise
    .then(response => {
        console.log(response)
        return response.json()
    })
    .then (handleAuthData)  
    .catch(err => {
        console.log('err', err)
    })

}

function handleAuthData(authData){
    localStorage.setItem('access', authData.access)
    localStorage.setItem('refresh', authData.refresh)
}

function getProductList(){
    const endpoint = `${baseEndpoint}/products/`
    const options = {
        method: "GET",
        headers: {
            "Content-Type": "application/json"
        },
        // body:JSON.stringify(loginObjectData)
    }
    fetch(endpoint, options)
    .then(response => response.json())
    .then()
}