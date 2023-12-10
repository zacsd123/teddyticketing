$(document).ready(function() {
    // sign-up
    $("#sign-up-input-id").change(function() {
        $("#sign-up-chack").text("중복체크")
    })

    // modal
    $("#ticketing-close-button").click(function() {
        $("body").removeClass("static")
        $("#ticketing-close-button").addClass("hidden")
        $("#ticketing-modalContainer").addClass("hidden")
    })

    $("#modalCloseButton").click(function() {
        var value = $('#modalbody').text()
        if (value.includes("아이디")) {
            $("#sign-up-input-id").focus()
        } else if (value.includes("비밀번호")) {
            $("#sign-up-input-password").focus()
        } else if (value.includes("이메일")) {
            $("#sign-up-input-email").focus()
        }
        $("body").removeClass("static")
        $("#modalContainer").addClass("hidden")
    })

    $("#modalCloseIcon").click(function() {
        $("body").removeClass("static")
        $("#modalContainer").addClass("hidden")
    })

    $("#ticketing-modalCloseButton").click(function() {
        var content = $("#ticketing-modalbody").text()[0]
        if (content == "다") {
            var locations = $(".select-place").text()
            var place = $("#"+locations).val()
            axios.post("/ticketing", { value: place })
                .then(function(response) {
                    var res = response.data
                    $("body").removeClass("static")
                    $("#ticketing-close-button").addClass("hidden")
                    $("#ticketing-modalContainer").addClass("hidden")
                    if (res["data"] == "이미") {
                        $("#modalContainer").removeClass("hidden")
                        $("body").addClass("static")
                        $('#modalbody').text("이미 예약하였습니다.")
                        location.href = "/"
                    } else if (res["data"] == "예매") {
                        location.href = "/"
                    }
                })
        } else {
            $("body").removeClass("static")
            $("#ticketing-close-button").addClass("hidden")
            $("#ticketing-modalContainer").addClass("hidden")
            location.href = "/"
        }
    })
})

// signup
function SignUpClick() {
    var name = $("#sign-up-input-id").val()
    var password = $("#sign-up-input-password").val()
    var email = $("#sign-up-input-email").val()
    var Idcheck =  $("#sign-up-chack").text()

    console.log(Idcheck)

    if (name == "") {
        $("#modalContainer").removeClass("hidden")
        $("body").addClass("static")
        $('#modalbody').text("아이디를 입력해 주세요.")
    } else if (password == "") {
        $("#modalContainer").removeClass("hidden")
        $("body").addClass("static")
        $('#modalbody').text("비밀번호를 작성해 주세요.")
    } else if (email == "") {
        $("#modalContainer").removeClass("hidden")
        $("body").addClass("static")
        $('#modalbody').text("이메일을 작성해 주세요.")
    } else {
        axios.post("/signup", { "name": name , "password": password, "email": email , "check": Idcheck})
            .then(function(response) {
                var res = response.data
                console.log(res)
                if (res["static"] == "noncheck") {
                    $("#modalContainer").removeClass("hidden")
                    $("body").addClass("static")
                    $('#modalbody').text("아이디 중복 체크를 해 주세요.")
                } else if (res["static"] == true) {
                    location.href = "email"
                } else {
                    $("#modalContainer").removeClass("hidden")
                    $("body").addClass("static")
                    $('#modalbody').text("정확히 입력해 주세요.")
                }
            })
            .catch(function(error) {
                console.log(error)
            })
    }
}

function EmailSignin() {
    var number = $("#email").val()
    console.log(number)

    axios.post("/email", { "number": number })
        .then(function(response) {
            var res = response.data
            if (res["error"] == "성공") {
                $("#modalContainer").removeClass("hidden")
                $("body").addClass("static")
                $('#modalbody').text("인증되었습니다.")
                location.href = "/"
            } else if (res["error"] == "실패") {
                $("#modalContainer").removeClass("hidden")
                $("body").addClass("static")
                $('#modalheader').text("성공")
                $('#modalbody').text("인증 번호가 틀렸습니다.")
            }
        })
}

function SignUpIdChack() {
    $("#sign-up-chack").html('<div id="loader" class="loader1"></div>')
    var id = $("#sign-up-input-id").val()
    if (id == "") {
        $("#modalContainer").removeClass("hidden")
        $("body").addClass("static")
        $('#modalbody').text("아이디를 입력해 주세요.")
        $("#sign-up-chack").text("실패");
    } else {
        setTimeout(function() {
            axios.post("/idcheck", {value: id})
            .then(function(response) {
                var res = response.data
                console.log(res["check"])
                if (!res["check"]) {
                    $("#sign-up-chack").text("사용가능")
                } else {
                    $("#sign-up-chack").text("사용중")
                }
            })
            .catch(function(error) {
                console.log(error)
            })
        }, 1500);
    }
}

// signin
function SignInButton() {
    var id = $("#text").val()
    var password = $("#password").val()
    axios.post("/signin", { "id": id, "password": password })
        .then(function(response) {
            var res = response.data
            console.log(res["value"])
            if (res["value"]) {
                location.href = "/"
            } else {
                $("#modalContainer").removeClass("hidden")
                $("body").addClass("static")
                $('#modalbody').text("아이디나 비밀번호가 틀렸습니다.")
            }
        })
        .catch(function(error) {
            console.log(error)
        })
}

// ticketing

function NonTicketing() {
    $("#modalContainer").removeClass("hidden")
    $("body").addClass("static")
    $('#modalbody').text("이미 예매된 자리입니다.")

}

function Place(asd) {
    $(".select-place").text(asd)
}

function Ticketing() {
    $("#ticketing-modalContainer").removeClass("hidden")
    $("body").addClass("static")
    var place = $(".select-place").text()
    if (place != "") {
        $("#ticketing-close-button").removeClass("hidden")
        $('#ticketing-modalbody').text("다음 자리로 예매하시겠습니까? : " + place)
    } else {
        $('#ticketing-modalbody').text("자리를 선택해 주세요.")
    }
}