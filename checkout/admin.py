from django.contrib import admin
from .models import Order, OrderLineItem

class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'purchase_date',
                    'delivery_cost', 'order_total',
                    'grand_total', 'original_cart',
                    'stripe_pid',)

    fields = ('order_number', 'user_profile', 'purchase_date', 'full_name',
            'email', 'phone_number', 'country',
            'postcode', 'town_or_city', 'address_line1',
            'address_line2', 'county', 'delivery_cost',
            'order_total', 'grand_total', 'original_cart',
            'stripe_pid')

    list_display = ('order_number', 'purchase_date', 'full_name',
                    'order_total', 'delivery_cost',
                    'grand_total',)

    ordering = ('-purchase_date',)

admin.site.register(Order, OrderAdmin)