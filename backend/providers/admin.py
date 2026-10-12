from django.contrib import admin, messages
from django.utils import timezone

from .models import Provider, Booking


@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'service',
        'phone',
        'status',
        'created_at',
        'verified_at',
    )

    list_filter = (
        'status',
        'service',
    )

    search_fields = (
        'full_name',
        'phone',
        'cnic',
        'user__email',
    )

    readonly_fields = (
        'created_at',
        'verified_at',
    )

    actions = (
        'approve_providers',
        'reject_providers',
    )

    @admin.action(description='Approve selected providers')
    def approve_providers(self, request, queryset):
        count = queryset.update(
            status='approved',
            rejection_reason='',
            verified_at=timezone.now()
        )

        messages.success(
            request,
            f'{count} provider(s) approved.'
        )

    @admin.action(description='Reject selected providers')
    def reject_providers(self, request, queryset):
        count = queryset.update(
            status='rejected',
            verified_at=None
        )

        messages.warning(
            request,
            f'{count} provider(s) rejected. '
            f'Add a rejection reason when opening the record.'
        )


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'client_name',
        'client_phone',
        'service',
        'booking_date',
        'booking_time',
        'status',
        'created_at',
    )

    list_filter = (
        'service',
        'status',
        'booking_date',
    )

    search_fields = (
        'client_name',
        'client_email',
        'client_phone',
        'address',
    )