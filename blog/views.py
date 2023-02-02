from django.shortcuts import render, get_object_or_404
from .models import Blog, Blogger, Tag, BlogComment

# Create your views here.

def index(request):
    """View function for home page of site"""

    # Generate counts of some of the main objects
    num_blogs = Blog.objects.all().count()

    # The 'all()' in implied by default
    num_bloggers = Blogger.objects.count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_blogs': num_blogs,
        'num_bloggers': num_bloggers,
        'num_visits': num_visits,
    }

    #Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

#------------------------- BlogList View ---------------------------
from django.views import generic
from .forms import NewCommentForm

class BlogListView(generic.ListView):
    model = Blog
    paginated_by = 2
#    def get_context_data(self, **kwargs):
        # Call the base implementation 1st to get the context
#        context = super(BookListView, self).get_context_data(**kwargs)
#        return context

class BlogDetailView(generic.DetailView):
    model = Blog

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        comments_connected = BlogComment.objects.filter(blog_connected = self.get_object()).order_by('-date_created')
        data['comments'] = comments_connected
        if self.request.user.is_authenticated:
            data['comment_form'] = NewCommentForm(instance=self.request.user)

        return data
        
    def post(self, request, *args, **kwargs):
        new_comment = BlogComment(comment=request.POST.get('comment'),
                author=self.request.user,
                blog_connected=self.get_object())
        new_comment.save()
        return self.get(self, *args, **kwargs)

class BloggerListView(generic.ListView):
    model = Blogger

class BloggerDetailView(generic.DetailView):
    model = Blogger

#----------  Add view for comment system ------------
#from .forms import CommentForm
# Refer to : https://stackoverflow.com/questions/60032366/how-to-get-the-pk-of-a-post-in-which-a-comment-is-contained
#from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

#class CommentCreateView(LoginRequiredMixin, generic.CreateView):
#    model = BlogComment
#    field = ['comment']

#    def form_valid(self, form):
#        form.instance.author = self.request.user
#        form.instance.blog_id = self.kwargs['pk']
#        return super().form_valid(form)

#    def get_success_url(self):
#        blog_number = Blog.object.get(pk=self.kwargs.get('pk'))
#        return blog_number.get_absolute_url()
