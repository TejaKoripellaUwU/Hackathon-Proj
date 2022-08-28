let select = document.querySelector("select");
let tGetter = document.querySelector("#getTopics");
let remove = document.querySelector("#containerRemove");
let removeTopic = document.querySelector("#remove");
let add = document.querySelector("#containerAdd");
let addTopic = document.querySelector("#add");
let finalFunctions = [];

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
                check.name = item[1];
                check.raw = item[0]
                add.appendChild(check);
                let label = document.createElement("label")
                label.for = item[1];
                add.appendChild(label).innerHTML ='<label>'+item[0]+'</label>'
                labels.push(label)
            }
            addTopic.addEventListener("click",()=>{
                for (child of add.children){
                    if(child.checked){
                        finalFunctions.push(child.textContent)
                        remove.appendChild(child)
                        let label = document.createElement("label")
                        label.for = child.name;
                        remove.appendChild(label).innerHTML ='<label>'+child.raw+'</label>'
                        
                    }
                }
            })
        },
        error: function (response) {
        }
    });
})

