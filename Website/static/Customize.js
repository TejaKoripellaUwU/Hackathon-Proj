let select = document.querySelector("select");
let tGetter = document.querySelector("#getTopics");
let remove = document.querySelector("#containerRemove");
let removeTopic = document.querySelector("#remove");
let add = document.querySelector("#containerAdd");
let addTopic = document.querySelector("#add");
let finish = document.querySelector("#Download")
let text = document.querySelector("#idk")
let finalFunctions = [];
let finalMeta = [];

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
            let labels = []
            for (item of response){
                let check = document.createElement('input')
                check.type = "checkbox"
                check.name = item[0];
                add.appendChild(check);
                let label = document.createElement("label")
                label.setAttribute("for",item[0]);
                add.appendChild(label).innerHTML = item[0]
                labels.push(label)
            }
            addTopic.addEventListener("click",()=>{
                for (let i = 0; i<add.childNodes.length;i++){
                    if(add.childNodes[i].checked){
                        finalFunctions.push(add.childNodes[i].name)
                        remove.appendChild(add.childNodes[i])
                        remove.appendChild(add.childNodes[i])
                    }
                }
            })
            removeTopic.addEventListener("click",()=>{
                for (let i = 0; i<remove.childNodes.length;i++){
                    if(remove.childNodes[i].checked){
                        var index = finalFunctions.indexOf(remove.childNodes[i].name);
                        if (index > -1) {
                            finalFunctions.splice(index, 1);
                        }
                        remove.removeChild(remove.childNodes[i])
                        remove.removeChild(remove.childNodes[i])
                    }
                }
            })
            finish.addEventListener('click',()=>{
                text.setAttribute("value",JSON.stringify(finalFunctions))
            })
            
        },
        error: function (response) {
        }
    });
})

