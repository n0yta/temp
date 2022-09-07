class Base:
    def fail(self):
        pass

    def __init_subclass__(cls, **kwargs):
        if cls.fail == Base.fail:
            raise TypeError(
               'Subclasses of `Base` must override the `fail` method'
            )



# this class definition works fine.
class Task2(Base):
    def fail(self):
        print('this is good')


t = Task2()
t.fail()
