function goBack() {
    window.history.back();
}

// ...existing code...

function validateForm() {
    // Pega os valores dos campos
    const bookName = document.getElementById('bookName').value.trim();
    const author = document.getElementById('author').value.trim();
    const publisher = document.getElementById('publisher').value.trim();
    const date = document.getElementById('date').value.trim();

    // Array para mensagens de erro
    let errors = [];

    // Validações
    if (bookName === '') {
        errors.push('Nome do livro é obrigatório');
        document.getElementById('bookName').style.borderColor = 'red';
    }

    if (author === '') {
        errors.push('Autor é obrigatório');
        document.getElementById('author').style.borderColor = 'red';
    }

    if (publisher === '') {
        errors.push('Editora é obrigatória');
        document.getElementById('publisher').style.borderColor = 'red';
    }

    if (date === '') {
        errors.push('Data é obrigatória');
        document.getElementById('date').style.borderColor = 'red';
    }

    // Se houver erros, mostra as mensagens
    if (errors.length > 0) {
        alert(errors.join('\n'));
        return false;
    }

    // Se passar nas validações, reseta as bordas e continua
    resetBorders();
    alert('Livro adicionado com sucesso!');

     // Se passar nas validações, adiciona o livro
    const newBookId = addBook(bookName, author, publisher, date);
    alert(`Livro adicionado com sucesso!\nID do livro: ${newBookId}`);
    return true;
    
}

function addBook(bookName, author, publisher, date) {
    lastBookId++; // Increment the ID counter
    
    // Cria objeto do livro
    const book = {
        id: lastBookId,
        name: bookName,
        author: author,
        publisher: publisher,
        date: date
    };

    // Adiciona ao array de livros
    books.push(book);

    // Salva no localStorage (incluindo o lastBookId)
    localStorage.setItem('books', JSON.stringify(books));
    localStorage.setItem('lastBookId', lastBookId);

    // Limpa o formulário
    clearForm();

    return lastBookId; // Return the generated ID
}

// Carrega livros salvos quando a página é carregada
window.onload = function() {
    const savedBooks = localStorage.getItem('books');
    const savedLastId = localStorage.getItem('lastBookId');
    
    if (savedBooks) {
        books = JSON.parse(savedBooks);
    }
    
    if (savedLastId) {
        lastBookId = parseInt(savedLastId);
    }
};

function resetBorders() {
    const inputs = document.querySelectorAll('.input-style');
    inputs.forEach(input => {
        input.style.borderColor = 'rgba(255, 255, 255, 0.1)';
    });
}