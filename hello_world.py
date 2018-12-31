import luigi
import time
tm = 15

class HelloTask(luigi.Task):
    def run(self):
        print("running hello")
        time.sleep(tm)
        with open('hello.txt', 'w') as fh:
            fh.write('Hello')
    def output(self):
        return luigi.LocalTarget('hello.txt')


class WorldTask(luigi.Task):
    def run(self):
        print("running world")
        time.sleep(tm)
        with open('world.txt', 'w') as fh:
            fh.write('World')
    def output(self):
        return luigi.LocalTarget('world.txt')

class HelloWorldTask(luigi.Task):
    def run(self):
        print("running HelloWorld")
        time.sleep(tm)
        with open('hello.txt') as fh:
            text = fh.read()
        with open('world.txt') as fh:
            text += fh.read()
        with open('hw.txt', 'w') as fh:
            fh.write(text)
    def output(self):
        return luigi.LocalTarget('hw.txt')
    def requires(self):
        return [HelloTask(), WorldTask()]


if __name__ == '__main__':
    luigi.run()
