from django.conf import settings
from django.http import FileResponse, HttpResponse
from django.shortcuts import render, get_object_or_404

import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from django.template.loader import render_to_string
import weasyprint


from blog.models import Post


def post_list(request):
    posts = Post.published.all()
    return render(request, 'blog/post/list.html', {'posts': posts})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post,
                             slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    return render(request, 'blog/post/detail.html', {'post': post})


def some_view(request):
    posts = Post.published.all()
    html_string = render_to_string('blog/pdf.html', {'posts': posts})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="somefilename.pdf"'
    weasyprint.HTML(string=html_string).write_pdf(response)
    return response
