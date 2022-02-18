from django.shortcuts import render, redirect
from pokedex.models import Pokemon, Type
# Create your views here.
def pokedb(request):    
    pokemons = Pokemon.objects.all().order_by('pokedex_number')
    data = {
        "pokemon_list":pokemons
    }
    return render(request, "pokedex.html", context=data)

    # def pokeList(request):
    #     pokemons = Pokemon.objects.all()
    #     data = {
    #         "pokemon_list": pokemons
    #     }
    #     return render(request, "pokemon_list.html", context = data)

def add_pokemon(request):
    if request.method == "POST":
        num = int(request.POST.get('pokemon_number'))
        name = request.POST.get('pokemon_name')
        type1 = Type.objects.get(id = int(request.POST.get('primary_type')))
        type2 = Type.objects.get(id = int(request.POST.get('secondary_type')))

        # if not Pokemon.objects.update_or_create()
        if not Pokemon.objects.filter(pokedex_number = num).first():
            Pokemon.objects.create(pokedex_number = num, name = name, primarytype = type1, secondarytype = type2)
        else:
            p = Pokemon.objects.get(pokedex_number = num)
            p.name = name
            p.primarytype = type1
            p.secondarytype = type2
            p.save()

        return redirect('pokedex')

    types = Type.objects.all()
    data = {
        "types": types
    }

    return render(request, "add_pokemon.html", context = data)

def delete_pokemon(request, id):
    Pokemon.objects.get(pokedex_number=id).delete()
    return redirect('pokedex')