//function getHello() {
    //const url = 'http://127.0.0.1:5000/hello'
    //fetch(url)
    //.then(response => response.json())  
    //.then(json => {
        //console.log(json);
        //document.getElementById("demo").innerHTML = JSON.stringify(json)
    //})
//}
let run = "jesus";
let selected = document.querySelector("select")
let elements;
let ul = document.querySelector("#listOfTopics")
let custom = document.querySelector("#customize");
selected.addEventListener("change",()=>{
    ul.replaceChildren();
    output = selected.value;
    //console.log(output)
    $.ajax({
        url: "/getTopics/",
        type: 'POST',
        data: {
            grade:output
        },
        success: function (response) {

            for (item of response){
                let li = document.createElement('li')
                ul.appendChild(li).innerHTML ='<li>'+item[0]+'</li>';
            }
        },
        error: function (response) {
        }
    });

})
