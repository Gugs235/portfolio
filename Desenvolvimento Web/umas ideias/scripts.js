// Animações ao rolar a página
document.addEventListener('scroll', () => {
    const elements = document.querySelectorAll('.fade-in');
    elements.forEach(el => {
        const position = el.getBoundingClientRect().top;
        const windowHeight = window.innerHeight;
        if (position < windowHeight - 100) {
            el.classList.add('visible');
        }
    });
});

// Formulário de Contato (exemplo básico)
document.getElementById('contact-form').addEventListener('submit', (e) => {
    e.preventDefault();
    alert('Mensagem enviada com sucesso! (Este é um exemplo - configure um backend para envio real)');
    e.target.reset();
});