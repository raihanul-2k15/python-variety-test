from django.shortcuts import render

from .calculation import Calculation


def index(req):
    try:
        submitted = req.GET['submit']
        submitted = True
    except(KeyError):
        submitted = False

    if submitted:
        # replace - separated keys to _ separated
        input_values = {key.replace(
            '-', '_'): val for (key, val) in req.GET.items()}

        context = {'input_values': input_values}
        try:
            output_values = Calculation.calculate(input_values)
            context['output_values'] = output_values
            print(output_values)
        except(KeyError):
            context['error_message'] = {'strong': 'All fields are required!',
                                        'description': 'All fields must have valid numbers'}
        except(ValueError):
            context['error_message'] = {'strong': 'Valid numbers are required!',
                                        'description': 'All fields must have valid numbers'}

        except(Exception):
            context['error_message'] = {
                'strong': 'Unknown Error!', 'description': 'Contact developer please'}
    else:
        input_values = Calculation.DEFAULT_INPUT_VALUES
        context = {"input_values": input_values}

    return render(req, 'pipe_calc/index.html', context)
