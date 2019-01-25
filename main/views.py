from django.shortcuts import render, redirect
from django.template import Template, Context
from django.http import HttpResponse
from main.models import Section,PageLayout,Post,PostComment,HomePage
from main.forms import *
# Create your views here.
def index(request):
    current_user = request.user
    home_page = HomePage.objects.first()
    if home_page is None:
        return render(request, 'main/404.html')
    if not (current_user.is_anonymous or not (current_user.is_superuser or current_user.is_staff or current_user.profile.moderator)) and request.method == 'POST':
        if request.POST.get('add_page_layout'): 
            form = PageLayoutForm(request.POST)
            if form.is_valid():
                page_layout = form.save(commit=False)
                page_layout.home_page = home_page
                page_layout.save()
        if request.POST.get('add_post') and request.POST.get('page_layout_id'):
            form = PostForm(request.POST)
            if form.is_valid():
                page_layout = PageLayout.objects.get(id=request.POST.get('page_layout_id'))
                if page_layout != None:
                    post = form.save(commit=False)
                    post.parent = page_layout
                    post.save()
        if request.POST.get('edit_post') and request.POST.get('post_id'):
            post = Post.objects.get(id=request.POST.get('post_id'))
            if post != None:
                form = PostForm(request.POST,instance=post)
                if form.is_valid():
                    post = form.save(commit=False)
                    post.edited = True
                    post.save()
        if request.POST.get('delete_post') and request.POST.get('post_id'):
            post = Post.objects.get(id=request.POST.get('post_id'))    
            post.deleted = True
            post.save()
        if request.POST.get('edit_page_layout') and request.POST.get('page_layout_id'):
            page_layout = PageLayout.objects.get(id=request.POST.get('page_layout_id'))
            if page_layout != None:
                form = PageLayoutEditForm(request.POST,instance=page_layout)
                if form.is_valid():
                    form.save()
        if request.POST.get('delete_page_layout') and request.POST.get('page_layout_id'):
            pageLayout = PageLayout.objects.get(id=request.POST.get('page_layout_id'))    
            pageLayout.deleted = True
            pageLayout.save()
    if not current_user.is_anonymous: 
        if request.POST.get('add_comment') and request.POST.get('post_id'):
            form = PostCommentForm(request.POST)
            if form.is_valid():
                post = Post.objects.get(id=request.POST.get('post_id'))
                if post != None:
                    comment = form.save(commit=False)
                    comment.post = post
                    comment.user = current_user
                    comment.save()
        if request.POST.get('edit_comment') and request.POST.get('comment_id'):
            comment = PostComment.objects.get(id=request.POST.get('comment_id'))
            if comment != None and comment.user == current_user:
                form = PostCommentForm(request.POST,instance=comment)
                if form.is_valid():
                    comm = form.save(commit=False)
                    comm.edited = True
                    comm.save()
        if request.POST.get('delete_comment') and request.POST.get('comment_id'):
            comment = PostComment.objects.get(id=request.POST.get('comment_id'))
            if comment != None and comment.user == current_user:
                comment.deleted = True
                comment.save()                    
    pageLayouts = PageLayout.objects.filter(home_page=home_page,deleted=False).order_by('order_number','id')
    for pageLayout in pageLayouts:
        if pageLayout.content_type.name == 'post':
            posts = Post.objects.filter(parent=pageLayout,deleted=False).order_by('id')
            for post in posts:
                comments = PostComment.objects.filter(post=post,deleted=False).order_by('id')
                editForm = PostForm(instance = post,auto_id=str(post.id)+'_post_id_for_%s')
                post.editForm = editForm
                for comment in comments:
                    if current_user == comment.user:
                        commentEditForm = PostCommentForm(instance=comment,auto_id=str(comment.id)+'_edit_comment_%s')
                        comment.editForm = commentEditForm
                post.addCommentForm = PostCommentForm(auto_id=str(post.id)+'_add_comment_%s')
                post.comments = comments
            pageLayout.posts = posts            
            pageLayout.addPostForm = PostForm(auto_id=str(pageLayout.id)+'_add_post_%s')
        pageLayout.editForm = PageLayoutEditForm(instance=pageLayout,auto_id=str(pageLayout.id)+'_edit_page_layout_%s')
    pageLayouts.addForm = PageLayoutForm()
    pageLayoutForm = PageLayoutForm
    return render(request, 'main/custom_page.html', {
        'section':home_page,
        'pageLayouts':pageLayouts
    })

