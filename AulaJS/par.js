const prompt = require("prompt-sync")();

let numero = parseInt(prompt("digite um numero: "));
if (numero % 2 === 0) {
    console.log(numero + " é par.");
}
else {
    console.log(numero + " é ímpar.");
}


