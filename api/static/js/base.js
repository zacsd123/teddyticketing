$(document).ready(function() {
    console.log("connect")
})

function SignUpClick() {
    var name = $("#text").val()
    var password = $("#password").val()
    var email = $("#email").val()
    // console.log(name, password, email)
    axios.post("/newuser", { value: name })
        .then(function(response) {
            var res = response.data
            console.log(res)
        })
        .catch(function(error) {
            console.log(error)
        })
}