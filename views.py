from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.shortcuts import render

from .models import Producto


def lista_productos(request):
    productos = Producto.objects.all()

    query = request.GET.get('q', '')
    if query:
        productos = productos.filter(
            Q(nombre__icontains=query) | Q(descripcion__icontains=query)
        )

    categoria = request.GET.get('categoria', '')
    if categoria:
        productos = productos.filter(categoria=categoria)

    paginator = Paginator(productos, 2)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    context = {
        'page_obj': page_obj,
        'productos': page_obj.object_list,
        'query': query,
        'categoria_seleccionada': categoria,
        'categorias': Producto.CATEGORIA_CHOICES,
    }
    return render(request, 'catalogo/lista_productos.html', context)
