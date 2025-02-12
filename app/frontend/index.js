const BASE_URL = 'https://quepeliveo.es';

async function obtenerPeliculas(prompt, numero) {
    const peliculas = await fetch(`${BASE_URL}/recomendador?prompt=${prompt}&numero=${numero}`);
    const pelis = await peliculas.json();
    pintarPeliculas(pelis);
};

function limpiarPelis() {
    const peliculas = document.getElementById("peliculas");
    peliculas.innerHTML = '';
}

async function pintarPeliculas(pelis) {
    await limpiarPelis();

    const peliculas = document.getElementById("peliculas");

    for (let peli in pelis) {
        const card = document.createElement("div");
        card.classList.add("card", "fixed-height-card");
        card.style.width = "18rem";

        const img = document.createElement("img");
        img.classList.add("card-img-top", "fixed-image", "mt-2");
        imagen = `${pelis[peli].poster}`
        if (imagen === "") {
            img.src = `./img/sin_poster.jpg`;
            img.alt = "Esta película no tiene póster conocido";
        }
        else {
            img.src = imagen;
            img.alt = "Póster de la película";
        }


        const cardBody = document.createElement("div");
        cardBody.classList.add("card-body");

        const cardTitle = document.createElement("h2");
        cardTitle.classList.add("card-title", "fixed-height-title");
        cardTitle.textContent = `${pelis[peli].nombre}`;

        const cardYear = document.createElement("h5");
        cardYear.classList.add("card-sub-title");
        if (`${pelis[peli].anyo}` === "") {
            cardYear.textContent = "Año desconocido"
        }
        else {
            cardYear.textContent = `${pelis[peli].anyo}`;
        }

        const cardText = document.createElement("p");
        cardText.classList.add("fixed-height-text");
        cardText.setAttribute("id", "texto-carta")
        cardText.textContent = `${pelis[peli].sinopsis}`;
        if (cardText.textContent === "") {
            cardText.textContent = "Esta película no tiene sinopsis...\nTe atreves?"
        }

        const cardTextDiv = document.createElement("div");
        cardTextDiv.classList.add("fixed");

        const cardDiv = document.createElement("div");
        cardDiv.classList.add("d-flex", "justify-content-center");
        cardDiv.setAttribute("id", "cardiv");

        const cardButton = document.createElement("a");
        cardButton.classList.add("btn", "btn-warning", "m-auto", "boton");
        cardButton.target = `_blank`;
        cardButton.textContent = "IMDb";
        if (pelis[peli].IMDB === "") {
            cardButton.setAttribute("disabled", "True")
            cardButton.classList.add("transparente")
        }
        else {
            cardButton.href = `${pelis[peli].IMDB}`;
        }

        cardBody.appendChild(cardTitle);
        cardBody.appendChild(cardYear);
        cardTextDiv.appendChild(cardText);
        cardBody.appendChild(cardTextDiv);
        cardBody.appendChild(cardDiv);
        carDiv = document.getElementById("cardiv");
        cardDiv.appendChild(cardButton);

        card.appendChild(img);
        card.appendChild(cardBody);

        peliculas.appendChild(card);
    }
}

function formularioListener() {
    const formulario = document.getElementById("specs");
    const selector = document.getElementById("selector");

    document.getElementById('prompt').addEventListener('input', function (event) {
        let value = event.target.value;
        if (value.length > 0) {
            event.target.value = value.charAt(0).toUpperCase() + value.slice(1);
        }
    });

    formulario.addEventListener('submit', async function (e) {
        e.preventDefault();
        const prompt = document.getElementById('prompt');
        if (!isNaN(selector.value)) {
            await obtenerPeliculas(prompt.value, selector.value);
            document.getElementById('peliculas').scrollIntoView({ behavior: "smooth" })
        }
    });

    formulario.addEventListener('keypress', function (event) {
        if (event.key === 'Enter') {
            event.preventDefault(); // Evita que se envíe el formulario
            document.getElementById('recomendar-btn').click(); // Simula un clic en el botón
        }
    });
}

function inicializar() {
    formularioListener();
}

inicializar();
