// FUNÇÃO PARA MOSTRAR CONTEÚDO EM CADA RADIO SELECIONADO

// ESPERAR QUE OS ELEMENTOS ESTEJAM TOTALMENTE CARREGADOS

document.addEventListener('DOMContentLoaded', function() {
    
    // SELECIONAR TODOS OS INPUTS COM O NOME DE " opcao "

    const radios = document.querySelectorAll('input[type="radio"][name="opcao"]');
    
    radios.forEach(radio => {
        // PARA CADA INPUT DO TIPO RADIO ENCONTRADO ADICIONA UM EVENTO " change "
        radio.addEventListener('change', function() {

            // SELECIONAR TODAS OS ELEMENTOS DIV COM A CLASSE " conteudo "

            const contentDivs = document.querySelectorAll('.conteudo');
            
            // REMOVE A CLASSE " ativo " DE TODAS AS DIVS DE CLASSE " conteudo "

            contentDivs.forEach(div => div.classList.remove('ativo'));
            
            // SELECIONA A DIV DE CLASSE " conteudo " COM O data-content IGUAL A ID DA OPÇÃO SELECIONADA

            const selectedContent = document.querySelector(`.conteudo[data-content="${this.id}"]`);
            
            // SE A DIV FOR ENCONTRADA ADICIONA A CLASSE " ativo " PARA SER VISUALIZADA

            if (selectedContent) {

                selectedContent.classList.add('ativo');
            }
        });
    });
});


// FUNÇÃO PARA DEFINIR SLIDES 

// ADICIONA UM EVENTO QUE SERÁ EXECUTADO QUANDO O DOCUMENTO HTML FOR TOTALMENTE CARREGADO E ANALISADO
document.addEventListener('DOMContentLoaded', () => {

  // SELECIONA TODOS OS ELEMENTOS COM A CLASSE " slider " E OS ARMAZENA NA CONSTANTE " sliders "
  const sliders = document.querySelectorAll('.slider');

  // PERCORRE CADA ELEMENTO " slider " NA CONSTANTE " sliders "
  sliders.forEach((slider) => {

    // SELECIONA TODOS OS ELEMENTOS COM A CLASSE " slide " DENTRO DO " slider " ATUAL E OS ARMAZENA NA CONSTANTE " slides "
    const slides = slider.querySelectorAll('.slide');

    // SELECIONA O ELEMENTO COM A CLASSE " slideWrapper " DENTRO DO " slider " ATUAL E O ARMAZENA NA CONSTANTE " sliderWrapper "
    const sliderWrapper = slider.querySelector('.slider-wrapper');

    // DEFINE A VARIÁVEL " currentIndex " COMO 0 PARA RASTREAR O SLIDE ATUAL
    let currentIndex = 0;

    // ARMAZENA O NÚMERO TOTAL DE SLIDES NA CONSTANTE " totalSlides "
    const totalSlides = slides.length;

    // DEFINE A FUNÇÃO " showSlide " QUE RECEBE UM ÍNDICE COMO PARÂMETRO
    const showSlide = (index) => {

      // CALCULA O DESLOCAMENTO (OFFSET) BASEADO NO ÍNDICE DO SLIDE ATUAL, MULTIPLICANDO POR -100 PARA MOVER O SLIDE CORRETAMENTE
      const offset = -index * 100;

      // ALTERA A PROPRIEDADE " transform " DO " sliderWrapper " PARA MOVER O SLIDE BASEADO NO DESLOCAMENTO CALCULADO
      sliderWrapper.style.transform = `translateX(${offset}%)`;
    };

    // DEFINE A FUNÇÃO " nextSlide " PARA MOSTRAR O PRÓXIMO SLIDE
    const nextSlide = () => {

      // ATUALIZA O " currentIndex " PARA O PRÓXIMO SLIDE, VOLTANDO AO PRIMEIRO SLIDE SE CHEGAR AO FINAL
      currentIndex = (currentIndex + 1) % totalSlides;

      // CHAMA A FUNÇÃO " showSlide " COM O ÍNDICE ATUALIZADO
      showSlide(currentIndex);
    };

    // DEFINE A FUNÇÃO " prevSlide " PARA MOSTRAR O SLIDE ANTERIOR
    const prevSlide = () => {

      // ATUALIZA O " currentIndex " PARA O SLIDE ANTERIOR, VOLTANDO AO ÚLTIMO SLIDE SE ESTIVER NO PRIMEIRO
      currentIndex = (currentIndex - 1 + totalSlides) % totalSlides;

      // CHAMA A FUNÇÃO " showSlide " COM O ÍNDICE ATUALIZADO
      showSlide(currentIndex);
    };

    // ADICIONA UM EVENTO DE CLIQUE AO BOTÃO 'NEXT' DENTRO DO " slider " ATUAL QUE CHAMA A FUNÇÃO " nextSlide "
    slider.querySelector('.next').addEventListener('click', nextSlide);

    // ADICIONA UM EVENTO DE CLIQUE AO BOTÃO 'PREV' DENTRO DO " slider " ATUAL QUE CHAMA A FUNÇÃO " prevSlide "
    slider.querySelector('.prev').addEventListener('click', prevSlide);

    // CONFIGURA UM INTERVALO PARA CHAMAR A FUNÇÃO " nextSlide " A CADA 10 SEGUNDOS, ALTERANDO AUTOMATICAMENTE OS SLIDES
    setInterval(nextSlide, 10000);

    // CHAMA A FUNÇÃO " showSlide " INICIALMENTE PARA MOSTRAR O PRIMEIRO SLIDE
    showSlide(currentIndex);
  });
});


  
