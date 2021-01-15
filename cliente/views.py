from django.shortcuts import render, redirect
from .models import Cliente
from .forms import ClienteForm
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
	
	data = {'clientes':Cliente.objects.all()}
	return render(request, 'index.html',data)


@login_required
def novo_cliente(request):
	form = ClienteForm(request.POST or None)
	if form.is_valid():
		form.save()
		return home(request)
	data = {'form':form}
	return render(request, 'form.html', data)


@login_required
def atualizacao(request):
	data = {'clientes':Cliente.objects.all()}
	return render(request, 'atualizacao.html', data)

	
@login_required
def update(request,id):
	cliente = Cliente.objects.get(id=id)
	form = ClienteForm(request.POST or None, instance=cliente)
	if form.is_valid():
		form.save()
		return home(request)
	data = {'form':form}
	return render(request, 'form.html', data)


@login_required
def excluir(request,id):
	cliente = Cliente.objects.get(id=id)
	cliente.delete()
	return redirect("home")