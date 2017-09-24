import abc

class AbstractTest:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def solve(self,callable_test_obj): 
        print("This abstract function should not have been called")
        raise NotImplementedError()

class AbstractSrc:
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def calculate_source(self,eqid,delta_t,delta_x,j):
        print("This abstract function should not have been called")
        raise NotImplementedError()
    
    @abc.abstractmethod
    def calculate_abc(self,eqid,delta_t,delta_x,j):
        print("This abstract function should not have been called")
        raise NotImplementedError()

class Params:
    def __init__(self,id):
        self.xmin = 0
        self.xmax = 1
        self.tmin = 0
        self.tmax = 1
        self.fpath = '.'
        self.name = id
        self.iter_count = 1

    def set_spatial_limits(self,xmin,xmax):
        self.xmin = xmin
        self.xmax = xmax

    def set_temporal_limits(self,tmin,tmax):
        self.tmin = tmin
        self.tmax = tmax

    #Absolute path
    def set_fig_path(self,fpath):
        self.fpath = fpath

    
