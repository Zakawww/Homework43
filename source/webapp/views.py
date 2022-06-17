from django.shortcuts import render


def index_view(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    else:
        context = {
            'first': request.POST.get('first'),
            'second': request.POST.get('second'),
            'step': request.POST.get('step'),
        }

        result = 0
        if context['step'] == 'add':
            result = int(context['first']) + int(context['second'])
        elif context['step'] == 'subtract':
            result = int(context['first']) - int(context['second'])
        elif context['step'] == 'multiply':
            result = int(context['first']) * int(context['second'])
        elif context['step'] == 'divide':
            result = int(context['first']) / int(context['second'])

        amount = {"amount": result}
        digits = {'add': '+', 'subtract': '-', 'multiply': '*', 'divide': '/'}

        operation = context['step']
        operation_text = digits[operation]

        answer = {'answer': f"{context['first']} {operation_text} {context['second']} = {result}"}

        context.update(dict(amount))
        context.update(answer)

        return render(request, 'index.html', context)
