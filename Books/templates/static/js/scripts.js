window.onload = initAll;

let saveBookButton;
function initAll(){
    saveBookButton = document.getElementById('save');
    saveBookButton.onclick = saveBook;
}

function saveBook(){

    let title = document.getElementById('title_js').value;
    let cover = document.getElementById('cover_js').value;
    let author = document.getElementById('author_js').value;
    let pages = document.getElementById('pages_js').value;
    let url = '/add_book?title='+title+'&cover='+cover+'&pages='+pages+'&author='+author
    var req = new XMLHttpRequest();
    req.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
          alert(req.responseText);  
        }
    };
    req.open("GET", url, true);
    req.send();

}