let countHTML = document.getElementById("count")
let addBtn = document.getElementById("add-btn")
let clearBtn = document.getElementById("clear-btn")

let name = "Anuj Gupta, Abhinav Lugun, Min Set Aung"
let none = "No names displayed"

countHTML.innerHTML = none

const updateCountDom = (value) => {
    countHTML.innerHTML = value.toString()
}

addBtn.addEventListener("click", () => {
    updateCountDom(name)
})

clearBtn.addEventListener("click", () => {
    updateCountDom("Name cleared")
})
