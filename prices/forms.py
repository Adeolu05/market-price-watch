from django import forms

from .models import PriceReport


class PriceReportForm(forms.ModelForm):
    class Meta:
        model = PriceReport
        fields = ["item", "market", "price", "note", "photo"]
        labels = {"price": "Price (₦)", "photo": "Photo of price tag (optional)"}
        widgets = {
            "note": forms.TextInput(attrs={"placeholder": "e.g. Price went up after the rain"}),
        }

    def clean_price(self):
        price = self.cleaned_data["price"]
        if price <= 0:
            raise forms.ValidationError("Price must be more than zero.")
        if price > 10_000_000:
            raise forms.ValidationError("That looks too high. Check for extra zeros.")
        return price

    def clean_photo(self):
        photo = self.cleaned_data.get("photo")
        if photo and photo.size > 3 * 1024 * 1024:
            raise forms.ValidationError("Photo must be 3MB or smaller.")
        return photo