import lazy
import numpy as np
import numbers

class TimeSeries:
    def __init__(self, values, times=None):
        """
        Stores a single, ordered set of numerical data.
        
        Parameters
        ----------
        values : a sequence 
           data used to populate time series instance.
        times  : a sequence (optional)
           time associated with each observation in `values`.

        Returns
        -------
        Nothing (for now).
        
        Notes
        -----
        PRE: 
           - 
           -
        POST: 
           - 
           -
        INVARIANTS: 
           -
           -
        WARNINGS:
           -
           -
        """
        if times == None:
            self._times = range(0,len(values))
        else:
            self._times = [x for x in times]
            
        self._values = [x for x in values]
        
        
    def __len__(self):
        """
        Reports the length of a TimeSeries instance.
        
        Parameters
        ----------
        self : a TimeSeries instance.

        Returns
        -------
        An integer representing the length of the instance.
        
        Notes
        -----
        PRE: 
           - 
           -
        POST: 
           - 
           -
        INVARIANTS: 
           -
           -
        WARNINGS:
           -
           -
        """        
        return len(self._values)
    
    
    def __getitem__(self, time):
        """
        Reports the data value located at `self[time]`, where
           `self` is a TimeSeries instance.
        
        Parameters
        ----------
        self  : a TimeSeries instance.
        time  : time associated with the desired data value.

        Returns
        -------
        The data value associated with `self[time]`.
        
        Notes
        -----
        PRE: 
           - 
           -
        POST: 
           - 
           -
        INVARIANTS: 
           -
           -
        WARNINGS:
           - Assumes the user knows the appropriate type of `time`.
           -
        """        
        try:
            return self._values[self._times.index(time)]
        except IndexError:
            raise("Index out of bounds.")
        
    
    def __setitem__(self, time, value):
        """
        Assigns the data value `value` to `self[time]`, where
           `self` is a TimeSeries instance.
        
        Parameters
        ----------
        self  : a TimeSeries instance.
        time  : time associated with the desired data value.
        value : the data value being associated with `time`.

        Returns
        -------
        Nothing (for now).
        
        Notes
        -----
        PRE: 
           - 
           -
        POST: 
           - 
           -
        INVARIANTS: 
           -
           -
        WARNINGS:
           - Assumes the user knows the appropriate type of `time`
                and `value`.
           -
        """         
        try:
            self._values[self._times.index(time)] = value
        except IndexError:
            raise("Index out of bounds.")
        
    def __repr__(self):
        """
        Prints a string representation of a TimeSeries instance.
        - For a TimeSeries instance with > 10 elements:
             returns a string with name of the class, length of the instance, 
             and list containing the first element and the last element 
             separated by an ellipsis. 
        - For a TimeSeries instance with <= 10 elements: 
             returns a string with name of the class, length of the instance, 
             and the full list representation of the data.        
        
        Parameters
        ----------
        self  : a TimeSeries instance.
        time  : time associated with the desired data value.
        value : the data value being associated with `time`.

        Returns
        -------
        Nothing (for now).
        
        Notes
        -----
        PRE: 
           - 
           -
        POST: 
           - 
           -
        INVARIANTS: 
           -
           -
        WARNINGS:
           - 
           -
        """           
        class_name = type(self).__name__
        print(type(self))
        if len(self._values) > 10:
            if np.ndim(self._values)==1:
                return '{}(Length: {}, Contents:[({},{}), ... ,({},{})])'.format(class_name, len(self._values), self._times[0], self._values[0], self._times[-1],self._values[-1]) 
            else:
                return '{}(Length: {}, Contents:[({}), ... ,({})])'.format(class_name, len(self._values), self._values[0], self._values[-1])                 
        else:
            if np.ndim(self._values)==1:               
                return '{}(Length: {}, Contents:[{}])'.format(class_name, len(self._values), ','.join([str(z) for z in zip(self._times, self._values)]))      
            else:
                return '{}(Length: {}, Contents:[{}])'.format(class_name, len(self._values), ','.join([str(z) for z in self._values]))                      
        
    def __str__(self):
        """
        Prints a string representation of a TimeSeries instance.
        - For a TimeSeries instance with > 10 elements:
             prints a string with a list containing the first element 
             and the last element separated by an ellipsis. 
        - For a TimeSeries instance with <= 10 elements: 
             prints the full list representation of the data.        
        
        Parameters
        ----------
        self  : a TimeSeries instance.
        time  : time associated with the desired data value.
        value : the data value being associated with `time`.

        Returns
        -------
        Nothing (for now).
        
        Notes
        -----
        PRE: 
           - 
           -
        POST: 
           - 
           -
        INVARIANTS: 
           -
           -
        WARNINGS:
           - 
           -
        """           
        class_name = type(self).__name__
        if len(self._values) > 10:
            if np.ndim(self._values)==1:
                return 'Length: {} [({},{}), ... ,({},{})]'.format(len(self._values), self._times[0], self._values[0], self._times[-1],self._values[-1]) 
            else:
                return 'Length: {} [({}), ... ,({})]'.format(len(self._values), self._values[0],self._values[-1]) 
        else:
            if np.ndim(self._values)==1:
                return 'Length: {} [{}]'.format(len(self._values), ','.join([str(z) for z in zip(self._times, self._values)]))      
            else:
                return 'Length: {} [{}]'.format(len(self._values), ','.join([str(z) for z in  self._values]))                      
        
    def __iter__(self):
        """
        Called when an iterator is required for a container. 
        
        Parameters
        ----------
        self  : a TimeSeries instance.

        Returns
        -------
        A new iterator object that can iterate over all the objects in the
           container. For mappings, it should iterate over the keys of the 
           container.
        
        Notes
        -----
        PRE: 
           - 
           -
        POST: 
           - 
           -
        INVARIANTS: 
           -
           -
        WARNINGS:
           - 
           -
        """            
        for i in self._values:
            yield i
            
    def __itertimes__(self):
        """
        Description.
        
        Parameters
        ----------
        self  : a TimeSeries instance.

        Returns
        -------
        Nothing (for now).
        
        Notes
        -----
        PRE: 
           - 
           -
        POST: 
           - 
           -
        INVARIANTS: 
           -
           -
        WARNINGS:
           - 
           -
        """           
        for i in self._times:
            yield i    
            
    def __iteritems__(self):
        """
        Description.
        
        Parameters
        ----------
        self  : a TimeSeries instance.

        Returns
        -------
        Nothing (for now).
        
        Notes
        -----
        PRE: 
           - 
           -
        POST: 
           - 
           -
        INVARIANTS: 
           -
           -
        WARNINGS:
           - 
           -
        """           
        for i,j in zip(self._times,self._values):
            yield i,j
    
    @lazy.lazy
    def identity(self):
        """
        Lazy implementation of the identity function
        
        Parameters
        ----------
        self  : a TimeSeries instance.

        Returns
        -------
        self  : a TimeSeries instance
        
        Notes
        -----
        PRE: 
           - 
           -
        POST: 
           - 
           -
        INVARIANTS: 
           -
           -
        WARNINGS:
           - 
           -
        """   
        return self
    
    @property
    def lazy(self):
        """
        Lazy identity property.  
        self.lazy returns a LazyOperation instance of self.identity(), so that  
        self.lazy.eval() is self.  
        
        Parameters
        ----------
        self  : a TimeSeries instance.

        Returns
        -------
        self.identity()  : a LazyOperation instance
        
        Notes
        -----
        PRE: 
           - 
           -
        POST: 
           - 
           -
        INVARIANTS: 
           -
           -
        WARNINGS:
           - 
           -
        """   

        return self.identity()
    
    def __pos__(self):
        #TimeSeries instance with
        # no change to the values or times
        return self
        
    def __neg__(self):
        # TimeSeries instance with
        # negated values 
        # and no change to the times
        cls = type(self)
        return cls((-v for v in self._values),self._times)
        
    def __abs__(self):
        # TimeSeries instance with 
        # absolute value of the values
        # and no change to the times
        cls = type(self)
        return cls((abs(v) for v in self._values),self._times)
    
    def __bool__(self):
        # False only if all values are zero
        return bool(any(self._values))
        
    def __add__(self, rhs):
        # If rhs is Real, add it to all elements of values.
        # If it is a TimeSeries instance with the same times,
        # add it element-by-element.
        # Return a TimeSeries instance with the same times but the new values
        cls = type(self)
        try:
            if isinstance(rhs, numbers.Real):
                return cls((a + rhs for a in self._values),self._times) 
            elif isinstance(rhs,cls):
                if (len(self)==len(rhs)) and self._eqtimes(rhs): 
                    return cls((a + b for a, b in zip(self._values,rhs._values)),self._times)
                else:
                    raise ValueError(str(self)+' and '+str(rhs)+' must have the same time points')
            else:
                return NotImplemented
        except TypeError:
            return NotImplemented
            
    def __sub__(self, rhs):
        # If rhs is Real, subtract it from all elements of values.
        # If it is a TimeSeries instance with the same times,
        # subtract it element-by-element.
        # Return a TimeSeries instance with the same times but the new values
        try:
            return self + (-rhs)
        except TypeError:
            return NotImplemented
    
    def __mul__(self, rhs):
        # If rhs is Real, multiply it by all elements of values.
        # If it is a TimeSeries instance with the same times,
        # multiply it element-by-element.
        # Return a TimeSeries instance with the same times but the new values
        cls = type(self)
        try:
            if isinstance(rhs, numbers.Real):
                return cls((a*rhs for a in self._values),self._times) 
            elif isinstance(rhs,cls):
                if (len(self)==len(rhs)) and self._eqtimes(rhs): 
                    return cls((a*b for a, b in zip(self._values,rhs._values)),self._times)
                else:
                    raise ValueError(str(self)+' and '+str(rhs)+' must have the same time points')
            else:
                return NotImplemented
        except TypeError:
            return NotImplemented
    
    def _eqtimes(self,rhs):
        # Test equality of the time components of two TimeSeries instances
        return len(self._times)==len(rhs._times) and all(a==b for a,b in zip(self._times,rhs._times))

    def _eqvalues(self,rhs):
        # Test equality of the values components of two TimeSeries instances
        return len(self._values)==len(rhs._values) and all(a==b for a,b in zip(self._values,rhs._values))
        
    def __eq__(self,rhs):
        # True if the times and values are the same; 
        # Otherwise, False
        cls = type(self)
        if isinstance(rhs, cls):
            return self._eqtimes(rhs) and self._eqvalues(rhs)
        #elif isinstance(rhs, numbers.Real):
        #    return all(v==rhs for v in self._values)
        else:
            return False
            