import datetime
import re
import markdown

from django import forms

from models import Article


class ArticlePublishForm(forms.Form):
    title = forms.CharField(
        label=u'title',
        max_length=50,
        widget=forms.TextInput(attrs={'class': '', 'placeholder': u'title, remember to add at the end of title".html"'}),
        )

    content = forms.CharField(
        label=u'content',
        min_length=10,
        widget=forms.Textarea(),
        )

    tags = forms.CharField(
        label=u'tag',
        max_length=30,
        widget=forms.TextInput(attrs={'class': '', 'placeholder': u'tag'}),
        )

    def save(self, username):
        cd = self.cleaned_data
        title = cd['title']
        title_zh = title
        now = datetime.datetime.now()
        content_md = cd['content']
        content_html = markdown.markdown(cd['content'])
        re_title = '<h\d>(.+)</h\d>'
        data = content_html.split('\n')
        for line in data:
            title_info = re.findall(re_title, line)
            if title_info:
                title_zh = title_info[0]
                break
        url = '/article/%s' % (title)
        tags = cd['tags']
        article = Article(
            url=url,
            title=title,
            author=username,
            content_md=content_md,
            content_html=content_html,
            tags=tags,
            views=0,
            created=now,
            updated=now)
        article.save()