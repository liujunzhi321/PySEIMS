import numpy as np
import math


def update_until():
    
    eaList,srzList,rfList,rsList,qffList,qfList,qsList = []
    s_inital = []
    paraList = []
    
    for i in range(steps):
        ea,srz,rf,rs,qff,qf,qs,s_init_e = run(prec[i], tmean[i], pet[i], s_init, paraList)
        eaList.append(ea)
        srzList.append(srz)
        rfList.append(rf)
        rsList.append(rs)
        qffList.append(qff)
        qfList.append(qf)
        qsList.append(qs)
        s_init = s_init_e 
    return eaList,srzList,rfList,rsList,qffList,qfList,qsList

# 目前的模型结构不支持单个步长的timelag。
def run(prec, tmean, pet, s_init, paraList):
    
    si, sw, srz, sf, ss = s_init
    tt,fdd,simax,ce,beta,fs,rsmax,tlagf,tlags,sftr,kff,kf,ks,crmax,rzsc = paraList
    
    pr, snowm, sw = prec_split(prec, tmean, tt, fdd, sw)
    ptf, si = intercept(pr, si, simax)
    ei, si, pet_r = evap_i(pet, si, simax)
    infil, runoff = rainfall_parti(ptf, snowm, srz, rzsc, beta)
    eu, srz = evap_u(infil, pet_r, srz, rzsc, beta, ce)
    ea = ei + eu
    rf, rs = runoff_split(runoff, fs, rsmax)
    srz, ss = capillary(srz, ss, crmax, rzsc)
    
    qff, qf, qs, sf, ss = runoff_routine(rf, rs, sf, ss, sftr, kff, kf, ks)
    s_init_e = [si, sw, srz, sf, ss]
    
    return ea, srz, rf, rs, qff, qf, qs, s_init_e


def prec_split(p, t, tt, fdd, sw):
    if t > tt:
        rainfall = p
        snowmelt = min(fdd * (t - tt), sw)
        sw -= snowmelt
    else：
        rainfall = 0.
        snowmelt = 0.
        sw += p
    return rainfall, snowmelt, sw
    
def intercept(rainfall, si, simax=0):
    """interception"""
    # ptf: precipitation throughfall
        if simax == 0:
        si = 0
        ptf = pr
    else:
        if pr + si > simax:
            ptf = pr - (simax - si)
            si = simax
        else:
            ptf = 0
            si = si + pr
    return ptf, si
    
def evap_i(pet, si, simax):
    """evaporation from interception"""
    # set to 0 when FAO pet is negative (Wilcox & Sly (1976))
    if pet < 0:
        pet = 0
    if simax == 0:
        ei = 0
    else:
        ei = min(si, pet * (si / simax) ** (2 / 3))
    si = si - ei
    pet_r = pet - ei
    return ei, si, pet_r
    
def rainfall_parti(ptf, snowm, srz, rzsc, beta):
    """effective precipitation partition"""
    # pe: effective precipitation
    pe = ptf + snowm
    # runoff coefficient
    rcoeff = 1 - (1 - srz / (rzsc * (1 + beta))) ** beta
    # infiltration
    infil = pe * (1 - rcoeff)
    # water exceed rzsc
    if infil + srz > rzsc:
        infil = rzsc - srz
    # runoff
    runoff = pe - infil
    return infil, runoff
    
def evap_u(infil, pet_r, srz, rzsc, beta, ce):
    """evaporation from unsaturated soil"""
    srz += infil
    eu = pet_r * min(srz / (rzsc * (1 + beta) * ce), 1)
    eu = min(eu, srz)
    srz -= eu
    return eu, srz

def runoff_split(runoff, fs, rsmax):
    rs = min(runoff * fs, rsmax)
    rf = runoff - rs
    return rf, fs
    
def capillary(srz, ss, crmax, rzsc):
    """capillary rise"""
    if rzsc - srz > crmax:
        srz += crmax
        ss -= crmax
    else:
        srz += rzsc - srz
        ss -= rzsc - srz
    return srz, ss
    
def runoff_routine(rf, rs, sf, ss, sftr, kff, kf, ks):
    """runoff generation"""
    # qff: surface runoff
    # qf:  fast subsurface runoff
    # sf:  slow subsurface runoff
    sf += rf
    qff = max(0, sf - sftr) / kff
    sf -= qff
    qf = sf / kf
    sf -= qf
    ss += rs
    qs = ss / ks
    ss -= qs
    return qff, qf, qs, sf, ss

    