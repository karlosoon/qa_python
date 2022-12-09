# qa_python

 # Тест на невозможность добавить дубликат книги в словарь books_rating
def test_add_new_book_add_duplicate_not_added(self, book_collector):

 # Позитивный тест на изменение рейтинга (изменили рейтинг на 1-10 - рейтинг изменился)
def test_set_book_rating_set_correct_rating_rating_changed(self, book_collector):

 # Негативный тест на изменение рейтинга (изменили рейтинг на 11 - рейтинг не изменился)
def test_set_book_rating_set_incorrect_rating_rating_not_changed(self, book_collector):

 # Тест на получение рейтинга книги по имени
def test_get_book_rating_book_added_return_rating(self, book_collector):

 # Тест на получение рейтинга недобавленной книги
def test_get_book_rating_book_not_added_return_none(self, book_collector):

 # Тест на изменение рейтинга недобавленной книги
def test_set_book_rating_book_not_added_rating_is_none(self, book_collector):

 # Тест на добавление книги в избранное
def test_add_book_in_favorites_add_existing_book(self, book_collector):

 # Тест на добавление в избранное книги, которой нет в books_rating
def test_add_book_in_favorites_add_not_existing_book(self, book_collector):

 # Тест на удаление книги из избранного
def test_delete_book_from_favorites_book_deleted(self, book_collector):
 
 # Тест на невозможность добавить дубликат в избранное
def test_add_book_in_favorites_duplicate_not_added(self, book_collector):

 # Тест метода init - у экземпляра класса атрибут books_rating == {}
def test_init_books_rating_is_dict(self, book_collector):

 # Тест метода init - у экземпляра класса атрибут favorites == []
def test_init_favourites_is_list(self, book_collector):

 # Тест на получение списка книг с определенным рейтингом
def test_get_books_with_specific_rating_return_not_empty_list(self, book_collector):

 # Тест на получение пустого списка при попытке получить книги по рейтингу больше 10
def test_get_books_with_specific_rating_out_of_range_rating_return_empty_list(self, book_collector):

