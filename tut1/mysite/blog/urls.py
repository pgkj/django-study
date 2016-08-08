from django.conf.urls import url
from views import blog_test
from views import ArticleListView
from views import ArticlePublishView

urlpatterns = [
	# url(r'^$', views.blog_index, name="blog_index"),
	url(r'^$', ArticleListView.as_view(), name="blog_index"),
	url(r'^testing$', blog_test, name="for_test"),
	url(r'^article/publish$', ArticlePublishView.as_view(), name="article_publish"),

]