def section_view(request, section_url):
    current_user = request.user
    section = Section.objects.filter(url=section_url).order_by('id').first()
    if section is None:
        #return redirect('main_index')
        return render(request, 'main/404.html')
    if section.restricted is True and current_user.is_anonymous:
        return render(request, 'main/restricted.html')
    if not (current_user.is_anonymous or not (current_user.is_superuser or current_user.is_staff or current_user.profile.moderator)) and request.method == 'POST':
        if request.POST.get('add_page_layout'): 
            form = PageLayoutForm(request.POST)
            if form.is_valid():
                page_layout = form.save(commit=False)
                page_layout.section = section
                page_layout.save()
        if request.POST.get('add_post') and request.POST.get('page_layout_id'):
            form = PostForm(request.POST)
            if form.is_valid():
                page_layout = PageLayout.objects.get(id=request.POST.get('page_layout_id'))
                if page_layout != None:
                    post = form.save(commit=False)
                    post.parent = page_layout
                    post.save()
        if request.POST.get('edit_post') and request.POST.get('post_id'):
            post = Post.objects.get(id=request.POST.get('post_id'))
            if post != None:
                form = PostForm(request.POST,instance=post)
                if form.is_valid():
                    post = form.save(commit=False)
                    post.edited = True
                    post.save()
        if request.POST.get('delete_post') and request.POST.get('post_id'):
            post = Post.objects.get(id=request.POST.get('post_id'))    
            post.deleted = True
            post.save()
        if request.POST.get('edit_page_layout') and request.POST.get('page_layout_id'):
            page_layout = PageLayout.objects.get(id=request.POST.get('page_layout_id'))
            if page_layout != None:
                form = PageLayoutEditForm(request.POST,instance=page_layout)
                if form.is_valid():
                    form.save()
        if request.POST.get('delete_page_layout') and request.POST.get('page_layout_id'):
            pageLayout = PageLayout.objects.get(id=request.POST.get('page_layout_id'))    
            pageLayout.deleted = True
            pageLayout.save()
    if not current_user.is_anonymous: 
        if request.POST.get('add_comment') and request.POST.get('post_id'):
            form = PostCommentForm(request.POST)
            if form.is_valid():
                post = Post.objects.get(id=request.POST.get('post_id'))
                if post != None:
                    comment = form.save(commit=False)
                    comment.post = post
                    comment.user = current_user
                    comment.save()
        if request.POST.get('edit_comment') and request.POST.get('comment_id'):
            comment = PostComment.objects.get(id=request.POST.get('comment_id'))
            if comment != None and comment.user == current_user:
                form = PostCommentForm(request.POST,instance=comment)
                if form.is_valid():
                    comm = form.save(commit=False)
                    comm.edited = True
                    comm.save()
        if request.POST.get('delete_comment') and request.POST.get('comment_id'):
            comment = PostComment.objects.get(id=request.POST.get('comment_id'))
            if comment != None and comment.user == current_user:
                comment.deleted = True
                comment.save()                    
    pageLayouts = PageLayout.objects.filter(section=section,deleted=False).order_by('order_number','id')
    for pageLayout in pageLayouts:
        if pageLayout.content_type.name == 'post':
            posts = Post.objects.filter(parent=pageLayout,deleted=False).order_by('id')
            for post in posts:
                comments = PostComment.objects.filter(post=post,deleted=False).order_by('id')
                editForm = PostForm(instance = post,auto_id=str(post.id)+'_post_id_for_%s')
                post.editForm = editForm
                for comment in comments:
                    if current_user == comment.user:
                        commentEditForm = PostCommentForm(instance=comment,auto_id=str(comment.id)+'_edit_comment_%s')
                        comment.editForm = commentEditForm
                post.addCommentForm = PostCommentForm(auto_id=str(post.id)+'_add_comment_%s')
                post.comments = comments
            pageLayout.posts = posts            
            pageLayout.addPostForm = PostForm(auto_id=str(pageLayout.id)+'_add_post_%s')
        pageLayout.editForm = PageLayoutEditForm(instance=pageLayout,auto_id=str(pageLayout.id)+'_edit_page_layout_%s')
    pageLayouts.addForm = PageLayoutForm()
    pageLayoutForm = PageLayoutForm
    return render(request, 'main/custom_page.html', {
        'section':section,
        'pageLayouts':pageLayouts
    })

