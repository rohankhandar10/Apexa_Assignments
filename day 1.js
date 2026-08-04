document.getElementById("studentForm").addEventListener("submit", function(event){

    event.preventDefault();

    let name = document.getElementById("name").value;

    let roll = document.getElementById("roll").value;

    let department = document.getElementById("department").value;

    let year = document.getElementById("year").value;

    let email = document.getElementById("email").value;

    let mobile = document.getElementById("mobile").value;

    let gender = document.querySelector('input[name="gender"]:checked');

    if(gender==null){

        alert("Please select Gender");

        return;
    }

    alert(

        "Student Registration Successful\n\n"+

        "Name : "+name+

        "\nRoll No : "+roll+

        "\nDepartment : "+department+

        "\nYear : "+year+

        "\nEmail : "+email+

        "\nMobile : "+mobile+

        "\nGender : "+gender.value

    );

});

var name ="rohan"
console.log.(name) 