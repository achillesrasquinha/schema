def get_type_name(instance):
    type_ = type(instance)
    name  = type_.__name__

    return name