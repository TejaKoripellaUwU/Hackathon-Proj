let select = document.querySelector("select")
let tGetter = document.querySelector("#getTopics")
let add = document.querySelector("#containerAdd")
tGetter.addEventListener("click",()=>{
    add.replaceChildren();
    output = select.value;
    $.ajax({
        url: "/getTopics/",
        type: 'POST',
        data: {
            grade:output
        },
        success: function (response) {
            for (item of response){
                let check = document.createElement('input')
                check.type = "checkbox"
                check.name = item[1];
                add.appendChild(check);
                let label = document.createElement("label")
                label.for = item[1];
                add.appendChild(label).innerHTML ='<label>'+item[0]+'</label>'
            }
        },
        error: function (response) {
        }
    });
})
