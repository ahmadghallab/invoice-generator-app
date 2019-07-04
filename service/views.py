from django.shortcuts import render
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.db.models import Sum, Count, Avg, Q, F, FloatField
from django.db.models.functions import Coalesce
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from datetime import datetime
from django.core import serializers

from . import forms
from . import models
from . import functions as func

# Stock
class StockListView(generic.ListView):
    model = models.Stock
    context_object_name = 'items'
    template_name = 'service/stock_list.html'

class StockCreateView(SuccessMessageMixin, generic.CreateView):
    form_class = forms.StockForm
    model = models.Stock
    success_url = '/service/items/create'
    success_message = "%(name)s has been created successfully"

class StockUpdateView(SuccessMessageMixin, generic.UpdateView):
    form_class = forms.StockForm
    model = models.Stock
    success_url = '/service/items/'
    success_message = "%(name)s has been updated successfully"

class StockDeleteView(SuccessMessageMixin, generic.DeleteView):
    model = models.Stock
    success_url = '/service/items/'

# Service categories
class ServiceCategoryListView(generic.ListView):
    model = models.ServiceCategory
    context_object_name = 'categories'
    template_name = 'service/service_category_list.html'

class ServiceCategoryCreateView(SuccessMessageMixin, generic.CreateView):
    form_class = forms.ServiceCategoryForm
    model = models.ServiceCategory
    success_url = '/service/categories/create'
    success_message = "%(ar_name)s has been created successfully"

class ServiceCategoryUpdateView(SuccessMessageMixin, generic.UpdateView):
    form_class = forms.ServiceCategoryForm
    model = models.ServiceCategory
    success_url = '/service/categories/'
    success_message = "%(ar_name)s has been updated successfully"

class ServiceCategoryDeleteView(generic.DeleteView):
    model = models.ServiceCategory
    success_url = '/service/categories/'

# Vehicles


class VehicleListView(generic.ListView):
    model = models.Vehicle
    context_object_name = 'vehicles'
    template_name = 'service/vehicle_list.html'


class VehicleCreateView(SuccessMessageMixin, generic.CreateView):
    form_class = forms.VehicleForm
    model = models.Vehicle
    success_url = '/service/vehicles/create'
    success_message = "%(ar_name)s has been created successfully"


class VehicleUpdateView(SuccessMessageMixin, generic.UpdateView):
    form_class = forms.VehicleForm
    model = models.Vehicle
    success_url = '/service/vehicles/'
    success_message = "%(ar_name)s has been updated successfully"


class VehicleDeleteView(generic.DeleteView):
    model = models.Vehicle
    success_url = '/service/vehicles/'

# Customers
class CustomerListView(generic.ListView):
    model = models.Customer
    context_object_name = 'customers'
    template_name = 'service/customer_list.html'


class CustomerCreateView(SuccessMessageMixin, generic.CreateView):
    form_class = forms.CustomerForm
    model = models.Customer
    success_url = '/service/customers/create'
    success_message = "%(ar_name)s has been created successfully"


class CustomerUpdateView(SuccessMessageMixin, generic.UpdateView):
    form_class = forms.CustomerForm
    model = models.Customer
    success_url = '/service/customers/'
    success_message = "%(ar_name)s has been updated successfully"


class CustomerDeleteView(generic.DeleteView):
    model = models.Customer
    success_url = '/service/customers/'

