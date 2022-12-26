from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DeleteView, CreateView

from .forms import *
from .models import Text
from django.urls import reverse, reverse_lazy
from .models import *


class Index(ListView):
    model = Text
    template_name = 'app/index.html'
    context_object_name = 'pages'

# class Index(View):
#     def get(self, request, *agrs, **kwagrs):
#         return render(request, 'app/index.html', {'pages': Text.objects.all()})

#
# def index(request):
#     return render(request, 'app/index.html', {'pages': Text.objects.all()})


class Form(CreateView):
    form_class = One
    template_name = 'app/form.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, form=form_class, **kwargs):
        print('вызов', intilizer())

        return {'form': form}

    def form_valid(self, form):

        Publishing = Publishing_house.objects.filter(id__in=form.cleaned_data['publishing_house'])
        text = Text(category_id=form.cleaned_data['category'],
                    Info_id=Author.objects.create(info=form.cleaned_data['Info']).id,
                    title= form.cleaned_data['title'],
                    img_href= form.cleaned_data['img_href'],
                    CheckBox= form.cleaned_data['CheckBox'],
        )
        text.save()
        print(text.id)
        text.publishing_house.set(Publishing, through_defaults={})

        form.instance = text
        return super(Form, self).form_valid(form)



# class Form(View):
#     def post(self, request, *args, **kwagrs):
#         form = One(data=request.POST)
#         if form.is_valid():
#             id = Author.objects.create(info=form.cleaned_data['Info']).id
#             text = Text.objects.create(title=form.cleaned_data['Title'], content=form.cleaned_data['TextArea'],
#                                        img_href=form.cleaned_data['Url'], CheckBox=form.cleaned_data['CheckBox'],
#                                        category_id=form.cleaned_data['Selection'], Info_id=id)
#
#             Publishing_house_ids = form.cleaned_data['Publishing_house_selection']
#             Publishing = Publishing_house.objects.filter(id__in=Publishing_house_ids)
#
#             text.id = Text.objects.last().id
#             text.publishing_house.set(Publishing, through_defaults={})
#
#             return HttpResponseRedirect(reverse('home'))
#
#     def get(self, request, *agrs, **kwagrs):
#         intilizer()
#         form = One()
#         return render(request, 'app/form.html', {'form': form})



# def form(request):
#     intilizer()
#     if request.method == 'POST':
#         form = One(request.POST)
#         if form.is_valid():
#             id = Author.objects.create(info=form.cleaned_data['Info']).id
#             text = Text.objects.create(title=form.cleaned_data['Title'], content=form.cleaned_data['TextArea'], img_href=form.cleaned_data['Url'], CheckBox=form.cleaned_data['CheckBox'], category_id=form.cleaned_data['Selection'], Info_id=id)
#
#             Publishing_house_ids = form.cleaned_data['Publishing_house_selection']
#             Publishing = Publishing_house.objects.filter(id__in=Publishing_house_ids)
#
#             text.id = Text.objects.last().id
#             text.publishing_house.set(Publishing, through_defaults={})
#
#             return HttpResponseRedirect(reverse('home'))
#     else:
#         form = One()
#     return render(request, 'app/form.html', {'form': form})


# не понял как мне нормально переипсать это egit с CreateView. Помоему легче написать с View
# class Edit(CreateView):
#
#     # try:
#     #     text = Text.objects.get(id=id)
#     # except:
#     #     HttpResponseNotFound('<h2>Page not found</h2>')
#     model = Text
#
#     form_class = One(initial={'title': .model.title,
#                                           'category': Edit.model.category_id,
#                                           'Info': super().model.Info_id,
#                                           'img_href': super().model.img_href,
#                                           'CheckBox':  super().model.CheckBox,
#                                           'publishing_house': super().model.publishing_house
#                                           })
#     template_name = 'app/edit.html'
#     success_url = reverse_lazy('home')
#
#     def get_queryset(self):
#         try:
#             text = Text.objects.get(id=id)
#         except:
#             not_found(self.request)
#         return Text.objects.get(id=self.kwargs['id'])
#
#     def get_context_data(self, form=form_class, **kwargs):
#         print('вызов', intilizer())
#
#         return {'form': form}
#
#     def post(self, request, id, *args, **kwargs):
#
#         try:
#             text = Text.objects.get(id=id)
#         except:
#             HttpResponseNotFound('<h2>Page not found</h2>')
#
#         form = One(request.POST)
#
#         Publishing = Publishing_house.objects.filter(id__in=form.cleaned_data['publishing_house'])
#         text.category_id = form.cleaned_data['category']
#         text.Info_id = Author.objects.create(info=form.cleaned_data['Info']).id
#         text.title = form.cleaned_data['title']
#         text.img_href = form.cleaned_data['img_href']
#         text.CheckBox = form.cleaned_data['CheckBox']
#
#         text.publishing_house.set(Publishing, through_defaults={})
#
#         text.save()
#         self.get(request)

