function iniciarContagemRegressiva(segundos) {
  let timer = setInterval(function() {
      console.log(segundos);
      segundos--;
      if (segundos < 0) {
          clearInterval(timer);
          console.log('Tempo esgotado!');
      }
  }, 1000);
}

iniciarContagemRegressiva(10); // Inicia uma contagem regressiva de 10 segundos
