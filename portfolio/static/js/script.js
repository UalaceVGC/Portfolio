document.addEventListener('DOMContentLoaded', () => {
    console.log('Landing page de portfólio carregada!');

    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();

            const targetId = this.getAttribute('href');
            if (targetId) {
                const targetElement = document.querySelector(targetId);
                if (targetElement) {
                    targetElement.scrollIntoView({
                        behavior: 'smooth'
                    });
                }
            }
        });
    });

    // Função para iniciar a animação de digitação
    function startTypingAnimation() {
        const typingElement = document.querySelector('.typing-effect');
        if (typingElement) {
            const textToType = typingElement.getAttribute('data-text');
            const numberOfChars = textToType.length;

            // Define o número de steps dinamicamente baseado no texto
            // Isso garante que cada caractere seja um "passo"
            typingElement.style.setProperty('--typing-steps', numberOfChars);
            typingElement.style.setProperty('--typing-time', `${numberOfChars * 0.15}s`); // 0.15s por caractere

            // Adiciona o texto ao elemento (invisível inicialmente pelo CSS)
            typingElement.textContent = textToType;

            // Adiciona a classe para iniciar a animação
            typingElement.classList.add('typing-active');

            // Opcional: remover o cursor piscando após a digitação
            // setTimeout(() => {
            //     typingElement.style.borderRight = 'none';
            // }, numberOfChars * 150 + 500); // Tempo da animação + um pequeno atraso
        }
    }

    // Inicia a animação de digitação quando a página carrega
    startTypingAnimation();


    // Exemplo de funcionalidade para o botão "Mostrar mais projetos"
    const showMoreProjectsBtn = document.querySelector('.btn--primary');
    if (showMoreProjectsBtn) {
        showMoreProjectsBtn.addEventListener('click', () => {
            alert('Funcionalidade de "Mostrar mais projetos" a ser implementada!');
        });
    }
});