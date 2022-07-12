class Range_Check:
    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end
        self.print_msg = lambda str, verbosity : print(str) if verbosity else None

    def check_out_of_range(self, element_val):
        if(element_val < self.start or element_val > self.end):
            return True
        return False
