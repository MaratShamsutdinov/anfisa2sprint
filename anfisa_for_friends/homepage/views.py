from django.shortcuts import render

from ice_cream.models import IceCream


def index(request):
    template_name = 'homepage/index.html'
    ice_cream_list = IceCream.objects.values(
        'id',
        'title',
        'description',
        'price',
        'category__title'
        ).filter(
        is_published__exact=True,
        is_on_main__exact=True,
        category__is_published=True
        ).order_by(
            'title'
            )[0:3]

    # .filter(is_on_main__exact=True, is_published__exact=True
    #          )

    # .filter(
    #     Q(is_published__exact=True) & ~Q(is_on_main__exact=False
    # )
    context = {'ice_cream_list': ice_cream_list}
    return render(request, template_name, context)