def subsection_view(request, section_url, subsection_url):
    html = Section.objects.filter(parent__url=section_url, url=subsection_url).first()
    return render(request, 'main/custom_page.html', {
        'title':html.title,
    })

def add_section(request):
    current_user = request.user
    if current_user.is_anonymous or not (current_user.is_superuser or current_user.is_staff or current_user.profile.moderator):
        return redirect('main_index')
    if request.method == 'POST':
        if request.POST.get('add_section'):
            form = SectionForm(request.POST)
            if form.is_valid():
                section = form.save(commit=False)
                section.parent = None
                section.save()
                return redirect('main_index')
        else:
            form = SectionForm()
    else:
        form = SectionForm()
    return render(request, 'main/edit_section.html', {
        'form':form,
        'title':"Add section",
        'edit':False

    })

def edit_section(request,section_id):
    current_user = request.user
    if current_user.is_anonymous or not (current_user.is_superuser or current_user.is_staff or current_user.profile.moderator):
        return redirect('main_index')
    section = Section.objects.get(id=section_id)
    if section is None:
        return render(request, 'main/404.html')
    if request.method == 'POST':
        if request.POST.get('edit_section'):
            form = SectionForm(request.POST,instance=section)
            if form.is_valid():
                form.save()
                return redirect('main_index')
        else:
            form = SectionForm(instance=section)
    else:
        form = SectionForm(instance=section)
    return render(request, 'main/edit_section.html', {
        'form':form,
        'title':"Edit section",
        'edit':True
    })

def add_subsection(request,section_id):
    current_user = request.user
    if current_user.is_anonymous or not (current_user.is_superuser or current_user.is_staff or current_user.profile.moderator):
        return redirect('main_index')
    if request.method == 'POST':
        if request.POST.get('add_section'):
            form = SectionForm(request.POST)
            if form.is_valid():
                subsection = form.save(commit=False)
                section = Section.objects.get(id=section_id)
                subsection.parent = section
                subsection.save()
                return redirect('main_index')
        else:
            form = SectionForm()
    else:
        form = SectionForm()
    return render(request, 'main/edit_section.html', {
        'form':form,
        'title':"Add subsection",
        'edit':False

    })

def edit_subsection(request,subsection_id):
    current_user = request.user
    if current_user.is_anonymous or not (current_user.is_superuser or current_user.is_staff or current_user.profile.moderator):
        return redirect('main_index')
    subsection = Section.objects.get(id=subsection_id)
    if subsection is None:
        return render(request, 'main/404.html')
    if request.method == 'POST':
        if request.POST.get('edit_section'):
            form = SectionForm(request.POST,instance=subsection)
            if form.is_valid():
                form.save()
                return redirect('main_index')
        else:
            form = SectionForm(instance=subsection)
    else:
        form = SectionForm(instance=subsection)
    return render(request, 'main/edit_section.html', {
        'form':form,
        'title':"Edit subsection",
        'edit':True
    })
