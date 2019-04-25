from django.shortcuts import render, redirect, HttpResponse
from app01.models import Book, Publish, Author, User





# Create your views here.

# show all
def show(request):
    return render(request,'show.html')

# login
def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user_obj=User.objects.filter(name=username,password=password)
        if user_obj:
            request.session['username']=username
            request.session['password']=password

            return redirect('/show/')
    return render(request,'login.html')

# reg
def reg(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        repassword=request.POST.get('repassword')
        user_obj=User.objects.filter(name=username).exists()
        if user_obj:
            return HttpResponse('用户名已存在，请直接登录')
        else:
            new_user=User.objects.create(name=username,password=password)

        return redirect('/login/')
    return render(request,'reg.html')

# logout
def logout(request):
    request.session.flush()
    return redirect('/login/')

# 图书展示
def book_list(request):
    book_list = Book.objects.all()
    return render(request, 'book_list.html', {'book_list': book_list})


# 增加图书
def add_book(request):
    publish_list = Publish.objects.all()
    if request.method == 'POST':
        title = request.POST.get('title')
        new_book_publish = request.POST.get('new_book_publish')
        Book.objects.create(book_name=title, publish_id_id=new_book_publish)
        return redirect('/book_list')

    return render(request, 'add_book.html', {'publish_list': publish_list})


# 编辑书籍
def edit_book(request):
    if request.method == 'POST':
        edit_book_id = request.POST.get('id')
        edit_book_name = request.POST.get('name')
        edit_book_publish = request.POST.get('edit_book_publish')

        book_obj = Book.objects.get(id=edit_book_id)
        book_obj.book_name = edit_book_name
        book_obj.publish_id_id = edit_book_publish
        book_obj.save()
        return redirect('/book_list')

    edit_book_id = request.GET.get('id')
    book_object = Book.objects.get(id=edit_book_id)
    publish_list = Publish.objects.all()
    return render(request, 'edit_book.html', {'publish_list': publish_list, 'book_obj': book_object})


# 删除书籍
def del_book(request):
    del_id = request.GET.get('id')
    book_obj = Book.objects.get(id=del_id).delete()

    return redirect('/book_list')


# 作者列表
def author_list(request):
    author_list = Author.objects.all()
    return render(request, 'author_list.html', {'author_list': author_list})


# 增加作者
def add_author(request):
    if request.method == 'POST':
        author_name = request.POST.get('author_name')
        author_books = request.POST.getlist('books')
        author_obj = Author.objects.create(name=author_name)
        # 多对多的插入数据库方法
        author_obj.books.set(author_books)
        return redirect('/author_list/')
    book_list = Book.objects.all()
    return render(request, 'add_author.html', {'book_list': book_list})


# 删除作者
def del_author(request):
    author_id = request.GET.get('id')
    Author.objects.get(id=author_id).delete()
    return redirect('/author_list/')


# 编辑作者
def edit_author(request):
    if request.method == 'POST':
        author_id = request.POST.get('author_id')
        author_name = request.POST.get('author_name')
        author_books = request.POST.getlist('books')
        author_obj = Author.objects.get(id=author_id)

        author_obj.name = author_name
        author_obj.save()

        author_obj.books.set(author_books)
        return redirect('/author_list/')

    book_list = Book.objects.all()
    edit_author_id = request.GET.get('id')
    author_obj = Author.objects.get(id=edit_author_id)
    return render(request, 'edit_author.html', {'book_list': book_list, 'author_obj': author_obj})


# 展示出版社
def publish_list(request):
    publish_list = Publish.objects.all()
    return render(request, 'publish_list.html', {'publish_list': publish_list})


# 增加爱出版社
def add_publish(request):
    if request.method == 'POST':
        publish_id = request.POST.get('id')
        publish_name = request.POST.get('publish_name')
        Publish.objects.create(id=publish_id, name=publish_name)
        return redirect('/publish_list/')
    return render(request, 'add_publish.html')


# 编辑出版社
def edit_publish(request):
    if request.method == 'POST':
        edit_id = request.POST.get('publish_id')
        edit_name = request.POST.get('publish_name')
        publish_obj = Publish.objects.get(id=edit_id)
        publish_obj.name = edit_name
        publish_obj.save()
        return redirect('/publish_list/')

    # publish_list=Publish.objects.all()
    publish_edit_id = request.GET.get('id')
    publish_edit_obj = Publish.objects.get(id=publish_edit_id)
    return render(request, 'edit_publish.html', {'publish_edit_obj': publish_edit_obj})


# 删除出版社
def del_publish(request):
    del_id=request.GET.get('id')
    Publish.objects.get(id=del_id).delete()
    return redirect('/publish_list/')
