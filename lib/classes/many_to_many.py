class Author:
    def __init__(self, name):
        # Validate and set the author's name
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string")
        self._name = name
        self._articles = []  # Initialize an empty list for articles

    @property
    def name(self):
        # Return the author's name
        return self._name

    def articles(self):
        # Return the list of articles by the author
        return self._articles

    def magazines(self):
        # Return unique magazines the author has written for
        return list(set(article.magazine for article in self._articles))

    def add_article(self, magazine, title):
        # Create and return a new article
        return Article(self, magazine, title)

    def topic_areas(self):
        # Return unique topic areas based on the author's articles
        topic_areas = {article.magazine.category for article in self._articles}
        return list(topic_areas) if topic_areas else None


class Magazine:
    _all_magazines = []  # Class variable to store all magazines

    def __init__(self, name, category):
        # Validate and set the magazine's name and category
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Magazine name must be a string between 2 and 16 characters")
        if not isinstance(category, str) or not category:
            raise ValueError("Category must be a non-empty string")
        self._name = name
        self._category = category
        self._articles = []  # Initialize an empty list for articles
        Magazine._all_magazines.append(self)  # Add to all magazines list

    @property
    def name(self):
        # Return the magazine's name
        return self._name

    @name.setter
    def name(self, value):
        # Validate and set the magazine's name
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise ValueError("Magazine name must be between 2 and 16 characters")
        self._name = value

    @property
    def category(self):
        # Return the magazine's category
        return self._category

    @category.setter
    def category(self, value):
        # Validate and set the magazine's category
        if not value or not isinstance(value, str):
            raise ValueError("Category must be a non-empty string")
        self._category = value

    def articles(self):
        # Return the list of articles in the magazine
        return self._articles

    def contributors(self):
        # Return unique authors who contributed to the magazine
        return list({article.author for article in self._articles})

    def article_titles(self):
        # Return titles of articles in the magazine
        return [article.title for article in self._articles] if self._articles else None

    def add_article(self, author, title):
        # Validate and add a new article to the magazine
        if not isinstance(author, Author) or not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Invalid author or title")
        article = Article(author, self, title)
        self._articles.append(article)  # Add article to magazine's list
        return article

    def contributing_authors(self):
        # Count authors with more than 2 articles in the magazine
        author_counts = {}
        for article in self.articles():
            author = article.author
            author_counts[author] = author_counts.get(author, 0) + 1

        # Return authors with multiple articles
        authors_with_multiple_articles = [author for author, count in author_counts.items() if count > 2]
        return authors_with_multiple_articles if authors_with_multiple_articles else None


class Article:
    all_articles = []  # Class variable to store all articles

    def __init__(self, author, magazine, title):
        # Validate and set the article's author, magazine, and title
        if not isinstance(author, Author) or not isinstance(magazine, Magazine) or not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Invalid author, magazine, or title")

        self._author = author
        self._magazine = magazine
        self._title = title
        Article.all_articles.append(self)  # Add article to all articles list
        author._articles.append(self)  # Add article to author's list
        magazine._articles.append(self)  # Add article to magazine's list

    @property
    def title(self):
        # Return the article's title
        return self._title

    @property
    def author(self):
        # Return the article's author
        return self._author

    @property
    def magazine(self):
        # Return the article's magazine
        return self._magazine

    @classmethod
    def all(cls):
        # Return all articles
        return cls.all_articles