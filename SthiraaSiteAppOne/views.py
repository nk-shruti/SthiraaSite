from django.shortcuts import render

# Create your views here.
# add to the top
from forms import ArticleForm



# add to your views
def article_form(request):

    if request.method == 'POST':
        form = ArticleForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()
    # form_class = ArticleForm
    
        # return render(request, 'article_form.html', {'form': form})
    else:
        form = ArticleForm()
    return render(request, 'article_form.html', {'form': form})
