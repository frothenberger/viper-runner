import os

__author__ = 'froth'


class FileWriter:
    """
    Writes the various result files of the benchmark.
    """

    def __init__(self, ):
        self.csv_header = "runtime [s], input file, run configuration, exit condition"
        self.file = None

    def finalize(self):
        self.file.close()

    def init_output_file(self, filename, print_header=False):
        try:
            if not os.path.exists(os.path.dirname(filename)):
                os.makedirs(os.path.dirname(filename))
            self.file = open(os.path.join(os.getcwd(), filename), "w+")
            if print_header:
                print(self.csv_header, file=self.file)
        except IOError:
            print("Unable to open file '" + filename + "'. Aborting.")
            exit(-1)

    def add_timing_entry(self, timings, input_file, run_config_name):
        try:
            for (t, exit_condition) in timings:
                # writes all the timing triplets (timing, file, command)
                print(", ".join([str(t), input_file, run_config_name, exit_condition]),
                      file=self.file, flush=True)
        except IOError:
            print("Unable to write to file '" + self.file.name + "'. Aborting.")
            exit(-1)

    def write_line(self, line):
        try:
            print(line, file=self.file, flush=True)
        except IOError:
            print("Unable to write to file '" + self.file.name + "'. Aborting.")
            exit(-1)

    def write_raw(self, line):
        try:
            self.file.write(line)
        except IOError:
            print("Unable to write to file '" + self.file.name + "'. Aborting.")
            exit(-1)