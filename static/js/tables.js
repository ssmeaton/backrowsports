document.addEventListener("DOMContentLoaded", () => {
    // get all tables and add "table" class to them
    document.querySelectorAll("table").forEach(table => {
        table.classList.add("table")
    })
})
