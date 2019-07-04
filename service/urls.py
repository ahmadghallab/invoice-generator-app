from django.urls import path
from . import views

app_name = 'service'

urlpatterns = [
    # Stock
    path('items/', views.StockListView.as_view(), name='item_list'),
    path('items/create', views.StockCreateView.as_view(), name='item_create'),
    path('items/edit/<int:pk>', views.StockUpdateView.as_view(), name='item_edit'),
    path('items/delete/<int:pk>', views.StockDeleteView.as_view(), name='item_delete'),
    # Service categories
    path('categories/', views.ServiceCategoryListView.as_view(),
         name='list_service_category'),
    path('categories/create/', views.ServiceCategoryCreateView.as_view(),
         name='create_service_category'),
    path('categories/edit/<int:pk>',
         views.ServiceCategoryUpdateView.as_view(), name='edit_service_category'),
    path('categories/delete/<int:pk>',
         views.ServiceCategoryDeleteView.as_view(), name='delete_service_category'),
    # Vehicles
    path('vehicles/', views.VehicleListView.as_view(), name='list_vehicle'),
    path('vehicles/create/', views.VehicleCreateView.as_view(),
         name='create_vehicle'),
    path('vehicles/edit/<int:pk>',
         views.VehicleUpdateView.as_view(), name='edit_vehicle'),
    path('vehicles/delete/<int:pk>',
         views.VehicleDeleteView.as_view(), name='delete_vehicle'),
    # Customers
    path('customers/', views.CustomerListView.as_view(), name='list_customer'),
    path('customers/create/', views.CustomerCreateView.as_view(),
         name='create_customer'),
    path('customers/edit/<int:pk>',
         views.CustomerUpdateView.as_view(), name='edit_customer'),
    path('customers/delete/<int:pk>',
         views.CustomerDeleteView.as_view(), name='delete_customer'),
    # Create Order
    path('customers/<int:customer_pk>/orders/new',
         views.OrderManipulation.order_creation, name='order_creation'),
    path('orders/', views.OrderManipulation.order_list, name='order_list'),
    path('orders/<int:order_pk>/edit',
         views.OrderManipulation.edit_order, name='edit_order'),
    path('orders/<int:order_pk>/bill',
         views.OrderManipulation.create_bill, name='create_bill'),
    path('orders/<int:order_pk>/bill/<int:bill_pk>/edit',
         views.OrderManipulation.edit_bill, name='edit_bill'),
    path('orders/<int:order_pk>/bill/<int:bill_pk>/delete',
         views.OrderManipulation.del_bill, name='delete_bill'),
    path('orders/<int:order_pk>/delete', views.OrderManipulation.del_order, name='delete_order'),
    path('get_items', views.get_items, name='get_items'),
]
