import os
import numpy

class Parameters():
    
    auto_frac = 0.5    # range(0.3, 0.7) 自养呼吸分配比例
    lab_frac  = 0.5    # range(0.01,0.5) GPP分配到不稳定碳库的比例
    fol_frac  = 0.5    # range(0.01,0.5) GPP分配到叶片碳库的比例
    roo_frac  = 0.5    # range(0.01,0.5) GPP分配到根系碳库的比例
    
    theta_woo = 0.0    # range(2.5E-5, 1E-3) 木质结构   ---- 土壤有机碳  周转速率       
    theta_min = 0.0    # range(1E-5  , 1E-2) 凋落物     ---- 土壤有机碳  周转速率
    theta_roo = 0.0    # range(1E-4  , 1E-2) 根系结构   ---- 凋落物      周转速率
    theta_som = 0.0    # range(1E-7  , 1E-3) 土壤有机碳 ---- 异养呼吸    周转速率
    theta_lit = 0.0    # range(1E-4  , 1E-2) 凋落物     ---- 异养呼吸    周转速率    
    temp_expF = 0.0    # range(0.018 , 0.08) 
    
    onset_day = 60     # range(1, 365)       叶子开始生长的日期
    fall_day  = 180    # range(1, 365)       叶子开始掉落的日期
    canopy_ef = 10     # range(10, 100)      冠层光合作用效率系数
    leaf_mass = 10     # range(10, 400)      单位面积上的叶片质量
    leaf_loss = 0.5    # range(1/8,  1)      叶片每年的损失比列
    onset_per = 10     # range(10, 100)      叶子生长的持续周期
    fall_per  = 20     # range(20, 150)      叶子掉落的持续周期
    
   acm_williams_xls = np.array([0.0155, 1.526, 324.1, 0.2017,
                                          1.315, 2.595, 0.037, 0.2268,
                                          0.9576])
    acm_reflex = np.array([0.0156935, 4.22273, 208.868, 0.0453194,
                                   0.37836, 7.19298, 0.011136, 2.1001,
                                   0.789798])
    acm_constants = self.acm_reflex  # (currently using params from REFLEX)
    
def ACM(cfol, c_lma, c_eff, acm_Constants, t_mean, t_range):
    
    LAI = cfol / c_lma
    
    gc = (water_potential * np.exp(acm_Constants.b1 * t_mean)) / (acm_Constants.b2 * H + t_range)
    
    Ci = 0.5 * (ca + q - p + np.sqrt((ca + q - p)**2 - 4*(ca*q-p*acm_Constants.theta)))
    
    E0 = (c1 * LAI**2) / (c2 + LAI**2)
    
    PD = gc * (ca - ci)
    
    Pi = (E0*driver[t].I*PD) / (E0*driver[t].I+PD)
    
    PT = Pi * (d1 * Dms +d2)
    
    return PT
    
def acm(self, cf, clma, ceff, tmax, t_range, wp_diff, i, ca, julian_day, hydro_resist, lat, constants):
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
    t_range = 0.5 * t_range
    L = cf / clma
    q = acm[1] - acm[2]
    gc = (abs(wp_diff))**acm[8] / \
         (t_range + acm[4]*hydro_resist)
    p = ((ceff*L) / gc)*np.exp(acm[6]*t_max)
    ci = 0.5*(ca + q - p + np.sqrt((ca + q - p)**2 - 4*(ca*q - p*acm[1])))
    E0 = (acm[5]*L**2) / (L**2 + acm[7])
    delta = -23.4*np.cos((360.*(julian_day + 10) / 365.) *
                         (np.pi/180.))*(np.pi/180.)
    s = 24*np.arccos((- np.tan(lat*np.pi/180.)*np.tan(delta))) / np.pi
    if s >= 24.:
        s = 24.
    elif s <= 0.:
        s = 0.
    else:
        s = s
    gpp = (i*gc*(ca - ci))*(acm[0]*s + acm[3]) / (E0*i + gc*(ca - ci))
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
    
    release_coeff = np.sqrt(2.)*crfall / 2.
    mag_coeff = (np.log(clspan) - np.log(clspan - 1.)) / 2.
    offset = self.fit_polynomial(clspan, release_coeff)
    phi_fall = (2. / np.sqrt(np.pi))*(mag_coeff / release_coeff) * \
        np.exp(-(np.sin((t - d_fall + offset) / s) * s / release_coeff)**2)
    
    return phi_fall
    

def run(inital_state, julian_day, soil_moisture, water_threshold, t_mean, t_max, acm_constants, 
        wp_diff, i, ca, hydro_resist, lat, paraList):
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
    clab, cfol, croo, cwoo, clit, csom = inital_state
    f_auto,f_fol,f_lab,f_roo,theta_woo,theta_min,theta_roo,theta_som,theta_lit,
    theta_t,d_onset,d_fall,c_eff,c_lma,c_lf,c_ronset,c_rfall = paraList
    
    gpp = ACM(cf, clma, ceff, tmax, t_range, wp_diff, i, ca, julian_day, hydro_resist, lat, acm_constants) * min(soil_moisture / water_threshold, 1)
    phi_onset = onset(julian_day, d_onset, c_ronset)
    phi_fall  = fall(julian_day, d_fal, c_rfall,)
    temp = np.exp(t_mean * theta_t)
    
    cfol_next = (1 - phi_fall)   * cfol + (1 - f_auto)* f_fol * gpp + phi_on*clab
    clab_next = (1 - phi_onset) * clab + (1 - f_auto)*(1-f_fol)*f_lab*gpp
    croo_next = (1 - theta_roo) * croo + (1 - f_auto)*(1-f_fol)*(1-f_lab)*f_roo*gpp
    cwoo_next = (1 - theta_woo) * cwoo + (1 - f_auto)*(1-f_fol)*(1-f_lab)*(1-f_roo)*gpp
    clit_next = (1 - (theta_lit+theta_min)*temp)*clit + theta_roo*croo + phi_fall*cfol
    csom_next = (1 - theta_som*temp) *csom + theta_woo*cwoo + theta_min*temp*clit
    
    return cfol_next,clab_next,croo_next,cwoo_next,clit_next,csom_next
    
    