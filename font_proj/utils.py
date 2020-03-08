# -*- encoding: utf-8 -*-


class GenericFilter:
    def filter_queryset(self, request, queryset, view):
        filter_fields = getattr(view, "filter_fields")
        kw = {}
        for field in filter_fields:
            value = request.query_params.get(field)
            if not value:
                continue
            kw[field] = value
        return queryset.filter(**kw)
