from django.contrib import messages
from django.db.models import Avg, Max, Min
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PriceReportForm
from .models import Item, PriceReport

def home(request):
    latest_reports = PriceReport.objects.select_related("item", "market")[:10]
    items = Item.objects.all()
    return render(request, "prices/home.html", {
        "latest_reports": latest_reports,
        "items": items,
    })


def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    reports = item.reports.select_related("market")
    stats = reports.aggregate(
        lowest=Min("price"),
        average=Avg("price"),
        highest=Max("price"),
    )
    cheapest = reports.order_by("price").first()
    return render(request, "prices/item_detail.html", {
        "item": item,
        "reports": reports,
        "stats": stats,
        "cheapest": cheapest,
    })

def report_price(request):
    if request.method == "POST":
        form = PriceReportForm(request.POST, request.FILES)
        if form.is_valid():
            report = form.save()
            messages.success(
                request,
                f"Thanks! {report.item.name} at {report.market.name} has been recorded.",
            )
            return redirect("prices:item_detail", pk=report.item.pk)
    else:
        form = PriceReportForm()
    return render(request, "prices/report_form.html", {"form": form})