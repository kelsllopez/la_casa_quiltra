document.addEventListener("DOMContentLoaded", () => {
    // Funcionalidad para mostrar/ocultar la historia completa
    const toggleButton = document.getElementById("toggle-history")
    const shortHistory = document.getElementById("short-history")
    const fullHistory = document.getElementById("full-history")
  
    if (toggleButton && shortHistory && fullHistory) {
      toggleButton.style.display = "inline-block"
  
      toggleButton.addEventListener("click", () => {
        if (fullHistory.style.display === "none") {
          shortHistory.style.display = "none"
          fullHistory.style.display = "block"
          toggleButton.textContent = "Ver menos"
        } else {
          shortHistory.style.display = "block"
          fullHistory.style.display = "none"
          toggleButton.textContent = "Ver más"
        }
      })
    }
  
    // Filtrado de voluntarios
    const filterButtons = document.querySelectorAll(".btn-filter");
    const volunteerItems = document.querySelectorAll(".volunteer-item");

    filterButtons.forEach((button) => {
      button.addEventListener("click", function () {
        // Remover clase active de todos los botones
        filterButtons.forEach((btn) => btn.classList.remove("active"));

        // Agregar clase active al botón clickeado
        this.classList.add("active");

        const filterValue = this.getAttribute("data-filter");

        // Filtrar voluntarios
        volunteerItems.forEach((item) => {
          const disponibilidad = item.getAttribute("data-disponibilidad");

          if (filterValue === "all" || disponibilidad === filterValue) {
            item.style.display = "block";
            setTimeout(() => {
              item.style.opacity = "1";
              item.style.transform = "translateY(0)";
              item.classList.add('fade-up');
            }, 100);
          } else {
            item.style.opacity = "0";
            item.style.transform = "translateY(20px)";
            setTimeout(() => {
              item.style.display = "none";
            }, 300);
          }
        });
      });
    });

    // Inicializar AOS (Animate On Scroll)
    if (typeof AOS !== "undefined") {
      AOS.init({
        duration: 800,
        easing: "ease-in-out",
        once: true,
      });
    } else {
      console.warn("AOS is not defined. Make sure it is properly imported.");
    }

  
    // Efecto hover para las tarjetas de equipo en dispositivos táctiles
    const teamCards = document.querySelectorAll(".team-card")
  
    teamCards.forEach((card) => {
      card.addEventListener(
        "touchstart",
        function () {
          this.classList.add("hover-effect")
        },
        { passive: true },
      )
  
      card.addEventListener(
        "touchend",
        function () {
          setTimeout(() => {
            this.classList.remove("hover-effect")
          }, 500)
        },
        { passive: true },
      )
    })
  })

  
  const loadMoreBtn = document.getElementById('load-more-btn');
  const loadLessBtn = document.getElementById('load-less-btn');
  const teamCards = document.querySelectorAll('.team-card-container');
  
  // Inicialmente, ocultamos todas las tarjetas después de la octava
  teamCards.forEach((card, index) => {
    if (index >= 8) {
      card.style.display = 'none';
    }
  });
  
  // Mostrar más tarjetas al hacer clic en el botón "Ver más"
  loadMoreBtn.addEventListener('click', () => {
    teamCards.forEach((card, index) => {
      if (index >= 8) {
        card.style.display = 'block';
      }
    });
  
    // Ocultar el botón "Ver más"
    loadMoreBtn.style.display = 'none';
  
    // Mostrar el botón "Ver menos"
    document.getElementById('load-less-btn-container').style.display = 'block';
  });
  
  // Mostrar menos tarjetas al hacer clic en el botón "Ver menos"
  loadLessBtn.addEventListener('click', () => {
    // Ocultar todas las tarjetas después de la octava
    teamCards.forEach((card, index) => {
      if (index >= 8) {
        card.style.display = 'none';
      }
    });
  
    // Mostrar el botón "Ver más" centrado
    loadMoreBtn.style.display = 'block';
  
    // Ocultar el botón "Ver menos"
    document.getElementById('load-less-btn-container').style.display = 'none';
  });
  
  let currentFilter = 'all';

  function toggleDetails(button) {
    let details = button.previousElementSibling;
    if (details.style.display === "none") {
      details.style.display = "block";
      button.textContent = "Ocultar información";
    } else {
      details.style.display = "none";
      button.textContent = "¿Quieres ver más información?";
    }
  }
  
  function filterVolunteers(filter) {
    currentFilter = filter;
    let count = 0;
    let displayedItems = 0;
    
    // Primero, contar cuántos elementos coinciden con el filtro
    document.querySelectorAll('.volunteer-item').forEach(item => {
      if (filter === 'all' || item.getAttribute('data-disponibilidad') === filter) {
        displayedItems++;
      }
    });
  
    // Luego, aplicar el filtro: mostrar u ocultar según corresponda
    document.querySelectorAll('.volunteer-item').forEach(item => {
      if ((filter === 'all' || item.getAttribute('data-disponibilidad') === filter) && count < 8) {
        item.style.display = "block";  // Mostrar los primeros 8 que coinciden
        count++;
      } else {
        item.style.display = "none";  // Ocultar el resto
      }
    });
  
    // Actualizar botones
    document.getElementById("show-more").style.display = displayedItems > 8 ? "inline-block" : "none";
    document.getElementById("show-less").style.display = "none";
    
    // Actualizar botones de filtro activos
    document.querySelectorAll('.btn-filter').forEach(btn => {
      btn.classList.remove('active');
    });
    document.querySelector(`[data-filter="${filter}"]`).classList.add('active');
  }
  
  function showMore() {
    let count = 0;
    let alreadyDisplayed = 0;
    let totalItems = 0;
    
    // Contar elementos ya mostrados
    document.querySelectorAll('.volunteer-item').forEach(item => {
      if ((currentFilter === 'all' || item.getAttribute('data-disponibilidad') === currentFilter)) {
        totalItems++;
        if (item.style.display === "block") {
          alreadyDisplayed++;
        }
      }
    });
  
    // Mostrar más elementos (los siguientes 8 o los que queden)
    document.querySelectorAll('.volunteer-item').forEach(item => {
      if ((currentFilter === 'all' || item.getAttribute('data-disponibilidad') === currentFilter) && item.style.display === "none") {
        if (count < 8) {
          item.style.display = "block";
          count++;
        }
      }
    });
  
    // Actualizar la visibilidad de los botones
    if (alreadyDisplayed + count >= totalItems) {
      document.getElementById("show-more").style.display = "none";
    }
    document.getElementById("show-less").style.display = "inline-block";
  }
  
  function showLess() {
    let count = 0;
    // Mostrar solo los primeros 8 elementos del filtro actual
    document.querySelectorAll('.volunteer-item').forEach(item => {
      if ((currentFilter === 'all' || item.getAttribute('data-disponibilidad') === currentFilter)) {
        if (count < 8) {
          item.style.display = "block";
          count++;
        } else {
          item.style.display = "none";
        }
      } else {
        item.style.display = "none";
      }
    });
  
    // Actualizar botones
    document.getElementById("show-more").style.display = "inline-block";
    document.getElementById("show-less").style.display = "none";
  }
  
  // Ejecutar esta función cuando se cargue la página
  document.addEventListener("DOMContentLoaded", function() {
    // Mostrar los voluntarios al cargar la página
    filterVolunteers('all');
  });

  