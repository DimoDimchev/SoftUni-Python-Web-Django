const urls = {
    'books': '/api/books',
};

const load = () => {
    fetch(urls.books)
        .then(response => response.json())
        .then(books => {
            const booksList = document.getElementsByClassName('books-list')[0];
            const booksListItems = books.map(book => `<li>${book.title}</li>`).join('');

            booksList.innerHTML = booksListItems;

        });
};

load();
