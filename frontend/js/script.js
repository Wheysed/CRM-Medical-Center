document.addEventListener('DOMContentLoaded', function() {
    console.log('Сайт медицинской CRM загружен!');
    
    const header = document.querySelector('h1');
    if(header) {
        header.addEventListener('click', function() {
            this.style.color = this.style.color === 'blue' ? '#2c3e50' : 'blue';
        });
    }
    
    setTimeout(() => {
        alert('Добро пожаловать на сайт CRM для диагностического центра!');
    }, 500);
});
