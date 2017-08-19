import abc

class InitialValues:
    __metaclass__ = abc.ABCMeta
 
    #initial value assigned over a grid
    @abc.abstractmethod
    def distribute_init(self,N,var): 
        print("This abstract function should not have been called")
        raise NotImplementedError()


class BoundaryValues:
    __metaclass__ = abc.ABCMeta
 
    #TBD: Define some new function
    @abc.abstractmethod
    def distribute_bry(self,N,var): 
        print("This abstract function should not have been called")
        raise NotImplementedError()
