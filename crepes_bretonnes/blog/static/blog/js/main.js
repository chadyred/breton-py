test()

function xhrSend(e) {
  var myForm = document.getElementsByTagName('form');
  var form = new FormData(myForm);

  console.log(form);
  var content = e.target.innerHTML
  var idArticle = e.target.getAttribute('data-id-article');

  var url = 'http://localhost:8000/blog/article/edit/' + idArticle + '/json'
  var csrf = document.querySelector('input[name="csrfmiddlewaretoken');
  var token = csrf.getAttribute('value');

  xhr = new XMLHttpRequest()

  xhr.open('POST', url );
  xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
  xhr.setRequestHeader("X-CSRFToken", token);

  xhr.addEventListener('readystatechange', function () {

     if (xhr.readyState == XMLHttpRequest.DONE && (xhr.status == 200 ||xhr.status == 0)) {
          alert("Data receive, DONE");

          var result = JSON.parse(xhr.responseText)

          console.log(result)

     } else if (xhr.readyState === XMLHttpRequest.DONE && xhr.status != 200) { // En cas d'erreur !



        alert('Une erreur est survenue !\n\nCode :' + xhr.status + '\nTexte : ' + xhr.statusText);


    }
  });

  // xhr.send('titre='+ titre + '&image'+ image + '&categorie'+ categorie + '&auteur'+ auteur + '&contenu=' + content + '&csrfmiddlewaretoken=' + token);
  xhr.send(form);
}

// blur : évènement natif émis et que l'on observe afin de pouvoir exécuter une fonction au changement de "focus" (touché tab lors de l'édition par exemple)
$('test').addEventListener("blur", xhrSend, false)
$('test').spellcheck = 'true'

