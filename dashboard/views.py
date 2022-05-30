from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from dashboard.decorators import logout_required
from core.models import SpecialTechnique, SpecialTechniqueCategory, Factory, Contact, FactoryApplication
from dashboard.form import STForm, STCForm, BlogForm, FactoryForm, ArticleForm
from blog.models import Blog, Article
from django.core.paginator import Paginator


@logout_required
def login_admin(request):
    if request.method == "POST":
        phone = request.POST.get("phone")
        password = request.POST.get("password")
        user = authenticate(phone=phone, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect("dashboard:st")
    return render(request, "dashboard/login.html")


@login_required(login_url='dashboard:login')
def logout_admin(request):
    logout(request)
    return redirect("/")


@login_required(login_url='dashboard:login')
def home(request):
    ctx = {
        "st": SpecialTechnique.objects.count(),
        "stc": SpecialTechniqueCategory.objects.count(),
        "f": Factory.objects.count(),
        "c": Contact.objects.count(),
        "a": Article.objects.count(),
        "b": Blog.objects.count()
    }
    return render(request, 'dashboard/home.html', context=ctx)


@login_required(login_url='dashboard:login')
def st(request):
    queryset = SpecialTechnique.objects.all()
    paginator = Paginator(queryset, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'dashboard/st.html', context={"queryset": queryset, 'page_obj': page_obj})


@login_required(login_url='dashboard:login')
def create_st(request):
    form = STForm()
    if request.method == 'POST':
        form = STForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard:st')

    context = {'form': form}
    return render(request, 'dashboard/create/createSt.html', context)


@login_required(login_url='dashboard:login')
def update_st(request, pk):
    query = SpecialTechnique.objects.get(id=pk)
    form = STForm(instance=query)

    if request.method == 'POST':
        form = STForm(request.POST, instance=query, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard:st')

    context = {'form': form, 'item': query}
    return render(request, 'dashboard/update/updateSt.html', context)


@login_required(login_url='dashboard:login')
def delete_st(request, pk):
    queryset = SpecialTechnique.objects.get(id=pk)
    if request.method == "POST":
        queryset.delete()
        return redirect('/')

    return render(request, 'dashboard/delete/deleteSt.html', context={'item': queryset})


@login_required(login_url='dashboard:login')
def specialtechniquecategory(request):
    queryset = SpecialTechniqueCategory.objects.all()
    paginator = Paginator(queryset, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'dashboard/stc.html', context={"queryset": queryset, 'page_obj': page_obj})


@login_required(login_url='dashboard:login')
def create_stc(request):
    form = STCForm()
    if request.method == 'POST':
        form = STCForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard:stc')

    context = {'form': form}
    return render(request, 'dashboard/create/createStc.html', context)


@login_required(login_url='dashboard:login')
def update_stc(request, pk):
    query = SpecialTechniqueCategory.objects.get(id=pk)
    form = STCForm(instance=query)

    if request.method == 'POST':
        form = STCForm(request.POST, instance=query, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard:stc')

    context = {'form': form, 'item': query}
    return render(request, 'dashboard/update/updateStc.html', context)


@login_required(login_url='dashboard:login')
def delete_stc(request, pk):
    query = SpecialTechniqueCategory.objects.get(id=pk)
    if request.method == "POST":
        query.delete()
        return redirect('dashboard:stc')

    return render(request, 'dashboard/delete/deleteStc.html', context={'item': query})


@login_required(login_url='dashboard:login')
def factory(request):
    queryset = Factory.objects.all()
    paginator = Paginator(queryset, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'dashboard/factory.html', context={"queryset": queryset, 'page_obj': page_obj})


@login_required(login_url='dashboard:login')
def create_factory(request):
    form = FactoryForm()
    if request.method == 'POST':
        form = FactoryForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard:factory')

    context = {'form': form}
    return render(request, 'dashboard/create/createFactory.html', context)


@login_required(login_url='dashboard:login')
def update_factory(request, pk):
    query = Factory.objects.get(id=pk)
    form = FactoryForm(instance=query)

    if request.method == 'POST':
        form = FactoryForm(request.POST, instance=query, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard:factory')

    context = {'form': form, 'item': query}
    return render(request, 'dashboard/update/updateFactory.html', context)


@login_required(login_url='dashboard:login')
def delete_factory(request, pk):
    query = Factory.objects.get(id=pk)
    if request.method == "POST":
        query.delete()
        return redirect('dashboard:factory')

    return render(request, 'dashboard/delete/deleteFactory.html', context={'item': query})


@login_required(login_url='dashboard:login')
def delete_factoryapp(request, pk):
    query = FactoryApplication.objects.get(id=pk)
    if request.method == "POST":
        query.delete()
        return redirect('dashboard:factoryapp')

    return render(request, 'dashboard/delete/deleteFactoryapp.html', context={'item': query})


@login_required(login_url='dashboard:login')
def blogs(request):
    queryset = Blog.objects.all()
    paginator = Paginator(queryset, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'dashboard/blog.html', context={"queryset": queryset, 'page_obj': page_obj})


@login_required(login_url='dashboard:login')
def create_blog(request):
    form = BlogForm()
    if request.method == 'POST':
        form = BlogForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard:blog')

    context = {'form': form}
    return render(request, 'dashboard/create/createBlog.html', context)


@login_required(login_url='dashboard:login')
def update_blog(request, pk):
    query = Blog.objects.get(id=pk)
    form = BlogForm(instance=query)

    if request.method == 'POST':
        form = BlogForm(request.POST, instance=query, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard:blog')

    context = {'form': form, 'item': query}
    return render(request, 'dashboard/update/updateBlog.html', context)


@login_required(login_url='dashboard:login')
def delete_blog(request, pk):
    query = Blog.objects.get(id=pk)
    if request.method == "POST":
        query.delete()
        return redirect('dashboard:blog')

    return render(request, 'dashboard/delete/deleteBlog.html', context={'item': query})


@login_required(login_url='dashboard:login')
def contact(request):
    queryset = Contact.objects.all()
    paginator = Paginator(queryset, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'dashboard/contact.html', context={"queryset": queryset, 'page_obj': page_obj})


@login_required(login_url='dashboard:login')
def article(request):
    queryset = Article.objects.all()
    paginator = Paginator(queryset, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'dashboard/article.html', context={"queryset": queryset, 'page_obj': page_obj})


@login_required(login_url='dashboard:login')
def create_article(request):
    form = ArticleForm()
    if request.method == 'POST':
        form = ArticleForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard:article')

    context = {'form': form}
    return render(request, 'dashboard/create/createArticle.html', context)


@login_required(login_url='dashboard:login')
def update_article(request, pk):
    query = Article.objects.get(id=pk)
    form = ArticleForm(instance=query)

    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=query, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard:article')

    context = {'form': form, 'item': query}
    return render(request, 'dashboard/update/updateArticle.html', context)


@login_required(login_url='dashboard:login')
def delete_article(request, pk):
    query = Article.objects.get(id=pk)
    if request.method == "POST":
        query.delete()
        return redirect('dashboard:article')

    return render(request, 'dashboard/delete/deleteArticle.html', context={'item': query})
