from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_rating()) == 2

    def test_add_new_book_add_duplicate_not_added(self, book_collector):
        book_collector.add_new_book('x')
        book_collector.add_new_book('x')
        assert len(book_collector.get_books_rating()) == 1

    def test_set_book_rating_set_correct_rating_rating_changed(self, book_collector):
        book_collector.add_new_book('x')
        book_collector.set_book_rating('x', 5)
        books_rating = book_collector.get_books_rating()
        assert books_rating['x'] == 5

    def test_set_book_rating_set_incorrect_rating_rating_not_changed(self, book_collector):
        book_collector.add_new_book('x')
        book_collector.set_book_rating('x', 11)
        books_rating = book_collector.get_books_rating()
        assert books_rating['x'] == 1

    def test_get_book_rating_book_added_return_rating(self, book_collector):
        book_collector.add_new_book('x')
        assert book_collector.get_book_rating('x') == 1

    def test_get_book_rating_book_not_added_return_none(self, book_collector):
        assert book_collector.get_book_rating('x') is None

    def test_set_book_rating_book_not_added_rating_is_none(self, book_collector):
        book_collector.set_book_rating('x', 5)
        assert book_collector.get_book_rating('x') is None

    def test_add_book_in_favorites_add_existing_book(self, book_collector):
        book_collector.add_new_book('x')
        book_collector.add_book_in_favorites('x')
        assert len(book_collector.get_list_of_favorites_books()) == 1

    def test_add_book_in_favorites_add_not_existing_book(self, book_collector):
        book_collector.add_book_in_favorites('x')
        assert len(book_collector.get_list_of_favorites_books()) == 0

    def test_delete_book_from_favorites_book_deleted(self, book_collector):
        book_collector.add_new_book('x')
        book_collector.add_new_book('y')
        book_collector.add_book_in_favorites('x')
        book_collector.add_book_in_favorites('y')
        book_collector.delete_book_from_favorites('x')
        assert len(book_collector.get_list_of_favorites_books()) == 1

    def test_add_book_in_favorites_duplicate_not_added(self, book_collector):
        book_collector.add_new_book('x')
        book_collector.add_book_in_favorites('x')
        book_collector.add_book_in_favorites('x')
        assert len(book_collector.get_list_of_favorites_books()) == 1

    def test_init_books_rating_is_dict(self, book_collector):
        assert book_collector.books_rating == {}

    def test_init_favorites_is_list(self, book_collector):
        assert book_collector.favorites == []

    def test_get_books_with_specific_rating_return_not_empty_list(self, book_collector):
        book_collector.add_new_book('x')
        book_collector.set_book_rating('x', 10)
        rating_10_books = book_collector.get_books_with_specific_rating(10)
        assert len(rating_10_books) == 1

    def test_get_books_with_specific_rating_out_of_range_rating_return_empty_list(self, book_collector):
        book_collector.add_new_book('x')
        rating_11_books = book_collector.get_books_with_specific_rating(11)
        assert rating_11_books == []
