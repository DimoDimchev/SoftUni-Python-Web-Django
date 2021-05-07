from django.template import Library

register = Library()


@register.inclusion_tag('templates_advanced/tags/bootstrap_form.html')
def bootstrap_form(form, method, action):
    for(_, field) in form.fields.items():
        field.widget.attrs['class'] = 'form-control'

    return {
        'form': form,
        'method': method,
        'action': action,
    }

