class SomeTask(luigi.Task):
    def run(self):
        # do something
        pass

    def output(self):
        return [SomeTarget()]
        # Target implements an exists method telling if the job has been done

    def requires(self):
        return [AnotherTask()]
        # indicating the dependencies
