const todoElement = document.getElementById("todos");
const inputBox = document.getElementById("input_box");

const addButton = document.getElementById("add_item");

function deleteItem(index) {
    fetch("/todos/" + index, { method: "DELETE" })
        .then(x => x.json())
        .then(updateItems);
}

function updateItems(items) {
    todoElement.innerHTML = "";
    items.forEach((item, index) => {
        todoElement.innerHTML += `<li>${item.value}</li><button class="delete" onclick="deleteItem(${index})">Delete</button>`;
    });
}

//Get all the items in the list
fetch("/todos", { method: "GET" })
    .then(x => x.json())
    .then(updateItems);

//Add Item to list
addButton.addEventListener("click", () => {
    fetch("/todos", {
        method: "PUT",
        // We need to let the server know that it is expecting JSON data 
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        // Stringify converts our data into a format it can be sent in
        body: JSON.stringify({ "value": inputBox.value })
    })
        .then(x => x.json())
        .then(updateItems);
})