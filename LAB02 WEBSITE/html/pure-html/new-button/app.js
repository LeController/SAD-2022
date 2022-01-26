let countHTML = document.getElementById("count")
let addBtn = document.getElementById("add-btn")
let clearBtn = document.getElementById("clear-btn")

let name = "Anuj Gupta"
let none = "No name displayed"

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
