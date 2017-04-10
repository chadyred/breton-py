function xhrSend(e) {
  // On recupère le formulaire
  var myForm = document.querySelector('form');

  // On utilise le formdata pour le maper
  var form = new FormData(myForm);

  // On récupère le conteu de notre champ ContentEditable
  var content = e.target.innerHTML;

  alert(content)
  // On récupère l'id de l'article cible.s
  var idArticle = e.target.getAttribute('data-id-article');

  var url = 'http://localhost:8000/blog/article/edit/' + idArticle + '/json'
  var csrf = document.querySelector('input[name="csrfmiddlewaretoken');

  // Egalement récupérable dans le cookie si ce champs n'est pas présent.
  // form.append("csrfmiddlewaretoken",getCookie('csrftoken'));
  var token = csrf.getAttribute('value');

  xhr = new XMLHttpRequest()

  xhr.open('POST', url );

  // Nécessaire pour un envoie en json des élément afin qu'il soit encodé, ATTENTION lENCODAGE DE BASE EST GOOD, PAS BESON DE CELA !
  // SUREMENT DE FormData qui réalise cela

  // xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");

  // Token nécessaire dans l'URL afin que l'utilisation fait par Django soit effectif
  xhr.setRequestHeader("X-CSRFToken", token);

  // Nécessité afin de préciser qu'il s'agit d'une requête AJAX, utile pour le check.
  xhr.setRequestHeader("X-Requested-With", "XMLHttpRequest");

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
  // On le place dans le formulaire en remplacant ce dernier ICI APRES L'EVENT, SANS QUOI LA VALEUR NE SERA PAS MODIFIER
  form.set('contenu', content);
  xhr.send(form);
}

if ($('test') != null) {
  // blur : évènement natif émis et que l'on observe afin de pouvoir exécuter une fonction au changement de "focus" (touché tab lors de l'édition par exemple)
  $('test').addEventListener("blur", xhrSend, false)
  $('test').spellcheck = 'true'
}

// Utilisation du Webstorage
localStorage.setItem('fuck', 'me');
sessionStorage.setItem('fuck', 'me');

console.log(localStorage.getItem('fuck'));
console.log(sessionStorage.getItem('fuck'));
