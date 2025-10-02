window.addEventListener('DOMContentLoaded', (event) => {

    const symbol = document.querySelector('.symbol');

    window.addEventListener('scroll', function () {
        let scrollPos = window.scrollY;

        let distanciaFade = 50;

        let novaOpacidade = 1 - (scrollPos / distanciaFade);

        // Garante que a opacidade não seja menor que 0
        if (novaOpacidade < 0) {
            novaOpacidade = 0;
        }

        // Garante que a opacidade não seja maior que 1
        if (novaOpacidade > 1) {
            novaOpacidade = 1;
        }

        symbol.style.opacity = novaOpacidade;
    });
});
