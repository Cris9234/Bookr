from django.db import models
from django.contrib import auth


class Publisher(models.Model):
    """A company that publishes books"""
    name = models.CharField(max_length=50, help_text="The name of the Publisher.")
    website = models.URLField(help_text="The publisher website.")
    email = models.EmailField(help_text="The Publisher's email address.")

    def __init__(self):
        return self.name


class Book(models.Model):
    """A published book."""
    title = models.CharField(max_length=70, help_text="The title of the book.")
    publication_date = models.DateField(verbose_name="Date the book was published.")
    isbn = models.CharField(max_length=20, verbose_name="ISBN number of the book.")
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    contributors = models.ManyToManyField('Contributor', through="BookContributor")

    def __init__(self):
        return self.title


class Contributor(models.Model):
    """A contributor to a book, e.g. author, editor, co-author"""
    first_name = models.CharField(max_length=50, help_text="The contributor's first name or names")
    last_name = models.CharField(max_length=50, help_text="The contributor's first last name or names")
    email = models.EmailField(help_text="The contact email for the contributor")

    def __init__(self):
        return self.first_name


class BookContributor(models.Model):
    class ContributionRole(models.TextChoices):
        AUTHOR = "AUTHOR", "Author"
        CO_AUTHOR = "CO_AUTHOR", "Co-Author"
        EDITOR = "EDITOR", "Editor"

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    contributor = models.ForeignKey(Contributor, on_delete=models.CASCADE)
    role = models.CharField(verbose_name="The role this contributor had in te book", choices=ContributionRole.choices,
                            max_length=20)


class Review(models.Model):
    content = models.TextField(help_text="The Review text.")
    rating = models.IntegerField(help_text="The rating the reviewer has given.")
    date_created = models.DateField(auto_now_add=True, help_text="The date and time the review was created.")
    date_editing = models.DateField(null=True, help_text="The date and time the review was last edited.")
    creator = models.ForeignKey(auth.get_user_model(), on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, help_text="The book that this review in for.")
