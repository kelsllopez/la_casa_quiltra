document.addEventListener("DOMContentLoaded", function () {
    // Restaurar la pestaña activa desde localStorage
    let activeTab = localStorage.getItem("activeTab");
    if (activeTab) {
        let tabElement = document.querySelector(`[data-bs-target="${activeTab}"]`);
        if (tabElement) {
            new bootstrap.Tab(tabElement).show();
        }
    }

    // Guardar la pestaña activa cuando el usuario cambia de pestaña
    document.querySelectorAll('.nav-link').forEach(tab => {
        tab.addEventListener("shown.bs.tab", function (event) {
            localStorage.setItem("activeTab", event.target.dataset.bsTarget);
        });
    });
});