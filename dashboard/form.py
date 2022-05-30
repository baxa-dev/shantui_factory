from django.forms import ModelForm
from core.models import SpecialTechnique, SpecialTechniqueCategory, Factory, Contact, FactoryApplication
from blog.models import Blog, Article


class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = "__all__"


class STForm(ModelForm):
    class Meta:
        model = SpecialTechnique
        fields = '__all__'


class STCForm(ModelForm):
    class Meta:
        model = SpecialTechniqueCategory
        fields = '__all__'


class FactoryForm(ModelForm):
    class Meta:
        model = Factory
        fields = '__all__'


class FactoryappForm(ModelForm):
    class Meta:
        model = FactoryApplication
        fields = '__all__'
        

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


