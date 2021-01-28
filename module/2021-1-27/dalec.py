import dalec

class DALEC(object):

    metadata_inputs = {      
        'initial_cpool' : {
            'data_type'   : 'FloatArray1D',
            'unit'        : 'g*m-2',
            'range'       : [(20,2000),(20,2000),(20,2000),(100,100000),(20,2000),(100,200000)]，
            'description' : 'the values of six carbon pools at time t'      
        },
        'auto_frac' : {
            'data_type'   : 'float',
            'unit'        : 'dimensionless',      
            'range'       : [(0.3,0.7)],
            'description' : 'autotrophic respiration fraction'      
        },
        'lab_frac' : {
            'data_type'   : 'dimensionless',
            'unit'        : 'dimensionless',
            'range'       : [(0.01,0.5)],
            'description' : 'the depth of melt snow per degree above tt per day'      
        },
        'fol_frac' : {
            'data_type'   : 'float',
            'unit'        : 'dimensionless',
            'range'       : [(0.01,0.5)],
            'description' : 'the maximum storage of interception reservoir'     
        },
        'roo_frac' : {
            'data_type'   : 'float',
            'unit'        : 'dimensionless',
            'range'       : [(0.01,0.5)],
            'description' : 'evapotranspiration_scale_parameter'
            #'source'        
        },
        'theta_woo' : {
            'data_type'   : 'float',
            'unit'        : 'dimensionless',
            'range'       : [(2.5E-5,1E-3)],
            'description' : 'evapotranspiration_scale_parameter'       
        },
        'theta_min' : {
            'data_type'   : 'float',
            'unit'        : 'dimensionless',
            'range'       : [(1E-5,1E-2)],
            'description' : 'evapotranspiration_scale_parameter'      
        },
        'theta_roo' : {
            'data_type'   : 'float',
            'unit'        : 'dimensionless',
            'range'       : [(1E-4,1E-2)],
            'description' : 'evapotranspiration_scale_parameter'      
        },
        'theta_som' : {
            'data_type'   : 'float',
            'unit'        : 'dimensionless',
            'range'       : [(1E-7,1E-3)],
            'description' : 'evapotranspiration_scale_parameter'       
        },
        'theta_lit' : {
            'data_type'   : 'float',
            'unit'        : 'dimensionless',
            'range'       : [(1E-4,1E-2)],
            'description' : 'evapotranspiration_scale_parameter'
            #'source'        
        },
        'temp_expf' : {
            'data_type'   : 'float',
            'unit'        : 'dimensionless',
            'range'       : [(0.018,0.08)],
            'description' : 'evapotranspiration_scale_parameter'        
        },
        'onset_day' : {
            'data_type'   : 'int',
            'unit'        : 'day',
            'range'       : [(1,365)],
            'description' : 'evapotranspiration_scale_parameter'       
        },
        'fall_day' : {
            'data_type'   : 'int',
            'unit'        : 'day',
            'range'       : [(1,365)],
            'description' : 'evapotranspiration_scale_parameter'    
        },
        'canopy_eff' : {
            'data_type'   : 'float',
            'unit'        : 'dimensionless',
            'range'       : [(10,100)],
            'description' : 'evapotranspiration_scale_parameter'
        },
        'leaf_mass' : {
            'data_type'   : 'float',
            'unit'        : 'g*m-2',
            'range'       : [(10,400)],
            'description' : 'evapotranspiration_scale_parameter'
        },
        'leaf_loss' : {
            'data_type'   : 'float',
            'unit'        : 'dimensionless',
            'range'       : [(1/8,1)],
            'description' : 'evapotranspiration_scale_parameter'      
        },
        'onset_per' : {
            'data_type'   : 'int',
            'unit'        : 'day',
            'range'       : [(10,100)],
            'description' : 'evapotranspiration_scale_parameter'      
        },
        'fall_per' : {
            'data_type'   : 'int',
            'unit'        : 'day',
            'range'       : [(20,150)],
            'description' : 'evapotranspiration_scale_parameter'
            #'source'        
        },
        'acm_constants' : {
            'data_type'   : 'FloatArray1D',
            'unit'        : 'day',
            'range'       : [None,None,None,None,None,None,None,None,None],
            'description' : 'evapotranspiration_scale_parameter'        
        }
        # 'lat' : {
            # 'data_type'   : 'float',
            # 'unit'        : 'degree',
            # 'range'       : [None],
            # 'description' : 'latitude of the site'       
        # }, 
         # 'ca' : {
            # 'data_type'   : 'float',
            # 'unit'        : 'ppm',
            # 'range'       : [None],
            # 'description' : 'CO2 mole fraction '       
        # }       
    }
    

    
    def __init__(self, parameters:dict=None)->None:
        """
        time:string of date like "YYYY-MM-DD"    
        """
        
        # self.ipools = None
        # self.autof  = None
        # self.labf   = None
        # self.folf   = None
        # self.roof   = None
        # self.woot   = None
        # self.mint   = None
        # self.root   = None
        # self.somt   = None
        # self.litt   = None
        # self.tempf  = None
        # self.don    = None
        # self.dfall  = None
        # self.ce     = None
        # self.pon    = None
        # self.pfall  = None
        # self.lma    = None
        # self.loss   = None
        # self.acmc   = None
        
        # self.inner_vars = {
            # 'initial_cpool' : self.ipools,
            # 'auto_frac'     : self.autof,
            # 'lab_frac'      : self.labf,
            # 'fol_frac'      : self.folf,
            # 'roo_frac'      : self.roof,
            # 'theta_woo'     : self.woot,
            # 'theta_min'     : self.mint,
            # 'theta_roo'     : self.root,
            # 'theta_som'     : self.somt,
            # 'theta_lit'     : self.litt,
            # 'temp_expf'     : self.tempf,
            # 'onset_day'     : self.don,
            # 'fall_day'      : self.dfall,
            # 'canopy_eff'    : self.ce,
            # 'leaf_mass'     : self.lma,
            # 'leaf_loss'     : self.loss,
            # 'onset_per'     : self.pon,
            # 'fall_per'      : self.pfall,
            # 'cam_constants' : self.acmc
        # }
        
        self.inner_vars = {
            'initial_cpool' : None,
            'auto_frac'     : None,
            'lab_frac'      : None,
            'fol_frac'      : None,
            'roo_frac'      : None,
            'theta_woo'     : None,
            'theta_min'     : None,
            'theta_roo'     : None,
            'theta_som'     : None,
            'theta_lit'     : None,
            'temp_expf'     : None,
            'onset_day'     : None,
            'fall_day'      : None,
            'canopy_eff'    : None,
            'leaf_mass'     : None,
            'leaf_loss'     : None,
            'onset_per'     : None,
            'fall_per'      : None,
            'cam_constants' : None
        }
        
        
        assert len(parameters) == paralength(),'The input dictionary has more or less items than the module needed'
        for key, value in self.inner_vars.items():
            if self.inner_vars.has_key(key):
                self.inner_vars[key] = value
            
    
    def check_inputs():
        for k in inner_vars.keys():
            pass
    
    def set_value(k, val):
        if not k in inner_vars.keys():
            print('Invalid key name:', k, 'in set_value function of delec_i.py')
            return
        self.inner_vars[k] = val
        
    def get_value():
        return self.inner_vars.get(k, None)
                    
    def run(self, inital_state, julian_day, t_mean, t_max, tmin, i, ca, lat, water_stress=1):
        #prepare inputs to the calculation function
        
        # 直接把代码写这里
        
        
        
        
        
        
        
        
        
    @staticmethod    
    def paraLength()->int:
        return 18
