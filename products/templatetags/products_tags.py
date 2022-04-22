# Replace correct URL for filtered Django queries,
# for first/previous/next/last pages
# accessed on April 22nd, 2022, at 02:00, at
# https://stackoverflow.com/questions/68820700/paginate-a-filter

from django import template

register = template.Library()

@register.simple_tag
def querystring_replace(request, key, value):
    """Replace the given `key` with the given `value`
    in the request's querystring. The rest of the
    querystring remains unchanged.
    """
    query_dict = request.GET.copy()
    query_dict[key] = value
    print("NEW URL")
    print(query_dict.urlencode())
    return "?"+query_dict.urlencode()