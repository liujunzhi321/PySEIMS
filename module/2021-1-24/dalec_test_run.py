import numpy as np
from dalec_i import DALEC
import xarray

if __name__ == '__main__':

    file = 'F:\Desktop\Daily meteorology1.csv'
    forcing_data = np.genfromtxt(file,delimiter=',',skip_header=1,usecols=(2,3,4))
    
    paraDict = {
        'auto_frac':0.45,
        'fol_frac':0.01,
        'roo_frac':0.457,
        'theta_min':1.1e-5,
        'leaf_loss':1/3,
        'theta_woo':4.8e-5,
        'theta_roo':6.72e-3,
        'theta_lit':0.024,
        'theta_som':2.4e-5,
        'temp_expf':0.0193,
        'canopy_eff':90,
        'onset_day':140,
        'lab_frac':0.7,
        'onset_per':27,
        'fall_day':308,
        'fall_per':35,
        'leaf_mass':24.2,
        'acm_constants':[0.0156935, 4.22273, 208.868, 0.0453194,0.37836, 7.19298, 
                                    0.011136, 2.1001,0.789798]  
    }
    
    #'inital_cpool':[75.,0.,135.,14313.,70.,18624.],
    
    def Date2Juday(date:tuple)->int:   
        # nonlear_year = [31,28,31,30,31,30,31,31,30,31,30,31]
        nonleap_year = [0,31,59,90,120,151,181,212,243,273,304,334]
        leap_year    = [0,31,60,91,121,152,182,213,244,274,305,335] 
        return leap_year[date[1]-1]+date[2] if (date[0]%4)==0 else nonleap_year[date[1]-1]+date[2]
        
    file = r'F:\Desktop\data\FLUXNET\DD\2016_01\AR-SLu.DD.2009.2011.nc'
    ds = xarray.open_dataset(file)
    lat = ds['latitude'].data
    dates = zip(ds['year'].data.astype(int),ds['month'].data.astype(int),ds['day'].data.astype(int))
    julianday = []
    for d in dates:
        julianday.append(Date2Juday(d))
        
    model = DALEC(paraDict)
    initial_cpool = [75.,0.,135.,14313.,70.,18624.]
    ca = 390.  # in  2010
    tmean = ds['TA_ERA'].data
    tmax  = ds['TA_ERA_DAY'].data
    tmin  = ds['TA_ERA_NIGHT'].data
    sw    = ds['SW_IN_ERA'].data
    steps = len(tmean)

    for i in range(steps):
        initial_cpool,_,_,_,_ = model.run(initial_cpool, julianday[i], tmean[i], tmax[i], tmin[i], sw[i], ca, lat)

    print(initial_cpool)