class Edit(View):

    def get(self, request, id, *agrs, **kwagrs):
        try:
            text = Text.objects.get(id=id)
        except:
            return HttpResponseNotFound('<h2>Person not found</h2>')
        text = Text.objects.get(id=id)
        print(text.publishing_house)
        form = One(initial={'title': text.title,
                              'category': text.category_id,
                              'Info': text.Info_id,
                              'img_href': text.img_href,
                              'CheckBox':  text.CheckBox,
                              'publishing_house': text.publishing_house.all(),
                               'content': text.content
                              })
        return render(request, 'app/edit.html', {'form': form})

    def post(self, request, id, *agrs, **kwagrs):
        try:
            text = Text.objects.get(id=id)
        except:
            return HttpResponseNotFound('<h2>Person not found</h2>')
        form = One(request.POST)
        if form.is_valid():

            Publishing = Publishing_house.objects.filter(id__in=form.cleaned_data['publishing_house'])
            text.category_id = form.cleaned_data['category']
            text.Info_id = Author.objects.create(info=form.cleaned_data['Info']).id
            text.title = form.cleaned_data['title']
            text.img_href = form.cleaned_data['img_href']
            text.CheckBox = form.cleaned_data['CheckBox']
            text.content = form.cleaned_data['content']
            text.publishing_house.set(Publishing, through_defaults={})

            text.save()
            return HttpResponseRedirect(reverse('home'))
        else:
            self.get(request)


# def edit(request, id):
#     if request.method == 'POST':
#         try:
#             cart = Text.objects.get(id=id)
#         except:
#             return HttpResponseNotFound('<h2>Person not found</h2>')
#         form = One(request.POST)
#         if form.is_valid():
#             cart.title = form.cleaned_data['Title']
#             cart.img_href = form.cleaned_data['Url']
#             cart.content = form.cleaned_data['TextArea']
#             cart.CheckBox = form.cleaned_data['CheckBox']
#             cart.category_id = form.cleaned_data['Selection']
#
#             id = Author.objects.create(info=form.cleaned_data['Info']).id
#             cart.Info_id = id
#
#             Publishing = Publishing_house.objects.filter(id__in=form.cleaned_data['Publishing_house_selection'])
#             cart.publishing_house.set(Publishing, through_defaults={})
#             cart.save()
#             return HttpResponseRedirect(reverse('home'))
#         else:
#             print('is_not_valud')
#     else:
#         form = One()
#
#     return render(request, 'app/edit.html', {'form': form})

class Delete(DeleteView):
    model = Text
    template_name = 'app/Delete.html'
    success_url = reverse_lazy('home')

# class Delete(View):
#     def get(self, request, id, *agrs, **kwagrs):
#         try:
#             cart = Text.objects.get(id=id)
#         except:
#             return HttpResponseNotFound('<h2>Person not found</h2>')
#         cart.delete()
#         return HttpResponseRedirect(reverse('home'))

# def delete(request, id):
#     try:
#         cart = Text.objects.get(id=id)
#     except:
#         return HttpResponseNotFound('<h2>Person not found</h2>')
#     cart.delete()
#     return HttpResponseRedirect(reverse('home'))


def intilizer():
    if category.objects.all().count() == 0:
        category.objects.create(name='Python')
        category.objects.create(name='Django')
    if Publishing_house.objects.all().count() == 0:
        Publishing_house.objects.create(name='Publishing_house23')
        Publishing_house.objects.create(name='Publishing_house11111')


