
function $(element) {
 return document.getElementById(element)
}

function $H(element) {
  return $(element).innerHTML
}

function test() {
  alert($H('test'))
}

test()
