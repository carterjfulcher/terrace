def test_context():
    from terrace.data import Context
    from terrace.data import CSV
    custom_data = CSV('examples/sample.csv')
    context = Context(custom_data)
    print(context)

if __name__ == "__main__":
    test_context()