import numpy as np

def acm(cf, clma, ceff, t_max, t_range, i, ca, julian_day, lat, constants):
    """ Aggregated canopy model (ACM) function
    ------------------------------------------
    Takes a foliar carbon (cf) value, leaf mass per area (clma) and canopy
    efficiency (ceff) and returns the estimated value for Gross Primary
    Productivity (gpp) of the forest at that time.
    :param cf: foliar carbon (g C m-2)
    :param clma: leaf mass area (g C m-2)
    :param ceff: canopy efficiency parameter
    :return: GPP value
    """
    
    hydro_resist = 1.0
    wp_diff = 2.5
    
    t_range = 0.5 * t_range
    L = cf / clma
    q = constants[1] - constants[2]
    gc = (abs(wp_diff))**constants[8] / \
         (t_range + constants[4]*hydro_resist)
    p = ((ceff*L) / gc)*np.exp(constants[6]*t_max)
    ci = 0.5*(ca + q - p + np.sqrt((ca + q - p)**2 - 4*(ca*q - p*constants[1])))
    E0 = (constants[5]*L**2) / (L**2 + constants[7])
    delta = -23.4*np.cos((360.*(julian_day + 10) / 365.) *
                         (np.pi/180.))*(np.pi/180.)
    s = 24*np.arccos((- np.tan(lat*np.pi/180.)*np.tan(delta))) / np.pi
    if s >= 24.:
        s = 24.
    elif s <= 0.:
        s = 0.
    else:
        s = s
    gpp = (i*gc*(ca - ci))*(constants[0]*s + constants[3]) / (E0*i + gc*(ca - ci))
    return gpp
    
def fit_polynomial(ep, mult_fac):
    """ Polynomial used to find phi_f and phi (offset terms used in
    phi_onset and phi_fall), given an evaluation point for the polynomial
    and a multiplication term.
    :param ep: evaluation point
    :param mult_fac: multiplication term
    :return: fitted polynomial value ---- https://github.com/Ewan82/dalec2/blob/master/src/model/mod_class.py
    """
    cf = [2.359978471e-05, 0.000332730053021, 0.000901865258885,
          -0.005437736864888, -0.020836027517787, 0.126972018064287,
          -0.188459767342504]
    poly_val = cf[0]*ep**6 + cf[1]*ep**5 + cf[2]*ep**4 + cf[3]*ep**3 + cf[4]*ep**2 + \
        cf[5]*ep**1 + cf[6]*ep**0
    phi = poly_val*mult_fac
    return phi

def onset(t, d_onset, c_ronset):
    
    s = 365.25 / np.pi
    term = np.exp(-1 * (np.sin((t - d_onset - 0.6245*c_ronset) / s))**2)
    phi_onset = np.sqrt(2 / np.pi) * (6.9088 / c_ronset) * term
    
    return phi_onset
    
def fall(t, d_fall, crfall, clspan):
    
    """Leaf fall function (controls foliar to litter carbon transfer) takes
    d_fall value, crfall value, clspan value and returns a value for
    phi_fall. ----https://github.com/Ewan82/dalec2/blob/master/src/model/mod_class.py
    """
    s = 365.25 / np.pi
    release_coeff = np.sqrt(2.)*crfall / 2.
    mag_coeff = (np.log(clspan) - np.log(clspan - 1.)) / 2.
    offset = fit_polynomial(clspan, release_coeff)
    phi_fall = (2. / np.sqrt(np.pi))*(mag_coeff / release_coeff) * \
        np.exp(-(np.sin((t - d_fall + offset) / s) * s / release_coeff)**2)
    
    return phi_fall

def run(paraList, inital_state, julian_day, t_mean, t_max, t_min, i, ca, lat, water_stress=1):
    """
        inital_state, 六个碳库的初始状态
        julian_day,   一年中的第几天
        soil_moisture,土壤含水量
        water_threshold,水分胁迫时的土壤含水量
        t_mean，平均气温
        t_max，最高气温
        acm_constants，acm模型的9个常数
        wp_diff，冠层和土壤的最大水势差
        i，太阳辐射
        ca，大气二氧化碳浓度
        hydro_resist，水分从土壤到冠层遇到的阻力
        lat，纬度
        paraList，DALEC模型的参数
    """
    cfol, clab, croo, cwoo, clit, csom = inital_state
    f_auto,f_fol,f_lab,f_roo,theta_woo,theta_min,theta_roo,theta_som,theta_lit,\
    theta_t,d_onset,d_fall,c_eff,c_lma,c_lf,c_ronset,c_rfall,acm_constants = paraList[0:18]
    
    t_range = t_max - t_min
    gpp = acm(cfol, c_lma, c_eff, t_max, t_range, i, ca, julian_day, lat, acm_constants)*water_stress
    phi_onset = onset(julian_day, d_onset, c_ronset)
    phi_fall  = fall(julian_day, d_fall, c_rfall, 1/c_lf)
    temp = np.exp(t_mean * theta_t)
    
    cfol_next = (1 - phi_fall)  * cfol + (1 - f_auto)* f_fol * gpp + phi_onset*clab
    clab_next = (1 - phi_onset) * clab + (1 - f_auto)*(1-f_fol)*f_lab*gpp
    croo_next = (1 - theta_roo) * croo + (1 - f_auto)*(1-f_fol)*(1-f_lab)*f_roo*gpp
    cwoo_next = (1 - theta_woo) * cwoo + (1 - f_auto)*(1-f_fol)*(1-f_lab)*(1-f_roo)*gpp
    clit_next = (1 - (theta_lit+theta_min)*temp)*clit + theta_roo*croo + phi_fall*cfol
    csom_next = (1 - theta_som*temp) *csom + theta_woo*cwoo + theta_min*temp*clit
    
    rtot = gpp + (theta_lit*clit + theta_som*csom)*temp 
    nee = -(1. - f_auto) * gpp + rtot
    lai = c_lf / c_lma
    
    return [cfol_next,clab_next,croo_next,cwoo_next,clit_next,csom_next], gpp, rtot, nee, lai
