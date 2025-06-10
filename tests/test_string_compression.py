import decorator_itertool_challenges.string_compression as sc

sample_string = "Fibonacci is ccccool for ccccccrows."
output = "Fibona2ci is 4cool for 6crows."

def test_compress_c():
    assert sc.compress_c(sample_string) == output