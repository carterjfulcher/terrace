def test_context():
    from terrace.data import Context
    from terrace.data import CSV
    custom_data = CSV('examples/sample.csv')
    context = Context(custom_data)
    print(context)

def test_polygon():
    from terrace.data import Context
    from terrace.data import Polygon

    polygon = Polygon("test")
    print(polygon.fields)
    context = Context(polygon)
    print(context.providers)
    print(context)

if __name__ == "__main__":
    test_polygon()