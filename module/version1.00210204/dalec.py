import dalec_func as func
import numpy as np

class dalec(object):

    metadata_paras = {
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
    }
    
    metadata_inputs = {
        'initial_cpools' : {
            'data_type'   : 'FloatArray1D',
            'unit'        : 'g*m-2',      
            'range'       : [(20,2000),(20,2000),(20,2000),(100,100000),(20,2000),(100,200000)],
            'description' : 'the values of six carbon pools at time t'      
        },
        'mean_temperature' : {
            'data_type'   : 'float',
            'unit'        : 'degreeC',      
            'range'       : [None],
            'description' : 'daily mean temperature at time t'      
        },
        'max_temperature' : {
            'data_type'   : 'float',
            'unit'        : 'degreeC',      
            'range'       : [None],
            'description' : 'daily minimum temperature at time t'      
        },
        'min_temperature' : {
            'data_type'   : 'float',
            'unit'        : 'degreeC',      
            'range'       : [None],
            'description' : 'daily minimum temperature at time t'
        },
        'sw' : {
            'data_type'   : 'float',
            'unit'        : 'W*m-2',      
            'range'       : [None],
            'description' : 'short wave downward radiation at time t'      
        },
        'ca' : {
            'data_type'   : 'float',
            'unit'        : 'ppm',      
            'range'       : [None],
            'description' : 'atmospheric carbon dioxide concentration at time t'      
        },     
        'lat' : {
            'data_type'   : 'float',
            'unit'        : 'degree',      
            'range'       : [(-90,90)],
            'description' : 'atmospheric carbon dioxide concentration at time t'      
        },
        'soil_moisture' : {
            'data_type'   : 'float',
            'unit'        : 'mm',      
            'range'       : [(0,2000)],
            'description' : 'soil moisture at time t'      
        },
        'field_capacity' : {
            'data_type'   : 'float',
            'unit'        : 'mm',      
            'range'       : [(200,2000)],
            'description' : 'field capacity at time t'      
        },
    }
    
    metadata_outputs = {
        'next_cpools' : {
            'data_type'   : 'FloatArray1D',
            'unit'        : 'g*m-2',      
            'range'       : [(20,2000),(20,2000),(20,2000),(100,100000),(20,2000),(100,200000)],
            'description' : 'the values of six carbon pools at time t+1' 
        },
        'gpp' : {
            'data_type'   : 'float',
            'unit'        : 'g*m-2',      
            'range'       : [None],
            'description' : 'gross primary productivity at time t' 
        },
        'rtot' : {
            'data_type'   : 'float',
            'unit'        : 'g*m-2',      
            'range'       : [None],
            'description' : 'total ecosystem respiration at time t' 
        },
        'nee' : {
            'data_type'   : 'float',
            'unit'        : 'g*m-2',      
            'range'       : [None],
            'description' : 'net ecosystem exchange at time t' 
        },
        'LAI' : {
            'data_type'   : 'float',
            'unit'        : 'dimensionless',      
            'range'       : [None],
            'description' : 'leaf area index at time t' 
        },
    }
    
    def __init__(self, parameters:dict=None)->None:
      
        self.autof  = None
        self.labf   = None
        self.folf   = None
        self.roof   = None
        self.woot   = None
        self.mint   = None
        self.root   = None
        self.somt   = None
        self.litt   = None
        self.tempf  = None
        self.don    = None
        self.dfall  = None
        self.ce     = None
        self.pon    = None
        self.pfall  = None
        self.lma    = None
        self.loss   = None
        self.acmc   = None
        
        self.alias = {
            'auto_frac'     : 'autof',
            'lab_frac'      : 'labf',
            'fol_frac'      : 'folf',
            'roo_frac'      : 'roof',
            'theta_woo'     : 'woot',
            'theta_min'     : 'mint',
            'theta_roo'     : 'root',
            'theta_som'     : 'somt',
            'theta_lit'     : 'litt',
            'temp_expf'     : 'tempf',
            'onset_day'     : 'don',
            'fall_day'      : 'dfall',
            'canopy_eff'    : 'ce',
            'leaf_mass'     : 'lma',
            'leaf_loss'     : 'loss',
            'onset_per'     : 'pon',
            'fall_per'      : 'pfall',
            'acm_constants' : 'acmc'
        }
              
        assert len(parameters) == 18,'The input dictionary has more or less items than the module needed'
        for key, value in parameters.items():
            if self.alias.__contains__(key):
                setattr(self, self.alias[key], value)
             
    def check_inputs(self):
        for k in self.alias.keys():
            pass
    
    def set_value(self, k, val):
        if not k in self.alias.keys():
            print('Invalid key name:', k, 'in set_value function of delec.py')
            return -1
        setattr(self, self.alias[k], val)
        
    def get_value(self, k):
        return getattr(self, self.alias[k], None)
                    
    def run(self, inital_state, julian_day, t_mean, t_max, t_min, i, ca, lat, water_stress=1):
        #prepare inputs to the calculation function       
        cfol, clab, croo, cwoo, clit, csom = inital_state     
        i = i * 86400 / 1E6
        gpp       = func.acm(cfol, self.lma, self.ce, t_max, t_max-t_min, i, ca, julian_day, lat, self.acmc)*water_stress
        phi_onset = func.onset(julian_day, self.don, self.pon)
        phi_fall  = func.fall(julian_day, self.dfall, self.pfall, 1/self.loss)
        temp      = np.exp(t_mean * self.tempf)
        
        # calculate the six carbom pools after a time step (one day)
        cfol_next = (1 - phi_fall)  * cfol + (1 - self.autof) * self.folf * gpp + phi_onset * clab
        clab_next = (1 - phi_onset) * clab + (1 - self.autof) * (1 - self.folf) * self.labf * gpp
        croo_next = (1 - self.root) * croo + (1 - self.autof) * (1 - self.folf) * (1 - self.labf) * self.roof * gpp
        cwoo_next = (1 - self.woot) * cwoo + (1 - self.autof) * (1 - self.folf) * (1 - self.labf) * (1 - self.roof) * gpp
        clit_next = (1 - (self.litt+self.mint)*temp)*clit + self.root*croo + phi_fall*cfol
        csom_next = (1 - self.somt*temp) *csom + self.woot*cwoo + self.litt*temp*clit
        
        # variables that can help to calibrate the dalec mode
        rtot = gpp + (self.litt*clit + self.somt*csom)*temp 
        nee  = -(1. - self.autof) * gpp + rtot
        lai  = cfol / self.lma
        
        return [cfol_next,clab_next,croo_next,cwoo_next,clit_next,csom_next], gpp, rtot, nee, lai
    