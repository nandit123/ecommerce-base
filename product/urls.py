from django.conf.urls import url
from . import views

app_name = 'product'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^about/$', views.AboutView.as_view(), name='about'),
    url(r'^contact/$', views.email, name='contact'),
    url(r'^category/$', views.CategoryView.as_view(), name='category'),
    url(r'^(?P<pk>[0-9]+)/$', views.ProductView.as_view(), name='product_detail'),
    url(r'^cart/$', views.CartView.as_view(), name='cart'),

    url(r'^product/add/$', views.ProductCreate.as_view(), name='product-add'),
    url(r'^product/(?P<pk>[0-9]+)/$', views.ProductUpdate.as_view(), name='product-update'),

    url(r'^product/(?P<pk>[0-9]+)/delete/$', views.ProductDelete.as_view(), name='product-delete'),
    url(r'^thanks/$', views.thanks, name='thanks'),

]