def func(host=None, port=None):
    print host, port

func(host="127.0.0.1", port=5432)

params = dict(host="127.0.0.1", port=5432)
func(**params)
params.update(dict(port=5432))
func(**params)