# Create Order
class OrderManipulation:
    # Create order
    def order_creation(request, customer_pk):
        customer = get_object_or_404(models.Customer, pk=customer_pk)
        currentDate = datetime.now()
        form = None
        if request.method == 'POST':
            form = forms.OrderForm(request.POST)
            form.fields['customer_call'].required = False
            if form.is_valid():
                result = models.Order()
                result.enter_date = request.POST.get('enter_date')
                result.exit_date = request.POST.get('exit_date')
                result.enter_time = request.POST.get('enter_time')
                result.exit_time = request.POST.get('exit_time')
                customer_call = request.POST.get('customer_call')
                customer_call = True if customer_call else False
                result.customer_call = customer_call
                result.type = request.POST.get('type')
                result.vehicle_counter = request.POST.get('vehicle_counter') or 0
                result.complaint = request.POST.get('complaint')
                result.customer = customer
                result.save()
                order_bill_no = '1900' + str(result.pk)
                order_no = '1800' + str(result.pk)
                result.bill_no = int(order_bill_no)
                result.order_no = int(order_no)
                result.save()
                messages.add_message(request, messages.SUCCESS, 'Order has been saved successfully')
                return HttpResponseRedirect(reverse('service:order_list'))
            else:
                messages.add_message(request, messages.ERROR, 'Order has note been saved successfully')

        return render(request, 'service/order_create_form.html',{
            'customer':customer,
            'currentDate':currentDate,
            'form':form
            })
    
    # Edit order
    def edit_order(request, order_pk):
        order = get_object_or_404(models.Order, pk=order_pk)
        form = forms.OrderForm()
        if request.method == 'POST': 
            form = forms.OrderForm(instance=order, data=request.POST)
            form.fields['customer_call'].required = False
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS,"Changes has been saved successfully")
            else:
                messages.add_message(request, messages.ERROR,"Changes not has been saved")
        return render(request, 'service/order_edit_form.html', {
            'order':order,
            'form':form
        })

    # Order list
    def order_list(request):
        orders = models.Order.objects.all()
        return render(request, 'service/order_list.html', {'orders':orders})

    # Delete bill
    def del_order(request, order_pk):
        order = get_object_or_404(models.Order, pk=order_pk)
        if request.method == 'POST':
            models.Order.objects.filter(pk=order_pk).delete()
            messages.add_message(request, messages.SUCCESS,"Order has been deleted successfully")
            return HttpResponseRedirect(reverse('service:order_list'))
        return render(request, 'service/order_confirm_delete.html', {
            'order':order
        })

    # Create bill
    def create_bill(request, order_pk):
        results = total = net_total = labor_discount_value = parts_discount_value = oils_discount_value = total_words = None
        order = get_object_or_404(models.Order, pk=order_pk)
        types = models.Bill.objects.values('type').filter(order=order_pk).distinct().annotate(
            sub_total=Coalesce(Sum(F('price') * F('qty')),0),
        )
        if types:
            results = models.Bill.objects.filter(order=order_pk).annotate(
                net_price=(F('price') * F('qty'))
            )
            total = results.aggregate(
                sub_general=Coalesce(Sum(F('price') * F('qty')),0),
                total_tax=Coalesce(Sum(F('net_price') * 0.14, filter=Q(tax=True)),0),
                avg_discount_labor=Coalesce(Avg('discount', filter=Q(type='labour'), output_field=FloatField()),0),
                avg_discount_parts=Coalesce(Avg('discount', filter=Q(type='parts'), output_field=FloatField()),0),
                avg_discount_oils=Coalesce(Avg('discount', filter=Q(type='oils'), output_field=FloatField()),0),
                labour=Coalesce(Sum(F('price') * F('qty'), filter=Q(type='labour')),0),
                parts=Coalesce(Sum(F('price') * F('qty'), filter=Q(type='parts')),0),
                oils=Coalesce(Sum(F('price') * F('qty'), filter=Q(type='oils')),0)
            )
            labor_discount_value = (total['avg_discount_labor']/100) * total['labour']
            parts_discount_value = (total['avg_discount_parts']/100) * total['parts']
            oils_discount_value = (total['avg_discount_oils']/100) * total['oils']
            net_total = total['sub_general'] + total['total_tax'] - labor_discount_value - parts_discount_value - oils_discount_value
            total_words = func.num2word(round(net_total,2))
    
        if request.method == 'POST':
            form = forms.BillForm(request.POST)
            form.fields['qty'].required = False
            form.fields['discount'].required = False
            form.fields['item_code'].required = False
            form.fields['tax'].required = False
            if form.is_valid():
                result = models.Bill()
                result.date = request.POST.get('date')
                result.type = request.POST.get('type')
                result.qty = request.POST.get('qty') or 1
                result.price = request.POST.get('price')
                result.discount = request.POST.get('discount') or 0
                tax = request.POST.get('tax')
                tax = True if tax else False
                result.tax = tax
                result.item_code = request.POST.get('item_code')
                result.description = request.POST.get('description')
                result.order = order
                result.save()
                messages.add_message(request, messages.SUCCESS, 'Process has been saved successfully')
                return HttpResponseRedirect(reverse('service:create_bill', kwargs={'order_pk':order_pk}))
            else:
                messages.add_message(request, messages.ERROR, 'Process has not been saved')
        return render(request, 'service/bill_create_form.html', {
            'order':order,
            'types':types,
            'results':results,
            'total':total,
            'net_total':net_total,
            'labor_discount_value':labor_discount_value,
            'parts_discount_value':parts_discount_value,
            'oils_discount_value':oils_discount_value,
            'total_words':total_words
        })
    
    # Edit Bill
    def edit_bill(request, order_pk, bill_pk):
        bill = get_object_or_404(models.Bill, pk=bill_pk)
        order = get_object_or_404(models.Order, pk=order_pk)

        form = forms.BillForm()
        if request.method == 'POST': 
            form = forms.BillForm(instance=bill, data=request.POST)
            form.fields['tax'].required = False
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS,"Changes has been saved successfully")
                return HttpResponseRedirect(reverse('service:create_bill', kwargs={'order_pk':order_pk}))
            else:
                messages.add_message(request, messages.ERROR,"Changes not has been saved")
        return render(request, 'service/bill_edit_form.html', {'bill':bill})

    # Delete bill
    def del_bill(request, bill_pk, order_pk):
        bill = get_object_or_404(models.Bill, pk=bill_pk)
        if request.method == 'POST':
            models.Bill.objects.filter(pk=bill_pk).delete()
            messages.add_message(request, messages.SUCCESS,"Bill item has been deleted successfully")
            return HttpResponseRedirect(reverse('service:create_bill', kwargs={'order_pk':order_pk}))
        return render(request, 'service/bill_confirm_delete.html', {
            'bill':bill
        })

# Ajax Requests
# Get Items
def get_items(request):
    if request.method == 'POST':
        item = request.POST.get('itemName')
        if item:
            item_data = models.Stock.objects.filter(Q(code__contains=item) | Q(name__contains=item))
            data = serializers.serialize("json", item_data)
            return HttpResponse(data, content_type='application/json')
        return HttpResponse()
