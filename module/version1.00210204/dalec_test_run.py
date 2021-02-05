import numpy as np
from dalec import dalec
import xarray

# class ModelMain:
#     module_name_list = ['read_clim', 'dalec', 'ways']
#     mlist = []
#
#     def __init__():
#         # load all needed modules
#         self.mlist = []
#         for module_name in module_name_list:
#             m = __import__(module_name)
#             self.mlist.append(m)
#         self.set_values(mlist)
#
#
#     def set_values():
#         # set values #需要对数据的组织和格式做出规定,根据变量名称都文件中读取
#         # 气象要素，全局变量，空间变量
#
#         m_num = len(mlist)
#         if m_num == 0:
#             print('no module in module list')
#         elif m_num == 1:
#
#         else:
#             for i in range(1,m_num):
#                 for input_item in mlist[i].metadata_inputs():
#                     for j in range(0,i):
#                         for output_item in mlist[j].metadata_outputs():
#                             if input_item == output_item()
#
#
#             print()
#
#
#
#
#         for m in mlist:
#             set_func = getattr(m, 'set_value')
#             # 找出该模块需要哪些输入
#             for input_item in m.metadata_inputs.keys():
#
#                 '''
#                     模块应该是顺序运行的，但是检查耦合变量的时候应该是从第二个模块开始
#                     从第二个模块开始，检查输入是否是之前模块的输入或输出
#                 '''
#
#
#
#
#                 if m.metadata_inputs[input_item]['source'] == 'file': ##从文件中找是否有这个输入
#                     pass
#                 else:#从其他模块的输出里找是否有这个输入
#                     pass
#
#                 data
#
#                 set_func(input_item, data)
#
#
#     def run(): # one time step
#         for m in mlist:
#             run_func = getattr(m, 'run')
#             run_func()
        
if __name__ == '__main__':
    # file = 'F:\Desktop\Daily meteorology1.csv'
    # forcing_data = np.genfromtxt(file,delimiter=',',skip_header=1,usecols=(2,3,4))

    paraDict = {
        'auto_frac': 0.45,
        'fol_frac': 0.01,
        'roo_frac': 0.457,
        'theta_min': 1.1e-5,
        'leaf_loss': 1 / 3,
        'theta_woo': 4.8e-5,
        'theta_roo': 6.72e-3,
        'theta_lit': 0.024,
        'theta_som': 2.4e-5,
        'temp_expf': 0.0193,
        'canopy_eff': 90,
        'onset_day': 140,
        'lab_frac': 0.7,
        'onset_per': 27,
        'fall_day': 308,
        'fall_per': 35,
        'leaf_mass': 24.2,
        'acm_constants': [0.0156935, 4.22273, 208.868, 0.0453194, 0.37836, 7.19298,
                          0.011136, 2.1001, 0.789798]
    }


    # 'inital_cpool':[75.,0.,135.,14313.,70.,18624.],

    def Date2Juday(date: tuple) -> int:
        # nonlear_year = [31,28,31,30,31,30,31,31,30,31,30,31]
        nonleap_year = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
        leap_year = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]
        return leap_year[date[1] - 1] + date[2] if (date[0] % 4) == 0 else nonleap_year[date[1] - 1] + date[2]


    file = 'FAR-SLu.DD.2009.2011.nc'
    ds = xarray.open_dataset(file)
    lat = ds['latitude'].data
    dates = zip(ds['year'].data.astype(int), ds['month'].data.astype(int), ds['day'].data.astype(int))
    julianday = []
    for d in dates:
        julianday.append(Date2Juday(d))

    model = dalec(paraDict)
    initial_cpool = [75., 0., 135., 14313., 70., 18624.]
    ca = 390.  # in  2010
    tmean = ds['TA_ERA'].data
    tmax = ds['TA_ERA_DAY'].data
    tmin = ds['TA_ERA_NIGHT'].data
    sw = ds['SW_IN_ERA'].data
    steps = len(tmean)

    for i in range(steps):
        initial_cpool, _, _, _, _ = model.run(initial_cpool, julianday[i], tmean[i], tmax[i], tmin[i], sw[i], ca, lat)

    print(initial_cpool)