import numpy as np






class ModelMain:
    module_name_list = ['read_clim', 'delec', 'ways']
    mlist = []
    
    def __init__():
        # load all needed modules
        self.mlist = []
        for module_name in module_name_list:
            m = __import__(module_name)
            self.mlist.append(m)
        self.set_values(mlist)

    
    def set_values():
        # set values #需要对数据的组织和格式做出规定,根据变量名称都文件中读取
        # 气象要素，全局变量，空间变量
        for m in mlist:
            set_func = getattr(m, 'set_value') 
            # 找出该模块需要哪些输入
            for input_item in m.metadata_inputs.keys():
                
                if m.metadata_inputs[input_item]['source'] == 'file': ##从文件中找是否有这个输入
                    pass
                else:#从其他模块的输出里找是否有这个输入
                    pass
                    
                data
                
                set_func(input_item, data)

            
    def run(): # one time step
        for m in mlist:
            run_func = getattr(m, 'run')
            run_func()
        
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
        'd_onset':140,
        'lab_frac':0.7,
        'onset_per':27,
        'd_fall':308,
        'fall_per':35,
        'leaf_mass':24.2,
        'acm_constants':np.array([0.0156935, 4.22273, 208.868, 0.0453194,0.37836, 7.19298, 
                                    0.011136, 2.1001,0.789798])   
    }
    
    #'inital_cpool':[75.,0.,135.,14313.,70.,18624.],
    
    model = dalec_i(paraDict)
    inital_cpool = [75.,0.,135.,14313.,70.,18624.]