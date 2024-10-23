$(document).ready(function(){
    $('.mobile-btn').on('click', function(){
        $('.mobile-menu').toggleClass('active');
        $('.mobile-btn').find('i').toggleClass('fa-x')
    });
});

// html = document
// quando clicar na função, ira ativar o "mobile-menu", mudando o icone pra "fa-x"(x)