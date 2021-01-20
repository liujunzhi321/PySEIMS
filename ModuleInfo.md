# Module: Water And ecosYstem Simulator(WAYS)

## introduction:
&nbsp;&nbsp;&nbsp;&nbsp;***original author: Ganquan Mao (ganquan.mao@icloud.com)***
&nbsp;&nbsp;&nbsp;&nbsp;At present, it is running on the ***basin scale***. The time resolution is ***daily***.

## parameters need to be calibrated:
| var name | description | range | unit |
|:-------- |:-----------------------------------------------------------------------------------:|:---------:| ----------:|
| tt | threshold temperature below which rainfall becomes snowfall | 0 | ℃ | 
| fdd | the depth of melt snow per degree above tt per day | (0,5) | mm/(℃\*day) |
| simax | the depth of melt snow per degree above tt per day | (0,10) | mm |
| ce | evapotranspiration scale parameter  | (0.1,0.9) | scalar |
| beta | runoff shape parameter | (0,2) | scalar |
| fs | the fraction of runoff that infiltrate into groundwater | (0,0.5) | scalar |
| rsmax | the maximum of water that can rechareg to groundwater per day |  | scalar |
| tagf | the time lag of fast response runoff | (0,5) | day |
| tlas | the time lag of slow response runoff | (0,5) | day |
| sftr | the maximum water storage of fast response reservoir | (10,200) | mm |
| kff | surface runoff coefficient | (1,40) | scalar |
| kf | interflow coefficient| (1,9) | scalar |
| ks | baseflow coefficient| 100 | scalar |
| crmax | the maximum of water that rised from groundwater into soil | (0, 20) | mm |
| rzsc | the maximum water storage in root zone | (400,) | mm |

## inputs
| data | unit |
|:------------------------------------------:|:----------:|
| daily precipitation | mm |
| daily mean temperature | ℃ |
| daily potential evapotranspiration | mm |

