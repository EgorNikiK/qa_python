from main import BooksCollector
import pytest

class TestBooksCollector:

    @pytest.fixture
    def collector(self):
        return BooksCollector()

    # Тесты для add_new_book
    def test_add_new_book_valid_name(self, collector):
        collector.add_new_book('Гарри Поттер')
        assert 'Гарри Поттер' in collector.books_genre

    @pytest.mark.parametrize('name', ['', 'a' * 41])
    def test_add_new_book_invalid_name(self, collector, name):
        collector.add_new_book(name)
        assert name not in collector.books_genre

    def test_add_new_book_duplicate(self, collector):
        collector.add_new_book('Гарри Поттер')
        collector.add_new_book('Гарри Поттер')
        assert len(collector.books_genre) == 1

    # Тесты для set_book_genre
    def test_get_book_genre_for_empty_genre(self, collector):
        collector.add_new_book('Книга без жанра')
        assert collector.get_book_genre('Книга без жанра') == ''


    def test_get_books_genre_returns_full_dict(self, collector):
        collector.add_new_book('Книга 1')
        collector.add_new_book('Книга 2')
        collector.set_book_genre('Книга 1', 'Фантастика')
        assert collector.get_books_genre() == {'Книга 1': 'Фантастика', 'Книга 2': ''}


    def test_set_book_genre_valid(self, collector):
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        assert collector.books_genre['Гарри Поттер'] == 'Фантастика'

    # Тесты для get_books_with_specific_genre
    def test_get_books_with_specific_genre(self, collector):
        collector.add_new_book('Гарри Поттер')
        collector.add_new_book('Властелин Колец')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        collector.set_book_genre('Властелин Колец', 'Фантастика')
        books = collector.get_books_with_specific_genre('Фантастика')
        assert len(books) == 2
        assert 'Гарри Поттер' in books
        assert 'Властелин Колец' in books

    # Тесты для get_books_for_children
    def test_get_books_for_children(self, collector):
        collector.add_new_book('Гарри Поттер')
        collector.add_new_book('Оно')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        collector.set_book_genre('Оно', 'Ужасы')
        children_books = collector.get_books_for_children()
        assert 'Гарри Поттер' in children_books
        assert 'Оно' not in children_books

    # Тесты для add_book_in_favorites
    def test_add_book_in_favorites(self, collector):
        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')
        assert 'Гарри Поттер' in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_twice(self, collector):
        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')
        assert len(collector.get_list_of_favorites_books()) == 1

    # Тесты для delete_book_from_favorites
    def test_delete_book_from_favorites(self, collector):
        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')
        collector.delete_book_from_favorites('Гарри Поттер')
        assert 'Гарри Поттер' not in collector.get_list_of_favorites_books()

    # Тесты для get_list_of_favorites_books
    def test_get_list_of_favorites_books(self, collector):
        collector.add_new_book('Гарри Поттер')
        collector.add_new_book('Властелин Колец')
        collector.add_book_in_favorites('Гарри Поттер')
        collector.add_book_in_favorites('Властелин Колец')
        favorites = collector.get_list_of_favorites_books()
        assert len(favorites) == 2
        assert 'Гарри Поттер' in favorites
        assert 'Властелин Колец' in favorites