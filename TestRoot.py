import abc

class AbstractTest:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def solve(self,callable_test_obj): 
        print("This abstract function should not have been called")
        raise NotImplementedError()


class Params:
    def __init__(self):
         self.xmin = 0
         self.xmax = 1
         self.tmin = 0
         self.tmax = 1

    def set_spatial_limits(xmin,xmax):
        self.xmin = xmin
        self.xmax = xmax

    def set_temporal_limits(tmin,tmax):
        self.tmin = tmin
        self.tmax = tmax
  
    
