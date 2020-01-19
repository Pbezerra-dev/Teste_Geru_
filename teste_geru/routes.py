def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('index', '/')
    config.add_route('quotes', '/quotes')
    config.add_route('q_random', '/quotes/random')
    config.add_route('q_num', '/quotes/{pk}')
