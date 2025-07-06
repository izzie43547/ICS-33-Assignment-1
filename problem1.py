def keyword_filter(**kwargs):
    return {k: str(v) for k, v in kwargs.items() if v}
    