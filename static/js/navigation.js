document.addEventListener("DOMContentLoaded", () => {
    // handles the year and page select dropdowns
    document.getElementById('year-select').addEventListener('change', function () {
        window.location.href = this.value;
    });
    document.getElementById('page-select').addEventListener('change', function () {
        window.location.href = this.value;
    });
})
