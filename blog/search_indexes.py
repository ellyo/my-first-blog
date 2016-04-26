from django.utils import timezone
from haystack import indexes
from blog.models import Post


class PostIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.TextField(document=True, use_template=True)
    title = indexes.Charfield(model_attr='title')
    author = indexes.CharField(model_attr='user')
    published_date = indexes.DateTimeField(model_attr='published_date')

    def get_model(self):
        return Post

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(published_date__lte=datetime.datetime.now())
