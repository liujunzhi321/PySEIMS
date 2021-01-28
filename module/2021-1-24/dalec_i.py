import dalec

class DALEC(object):

    metadata_inputs = {
        # 'time' : {
            # 'data'        : self._time,
            # 'data_type'   : 'int',
            # 'unit'        : 'day',
            # 'range'       : (-9999,-9999)
            # 'loc'         : 0
            # 'description' : 'current time of the model; if the  model has not yet started to run, the value is set to 0'
            'source'        
        # },
        # 'time_step' : {
            # 'data'        : self._time_step,
            # 'data_type'   : 'int',
            # 'unit'        : 'day',
            # 'description' : 'time step; set to 1 by default'
            'source'        
        # },
        
        # 'inital_cpool' : {
            # 'data_type'   : 'FloatArray1D',
            # 'unit'        : 'g*m-2',
            # 'length'      : 6,
            # 'loc'         : 0,
            # 'range'       : [(20,2000),(20,2000),(20,2000),(100,100000),(20,2000),(100,200000)],
            # 'description' : 'the values of six carbon pools at time t'
            'source'        
        # },
        'auto_frac' : {
            'data_type'   : 'float',
            'unit'        : 'dimensionless',
            'loc'         : 0,
            'length'      : 1,          
            'range'       : [(0.3,0.7)],
            'description' : 'autotrophic respiration fraction'
            #'source'        
        },
        'lab_frac' : {
            'data_type'   : 'dimensionless',
            'unit'        : 'dimensionless',
            'loc'         : 1,
            'length'      : 1,
            'range'       : [(0.01,0.5)],
            'description' : 'the depth of melt snow per degree above tt per day'
            #'source'        
        },
        'fol_frac' : {
            'data_type'   : 'float',
            'unit'        : 'dimensionless',
            'loc'         : 2,
            'length'      : 1,
            'range'       : [(0.01,0.5)],
            'description' : 'the maximum storage of interception reservoir'
            #'source'        
        },
        'roo_frac' : {
            'data_type'   : 'float',
            'unit'        : 'dimensionless',
            'loc'         : 3,
            'length'      : 1,
            'range'       : [(0.01,0.5)],
            'description' : 'evapotranspiration_scale_parameter'
            #'source'        
        },
        'theta_woo' : {
            'data_type'   : 'float',
            'unit'        : 'dimensionless',
            'loc'         : 4,
            'length'      : 1,
            'range'       : [(2.5E-5,1E-3)],
            'description' : 'evapotranspiration_scale_parameter'
            #'source'        
        },
        'theta_min' : {
            'data_type'   : 'float',
            'unit'        : 'dimensionless',
            'loc'         : 5,
            'length'      : 1,
            'range'       : [(1E-5,1E-2)],
            'description' : 'evapotranspiration_scale_parameter'
            #'source'        
        },
        'theta_roo' : {
            'data_type'   : 'float',
            'unit'        : 'dimensionless',
            'loc'         : 6,
            'length'      : 1,
            'range'       : [(1E-4,1E-2)],
            'description' : 'evapotranspiration_scale_parameter'
            #'source'        
        },
        'theta_som' : {
            'data_type'   : 'float',
            'unit'        : 'dimensionless',
            'loc'         : 7,
            'length'      : 1,
            'range'       : [(1E-7,1E-3)],
            'description' : 'evapotranspiration_scale_parameter'
            #'source'        
        },
        'theta_lit' : {
            'data_type'   : 'float',
            'unit'        : 'dimensionless',
            'loc'         : 8,
            'length'      : 1,
            'range'       : [(1E-4,1E-2)],
            'description' : 'evapotranspiration_scale_parameter'
            #'source'        
        },
        'temp_expf' : {
            'data_type'   : 'float',
            'unit'        : 'dimensionless',
            'loc'         : 9,
            'length'      : 1,
            'range'       : [(0.018,0.08)],
            'description' : 'evapotranspiration_scale_parameter'
            #'source'        
        },
        'onset_day' : {
            'data_type'   : 'int',
            'unit'        : 'day',
            'loc'         : 10,
            'length'      : 1,
            'range'       : [(1,365)],
            'description' : 'evapotranspiration_scale_parameter'
            #'source'        
        },
        'fall_day' : {
            'data_type'   : 'int',
            'unit'        : 'day',
            'loc'         : 11,
            'length'      : 1,
            'range'       : [(1,365)],
            'description' : 'evapotranspiration_scale_parameter'
            #'source'        
        },
        'canopy_eff' : {
            'data_type'   : 'float',
            'unit'        : 'dimensionless',
            'loc'         : 12,
            'length'      : 1,
            'range'       : [(10,100)],
            'description' : 'evapotranspiration_scale_parameter'
            #'source'        
        },
        'leaf_mass' : {
            'data_type'   : 'float',
            'unit'        : 'g*m-2',
            'loc'         : 13,
            'length'      : 1,
            'range'       : [(10,400)],
            'description' : 'evapotranspiration_scale_parameter'
            #'source'        
        },
        'leaf_loss' : {
            'data_type'   : 'float',
            'unit'        : 'dimensionless',
            'loc'         : 14,
            'length'      : 1,
            'range'       : [(1/8,1)],
            'description' : 'evapotranspiration_scale_parameter'
            #'source'        
        },
        'onset_per' : {
            'data_type'   : 'int',
            'unit'        : 'day',
            'loc'         : 15,
            'length'      : 1,
            'range'       : [(10,100)],
            'description' : 'evapotranspiration_scale_parameter'
            #'source'        
        },
        'fall_per' : {
            'data_type'   : 'int',
            'unit'        : 'day',
            'loc'         : 16,
            'length'      : 1,
            'range'       : [(20,150)],
            'description' : 'evapotranspiration_scale_parameter'
            #'source'        
        },
        'acm_constants' : {
            'data_type'   : 'FloatArray1D',
            'unit'        : 'day',
            'loc'         : 17,
            'length'      : 9,
            'range'       : None,
            'description' : 'evapotranspiration_scale_parameter'
            #'source'        
        },
        # 'lat' : {
            # 'data_type'   : 'float',
            # 'unit'        : 'degree',
            # 'loc'         : 18,
            # 'length'      : 1,
            # 'range'       : None,
            # 'description' : 'latitude of the site'
            #'source'
        # }, 
         # 'ca' : {
            # 'data_type'   : 'float',
            # 'unit'        : 'ppm',
            # 'loc'         : 19,
            # 'length'      : 1,
            # 'range'       : None,
            # 'description' : 'CO2 mole fraction '
            #'source'
        # }       
    }
    
    def __init__(self, parameters:dict=None)->None:
        """
        time:string of date like "YYYY-MM-DD"
        
        """        
        self.paras = [-9999 for i in range(self.paraLength())]
        
        if len(parameters) == self.paraLength():
            for key, value in parameters.items():
                if key in self.metadata_inputs:
                    self.paras[self.metadata_inputs[key]['loc']] = value

    def run(self, initial_state, julian_day, t_mean, t_max, tmin, i, ca, lat, water_stress=1):
        return dalec.run(self.paras, initial_state, julian_day, t_mean, t_max, tmin, i, ca, lat, water_stress)

    @staticmethod    
    def paraLength()->int:
        return 18
